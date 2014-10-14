from django.contrib import admin

# Register your models here.
import models

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.User)