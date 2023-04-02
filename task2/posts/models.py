from django.db import models
from django.urls import reverse
from django.conf import settings

from accounts.models import User
# Create your models here.
POST_CATEGORIES = (
    ('Mental health','Mental health'),
    ('Heart disease','Heart disease'),
    ('Covid19','Covid19'),
    ('Immunization','Immunization'),
)

from django.contrib.auth import get_user_model
Users = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=256)
    image = models.ImageField(upload_to='post_image/', blank=True)
    category = models.CharField(max_length=32, choices=POST_CATEGORIES, default='Mental health', null=False)
    summary = models.TextField(max_length=256)
    content = models.TextField(max_length=1024)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.content_html = self.content
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','title']
