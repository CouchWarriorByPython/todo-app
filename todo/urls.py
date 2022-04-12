from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

v = settings.API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' + v + '/', include('todo_app.urls')),
    path('auth/', include('authenticate_app.urls')),
]