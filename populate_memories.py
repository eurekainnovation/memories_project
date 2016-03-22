import os
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memories_project.settings')
import django
from django.contrib.auth.models import User
from memories_project.settings import BASE_DIR

django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from albums.models import UserProfile
from albums.models import Album
from albums.models import Photo
from albums.models import Gallery
from albums.models import Message

def populate():
    image_profile_dir = os.path.join(BASE_DIR, 'init_data', 'profile_images')
    photo_dir = os.path.join(BASE_DIR, 'init_data', 'Album_Photos')
    cover_dir =  os.path.join(BASE_DIR, 'init_data', 'Cover_Photos')

    user1 = add_user("leifos", "Leif@gmail.com", "leifos", "Leif", "Azzopardi", image_path=os.path.join(image_profile_dir,'Leif.jpg'))
    user2 = add_user("laura", "Laura@gmail.com", "laura", "Laura", "L", image_path=os.path.join(image_profile_dir,'Laura.jpg'))
    user3 = add_user("david", "David@gmail.com", "david", "David", "D", image_path=os.path.join(image_profile_dir,"David.jpg"))


    alb1 = add_album("Castles", cover_path=os.path.join(cover_dir, 'sri.jpg'))
    gallery1 = add_gallery(user1, alb1)
    p1 = add_photo("name", alb1, photo_path=os.path.join(photo_dir, 'M1.jpg'))
    c2 = add_message(p1,user1,"Awesome")
    p2 = add_photo("name", alb1, photo_path=os.path.join(photo_dir, 'M2.jpg'))
    p3 = add_photo("name", alb1, photo_path=os.path.join(photo_dir, 'M3.jpg'))
    p4 = add_photo("name", alb1, photo_path=os.path.join(photo_dir, 'M4.jpeg'))
    pb = add_photo("name", alb1, photo_path=os.path.join(photo_dir, 'M.jpg'))

    alb5 = add_album("Nectar of Gods", cover_path=os.path.join(cover_dir, 'B.jpg'))
    gallery1 = add_gallery(user1, alb5)
    gallery1 = add_gallery(user2, alb5)
    gallery1 = add_gallery(user3, alb5)
    ph1 = add_photo("name", alb5, photo_path=os.path.join(photo_dir, 'B1.jpg'))
    c6 = add_message(ph1,user1,"I would love a cold beer right now!")
    c7 = add_message(ph1,user3,"Me too")
    c8 = add_message(ph1,user2,"I would prefer some wine...")
    ph2 = add_photo("name", alb5, photo_path=os.path.join(photo_dir, 'B2.jpg'))
    ph3 = add_photo("name", alb5, photo_path=os.path.join(photo_dir, 'B3.jpg'))
    ph4 = add_photo("name", alb5, photo_path=os.path.join(photo_dir, 'B4.jpg'))





    alb2 = add_album("Cupcakes", cover_path=os.path.join(cover_dir, 'Cup.jpg'))
    gallery2 = add_gallery(user2, alb2)
    p5 = add_photo("name", alb2, photo_path=os.path.join(photo_dir, 'Cup1.jpg'))
    c1 = add_message(p5,user2,"Yummy")
    p6 = add_photo("name", alb2, photo_path=os.path.join(photo_dir, 'Cup2.jpg'))
    p7 = add_photo("name", alb2, photo_path=os.path.join(photo_dir, 'Cup3.jpg'))
    p8 = add_photo("name", alb2, photo_path=os.path.join(photo_dir, 'Cup4.jpg'))

    alb3 = add_album("Doggies", cover_path=os.path.join(cover_dir, 'puppies.jpg'))
    gallery2 = add_gallery(user2, alb3)
    ph5 = add_photo("name", alb3, photo_path=os.path.join(photo_dir, 'D1.jpg'))
    c3 = add_message(ph5,user2,"Aw what a cutie!!")
    ph6 = add_photo("name", alb3, photo_path=os.path.join(photo_dir, 'D2.jpg'))
    ph7 = add_photo("name", alb3, photo_path=os.path.join(photo_dir, 'D3.jpg'))
    ph8 = add_photo("name", alb3, photo_path=os.path.join(photo_dir, 'D4.jpg'))



    alb4 = add_album("Sailing", cover_path=os.path.join(cover_dir, 'S.jpg'))
    gallery4 = add_gallery(user3, alb4)
    p9 = add_photo("name", alb4, photo_path=os.path.join(photo_dir, 'S1.jpg'))
    p10 = add_photo("name", alb4, photo_path=os.path.join(photo_dir, 'S2.jpg'))
    p11 = add_photo("name", alb4, photo_path=os.path.join(photo_dir, 'S3.jpg'))
    c4 = add_message(p11,user3,"Great memories from last summer...")
    p12 = add_photo("name", alb4, photo_path=os.path.join(photo_dir, 'S4.jpg'))

    alb6 = add_album("In home wine cellars", cover_path=os.path.join(cover_dir, 'W.jpg'))
    gallery6 = add_gallery(user3, alb6)
    ph9 = add_photo("name", alb6, photo_path=os.path.join(photo_dir, 'W1.jpg'))
    c5 = add_message(ph9,user3,"Next year my basement is going to look like that!!!")
    ph10 = add_photo("name", alb6, photo_path=os.path.join(photo_dir, 'W2.jpg'))
    ph11 = add_photo("name", alb6, photo_path=os.path.join(photo_dir, 'W3.jpg'))
    ph12 = add_photo("name", alb6, photo_path=os.path.join(photo_dir, 'W4.jpg'))


def add_user(username, email, password, first_name, last_name, image_path):

    image = SimpleUploadedFile(os.path.basename(image_path), open(image_path, 'rb').read(), content_type='image/jpeg')
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    u = UserProfile(user_id=user.pk)
    u.picture = image
    u.save()
    return user


def add_album(title, cover_path):

    cover = SimpleUploadedFile(os.path.basename(cover_path), open(cover_path, 'rb').read(), content_type='image/jpeg')
    a = Album.objects.create(title=title)
    a.cover_picture = cover
    a.save()
    return a


def add_gallery(user, albums,contributor=True):
    Gallery.objects.create(usr=user, albums=albums,contributor=contributor)

def add_photo(name,album,photo_path):
   photo = SimpleUploadedFile(os.path.basename(photo_path), open(photo_path, 'rb').read(), content_type='image/jpeg')
   p = Photo.objects.create(name=name, album=album)
   p.photo = photo
   p.save()
   return p

def add_message(photo,usr, comment):
   c = Message.objects.create(photo=photo,usr=usr,comment=comment)
   c.save()
   return c
# Start execution here!
if __name__ == '__main__':
    print("Starting Memories population script...")
    populate()
