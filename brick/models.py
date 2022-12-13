from django.db import models

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
        
