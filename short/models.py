from django.db import models

# Shorurl Model
class Myurl(models.Model):
    longurl = models.URLField('Long URL',max_length=2048,blank=False,null=False,unique=True)
    shorturl = models.URLField('Short URL',max_length=2048,blank=False,null=False,unique=True)
    desc = models.CharField('Description',max_length=400,blank=False,null=False)

