from django.db import models
from django.contrib.auth.models import User
import datetime
slug = models.SlugField()

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return 'user with info ' + self.user.username


class Album(models.Model):
    title = models.CharField(max_length=128, unique=True)
    cover_picture = models.ImageField(upload_to='cover_images', blank=True)
    slug = models.SlugField() 
    
    def save(self, *args, **kwargs):
    	self.slug = slugify(self.title)
    	super(Album, self),save(*args, **kwargs)


    def __unicode__(self):
        return self.title

class Gallery(models.Model):
    usr = models.ForeignKey(User, null=True)
    albums = models.ForeignKey(Album, null=True)
    contributor = models.BooleanField(default=True)

class Photo(models.Model):
    album = models.ForeignKey(Album)
    photo = models.ImageField(upload_to='album_images', blank=False)
    name = models.CharField(max_length=128, default=datetime.datetime.now())
    
    def __unicode__(self):
        return self.name
    

class Message(models.Model):
    photo = models.ForeignKey(Photo)
    comment = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.comment

