from django.shortcuts import render, redirect, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from django.contrib import messages

from allauth.account.views import SignupView, LoginView, EmailVerificationSentView
from allauth.account import app_settings, signals

from .models import Department
from .forms import DepartmentForm, DepartmentFormSet



# Department List View (Combining Create and List View)
class DepartmentListView(LoginRequiredMixin, CreateView):

    model = Department
    template_name = 'department/department_list.html'
    form_class = DepartmentForm
    formset = DepartmentFormSet

    def get_context_data(self, **kwargs):
        kwargs['departments'] = Department.objects.order_by('company')
        return super(DepartmentListView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        formset = self.formset(request.POST)
        if formset.is_valid():
            for form in formset:
                # Process the form data, save to the database, etc.
                form.save()

            return redirect('success_url')  # Redirect to a success page

        else:
            # throw an error message
            messages.error(request, "Error")


        return render(request, self.template_name, {'formset': formset})
