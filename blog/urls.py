from django.contrib import admin
from django.urls import path, include

#tvm
from django.conf.urls.static import static
from django.conf import settings
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home),
    path('posts/<int:post_id>', views.post)
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

