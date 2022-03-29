from tabnanny import verbose
from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=500,help_text="Bu yerda Menu nomini kiriting")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Menu '
        verbose_name_plural="Menular "


class Mahsulot(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,help_text="Mahsulot qaysi turga kirishini tanlang")
    title=models.CharField(max_length=400,help_text="Mahsulot nomini kiriting")
    desc=models.TextField(help_text="Mahsulot haqida qisqacha kiriting")
    image=models.ImageField(upload_to='products')
    cost=models.IntegerField(help_text="Mahsulot narxini kiriting")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Mahsulot '
        verbose_name_plural="Mahsulotlar "
