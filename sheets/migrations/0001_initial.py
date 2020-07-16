# Generated by Django 2.1.7 on 2019-03-10 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, verbose_name='Имя категории')),
            ],
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID записи')),
                ('subcategory_id', models.IntegerField(verbose_name='ID подкатегории')),
                ('lesson_nums', models.TextField(blank=True, verbose_name='Номер урока')),
                ('lesson_name', models.TextField(blank=True, verbose_name='Название урока')),
                ('sheet_url', models.TextField(blank=True, verbose_name='Ссылка на листок')),
                ('author', models.TextField(blank=True, verbose_name='Автор листка')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, verbose_name='Имя подкатегории')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheets.Categories')),
            ],
        ),
    ]