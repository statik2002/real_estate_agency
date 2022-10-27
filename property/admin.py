from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)

    search_fields = ('town', 'address', 'owner')

    readonly_fields = ('created_at', )

    list_filter = ('new_building', 'rooms_number', 'active', 'has_balcony')


admin.site.register(Flat, FlatAdmin)
