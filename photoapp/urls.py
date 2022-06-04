from django.urls import path
from . import views 

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [ 
    path('', views.index, name='index'),

    path('sign-up/', views.sign_up, name='sign-up'), 
    path('login/', views.login, name='login'),
    
    path('profile/', views.profile, name='profile'),
    path('new-post/', views.create_post, name='new-post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 