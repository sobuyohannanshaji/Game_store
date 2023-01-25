from django.urls import path
from .import views


urlpatterns=[
    path('register/',views.register,name='register'),
    path('home/<str:pk>', views.home, name='home'),
    path('admin_home/', views.homeadmin, name='homeadmin'),
    path('',views.log, name='log'),
    path('logout/',views.logout, name='logout'),
    path('payment/<str:pk>',views.payment, name='payment'),
    path('profile/<str:pk>',views.profile, name='profile'),
    path('update_profile/<str:pk>',views.update_profile, name='update_profile'),
    path('update_username_password/<str:pk>',views.update_password, name='update_user'),
    path('creategame/', views.creategame, name='creategame'),
    path('viewgames/', views.viewgames, name='viewgames'),
    path('editgame/<str:pk>', views.editgame, name='editgame'),
    path('user_game_page/<str:pk>/', views.gamepage, name='gamepage'),
    path('deletegame/<str:pk>', views.deletegame, name='deletegame'),
    path('deletereview/<str:pk>', views.deletereview, name='deletereview'),
    path('feedback/<str:pk>', views.feedss, name='feedss'),
    path('feedback/', views.feeds, name='feeds'),
    path('processing/<str:pk>', views.processing, name='processing'),
path('processing1/<str:pk>', views.processing1, name='processing1'),
path('download/<str:pk>', views.paid, name='paid'),
path('review/<str:pk>', views.reviews, name='reviews'),
path('updatepro/<str:pk>', views.changepro, name='changepro'),
    path('updateavatar/<str:pk>', views.avatar, name='avatar'),
    path('updateimage/<str:pk>', views.image, name='image'),
path('updatev1/<str:pk>', views.v1, name='v1'),
path('updatev2/<str:pk>', views.v2, name='v2'),
path('updatefile/<str:pk>', views.file, name='file'),
path('feedbacks/<str:pk>', views.feedbacks, name='feedbacks'),
]