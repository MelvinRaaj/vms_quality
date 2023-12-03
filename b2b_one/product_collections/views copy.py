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
from .forms import ProductCollectionForm, ProductForm, ProductFormSet

@login_required
def product_collections_list(request):
    queryset = ProductCollection.objects.all()
    form = ProductCollectionForm()
    if request.method == 'POST':
        form = ProductCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_collections:product_collections_list')
    return render(request, 'product_collections/product_collections_list.html', {'queryset': queryset, 'form': form})

class ProductCollectionCreate(LoginRequiredMixin, CreateView):
    #create view for ProductCollection
    model = ProductCollection
    form_class = ProductCollectionForm
    queryset = ProductCollection.objects.all()
    template_name = 'product_collections/product_collections_create.html'
    success_url = '/product_collections/'
            
@login_required
def product_collections_delete(request, pk):
    instance = get_object_or_404(ProductCollection, pk=pk)
    instance.delete()
    return redirect('product_collections:product_collections_list')

@login_required
def product_collections_update_all(request):
    if request.method == 'POST':
        # user_company = request.user.company
        action = request.POST.get('action')
        print(action)

        if action == 'delete_selected':
            selected_rows = request.POST.getlist('selected_rows[]')
            ProductCollection.objects.filter(pk__in=selected_rows).delete()
        else:
            # Process existing rows
            for instance in ProductCollection.objects.all():
                product_collections_name = request.POST.get(f'ProductCollection_Name_{instance.pk}')
                print(product_collections_name)
                delete = request.POST.get(f'delete_{instance.pk}')

                if delete:
                    instance.delete()
                else:
                    if product_collections_name:
                        #save all fields in form
                        instance.ProductCollection_Name = product_collections_name
                        instance.ProductCollection_Description = request.POST.get(f'ProductCollection_Description_{instance.pk}')
                        instance.CreateDate = request.POST.get(f'CreateDate_{instance.pk}')
                        instance.LaunchDate = request.POST.get(f'LaunchDate_{instance.pk}')
                        #save image if any
                        if request.FILES.get(f'ProductCollection_Image_{instance.pk}'):
                            instance.ProductCollection_Image = request.FILES.get(f'ProductCollection_Image_{instance.pk}')
                        instance.save()
                    else:
                        #show error message
                        messages.error(request, f'Error: Collection name cannot be empty. Please enter a valid collection name for row {instance.pk}.')

            # Process the data from the HTML table rows imported from Excel
            for i in range(int(request.POST.get('total_rows', 0))):
                product_collections_name = request.POST.get(f'product_collections_name_imported_{i}')

                if product_collections_name:
                    ProductCollection.objects.create(product_collections_name=product_collections_name)

    return redirect('product_collections:product_collections_list')

@login_required
def product_collections_update(request, pk):
    # queryset filter based on product collection name
    queryset = Products.objects.filter(ProductCollection_Name=pk)
    product_collection = get_object_or_404(ProductCollection, pk=pk)

    # Use inlineformset_factory to handle the relationship between ProductCollection and Products
    ProductFormSet = inlineformset_factory(ProductCollection, Products, form=ProductForm, extra=0)

    if request.method == 'POST':
        form = ProductCollectionForm(request.POST, instance=product_collection)
        formset = ProductFormSet(request.POST, instance=product_collection)

        if form.is_valid() and formset.is_valid():
            form.save()
            
            # Loop through the forms in the formset
            for product_form in formset:
                if product_form.has_changed():
                    product_name = product_form.cleaned_data.get('Product_Name')
                    # Check if a product with the same name exists for this collection
                    product, created = Products.objects.get_or_create(ProductCollection_Name=product_collection, Product_Name=product_name)
                    if not created:
                        # Update the existing product with the form data
                        product_form.instance = product
                        product_form.save()

            return redirect('product_collections:product_collections_list')
    else:
        form = ProductCollectionForm(instance=product_collection)
        formset = ProductFormSet(instance=product_collection)

    return render(
        request,
        'product_collections/product_collections_update.html',
        {'form': form, 'formset': formset, 'queryset': queryset, 'pk': pk}
    )

