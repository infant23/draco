from django.urls import path
from .views import *


app_name = 'blog'
urlpatterns = [
	# path('', index, name='index'),
	path('', PostList.as_view(), name='index'),
	path('<int:pk>/', PostDetail.as_view(), name='post_detail_url'),
	path('post/<int:pk>/comment/', PostDetail.as_view(), name='add_comment_url'),
]
