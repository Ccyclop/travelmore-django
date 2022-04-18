from users.views import user_registration_view, login_view
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('register/', user_registration_view.as_view(), name='register'),
    path('login/', login_view.as_view(), name='login')
]
