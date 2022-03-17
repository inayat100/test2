from django.contrib import admin
from .models import user_details,Post,Category
# Register your models here.
# @admin.register(user_details)
# class userform(admin.ModelAdmin):
#     list_display = 'all'

admin.site.register(user_details)
admin.site.register(Post)
admin.site.register(Category)