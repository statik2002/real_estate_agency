from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInlines(admin.TabularInline):

    model = Owner.flats.through

    raw_id_fields = ('flat', 'owner')

    extra = 1


class FlatAdmin(admin.ModelAdmin):

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)

    search_fields = ('town', 'address',)

    readonly_fields = ('created_at', )

    list_filter = ('new_building', 'rooms_number', 'active', 'has_balcony')

    raw_id_fields = ('likes', )

    inlines = [OwnerInlines]


class ComplaintAdmin(admin.ModelAdmin):

    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
