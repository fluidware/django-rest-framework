from django.contrib import admin
from rest_framework.authtoken.models import APIKey


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)

admin.site.register(APIKey, APIKeyAdmin)
