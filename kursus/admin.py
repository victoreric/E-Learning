from django.contrib import admin

# Register your models here.

from .models import Materi

class MateriAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'published',
        'update',
    ]
    list_display = ('id','judul', 'kategori', 'penulis')
    search_fields = ('judul', 'kategori', 'penulis')


admin.site.register(Materi, MateriAdmin)