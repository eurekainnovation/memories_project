from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
import datetime
from django.utils import timezone


class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return 'user with info ' + self.user.username


class Album(models.Model):
    title = models.CharField(max_length=128)
    cover_picture = models.ImageField(upload_to='cover_images', blank=True)
    slug = models.SlugField()
    date = models.DateTimeField(default=timezone.now(), blank=True)
    
    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
        self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)
    	
    

    def __unicode__(self):
        return self.title

class Gallery(models.Model):
    usr = models.ForeignKey(User, null=True)
    albums = models.ForeignKey(Album, null=True)
    contributor = models.BooleanField(default=True)

class Photo(models.Model):
    album = models.ForeignKey(Album)
    photo = models.ImageField(upload_to='album_images', blank=False)
    name = models.CharField(max_length=128, default=timezone.now())
    
    def __unicode__(self):
        return self.name
    

class Message(models.Model):
    photo = models.ForeignKey(Photo)
    comment = models.CharField(max_length=512, unique=False)
    usr = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.comment

