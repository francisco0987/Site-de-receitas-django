from django.contrib.auth.models import User
from django.db import models

# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_step = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    # cria data automatica
    created_at = models.DateTimeField(auto_now_add=True)
    # atualiza a data
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, default='')

    # ligando tabelas
    category = models.ForeignKey(
        # se a categoria for apagada os dados não seram apagados
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

