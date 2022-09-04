from django.db import models
from datetime import datetime
# Create your models here.
class Data(models.Model):
    username = models.CharField(max_length=100,null=True)
    filename = models.CharField(max_length=100)
    addedfiles = models.FileField(upload_to='files')
    date = models.DateTimeField(default=datetime.now)
 
    def __str__(self):
        return self.username
    