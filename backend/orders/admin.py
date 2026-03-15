from django.contrib import admin
from .models import CustomerOrder
import csv
from django.http import HttpResponse

@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','country','product','quantity','unit_price','total_amount','status','created_by','created_at')
    change_list_template='admin/orders_changelist.html'
