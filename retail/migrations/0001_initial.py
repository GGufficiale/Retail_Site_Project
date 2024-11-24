# Generated by Django 5.1.3 on 2024-11-23 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Введите имэйл', max_length=100, verbose_name='Email')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('house_number', models.IntegerField(verbose_name='№ дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите продукт', max_length=100, verbose_name='Наименование продукта')),
                ('description', models.CharField(blank=True, help_text='Введите описание продукта', max_length=1000, null=True, verbose_name='Описание')),
                ('model', models.CharField(blank=True, help_text='Введите модель продукта', max_length=1000, null=True, verbose_name='Модель')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='retail/photo', verbose_name='Фото продукта')),
                ('price', models.IntegerField(help_text='Введите цену продукта', verbose_name='Цена')),
                ('manufactured_at', models.DateField(blank=True, help_text='Введите дату выхода продукта на рынок', null=True, verbose_name='Дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name', 'description', 'model', 'price'],
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название завода', max_length=100, verbose_name='Название завода')),
                ('debt', models.DecimalField(decimal_places=2, help_text='Укажите долг перед поставщиком', max_digits=10, verbose_name='Долг перед поставщиком')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания записи в БД')),
                ('contact', models.ForeignKey(blank=True, help_text='Укажите контакт завода', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.contacts', verbose_name='Контакт завода')),
                ('product', models.ForeignKey(blank=True, help_text='Укажите продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводы',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите розничную сеть', max_length=100, verbose_name='Название розничной сети')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, help_text='Укажите долг перед поставщиком', max_digits=10, null=True, verbose_name='Долг перед поставщиком')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания записи в БД')),
                ('contact', models.ForeignKey(blank=True, help_text='Укажите контакт розничной сети', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.contacts', verbose_name='Контакт розничной сети')),
                ('factory_supplier', models.ForeignKey(blank=True, help_text='Укажите завод-поставщик', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.factory', verbose_name='Завод-поставщик')),
                ('product', models.ForeignKey(blank=True, help_text='Укажите продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование ИП', max_length=100, verbose_name='Наименование ИП')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, help_text='Укажите долг перед поставщиком', max_digits=10, null=True, verbose_name='Долг перед поставщиком')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания записи в БД')),
                ('contact', models.ForeignKey(blank=True, help_text='Укажите Контакт ИП', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.contacts', verbose_name='Контакт ИП')),
                ('factory_supplier', models.ForeignKey(blank=True, help_text='Укажите завод-поставщик', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.factory', verbose_name='Завод-поставщик')),
                ('product', models.ForeignKey(blank=True, help_text='Укажите продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.product', verbose_name='Продукт')),
                ('retail_network_supplier', models.ForeignKey(blank=True, help_text='Укажите розничную сеть-поставщик', null=True, on_delete=django.db.models.deletion.SET_NULL, to='retail.retailnetwork', verbose_name='Розничная сеть-поставщик')),
            ],
            options={
                'verbose_name': 'ИП',
                'verbose_name_plural': 'Ипешечки',
            },
        ),
    ]