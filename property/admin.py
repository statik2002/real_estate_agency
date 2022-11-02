from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInlines(admin.TabularInline):

    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')
    extra = 1


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):

    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at', )
    list_filter = ('new_building', 'rooms_number', 'active', 'has_balcony')
    raw_id_fields = ('likes', )

    inlines = [OwnerInlines]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats', )


