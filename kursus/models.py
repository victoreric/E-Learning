from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

class Materi(models.Model):
    judul       = models.CharField(max_length=255, verbose_name="название")
    isi         = RichTextUploadingField( verbose_name="Содержимые")
    # isi         = models.TextField()
    kategori    = models.CharField(max_length=100, verbose_name = "категория")
    published   = models.DateTimeField(auto_now_add=True, verbose_name="Опубликование")
    update      = models.DateTimeField(auto_now=True, verbose_name="Обновить")
    penulis     = models.CharField(max_length=255, verbose_name="Автор")
    slug        = models.SlugField(blank=True, editable=False)

    class Meta :
        verbose_name_plural = "Статьи"

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

     # related with CreateView, when saving  
    # # def get_absolute_url(self):
    #     return reverse("kursus:detail", kwargs={"pk": self.pk})
    

    # def __str__ (self):
    #     return "{}. {}". format(self.id, self.judul)  

     