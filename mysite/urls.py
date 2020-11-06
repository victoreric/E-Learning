from django.contrib import admin
from django.urls import path, include

from .views import index
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('kursus/', include('kursus.urls', namespace="kursus")),
    path('',index, name="index"),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = "ИРсМ Администратор"
admin.site.site_title = "ИРсМ Администратор Портал"
admin.site.index_title = "Добро пожаловать на исследовательский портал ИРсМ"
