from urllib import request
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from .forms import *
from django.db.models import Q
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
    # likes = Like.objects.filter(object_id = current_user_pk[1].pk)
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


def whichuserchat(request, id):
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

    receiver1 = User.objects.get(pk=id)
    sender1 = User.objects.get(pk=current_user.pk)
    Chat.objects.create(receiver=receiver1, sender=sender1, text=get_msg)
    receiver_user_name = User.objects.get(pk=id)
    print(receiver_user_name)
    current_user_pk = Chat.objects.filter(Q(receiver=id, sender=current_user.pk) | Q(
        receiver=current_user.pk, sender=id)).exclude(text='Connection made')
    return render(request, "registration/chat.html", {'user': current_user_pk, 'form': my_form, 'id': receiver_user_name, 'name': current_user_names})


def groupchat(request):
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

    sender1 = User.objects.get(pk=current_user.pk)
    Chat.objects.create(sender=sender1, text=get_msg)

    current_user_pk = Chat.objects.exclude(text='Connection made')
    return render(request, "registration/groupchat.html", {'user': current_user_pk, 'form': my_form, 'name': current_user_names})


def chat(request):
    '''
    This function is used to select the user for chat
    '''
    current_user = request.user
    all_users = User.objects.all().exclude(pk=current_user.pk)
    return render(request, "registration/whichuserchat.html", {'user': all_users, 'name': current_user})


def friends(request):
    '''
    To see the friends
    '''
    current_user = request.user
    connected_user = Connection.objects.get(primary_user=current_user.pk)
    if connected_user.status == True:
        connected_secondary_user = connected_user.secondary_user
    else:
        connected_secondary_user = ''
    print(connected_secondary_user.username)
    return render(request, "registration/friends.html", {'user': connected_secondary_user, 'profile': current_user})


def signup(request):
    '''
    This is used for sign up the user'''
    if request.method == 'POST':
        my_form = RegisterdForm(request.POST)

        if my_form.is_valid():
            usernames = my_form.cleaned_data['username']
            passwords = my_form.cleaned_data['password']
            # emails = my_form.cleaned_data['email']
            # ages = my_form.cleaned_data['age']
            user = User(username=usernames, password=passwords,
                        is_staff=True, is_active=True, is_superuser=True)
            user.set_password(passwords)
            user.save()
    else:
        my_form = RegisterdForm()

    return render(request, "registration/signup.html", {'form': my_form})


class Logout(RedirectView):
    '''
    This class is used for logout the user and redirect it login page
    '''
    url = '/accounts/login/'


class AddPost(CreateView):
    '''
   This is used to add the Post
    '''
    model = Post
    fields = ['user', 'text']
    template_name = 'registration/addpost.html'
    success_url = '/accounts/post/'


class AddComment(CreateView):
    '''
   This is used to add the Comment
    '''
    model = Comment
    fields = ['post', 'user', 'text']
    template_name = 'registration/addcomment.html'
    success_url = '/accounts/comment/'
