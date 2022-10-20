from django.contrib import admin
from  .models import Noticia
# Register your models here.
class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")

admin.site.register(Noticia,NoticiasAdmin)