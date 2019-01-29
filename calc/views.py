from django.http import Http404, HttpResponse, HttpResponseRedirect

def index(request):
	return HttpResponse("Hi, bro. This is calc.")
