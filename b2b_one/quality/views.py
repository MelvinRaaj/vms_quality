# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

#import messages
from django.contrib import messages
from django.urls import reverse_lazy

#import loginrequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory, formset_factory

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QualityTemplates, QualityTemplateItems, QualitySchedules
from .forms import QualityTemplateForm, QualityTemplateItemForm,QualityTemplateItemsFormSet,QualityScheduleForm

# Create your views here.

class QualityHome(LoginRequiredMixin,TemplateView):
    template_name = 'quality/qualityhome.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)
    
class Samples(LoginRequiredMixin,TemplateView):
    template_name = 'quality/samples.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)


class QualitySchedules1(LoginRequiredMixin,TemplateView):
    template_name = 'quality/qualityschedules1.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)


class InspectionSchedules1(LoginRequiredMixin,TemplateView):
    template_name = 'quality/inspectionschedules1.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)

class InspectionItemSchedules1(LoginRequiredMixin,TemplateView):
    template_name = 'quality/inspectionitemschedules1.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)

class InspectionItemAQL(LoginRequiredMixin,TemplateView):
    template_name = 'quality/inspectionitemsAQL.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)


@login_required
def qualitytemplatelist(request):
    queryset = QualityTemplates.objects.all()
    form = QualityTemplateForm()
    if request.method == 'POST':
        form = QualityTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality:qualitytemplatelist')
    return render(request, 'quality/quality_template_list.html', {'queryset': queryset, 'form': form})

class qualitytemplatelistcreate(CreateView):
    model = QualityTemplates
    template_name = 'quality/quality_template_update.html'
    form_class = QualityTemplateForm

    def form_valid(self, form):
        context = self.get_context_data()
        items_formset = context['items_formset']
        
        if items_formset.is_valid():
            self.object = form.save()
            items_formset.instance = self.object
            items_formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['items_formset'] = QualityTemplateItemsFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['items_formset'] = QualityTemplateItemsFormSet(instance=self.object)
        return data

# class QualitySchedules(LoginRequiredMixin,ListView):
#     model = QualitySchedules
#     template_name = 'quality/qualityschedules.html'
#     context_object_name = 'qualityschedules'


#     # #pass the context to the template
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['qualityschedules'] = QualitySchedules.GET
#     #     return context

@login_required
def QualitySchedulesView(request):
    queryset = QualitySchedules.objects.all()
    form = QualityScheduleForm()
    if request.method == 'POST':
        form = QualityScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality:QualitySchedules')
    return render(request, 'quality/qualityschedules.html', {'queryset': queryset, 'form': form})
