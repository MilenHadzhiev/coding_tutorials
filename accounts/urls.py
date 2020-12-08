from django.urls import path, include

from accounts.views import register_user, profile_user, profile_user_edit, logout_user

urlpatterns = [
    path('register/', register_user, name='register user'),
    path('profile/', profile_user, name='current user profile'),
    path('profile/<int:pk>', profile_user, name='user profile'),
    path('profile/edit/', profile_user_edit, name='edit profile'),
    path('logout/', logout_user, name='logout user'),
    path('', include('django.contrib.auth.urls')),
]
