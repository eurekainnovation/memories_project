from django import forms
from django.contrib.auth.models import User
from albums.models import UserProfile
from albums.models import Photo
from albums.models import Album

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')
		
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['username'].error_messages = {'required': 'Username is required'}
		self.fields['password'].error_messages = {'required': 'Password is required'}
		self.fields['first_name'].error_messages = {'required': 'First Name is required'}
		self.fields['last_name'].error_messages = {'required': 'Last Name is required'}
		self.fields['email'].error_messages = {'required': 'email is required'}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)
		
	def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['picture'].error_messages = {'required': 'Picture is required'}


class FileUploadForm(forms.ModelForm):

	photo = forms.ImageField(required=True)
	albumID = forms.IntegerField(required=True,initial=0)
	
	def getAlbumID():
		print self.albumId

	class Meta:
		model = Photo
		fields = ('photo',)
		
	
	
	
