from django.db import models

# Create your models here.
class Plan(models.Model):
    plan_name = models.CharField(max_length=30)
    plan_id = models.PositiveBigIntegerField(primary_key=True)
    
    class Meta:
        db_table = 'plans' 

    def __str__(self):
        return self.plan_name
