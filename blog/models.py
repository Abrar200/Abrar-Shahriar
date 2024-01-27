from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=2000)
    client = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000, null=True)
    date = models.DateField()
    description = models.TextField()
    image1 = models.ImageField(upload_to = 'Images/')
    image2 = models.ImageField(upload_to = 'Images/')
    image3 = models.ImageField(upload_to = 'Images/')
    image4 = models.ImageField(upload_to = 'Images/')
    image5 = models.ImageField(upload_to = 'Images/')
    image6 = models.ImageField(upload_to = 'Images/', null=True)
    image7 = models.ImageField(upload_to = 'Images/', null=True)
    slug = models.SlugField()
    link = models.URLField()
	
    def __str__(self):
        return self.title
	
    def get_short_description(self):
        words = self.description.split()
        if len(words) > 10:
            short_description = ' '.join(words[:20]) + '...'
        else:
            short_description = self.description
        return short_description


class Post(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'Images/')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default='')
    keyword1 = models.CharField(max_length = 100, null=True)
    keyword2 = models.CharField(max_length = 100, null=True)
    keyword3 = models.CharField(max_length = 100, null=True)

    def __str__(self):
        return self.title
	
    def get_short_content(self):
        words = self.content.split()
        if len(words) > 30:
            short_content = ' '.join(words[:120]) + '...'
        else:
            short_content = self.content
        return short_content
     

class Certificates(models.Model):
    name = models.CharField(max_length = 1000, unique=True)
    institution = models.CharField(max_length = 1000)
    image = models.ImageField(upload_to = 'Images/')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name