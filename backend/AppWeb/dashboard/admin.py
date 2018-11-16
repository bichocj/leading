from django.contrib import admin
from . import models

admin.site.register(models.Page)


class LeadAdmin(admin.ModelAdmin):
    model = models.Lead
    list_display = ('page', 'leadgen_id', 'first_name', 'last_name', 'phone_number', 'created_at',)


admin.site.register(models.Lead, LeadAdmin)
