from users.views import user_registration_view, login_view, user_info_view, user_delete, user_modify
from django.urls import path
from django.contrib.auth.views import LogoutView
from travelmore import settings

app_name = 'users'
urlpatterns = [
    path('register/', user_registration_view.as_view(), name='register'),
    path('login/', login_view.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('<str:username>/info/', user_info_view.as_view(), name='user-info'),
    path('<str:username>/delete/', user_delete.as_view(), name='user-delete'),
    path('<str:username>/edit/', user_modify.as_view(), name='user-modify')
]