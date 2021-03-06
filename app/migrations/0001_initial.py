# Generated by Django 4.0.3 on 2022-03-29 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Bu yerda Menu nomini kiriting', max_length=500)),
            ],
            options={
                'verbose_name': 'Menu ',
                'verbose_name_plural': 'Menular ',
            },
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Mahsulot nomini kiriting', max_length=400)),
                ('desc', models.TextField(help_text='Mahsulot haqida qisqacha kiriting')),
                ('image', models.ImageField(upload_to='products')),
                ('cost', models.IntegerField(help_text='Mahsulot narxini kiriting')),
                ('menu', models.ForeignKey(help_text='Mahsulot qaysi turga kirishini tanlang', on_delete=django.db.models.deletion.CASCADE, to='app.menu')),
            ],
            options={
                'verbose_name': 'Mahsulot ',
                'verbose_name_plural': 'Mahsulotlar ',
            },
        ),
    ]
