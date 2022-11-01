from django.contrib import admin

from django.urls import include,path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from pos.views import login





urlpatterns = [
    path('', RedirectView.as_view(url='/pos', permanent=True)),
    path('pos/', include('pos.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
        {'next_page': '/pos/order'}, name='logout'),
    path('accounts/login/', login, name='login'),
]