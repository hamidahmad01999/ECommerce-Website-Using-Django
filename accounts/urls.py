from django.urls import path
from .views import *


app_name='accounts'
urlpatterns = [
    path('register/', register_page, name="register_page"),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('activate/<email_token>', user_account_verification, name="user_verification"),
    path('', home, name='home')
]
