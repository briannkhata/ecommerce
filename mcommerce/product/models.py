from django.db import models
from django.utils import timezone
from category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, to_field='category_id', related_name='product', on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    
    class Meta:
        db_table = 'products' 
    
    def __str__(self):
        return self.name