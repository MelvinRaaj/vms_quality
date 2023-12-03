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

from .models import QualityTemplate, QualityTemplateItems,RFIQualitySchedules

from rfi.models import VendorSamplesResponse

from .forms import QualityTemplateItemsForm, QualityTemplateForm, QualityTemplate_Item_FormSet, RFIQualitySchedulesForm,RFIQualitySchedulesFormSet

from django.db import transaction

# import modelformset_factory
from django.forms import modelformset_factory

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

class QualityTemplateView(LoginRequiredMixin,ListView,BaseAppContextView):
    model = QualityTemplate
    template_name = "quality2/quality_template_list.html"
    context_object_name = "products"

class QualityTemplateItemsInline(BaseAppContextView):
    form_class = QualityTemplateForm
    model = QualityTemplate
    template_name = "quality2/product_create_or_update.html"

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
        return redirect('quality2:list_products')
    
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

class QualityTemplateCreate(QualityTemplateItemsInline, CreateView,LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        ctx = super(QualityTemplateCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': QualityTemplate_Item_FormSet(prefix='variants'),
            }
        else:
            return {
                'variants': QualityTemplate_Item_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            }

class QualityTemplateUpdate(QualityTemplateItemsInline, UpdateView,LoginRequiredMixin):

    def get_context_data(self, **kwargs):
        ctx = super(QualityTemplateUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):

        return {
            'variants': QualityTemplate_Item_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            # 'samples': SL_Samples_Form_FormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='samples'),
        }
    
def delete_variant(request, pk):
    try:
        variant = QualityTemplateItems.objects.get(id=pk)
    except QualityTemplateItems.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('quality2:update_product', pk=variant.rfi.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('quality2:update_product', pk=variant.rfi.id)

# class RFIScheduleView(LoginRequiredMixin,ListView,BaseAppContextView):
#     model = RFIQualitySchedules
#     template_name = "quality2/rfi_schedule_list.html"
#     context_object_name = "products"

# class RFIScheduleCreate(LoginRequiredMixin,CreateView,BaseAppContextView):
#     model = RFIQualitySchedules
#     form_class = QualityTemplateItemsForm
#     template_name = "quality2/rfi_schedule_create_or_update.html"
#     success_url = "/quality2/rfi_schedule_list"

#     def form_valid(self, form):
#         return super().form_valid(form)
    
# class RFIScheduleUpdate(LoginRequiredMixin,ListView,BaseAppContextView):
#     model = RFIQualitySchedules
#     template_name = "quality2/quality_template_list.html"
#     context_object_name = "products"

@login_required
def RFIScheduleUpdate(request):

    user_role = request.user.user_role

    ScheduleFormSet = modelformset_factory(
        RFIQualitySchedules,
        fields='__all__',
        extra=0,
    )

    if request.method == 'POST':
        formset = ScheduleFormSet(request.POST, queryset=RFIQualitySchedules.objects.all())
        if formset.is_valid():
            formset.save()
            return redirect('quality2:update_rfi_schedule')  # Redirect after successful form submission
        else:
            print(formset.errors)  # Print errors to console for debugging
    else:
        if user_role == 'Quality User':
            formset = ScheduleFormSet(queryset=RFIQualitySchedules.objects.filter(assigned_to=request.user))
        else:
            formset = ScheduleFormSet(queryset=RFIQualitySchedules.objects.all())

    return render(request, 'quality2/rfi_schedule_create_or_update.html', {'formset': formset})

@login_required
def RFIScheduleUpdate1(request, pk):
    # Get the VendorSamplesResponse instance using pk
    vendor_samples_response = get_object_or_404(VendorSamplesResponse, pk=pk)

    ScheduleFormSet = modelformset_factory(
        RFIQualitySchedules,
        fields='__all__',
        extra=0,
    )

    if request.method == 'GET':
        # Get all RFIQualitySchedules related to the VendorSamplesResponse
        schedules_queryset = RFIQualitySchedules.objects.filter(samplesresponse=vendor_samples_response)
        formset = ScheduleFormSet(queryset=schedules_queryset)

    elif request.method == 'POST':
        formset = ScheduleFormSet(request.POST, queryset=RFIQualitySchedules.objects.filter(samplesresponse=vendor_samples_response))
        if formset.is_valid():
            formset.save()
            return redirect('samples:list_products')  # Redirect after successful form submission
        else:
            print(formset.errors)  # Print errors to console for debugging

    return render(request, 'quality2/rfi_schedule_create_or_update.html', {'formset': formset})
