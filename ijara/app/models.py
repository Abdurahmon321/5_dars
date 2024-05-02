from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Home(models.Model):
    address = models.CharField(max_length=255)
    img = models.ImageField(upload_to="home/")
    price = models.IntegerField()
    description = models.TextField()
    area = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.address
