# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect

#import messages
from django.contrib import messages

#import loginrequired
from django.contrib.auth.decorators import login_required

from .serializers import DepartmentSerializer
from .models import Department
from .forms import DepartmentForm


# class DepartmentListView(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

#add login required to views

@login_required
def department_list(request):
    queryset = Department.objects.all()
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department:department_list')
    return render(request, 'department/department_list.html', {'queryset': queryset, 'form': form})

@login_required
def department_create(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('department:department_list')
    return render(request, 'department/department_list.html', {'form': form})

@login_required
def department_list(request):
    queryset = Department.objects.all()
    return render(request, 'department/department_list.html', {'queryset': queryset})

@login_required
def department_edit(request, pk):
    instance = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('department:department_list')
    return render(request, 'department/department_list.html', {'form': form})

@login_required
def department_delete(request, pk):
    instance = get_object_or_404(Department, pk=pk)
    instance.delete()
    return redirect('department:department_list')

@login_required
def department_update_all(request):
    if request.method == 'POST':
        user_company = request.user.company
        action = request.POST.get('action')

        if action == 'delete_selected':
            selected_rows = request.POST.getlist('selected_rows[]')
            Department.objects.filter(pk__in=selected_rows).delete()
        else:
            # Process existing rows
            for instance in Department.objects.all():
                department_name = request.POST.get(f'department_name_{instance.pk}')
                delete = request.POST.get(f'delete_{instance.pk}')

                if delete:
                    instance.delete()
                else:
                    if department_name:
                        instance.company = user_company
                        instance.department_name = department_name
                        instance.save()
                    else:
                        #show error message
                        messages.error(request, f'Error: Department name cannot be empty. Please enter a valid department name for row {instance.pk}.')

            # Process the data from the HTML table rows imported from Excel
            for i in range(int(request.POST.get('total_rows', 0))):
                department_name = request.POST.get(f'department_name_imported_{i}')

                if department_name:
                    Department.objects.create(company=user_company, department_name=department_name)

    return redirect('department:department_list')