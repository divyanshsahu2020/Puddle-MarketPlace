from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=120)
    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        verbose_name_plural='Items'
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    Name=models.CharField(max_length=120,null=False)
    Description=models.TextField(null=False)
    price=models.FloatField(default=0,null=False)
    is_sold=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='item_images',blank=True,null=True)

    def __str__(self):
        return self.Name
