from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "This is in bold"}
	
	return render(request, 'albums/index.html', context_dict)
	
def new(request):

	return render(request, 'albums/new.html')