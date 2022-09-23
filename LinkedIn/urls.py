from django.urls import path

from . import views

urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('experince/', views.experince, name='experince'),
    path('education/', views.education, name='education'),
    path('post/', views.post, name='post'),
    path('comment/', views.comment, name='comment'),
    path('connection/', views.connection, name='connection'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('chat/', views.chat, name='chat'),
    path('logout/', views.Logout.as_view(), name='logout'),

]
