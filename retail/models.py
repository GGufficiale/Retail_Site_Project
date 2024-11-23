from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}  # форма, если параметр необязателен


class Contacts(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Email', help_text="Введите имэйл")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="№ дома")

    def __str__(self):
        return f"{self.country} {self.city} {self.street} {self.house_number}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование продукта', help_text="Введите продукт")
    description = models.CharField(max_length=1000, verbose_name='Описание', help_text="Введите описание продукта",
                                   **NULLABLE)
    model = models.CharField(max_length=1000, verbose_name='Модель', help_text="Введите модель продукта", **NULLABLE)
    photo = models.ImageField(upload_to='retail/photo', verbose_name="Фото продукта", **NULLABLE)
    price = models.IntegerField(verbose_name='Цена', help_text="Введите цену продукта")
    manufactured_at = models.DateField(**NULLABLE, verbose_name='Дата выхода продукта на рынок',
                                       help_text="Введите дату выхода продукта на рынок")

    def __str__(self):
        return f'{self.name}: {self.description}. Модель:{self.model}. Цена: {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'description', 'model', 'price']
        # Поля для функционала прав доступа - варианты редактирования
        # permissions = [
        #     ('cancel_publication', 'Can cancel publication'),
        #     ('edit_description', 'Can edit description'),
        #     ('change_category', 'Can change category'),
        # ]


class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название завода', help_text="Введите название завода")
    contact = models.ForeignKey(Contacts, verbose_name='Контакт завода', help_text='Укажите контакт завода', **NULLABLE,
                                on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name='Продукт', help_text='Укажите продукт', **NULLABLE,
                                on_delete=models.SET_NULL)
    debt = models.DecimalField(verbose_name='Долг перед поставщиком', help_text='Укажите долг перед поставщиком',
                               max_digits=10, decimal_places=2)
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания записи в БД', auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.contact}"

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class RetailNetwork(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название розничной сети', help_text="Введите розничную сеть")
    contact = models.ForeignKey(Contacts, verbose_name='Контакт розничной сети',
                                help_text='Укажите контакт розничной сети', **NULLABLE, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name='Продукт', help_text='Укажите продукт', **NULLABLE,
                                on_delete=models.SET_NULL)
    factory_supplier = models.ForeignKey(Factory, verbose_name='Завод-поставщик', help_text='Укажите завод-поставщик',
                                         **NULLABLE, on_delete=models.SET_NULL)
    debt = models.DecimalField(verbose_name='Долг перед поставщиком', help_text='Укажите долг перед поставщиком',
                               max_digits=10, decimal_places=2, **NULLABLE)
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания записи в БД', auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.contact}"

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class IP(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование ИП', help_text="Введите наименование ИП")
    contact = models.ForeignKey(Contacts, verbose_name='Контакт ИП', help_text='Укажите Контакт ИП', **NULLABLE,
                                on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name='Продукт', help_text='Укажите продукт', **NULLABLE,
                                on_delete=models.SET_NULL)
    factory_supplier = models.ForeignKey(Factory, verbose_name='Завод-поставщик', help_text='Укажите завод-поставщик',
                                         **NULLABLE, on_delete=models.SET_NULL)
    retail_network_supplier = models.ForeignKey(RetailNetwork, verbose_name='Розничная сеть-поставщик',
                                                help_text='Укажите розничную сеть-поставщик', **NULLABLE,
                                                on_delete=models.SET_NULL)
    debt = models.DecimalField(verbose_name='Долг перед поставщиком', help_text='Укажите долг перед поставщиком',
                               max_digits=10, decimal_places=2, **NULLABLE)
    created_at = models.DateField(**NULLABLE, verbose_name='Дата создания записи в БД', auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.contact}"

    class Meta:
        verbose_name = "ИП"
        verbose_name_plural = "Ипешечки"
