from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','price','realtor','list_date')
    list_editable=('is_published',)
    search_fields=('title','price','description')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)