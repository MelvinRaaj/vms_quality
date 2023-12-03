# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

#import messages
from django.contrib import messages


#import loginrequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory, formset_factory

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ProductCollection, Products
from .forms import ProductCollectionForm, ProductsForm, ProductCollectionsFormSet

class ProductCollectionListView(ListView):
    model = ProductCollection
    template_name = 'product_collections/product_collections_list.html'
    context_object_name = 'collections'

# def edit_product_collection(request, pk):
#     product_collection = get_object_or_404(ProductCollection, pk=pk)
#     ProductFormSet = inlineformset_factory(ProductCollection, Products, form=ProductsForm, extra=0)

#     if request.method == 'POST':
#         formset = ProductFormSet(request.POST, instance=product_collection, queryset=Products.objects.filter(ProductCollection_Name=product_collection))
#         form = ProductCollectionForm(request.POST, instance=product_collection)

#         if form.is_valid() and formset.is_valid():
#             form.save()
#             formset.save()
#             # Redirect after saving
#             return redirect('product_collections:product_collections_list')

#     else:
#         form = ProductCollectionForm(instance=product_collection)
#         formset = ProductFormSet(instance=product_collection, queryset=Products.objects.filter(ProductCollection_Name=product_collection))

#     return render(request, 'product_collections/product_collections_edit.html', {'form': form, 'formset': formset})



# below this tak pakai lagi
class ProductsInline():
    form_class = ProductCollectionsFormSet
    model = Products
    # template_name = "products/product_create_or_update.html"
    template_name = "demo/product_collections_edit.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('demo:product_collections_list')

    def formset_products_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.ProductCollection_Name = self.object
            variant.save()

class ProductCreate(ProductsInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': ProductCollectionsFormSet(prefix='variants'),
            }
        else:
            return {
                'variants': ProductCollectionsFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
            }


class ProductUpdate(ProductsInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': ProductCollectionsFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
        }