from django import forms
from django.forms import inlineformset_factory

from .models import (
    ShoppingList, ShoppingListItem, bedlinen_fabrics, SL_Samples
)

class Shopping_List_Form(forms.ModelForm):

    class Meta:
        model = ShoppingList
        fields = '__all__'


class Shopping_List_Item_Form(forms.ModelForm):

    class Meta:
        model = ShoppingListItem
        fields = '__all__'

    # add form helper for dates
    expected_recieve_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    launch_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    

class SL_Samples_Form(forms.ModelForm):

    class Meta:
        model = SL_Samples
        fields = '__all__'

    # add form helper for dates
    sample_send_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    status_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


Shopping_List_Item_FormSet = inlineformset_factory(
    ShoppingList, ShoppingListItem, form=Shopping_List_Item_Form,
    extra=0, can_delete=True, can_delete_extra=True
)


SL_Samples_Form_FormSet = inlineformset_factory(
    ShoppingList, SL_Samples, form=SL_Samples_Form,
    extra=0, can_delete=True, can_delete_extra=True
)

class Bedlinen_Fabric_Form(forms.ModelForm):

    class Meta:
        model = bedlinen_fabrics
        fields = '__all__'


# class Shopping_List_Item_FormSet(inlineformset_factory(Shopping_List, Shopping_List_Item, form=Shopping_List_Item_Form, extra=1, can_delete=True, can_delete_extra=True)):
#     def __init__(self, *args, **kwargs):
#         collection_instance = kwargs.pop('collection_instance', None)
#         super(Shopping_List_Item_FormSet, self).__init__(*args, **kwargs)
#         if collection_instance:
#             # Limit product_sku choices to those belonging to the selected collection
#             self.forms[0].fields['product_sku'].queryset = Product_SKU.objects.filter(Collection_Name=collection_instance)