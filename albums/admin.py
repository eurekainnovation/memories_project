from django.contrib import admin
from albums.models import UserProfile, User, Gallery, Album, Photo, Message

class UserAdmin(admin.ModelAdmin):
	list_display = ('fname', 'lname', 'email', 'password')

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('usr', 'albums', 'contributor')

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(User, UserAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Message)
