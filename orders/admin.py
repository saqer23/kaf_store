from django.contrib import admin
from .models import Order,OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','address','phone_no','city',)
    list_filter = ('created','paid','update')
    search_fields = ['first_name','last_name','phone_no']
    inlines = [
        OrderItemAdmin,
    ]
admin.site.register(Order,OrderAdmin)