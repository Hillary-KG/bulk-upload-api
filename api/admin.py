from django.contrib import admin
from .models import UserRecord


# Register your models here.
class UserRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserRecord._meta.fields if field != "id"]


admin.site.register(UserRecord, UserRecordAdmin)
