from django.db import models

# Create your models here.

class Books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pages=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    profile_pic=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name

