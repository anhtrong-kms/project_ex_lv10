from django.db import models

# Create your models here.
class Category (models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length= 200)
    image = models.ImageField(null= True)
    date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.name
class Product(models.Model):
    Category = models.ManyToManyField(Category, related_name='productss')
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True)
    detal = models.TextField()
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(null= True, default=0)

    def __str__(self):
        return self.name