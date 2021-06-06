from django.urls import path
from users.views import register, login

urlpatterns = [
    path('gegister/', register, name='register'),
    path('login/', login, name='login')
]
