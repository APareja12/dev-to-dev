from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField 

class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # post = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    score = models.IntegerField()
    create_date = models.DateField('Created Date')
    
    def __str__(self):
        return f'{self.get_comment_display()} on {self.date}'

    # class Meta:
    #     ordering = ('-date',)
        
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # comments = ManyToManyField(Comment)
    # topic = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    score = models.IntegerField()
    admin = models.BooleanField()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})

class Topic(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    date = models.DateField()


# class User(models.Model):
#     id = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.CharField(max_length=50)
#     username = models.TextField(max_length=250)
#     password = models.CharField(max_length=50)
#     is_admin = admin = models.BooleanField()

#     def __str__(self):
#         return self.id

#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'pk': self.id})



# Create your models here.