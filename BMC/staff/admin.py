from django.contrib import admin
from staff.models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    sortable_by = 'id'  # field 'id' sorted by descending order
    search_fields = ['name', 'address']  # list of fields search in admin table
    list_display = ('name', 'address','is_active','age')
    list_display_links = ('name',)

admin.site.register(Employee,EmployeeAdmin)

# admin header and title modification
admin.site.site_header = "Admin DashBoard"
admin.site.site_title = "BMC"
admin.site.index_title = ''