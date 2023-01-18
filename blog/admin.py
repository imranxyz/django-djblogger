from django.contrib.auth.models import User, Group
from django.contrib import admin
from blog import models


@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "status", "created_at"]


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "Djblogger Admin Panel"
# admin.site.site_title = ""
# admin.site.index_title = ""