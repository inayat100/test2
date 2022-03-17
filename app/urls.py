from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('singin/',views.singup,name='singup'),
    path('login/',views.singin,name='singin'),
    path('logout/',views.user_logout,name='logout'),
    path('post/',views.post,name='post'),
    path('profile/',views.profile,name='profile'),
    path('all/',views.Up_post,name='show_post'),
    path('draft/',views.Df_post,name='drf_post'),
    path('publish/<int:pk>/',views.pub,name='pub_post'),
    path('full-post/<int:pk>/',views.full_post,name='full_post'),
]