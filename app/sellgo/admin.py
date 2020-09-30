from django.contrib import admin

from .models import CsvProduct, Customer

admin.site.register(Customer)
admin.site.register(CsvProduct)
