from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to='media/',blank =True)
    caption = models.CharField(max_length =250)
    post = models.TextField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)        
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_title(cls, search_term):
        cfc = cls.objects.filter(title__icontains=search_term)
        return cfc

    def __str__(self):
        return self.title

class Sermon(models.Model):
    title = models.CharField(max_length =100)        
    

class Image(models.Model):
    image = models.ImageField(upload_to='media/', blank= True) 
    description = models.CharField(max_length =500)       

    def __str__(self):
        return self.description