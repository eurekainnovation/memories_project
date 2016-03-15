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
from albums.models import UserProfile



@login_required
def index(request):
	print(request.user.username)
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
			print user_form.errors, profile_form.errors
		
	#Not a HTTP POST so render form using 2 modelForm instances			
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request, 'albums/login.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}) 
	
	
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
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
                return HttpResponseRedirect('/albums/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

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
    return HttpResponseRedirect('/albums/')
    
@login_required
def memory(request, album_name_slug):
	context_dict = {}
	
	if request.session.get('visits'):
		count = request.session.get('visits')
		
	else:
		count = 0
	
	context_dict['visits'] = count
	
	try:
		# Search gallery for all the albums corresponding to the logged in user
		gallery_list = Gallery.objects.filter(usr__id = request.user.id )
		
		cover_list=()

		
		#Within the albums returned, see if any are by the name of the album slug parameter and get cover photos
		for i in gallery_list:
			cover_list = cover_list + (i.albums,)
			if i.albums.slug == album_name_slug:
				print(i.albums.title)
				context_dict['album'] = i.albums
				memory = i.albums

		shared_with = Gallery.objects.filter(albums=memory)
		context_dict['shared'] = shared_with
				
		context_dict['covers'] = cover_list
		
		#next get list of all the photos associated with the selected memory and add to context dict
		photo_list = Photo.objects.filter(album=memory)
		context_dict['photos'] = photo_list
		
		#Get all the comments corresponding to each photo
		comment_list = Message.objects.filter(photo=photo_list)
		context_dict['comments'] = comment_list
		
		
		
		file_upload_form = FileUploadForm(initial={'albumID': memory.id})

		context_dict['upload_form'] = file_upload_form

		
	except Album.DoesNotExist:
		pass
	
	return render(request, 'albums/memory.html', context_dict)

		
def test(request):
	return render(request, 'albums/test.html', {})

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

    return HttpResponse('success')
	
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

