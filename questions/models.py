from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, blank=False)


class Question(models.Model):
    title =  models.CharField(max_length=100, null=False, blank=False)
    question = models.CharField(max_length=3000)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
