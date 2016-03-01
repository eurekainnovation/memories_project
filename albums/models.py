from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)

    def __unicode__(self):
        return 'user with info ' + self.fname + self.email


class Album(models.Model):
    title = models.CharField(max_length=128, unique=True)
    cover_picture = models.ImageField(upload_to='cover_images', blank=True)

    def __unicode__(self):
        return self.title

class Gallery(models.Model):
    usr = models.ForeignKey(User, null=True)
    albums = models.ForeignKey(Album, null=True)
    contributor = models.BooleanField(default=True)

class Photo(models.Model):
    album = models.ForeignKey(Album)
    photo = models.ImageField(upload_to='album_images', blank=False)


class Message(models.Model):
    photo = models.ForeignKey(Photo)
    comment = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.comment

class UserProfile(models.Model):

	user = models.OneToOneField(User)
	
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	
	def __unicode__(self):
		return selft.user.username