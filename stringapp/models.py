from django.db import models

# Create your models here.
class StringData(models.Model):
    string_data =models.TextField(null=False,blank=False)

class StringDataActivitylog(models.Model):
    strind_data_id = models.ForeignKey(StringData,on_delete=models.CASCADE)
    operation_performed=models.CharField(max_length=15)
    transformed_string_data = models.TextField()
