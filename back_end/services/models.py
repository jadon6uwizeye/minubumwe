from django.db import models
from  django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model() 

class Sector(models.Model):
    sector = models.CharField(max_length=100)
    def __str__(self):
        return self.sector
    
class Request(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    genocide_survivor_certificate = models.FileField(upload_to='documents/')
    social_status_class = models.CharField(max_length=100)
    deprived_certificate = models.FileField(upload_to='documents/')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    message = models.TextField()
    approved =  models.BooleanField(default=False)

class SectorApprovedRequest(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    user =  models.ForeignKey(user, on_delete=models.CASCADE)
    genocide_survivor_certificate = models.FileField(upload_to='documents/')
    social_status_class = models.CharField(max_length=100)
    deprived_certificate = models.FileField(upload_to='documents/')
    message = models.TextField()
    approved =  models.BooleanField(default=False)

    
    

class ApprovedRequest(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    genocide_survivor_certificate = models.FileField(upload_to='documents/')
    social_status_class = models.CharField(max_length=100)
    deprived_certificate = models.FileField(upload_to='documents/')
    message = models.TextField()
    approved =  models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name 