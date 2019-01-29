from django.shortcuts import redirect


def redirect_blog(request):
	return redirect('blog:index', permanent=True)
