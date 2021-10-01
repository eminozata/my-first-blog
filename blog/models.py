from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,null=True)
    text = models.TextField(null=True)
    img = models.ImageField(upload_to='post/',null=True,blank = True)
    created_date = models.DateTimeField(
            default=timezone.now,null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title



class ArchivePost(models.Model):
        author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
        title = models.CharField(max_length=200,null=True)
        text = models.TextField(null=True)
        img = models.ImageField(upload_to='archive/',null=True,blank = True)  
        created_date = models.DateTimeField(
                default=timezone.now,null=True)
        published_date = models.DateTimeField(
                blank=True, null=True)
        url = models.URLField(null=True)
        def publish(self):
            self.published_date = timezone.now()
            self.save()
        def __str__(self):
            return self.title       