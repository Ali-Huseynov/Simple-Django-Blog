from django.urls import path
from .views import UserRegisterView ,ProfileDetailView ,UpdateProfileView

urlpatterns = [

    path('register', UserRegisterView, name = 'register' ),
    path( 'profile/<str:username>/' , ProfileDetailView  , name = 'profile_detail' ),
    path( 'profile/<str:username>/edit' , UpdateProfileView  , name = 'update_profile' ),
    
 
]




