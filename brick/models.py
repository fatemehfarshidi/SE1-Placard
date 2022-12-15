from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Post(models.Model):
    TYPE_BORROW = 'B'
    TYPE_SELL = 'S'

    TYPE_CHOICES = [
        (TYPE_BORROW, 'Borrow'),
        (TYPE_SELL, 'Sell'),
    ]


    title = models.CharField(max_length=255)
    user_id = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=1, choices=TYPE_CHOICES, default=TYPE_SELL)
        
