from django.contrib import admin
from albums.models import UserProfile, Gallery, Album, Photo, Message



class GalleryAdmin(admin.ModelAdmin):
	list_display = ('usr', 'albums', 'contributor')

class AlbumAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo)
admin.site.register(Message)
