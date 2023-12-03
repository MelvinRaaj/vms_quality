# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.apps import apps
from django.http import JsonResponse

#import messages
from django.contrib import messages

#import loginrequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import ProductCollection, Products

from django.forms import inlineformset_factory

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product_Collection, Product_SKU, Materials
from .forms import CollectionForm, Product_SKU_FormSet,Collection_Material_FormSet

from products.models import Product_Collection, Product_SKU, Materials

# template view
from django.views.generic import TemplateView

# this is the baseContextView which should be inherited by all views in app apps (reusable apps)
class BaseAppContextView(View):
    def get_app_name(self):
        # Get the app name from the current view's app
        current_app = self.request.resolver_match.app_name
        app_label = apps.get_app_config(current_app).verbose_name
        return app_label

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = self.get_app_name()
        return context

class CollectionView(LoginRequiredMixin,ListView,BaseAppContextView):
    model = Product_Collection
    template_name = "products/collection_list.html"
    context_object_name = "products"

class ProductSKUInline(BaseAppContextView):
    form_class = CollectionForm
    model = Product_Collection
    template_name = "products/product_create_or_update.html"

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
        return redirect('products:list_products')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.product = self.object
            variant.save()

    def formset_materials_valid(self, formset):
        """
        Hook for custom formset saving. Useful if you have multiple formsets
        """
        materials = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for material in materials:
            material.product = self.object
            material.save()

class ProductCreate(LoginRequiredMixin,ProductSKUInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': Product_SKU_FormSet(prefix='variants'),
                'materials': Collection_Material_FormSet(prefix='materials'),
            }
        else:
            return {
                'variants': Product_SKU_FormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'materials': Collection_Material_FormSet(self.request.POST or None, self.request.FILES or None, prefix='materials'),
            }


class ProductUpdate(LoginRequiredMixin,ProductSKUInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': Product_SKU_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'materials': Collection_Material_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='materials'),
        }

@login_required    
def delete_variant(request, pk):
    try:
        variant = Product_SKU.objects.get(id=pk)
    except Product_SKU_FormSet.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('products:update_product', pk=variant.product.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('products:update_product', pk=variant.product.id)

@login_required    
def delete_material(request, pk):
    try:
        material = Materials.objects.get(id=pk)
    except Collection_Material_FormSet.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('products:update_product', pk=material.product.id)

    material.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('products:update_product', pk=material.product.id)

# class get_product_names(View):
#     def get(self, request, *args, **kwargs):
#         shopping_list_id = self.request.GET.get('collection_id')

#         # Fetch variants based on the collection_id or any other criteria
#         variants = Product_SKU.objects.filter(Collection_Name=shopping_list_id)

#         # Convert variant data to a format suitable for JSON response
#         variant_data = []
#         for variant in variants:
#             variant_data.append({
#                 'product_sku': str(variant.product_sku), #added the string here. Maybe an issue soon.
#                 'qty': variant.qty,
#                 # Add other fields as needed
#             })

#         # Prepare JSON response
#         response_data = {'variants': variant_data}

#         return JsonResponse(response_data)
