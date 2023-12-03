from django.shortcuts import render, redirect, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from allauth.account.views import SignupView, LoginView, EmailVerificationSentView
from allauth.account import app_settings, signals

from .models import Department
from .forms import DepartmentForm, DepartmentFormSet

# Department Create View
class DepartmentCreateView(LoginRequiredMixin, CreateView):
    pass
    model = Department

    template_name = 'department/department_list.html'

    formset = DepartmentFormSet

    def get(self, request, *args, **kwargs):
        formset = self.formset()
        return render(request, self.template_name, {'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.formset(request.POST)
        if formset.is_valid():
            for form in formset:
                # Process the form data, save to the database, etc.
                form.save()

            return redirect('success_url')  # Redirect to a success page

        return render(request, self.template_name, {'formset': formset})

    form_class = DepartmentForm
    template_name = 'department/department_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

# Department Update View
class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/department_edit.html'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

# Department List View (Combining Create and List View)
class DepartmentListView(LoginRequiredMixin, CreateView):

    model = Department
    template_name = 'department/department_list.html'
    # context_object_name = 'departments'
    form_class = DepartmentForm
    formset = DepartmentFormSet
    
    # passing the formset to the template
    def get_context_data(self, **kwargs):
        kwargs['departments'] = Department.objects.order_by('company')
        return super(DepartmentListView, self).get_context_data(**kwargs)
    