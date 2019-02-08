from django.urls import path
from .views import *


app_name = 'mail'
urlpatterns = [
	# path('', index, name='index'),
	path('', PostMan.as_view(), name='index'),
]
