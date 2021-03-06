from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from albums.forms import UserForm, UserProfileForm, FileUploadForm, NewAlbumForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
# Import the models
from albums.models import UserProfile
from albums.models import Album
from albums.models import Message
from albums.models import Photo
from albums.models import Gallery

import json


@login_required
def index(request):

	#List of gallery objects
	gallery_list = Gallery.objects.filter(usr = request.user )

	context_dict = {'gallery': gallery_list}

	visits = request.session.get('visits')
	if not visits:
		visits = 1
	reset_last_visit_time = False

	last_visit = request.session.get('last_visit')

	# if last visit cookie exists, update the latest visit time
	if last_visit:
		last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

		if (datetime.now() - last_visit_time).seconds > 0:
			visits = visits +1
			reset_last_visit_time = True

	# cookie doesnt exist
	else:
		reset_last_visit_time = True

	if reset_last_visit_time:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = visits

	context_dict['visits'] = visits

	new_album_form = NewAlbumForm()
	context_dict['new_album_form'] = new_album_form

	response = render(request, 'albums/index.html', context_dict)

	return response


def register(request):

	#boolean value for telling the template whether the registration was successfull
	#Initialise as false and the following will adjust it accordingly
	registered = False
	failed = False

	#If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':

		# Attempt to grab information from the raw form information.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			#hash the password
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance
			# Since we need to set the user attribute ourselves, we set commit=False
			profile = profile_form.save(commit=False)
			profile.user = user


			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']



			# Now save the UserProfile model instance
			profile.save()

			registered = True

		# Invalid forms, print mistakes to the terminal
		else:
			failed = True

	#Not a HTTP POST so render form using 2 modelForm instances
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'albums/login.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'failed': failed})


def user_login(request):


    if request.method == 'POST':

        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your memories account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            valid=True
            user_form=UserForm()
            profile_form=UserProfileForm()
            return render(request, 'albums/login.html', {'user_form': user_form, 'profile_form': profile_form, 'validate': valid})


    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:

		user_form = UserForm()
		profile_form = UserProfileForm()

		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render(request, 'albums/login.html', {'user_form': user_form, 'profile_form': profile_form})



@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('')

@login_required
def memory(request, album_name_slug):
	context_dict = {}


	try:
		# Search gallery for all the albums corresponding to the logged in user
		gallery_list = Gallery.objects.filter(usr__id = request.user.id )

		cover_list=()

		#Within the albums returned, see if any are by the name of the album slug parameter and get cover photos
		for i in gallery_list:

			if i.albums.slug == album_name_slug:
				context_dict['album'] = i.albums
				memory = i.albums
			else:
				cover_list = cover_list + (i.albums,)

		shared_with = Gallery.objects.filter(albums=memory)
		context_dict['shared'] = shared_with

		context_dict['covers'] = cover_list

		#next get list of all the photos associated with the selected memory and add to context dict
		photo_list = Photo.objects.filter(album=memory)
		context_dict['photos'] = photo_list

		#Get all the comments corresponding to each photo
		comment_list = Message.objects.filter(photo=photo_list)
		context_dict['comments'] = comment_list

		userprofile = UserProfile.objects.get(user=request.user)
		profilepic = userprofile.picture

		file_upload_form = FileUploadForm(initial={'albumID': memory.id})

		context_dict['upload_form'] = file_upload_form
		context_dict['artist_pic'] = profilepic


	except Album.DoesNotExist:
		pass

	return render(request, 'albums/memory.html', context_dict)


def upload_photo(request):

    if request.method == 'POST':

        form = FileUploadForm(request.POST, request.FILES)
        id =  request.POST['albumID']
        albumOb = Album.objects.get(pk=id)

        if form.is_valid():
			newphoto = Photo(photo = request.FILES['photo'], album = albumOb)
			newphoto.save()
			print('is valid')

        else :
			print('form not valid')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def new(request):

	if request.method == 'POST':
		form = NewAlbumForm(request.POST, request.FILES)

		if form.is_valid():
			#Create a new album with the title and photo from the submitted form
			newAlbum = Album(title = request.POST['title'], cover_picture = request.FILES['cover'])
			newAlbum.save()

			#We also need to create a new entry in Gallery to associate the user with the new album
			userOb = request.user
			newGallery = Gallery(usr = userOb, albums = newAlbum)
			newGallery.save()

		else:
			print('form not valid')

	return HttpResponseRedirect(reverse('index', args=(), kwargs={}))

@login_required
def remove(request, album_id):

	albumOb = Album.objects.get(pk=album_id)
	gallery = Gallery.objects.filter(usr = request.user, albums= albumOb).delete()

	return HttpResponseRedirect(reverse('index', args=(), kwargs={}))


@login_required
def post_comment(request):

	if request.method == 'POST':
		#get the photo corresponding to one that the comment was submitted for
		id =  request.POST['photoID']
		postedComment =  request.POST['comment']

		#need to do some form validation here because we aren't using a django form since its different for every photo in the album
		photoOb = Photo.objects.get(pk=id)
		userOb = request.user

		newComment = Message(photo=photoOb, comment = postedComment, usr = userOb)
		newComment.save()

	return HttpResponse('comment success')

@login_required
def add_collaborator(request):

	if request.method == 'POST':
		#get the album and collaborator
		new_collaborator =  request.POST['collaborator']
		#print new_collaborator
                print request.user
		#userprofile = UserProfile.objects.get(user=request.user)
		new_collaborator_obj = UserProfile.objects.get(user__username=new_collaborator)
		print new_collaborator_obj.user
		print "Suggested Users:"
		print get_usr_list(3, 's')
		id =  request.POST['albumID']
		print id
                albumOb = Album.objects.get(pk=id)
                print albumOb

		newC = Gallery(usr=new_collaborator_obj.user, albums=albumOb, contributor=True)
		newC.save()

	return HttpResponse('guy/gal added')

def suggest_users(request):

        usr_names = []
        sw = ''

        if request.method == 'GET':
                sw = request.GET['suggestion']

        usr_names = get_usr_list(5, sw)
        print "Suggested Users (AJAX):"
        print usr_names
        print "lenth:"
        print len(usr_names)

        results = []
        for i in range(len(usr_names)):
                d = {}
                d['id'] = i
                d['label'] = usr_names[i]
                d['value'] = usr_names[i]
                results.append(d)

        data = json.dumps(results)
        mimetype = 'application/json'

        return HttpResponse(data, mimetype)



def get_usr_list(max_results=0, sw=''):
        usr_list = []
        usr_names = []
        if sw:
                usr_list = UserProfile.objects.filter(user__username__istartswith=sw) #user__username__istartswith
        if max_results > 0:
                if usr_list.count() > max_results:
                        usr_list = usr_list[:max_results]
        for r in usr_list:
                usr_names.append(r.user.username) #{'label':r.user.username}

        return usr_names


