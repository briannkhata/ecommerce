from django.db import models

# Create your models here.
class Payment_Type(models.Model):
    payment_type_name = models.CharField(max_length=30)
    payment_type_id = models.PositiveBigIntegerField(primary_key=True)
    
    class Meta:
        db_table = 'payment_types' 

    def __str__(self):
        return self.payment_type_name
