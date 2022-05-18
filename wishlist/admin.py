from django.contrib import admin
from .models import Wishlist, WishlistItem


class ProductInline(admin.StackedInline):
    model = WishlistItem


class WishlistAdmin(admin.ModelAdmin):
    inlines = [ProductInline, ]


admin.site.register(Wishlist, WishlistAdmin)