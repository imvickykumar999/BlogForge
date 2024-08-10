
from django.contrib import admin
from .models import Domaindata

class DomaindataAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'url1', 'min_count', 'max_count', 'url2')
    search_fields = ('keyword', 'url1', 'url2')
    list_filter = ('min_count', 'max_count')

admin.site.register(Domaindata, DomaindataAdmin)
