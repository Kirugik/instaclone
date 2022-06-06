from django.urls import path
from . import views 

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [ 
    path('', views.index, name='index'),

    path('sign-up/', views.sign_up, name='sign-up'), 
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    
    path('profile/<str:id>', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update-profile'),

    path('new-post/', views.create_post, name='new-post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 