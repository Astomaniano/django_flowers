from django.contrib import admin
from .models import ManageOrder

class ManageOrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_id', 'phone_number', 'first_name', 'last_name', 'user_comment')
    fields = ('status', 'manager_comment', 'order_id', 'phone_number', 'first_name', 'last_name', 'user_comment')
    list_filter = ('status',)

admin.site.register(ManageOrder, ManageOrderAdmin)

