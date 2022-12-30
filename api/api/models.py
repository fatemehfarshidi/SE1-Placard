from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Post(models.Model):
    TYPE_BORROW = 'B'
    TYPE_SELL = 'S'
    TYPE_COLLAB = 'C'

    TYPE_CHOICES = [
        (TYPE_BORROW, 'Borrow'),
        (TYPE_SELL, 'Sell'),
        (TYPE_COLLAB, 'Collab'),
    ]

    title = models.CharField(max_length=255)
    user_id = models.PositiveIntegerField()
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=TYPE_SELL)
    price = models.FloatField(null=True)
    description = models.TextField(null=True, blank=True)
    user_field = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title

class Picture(models.Model):
    # TO DO :
    # blob
    # id
    pass

class Post_Picture(models.Model):
    # TO DO :
    # post id
    # picture id
    pass

class User_Picture(models.Model):
    # TO DO :
    # user id
    # picture id
    pass

class Phone_number(models.Model):
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.phone_number


class Email(models.Model):
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.email


class User_Email(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class User_Phone_number(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(Phone_number, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

