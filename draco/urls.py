from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import redirect_blog

urlpatterns = [
	path('', redirect_blog, name='index'),
	path('admin/', admin.site.urls),
	path('blog/', include('blog.urls')),
	path('calc/', include('calc.urls')),
	path('mail/', include('mail.urls')),
	path('shop/', include('shop.urls')),
	path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)