from django.contrib import admin
from .models import member_data, admin_data

admin.site.register(member_data)
admin.site.register(admin_data)
