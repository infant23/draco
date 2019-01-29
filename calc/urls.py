from django.urls import path
from .views import *


app_name = 'calc'
urlpatterns = [
	path('', index, name='index'),
]
