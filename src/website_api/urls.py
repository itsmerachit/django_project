import django
from django.contrib.auth import views as auth_views

from django.urls import path

from website_api import views

app_name = 'website_web'

urlpatterns = [
    path('list-articles', views.list_articles, name='article_list'),
    path('oauth/facebook', views.facebook_oauth, name='facebook_oauth'),
    path('get-articles', views.get_articles, name='article_get'),
    path('add-articles', views.add_articles, name='article_add'),
    path('auth/login', auth_views.LoginView.as_view(), name='login_page'),
    # path('', views.home_page, name='home_page'),
]