from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_id = models.PositiveBigIntegerField(primary_key=True)
    
    class Meta:
        db_table = 'categories' 

    def __str__(self):
        return self.category_name
