from django.db import models

class Students(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    state = models.CharField(max_length=255, null=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.fname} {self.lname}'
    
