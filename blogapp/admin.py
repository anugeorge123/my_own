from django.contrib import admin
from .models import Realuser,Category,Type,Ingredients,Recipe,Review

admin.site.register(Realuser, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Type, admin.ModelAdmin)
admin.site.register(Ingredients, admin.ModelAdmin)
admin.site.register(Recipe, admin.ModelAdmin)
admin.site.register(Review, admin.ModelAdmin)