def products_update_all(request):
    if request.method == 'POST':
        user_company = request.user.company
        action = request.POST.get('action')

        if action == 'delete_selected':
            selected_rows = request.POST.getlist('selected_rows[]')
            Products.objects.filter(pk__in=selected_rows).delete()
        else:
            # Process existing rows
            for instance in Products.objects.all():
                products = request.POST.get(f'Product_Name_{instance.pk}')
                Product_Name = request.POST.get(f'Product_Name_{instance.pk}')
                Product_Description = request.POST.get(f'Product_Description_{instance.pk}')
                CreateDate = request.POST.get(f'CreateDate_{instance.pk}')
                LaunchDate = request.POST.get(f'LaunchDate_{instance.pk}')
                SKU = request.POST.get(f'SKU_{instance.pk}')
                item_code = request.POST.get(f'item_code_{instance.pk}')
                cbm_unit = request.POST.get(f'cbm_unit_{instance.pk}')
                weight_unit = request.POST.get(f'weight_unit_{instance.pk}')
                Design_Name = request.POST.get(f'Design_Name_{instance.pk}')
                Color_Name = request.POST.get(f'Color_Name_{instance.pk}')
                UOM = request.POST.get(f'UOM_{instance.pk}')
                UOM1 = request.POST.get(f'UOM1_{instance.pk}')
                barcode = request.POST.get(f'barcode_{instance.pk}')
                Product_Status = request.POST.get(f'Product_Status_{instance.pk}')
                status_date = request.POST.get(f'status_date_{instance.pk}')
                delete = request.POST.get(f'delete_{instance.pk}')

                if delete:
                    instance.delete()
                else:
                    for i in range(int(request.POST.get('total_rows', 0))):
                        if products:
                            instance.Product_Name = Product_Name
                            instance.Product_Description = Product_Description
                            instance.CreateDate = CreateDate
                            instance.LaunchDate = LaunchDate
                            instance.SKU = SKU
                            instance.item_code = item_code
                            instance.cbm_unit = cbm_unit
                            instance.weight_unit = weight_unit
                            instance.Design_Name = Design_Name
                            instance.Color_Name = Color_Name
                            instance.UOM = UOM
                            instance.UOM1 = UOM1
                            instance.barcode = barcode
                            instance.Product_Status = Product_Status
                            instance.status_date = status_date
                            instance.save()
                        else:
                            #show error message
                            messages.error(request, f'Error: Product name cannot be empty. Please enter a valid name for row {instance.pk}.')

    return redirect('product_collections:product_collections_list')

# # create view for products_update_all
# @login_required
# def products_update_all(request):
#     if request.method == 'POST':
#         # user_company = request.user.company
#         action = request.POST.get('action')
#         print(action)

#         if action == 'delete_selected':
#             selected_rows = request.POST.getlist('selected_rows[]')
#             Products.objects.filter(pk__in=selected_rows).delete()
#         else:
#             # Process existing rows
#             for instance in Products.objects.all():
#                 product_name = request.POST.get(f'Product_Name_{instance.pk}')
#                 print(product_name)
#                 delete = request.POST.get(f'delete_{instance.pk}')

#                 if delete:
#                     instance.delete()
#                 else:
#                     if product_name:
#                         #save all fields in form
#                         instance.Product_Name = product_name
#                         instance.Product_Description = request.POST.get(f'Product_Description_{instance.pk}')
#                         instance.CreateDate = request.POST.get(f'CreateDate_{instance.pk}')
#                         instance.LaunchDate = request.POST.get(f'LaunchDate_{instance.pk}')
#                         instance.SKU = request.POST.get(f'SKU_{instance.pk}')
#                         instance.item_code = request.POST.get(f'item_code_{instance.pk}')
#                         instance.cbm_unit = request.POST.get(f'cbm_unit_{instance.pk}')
#                         instance.weight_unit = request.POST.get(f'weight_unit_{instance.pk}')
#                         instance.Design_Name = request.POST.get(f'Design_Name_{instance.pk}')
#                         instance.Color_Name = request.POST.get(f'Color_Name_{instance.pk}')
#                         instance.UOM = request.POST.get(f'UOM_{instance.pk}')
#                         instance.UOM1 = request.POST.get(f'UOM1_{instance.pk}')
#                         instance.barcode = request.POST.get(f'barcode_{instance.pk}')
#                         instance.Product_Status = request.POST.get(f'Product_Status_{instance.pk}')
#                         instance.status_date = request.POST.get(f'status_date_{instance.pk}')
#                         #save image if any
#                         if request.FILES.get(f'Product_Image_{instance.pk}'):
#                             instance.Product_Image = request.FILES.get(f'Product_Image_{instance.pk}')
#                         instance.save()
#                     else:
#                         #show error message
#                         messages.error(request, f'Error: Product name cannot be empty. Please enter a valid product name for row {instance.pk}.')

#     # redirect to same page
#     return redirect('product_collections:product_collections_list')
