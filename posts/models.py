from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime, date

#User = get_user_model()

# Create your models here.

class Post(models.Model):
    #author_id = models.AutoField(primary_key=True, default=1)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank = True, null = True)
    #image = models.FileField(upload_to='images/', blank = True, null = True)
    #post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.content + ' | ' + str(self.id)
    #def get_absolute_url(self):
        #return reverse('item-detail', args=(str(self.id)))
    #    return reverse('home')

class Stock(models.Model):
    #author_id = models.AutoField(primary_key=True, default=1)
    ticker = models.CharField(max_length=10)
    
    def __str__(self):
        return self.ticker
