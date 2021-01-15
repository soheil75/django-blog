from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class PublishArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = 'publish')

class Article(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('publish','Publish')
    )

    writer = models.ForeignKey(User,on_delete= models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150 ,unique=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS,default='draft')
    objects = models.Manager()
    published = PublishArticleManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:article_detail", args=[self.id,self.slug])
    