from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'feed_home'

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('like/', views.liked_post, name='like'),
    path('unlike/', views.unliked_post, name='unlike'),


     # Forget Password
    re_path(r'password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path(r'password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
