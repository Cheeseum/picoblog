from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['title', 'content']}),
        ('Date',    {'fields': ['date'], 'classes': ['collapse']}),
    ]

    def save_model(self, request, obj, form, change):
        if request.user.is_authenticated():
            obj.author = request.user
            obj.save()

admin.site.register(Post, PostAdmin)
