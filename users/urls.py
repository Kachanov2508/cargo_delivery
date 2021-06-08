from django.urls import path
from users.views import register, user_login, user_profile, user_logout

urlpatterns = [
    path('gegister/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('logout/', user_logout, name='logout')
]
