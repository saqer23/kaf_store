from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20,label='الاسم الاول')
    last_name = forms.CharField(max_length=20,label='الاسم الاخير')
    address = forms.CharField(max_length=200,label='رابط العنوان من google map')
    phone_no = forms.IntegerField(label='رقم الجوال')
    city = forms.CharField(max_length=20)
    class Meta:
        model = Order
        fields = list_display = ('first_name','last_name','address','phone_no','city',)