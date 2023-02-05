from django.db import models

class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    
    def __str__(self):
        return self.title + ': ' + self.desc
