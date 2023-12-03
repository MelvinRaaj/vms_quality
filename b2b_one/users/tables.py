from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

from django.utils.html import escape
from .models import CustomUser



# Create your views here.

class UserListTable(BaseDatatableView, LoginRequiredMixin):
    pass
    # The model we're going to show
    # model = CustomUser

    # # define the columns that will be returned
    # columns = ['username','company','email','phone', 'user_role']

    # # define column names that will be used in sorting
    # # order is important and should be same as order of columns
    # # displayed by datatables. For non-sortable columns use empty
    # # value like ''
    # columns = ['username','company','email','phone', 'user_role']

    # # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # # and make it return huge amount of data
    # max_display_length = 500

    # # def render_column(self, row, column):
    # #     # We want to render user as a custom column
    # #     if column == 'user':
    # #         # escape HTML for security reasons
    # #         return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
    # #     else:
    # #         return super(OrderListJson, self).render_column(row, column)

    # def filter_queryset(self, qs):
    #     # use parameters passed in GET request to filter queryset
    
    #     # simple example:
    #     search = self.request.GET.get('company_name', None)
    #     if search:
    #         qs = qs.filter(company__iexact=search)

    #     # # more advanced example using extra parameters
    #     # filter_customer = self.request.GET.get('customer', None)

    #     # if filter_customer:
    #     #     customer_parts = filter_customer.split(' ')
    #     #     qs_params = None
    #     #     for part in customer_parts:
    #     #         q = Q(customer_firstname__istartswith=part) | Q(customer_lastname__istartswith=part)
    #     #         qs_params = qs_params | q if qs_params else q
    #     #     qs = qs.filter(qs_params)
    #     # return qs

    # def get_initial_queryset(self):
    #     # if self.request.user.user_role != 'Management':
    #     #     return CustomUser.objects.filter(~Q(user_role="NEW"))
    #     # else:
    #         return CustomUser.objects.all()        

