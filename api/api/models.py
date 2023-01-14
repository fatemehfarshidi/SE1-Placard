from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.utils.text import slugify


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    TYPE_CHOICES = [
        ('Borrow', 'Borrow'),
        ('Sell', 'Sell'),
        ('Collab', 'Collab'),
    ]

    CONTACT_CHOICES = [
        ('Phone number', 'Phone number'),
        ('Telegram', 'Telegram'),
        ('Email', 'Email'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=250)
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='Sell')
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    contact_type = models.CharField(
        max_length=20, choices=CONTACT_CHOICES, default='Phone number')
    contact_info = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(
        gettext_lazy("Image"), upload_to=upload_to, default='posts/default.jpg', null=True)
    slug = models.SlugField(
        max_length=250, unique=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-date_created',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
