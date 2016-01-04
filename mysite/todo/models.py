from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Item(models.Model):
    item_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    due_date = models.DateTimeField('due date')
    done = models.BooleanField('done')

    def __str__(self):
        return self.item_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class User(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username
