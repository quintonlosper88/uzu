from django.contrib import admin
from .models import UserModel
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'employeeID', 'email','position', 'display_qr_code')

    def display_qr_code(self, obj):
        if obj.qr_code:
            return '<img src="{url}" width="100" height="100" />'.format(url=obj.qr_code.url)
        else:
            return 'No QR Code'

    display_qr_code.short_description = 'QR Code'
    display_qr_code.allow_tags = True

admin.site.register(UserModel, UserModelAdmin)

from .models import Timesheet

class TimesheetAdmin(admin.ModelAdmin):
    list_display = ['user', 'enter_time', 'leave_time']
    list_filter = ['user', 'enter_time']
    search_fields = ['user__employeeID', 'user__firstName', 'user__lastName']

admin.site.register(Timesheet, TimesheetAdmin)
