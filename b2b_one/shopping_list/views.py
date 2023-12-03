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

from .models import ShoppingList, ShoppingListItem, SL_Samples,bedlinen_fabrics
from products.models import Product_SKU

from products.models import Product_Collection, Product_SKU

from .forms import Shopping_List_Form, Shopping_List_Item_Form, SL_Samples_Form, Shopping_List_Item_FormSet, SL_Samples_Form_FormSet, Bedlinen_Fabric_Form

from django.db import transaction

# template view
from django.views.generic import TemplateView

# this is the baseContextView which should be inherited by all views in app apps (reusable apps)
class BaseAppContextView(View,LoginRequiredMixin):
    def get_app_name(self):
        # Get the app name from the current view's app
        current_app = self.request.resolver_match.app_name
        app_label = apps.get_app_config(current_app).verbose_name
        return app_label

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = self.get_app_name()
        return context

class Shopping_List_View(BaseAppContextView, ListView, LoginRequiredMixin):
    model = ShoppingList
    template_name = "shopping_list/shopping_list.html"
    context_object_name = "products"

class Shoppinglist_Products_Inline(BaseAppContextView):
    form_class = Shopping_List_Form
    model = ShoppingList
    template_name = "shopping_list/product_create_or_update.html"

    def form_valid(self, form):
        self.object = form.save()

        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('shopping_list:list_products')
    
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

    def formset_samples_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        samples = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for samples in samples:
            samples.product = self.object
            samples.save()


class SL_Line_Create(Shoppinglist_Products_Inline, CreateView,LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        ctx = super(SL_Line_Create, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': Shopping_List_Item_FormSet(prefix='variants'),
                'samples': SL_Samples_Form_FormSet(prefix='samples'),
            }
        else:
            return {
                'variants': Shopping_List_Item_FormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'samples': SL_Samples_Form_FormSet(self.request.POST or None, self.request.FILES or None, prefix='samples'),
            }


class SL_Line_Update(Shoppinglist_Products_Inline, UpdateView,LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        ctx = super(SL_Line_Update, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):

        return {
            'variants': Shopping_List_Item_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'samples': SL_Samples_Form_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='samples'),
        }
    
def delete_variant(request, pk):
    try:
        variant = ShoppingListItem.objects.get(id=pk)
    except ShoppingListItem.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('shopping_list:update_product', pk=variant.shopping_list.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('shopping_list:update_product', pk=variant.shopping_list.id)


def delete_samples(request, pk):
    try:
        samples = SL_Samples.objects.get(id=pk)
    except SL_Samples.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('shopping_list:update_product', pk=samples.shopping_list.id)

    samples.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('shopping_list:update_product', pk=samples.shopping_list.id)


class get_product_names(View):
    def get(self, request, *args, **kwargs):
        collection_id = self.request.GET.get('collection_id')

        # Fetch variants based on the collection_id or any other criteria
        variants = Product_SKU.objects.filter(Collection_Name=collection_id)

        print(variants)
        

        # Convert variant data to a format suitable for JSON response
        variant_data = []
        for variant in variants:
            variant_data.append({
                'product_sku': str(variant), #added the string here. Maybe an issue soon.
                # 'qty': variant.qty,
                # Add other fields as needed
            })

        # Prepare JSON response
        response_data = {'variants': variant_data}
        print(response_data)


        return JsonResponse(response_data)

