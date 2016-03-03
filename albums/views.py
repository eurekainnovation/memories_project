from django.shortcuts import render
from django.http import HttpResponse
from albums.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
	context_dict = {'boldmessage': "This is in bold"}
	
	return render(request, 'albums/index.html', context_dict)
	
@login_required
def new(request):

	return render(request, 'albums/new.html')
	
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
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
	
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/albums/')