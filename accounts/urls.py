from django.urls import path, include

from accounts.views import logout_user, RegisterUser, ProfileUser, ProfileUserEdit

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register user'),
    path('profile/', ProfileUser.as_view(), name='current user profile'),
    path('profile/<int:pk>/', ProfileUser.as_view(), name='user profile'),
    path('profile/edit/', ProfileUserEdit.as_view(), name='edit profile'),
    path('logout/', logout_user, name='logout user'),
    path('', include('django.contrib.auth.urls')),
]
