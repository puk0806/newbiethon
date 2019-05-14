from django.contrib import admin
from django.urls import path, include
import board.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",include('board.urls')),
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('accounts/', include('accounts.urls')),
]