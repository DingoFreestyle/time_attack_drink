#user/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True),
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Drink(models.Model):
    class Meta:
        db_table = "Drink_list"

    drink_name = models.CharField(max_length=20, null=False),
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    nutrient_info = models.TextField()
    alergy_info = models.TextField()

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/product/{self.pk}/'