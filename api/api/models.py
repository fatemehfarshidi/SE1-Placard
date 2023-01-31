from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.utils.text import slugify
from django.contrib.humanize.templatetags import humanize
# from googletrans import Translator
# from google_trans_new import google_translator


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    STATUS_CHOICES = [
        ('A', 'نو'),
        ('B', 'در حد نو'),
        ('C', 'کارکرده'),
    ]

    TYPE_CHOICES = [
        ('Sell', 'خرید و فروش'),
        ('StudyBuddy', 'تیم سازی '),
    ]

    title = models.CharField(max_length=50)
    post_type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='Sell')
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='A')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=200, null=True, blank=True)
    contact_info = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(
        gettext_lazy("Image"), upload_to=upload_to, default='media/nopicture.png', null=True)
    slug = models.SlugField(max_length=50, blank=True)
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

    def get_date(self):
        # translator = Translator(service_urls=['translate.googleapis.com'])
        # date = humanize.naturaltime(self.date_created)
        # date_fa = translator.translate(date, dest='fa', src='en').text()
        # return date_fa

        # translator = google_translator()
        # date = humanize.naturaltime(self.date_created)
        # date_fa = translator.translate(date, lang_src='en', lang_tgt='fa')
        # return date_fa
        return humanize.naturaltime(self.date_created)

    def get_price(self):
        return humanize.intcomma(self.price)
