# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect, render
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
from django.db import transaction

from .models import RFI, RFIItem, VendorsRFI, VendorResponseRFI, VendorSamplesResponse, RFISamples
from .forms import RFIForm, RFI_Item_FormSet, RFI_Vendor_FormSet, VendorResponseRFI_FormSet,VendorSamplesRFI_FormSet, RFI_Samples_FormSet

from shopping_list.models import ShoppingList, ShoppingListItem, SL_Samples
from tenant.models import Tenant

# Create your views here.
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

# RFI list view

class RFIListView(BaseAppContextView,ListView,LoginRequiredMixin):
    model = RFI
    template_name = 'rfi/rfi_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Get the user's role
        user_vendor = self.request.user.company
        user_role = self.request.user.user_role  # Assuming you have a 'user_role' attribute in your custom user model
        print(user_vendor)

        # Filter the queryset based on the user's role
        if user_role != 'Vendor':
            # If the user is an admin, show all RFIs
            queryset = RFI.objects.all()
        # elif user_role == 'manager':
        #     # If the user is a manager, filter RFIs based on manager-specific criteria
        #     queryset = RFI.objects.filter(manager_specific_field=some_value)
        else:
            # For other roles, customize the filter accordingly
            queryset = RFI.objects.filter(vendorsrfi__vendor=user_vendor)
        return queryset    

# RFI create view
class RFI_Inline(BaseAppContextView):
    form_class = RFIForm
    model = RFI
    template_name = "rfi/product_create_or_update.html"

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
        return redirect('rfi:list_products')
    
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

    def formset_vendors_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        vendors = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for vendor in vendors:
            vendor.product = self.object
            vendor.save()


class RFI_Create(RFI_Inline, CreateView,LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        ctx = super(RFI_Create, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': RFI_Item_FormSet(prefix='variants'),
                'vendors': RFI_Vendor_FormSet(prefix='vendors'),
                'response': VendorResponseRFI_FormSet(prefix='response'),
                'samples': RFI_Samples_FormSet(prefix='samples'),
                'sample_response': VendorSamplesRFI_FormSet(prefix='sample_response'),
            }
        else:
            return {
                'variants': RFI_Item_FormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'vendors': RFI_Vendor_FormSet(self.request.POST or None, self.request.FILES or None, prefix='vendors'),
                'response': VendorResponseRFI_FormSet(self.request.POST or None, self.request.FILES or None, prefix='response'),
                'samples': RFI_Samples_FormSet(self.request.POST or None, self.request.FILES or None, prefix='samples'),
                'sample_response': VendorSamplesRFI_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='sample_response'),
            }


class RFI_Update(RFI_Inline, UpdateView,LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        ctx = super(RFI_Update, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        user_role = self.request.user.user_role  # Assuming you have a 'user_role' attribute in your custom user model

        formsets = {
            'variants': RFI_Item_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'vendors': RFI_Vendor_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='vendors'),
            'response': VendorResponseRFI_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='response'),
            'samples': RFI_Samples_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='samples'),
            'sample_response': VendorSamplesRFI_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='sample_response'),
        }

        # Adjust formsets based on user role
        if user_role == 'Vendor':
            formsets = {
            # Only allow vendors to edit their own responses
            'variants': RFI_Item_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            # 'vendors': RFI_Vendor_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='vendors', queryset=VendorsRFI.objects.filter(vendor=self.request.user.company)),
            'response': VendorResponseRFI_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='response', queryset=VendorResponseRFI.objects.filter(vendor=self.request.user.company)),
            # 'samples': RFI_Samples_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='samples'),
            'sample_response': VendorSamplesRFI_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='sample_response', queryset=VendorSamplesResponse.objects.filter(vendor=self.request.user.company)),
            }

        return formsets

def delete_variant(request, pk):
    try:
        variant = RFIItem.objects.get(id=pk)
    except RFIItem.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('shopping_list:update_product', pk=variant.rfi.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('rfi:update_product', pk=variant.rfi.id)

def delete_samples(request, pk):
    try:
        variant = RFISamples.objects.get(id=pk)
    except RFISamples.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('rfi:update_productt', pk=variant.rfi.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('rfi:update_product', pk=variant.rfi.id)

def delete_vendors(request, pk):
    try:
        variant = VendorsRFI.objects.get(id=pk)
    except RFIItem.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('rfi:update_product', pk=variant.rfi.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('rfi', pk=variant.rfi.id)


class get_product_names(View):
    def get(self, request, *args, **kwargs):
        shopping_list_id = self.request.GET.get('shopping_list')

        # Fetch variants based on the collection_id or any other criteria
        variants = ShoppingListItem.objects.filter(shopping_list_id=shopping_list_id)

        #fetch samples based on shopping list id
        samples = SL_Samples.objects.filter(shopping_list_id=shopping_list_id)

        # Convert variant data to a format suitable for JSON response
        variant_data = []
        for variant in variants:
            variant_data.append({
                'product_sku': f"{variant.shopping_list} - {variant.product_sku} - {variant.qty}", #added the string here. Maybe an issue soon.
                'qty': variant.qty,
                # Add other fields as needed
            })


        sample_data = []
        for sample in samples:
            sample_data.append({
                'samples': f"{sample.shopping_list} - {sample.product_sku} - {sample.sample_qty}", #added the string here. Maybe an issue soon.
                'qty': sample.sample_qty,
                # Add other fields as needed
            })


        # Prepare JSON response
        response_data = {'variants': variant_data, 'samples': sample_data}
        print(response_data)

        return JsonResponse(response_data)

