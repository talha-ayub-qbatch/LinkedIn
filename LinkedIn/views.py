from urllib import request
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView,CreateView
from django.views.generic.detail import DetailView
from .forms import UserForm
# Create your views here.


def profile(request):
    '''
    This function get the request on 'profile/' and response the profile.html page 

    in which the user's personal information is shown on the screen.
    '''
    current_user = request.user
    return render(request, "registration/profile.html", {'user': current_user})


def experince(request):
    '''
    This function get the request on 'experience/' and response the experience.html page 

    in which the user's experience is shown on the screen.
    '''
    current_user = request.user
    current_user_name = User.objects.get(pk=current_user.pk)
    current_user_pk = Experience.objects.get(user=current_user.pk)
    return render(request, "registration/experince.html", {'user': current_user_pk, 'name': current_user_name})


def education(request):
    '''
    This function get the request on 'education/' and response the education.html page 

    in which the user's education is shown on the screen.
    '''
    current_user = request.user
    current_user_name = User.objects.get(pk=current_user.pk)
    current_user_pk = Education.objects.get(user=current_user.pk)
    return render(request, "registration/education.html", {'user': current_user_pk, 'name': current_user_name})


def post(request):
    '''
    This function get the request on 'post/' and response the post.html page 

    in which the user's all posts is shown on the screen.
    '''
    current_user = request.user

    current_user_name = User.objects.get(pk=current_user.pk)
    current_user_all = User.objects.all()
    current_user_pk = Post.objects.filter(user__in=current_user_all)
    print(current_user_pk[1].pk)
    likes = Like.objects.filter(object_id = current_user_pk[1].pk)
    print(likes)
    return render(request, "registration/post.html", {'user': current_user_pk, 'name': current_user_name})


def comment(request):
    '''
    This function get the request on 'comment/' and response the comment.html page 

    in which the user's all comments on post is shown on the screen.
    '''
    current_user = request.user
    current_user_name = User.objects.get(pk=current_user.pk)
    current_user_pk = Post.objects.all()
    current_user_post_comment = Comment.objects.filter(
        post__in=current_user_pk)
    return render(request, "registration/comment.html", {'user': current_user_post_comment, 'name': current_user_name})


def connection(request):
    '''
    This function get the request on 'connection/' and response the connection.html page 

    in which the user's connection is shown on the screen
    '''
    current_user = request.user
    current_user_name = User.objects.get(pk=current_user.pk)
    current_user_pk = Connection.objects.get(primary_user=current_user.pk)
    return render(request, "registration/connection.html", {'user': current_user_pk, 'name': current_user_name})


def viewprofile(request):
    '''
    This function get the request on 'viewprofile/' and response the viewprofile.html page 

    in which the user's viewed profile is shown on the screen
    '''
    current_user = request.user
    current_user_name = User.objects.get(pk=current_user.pk)
    current_user_pk = ViewProfile.objects.get(primary_user=current_user.pk)
    return render(request, "registration/viewprofile.html", {'user': current_user_pk, 'name': current_user_name})


def chat(request):
    '''
    This function get the request on 'chat/' and response the chat.html page 

    in which the user's can chat with other user
    '''
    current_user = request.user
    current_user_names = User.objects.get(pk=current_user.pk)
    get_msg = 'Connection made'
    if request.method == 'POST':
        my_form = UserForm(request.POST)
        if my_form.is_valid():
            get_msg = my_form.cleaned_data['message']
    else:
        my_form = UserForm()

    if current_user.pk == 1:
        receiver = User.objects.get(pk=2)
        sender = User.objects.get(pk=current_user.pk)
        Chat.objects.create(receiver=receiver, sender=sender, text=get_msg)
        current_user_name = User.objects.get(pk=2)

    elif current_user.pk == 2:
        receiver = User.objects.get(pk=1)
        sender = User.objects.get(pk=current_user.pk)
        Chat.objects.create(receiver=receiver, sender=sender, text=get_msg)
        current_user_name = User.objects.get(pk=1)

    current_user_pk = Chat.objects.all()
    return render(request, "registration/chat.html", {'user': current_user_pk, 'form': my_form, 'id': current_user_name, 'name': current_user_names})

def friends(request):
    current_user = request.user
    connected_user = Connection.objects.get(primary_user = current_user.pk)
    if connected_user.status == True:
        connected_secondary_user = connected_user.secondary_user
    else:    
        connected_secondary_user = ''
    print(connected_secondary_user.username)
    return render(request, "registration/friends.html", {'user': connected_secondary_user, 'profile':current_user})



class Logout(RedirectView):
    '''
    This class is used for logout the user and redirect it login page
    '''
    url = '/accounts/login/'

class AddPost(CreateView):
    model = Post
    fields = ['user', 'text']
    template_name = 'registration/addpost.html' 
    success_url = '/accounts/post/'

class AddComment(CreateView):
    model = Comment
    fields = ['post', 'user', 'text']
    template_name = 'registration/addcomment.html' 
    success_url = '/accounts/comment/'

class UserDetail(DetailView):
    model = User