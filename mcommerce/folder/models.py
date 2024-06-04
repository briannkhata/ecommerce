from django.db import models

# Create your models here.
class Folder(models.Model):
    folder_name = models.CharField(max_length=30)
    folder_id = models.PositiveBigIntegerField(primary_key=True)
    
    class Meta:
        db_table = 'folders' 

    def __str__(self):
        return self.folder_name
