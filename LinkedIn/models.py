
from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    '''
    This is an User class in which we have all the information of user.

    it is inherited with AbstractUser class
    '''
    age = models.PositiveIntegerField(null=True, blank=False)
    mobile = models.PositiveIntegerField(null=True, blank=False)
    address = models.CharField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    about = models.CharField(max_length=500)
    headlines = models.CharField(max_length=50)
    users = models.ManyToManyField(
        'User', through='Connection', related_name='users_connection')
    users = models.ManyToManyField(
        'User', through='ViewProfile', related_name='users_view')
    users = models.ManyToManyField(
        'User', through='Chat', related_name='users_chat')

    def __str__(self):
        return self.username


class Experience(models.Model):
    '''
    This class is for user professional experience with current position and company name
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    position = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)

    def __str__(self):
        return self.position


class Education(models.Model):
    '''
    This class is for user's education details 
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=200)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')

    def __str__(self):
        return self.institute


class Post(models.Model):
    '''
    This class deal with the post which user is made.
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_post', null=True)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(verbose_name='Post Date', auto_now=True)
    likes = GenericRelation('Like')

    def __str__(self) -> str:
        return self.text


class Comment(models.Model):
    '''
    This class is used when user comment on the post
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment', null=True)
    date = models.DateTimeField(verbose_name='Comment Date', auto_now=True)
    text = models.TextField(max_length=1000)
    likes = GenericRelation('Like')

    def __str__(self) -> str:
        return self.post.text


class Like(models.Model):
    '''
    This is an content type class and make generic foreign key for post and comment class
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.user.username


class Connection(models.Model):
    '''
    This class show's the connection between two users
    '''

    primary_user = models.ForeignKey(
        User, related_name='primary_user', on_delete=models.CASCADE, null=True)
    secondary_user = models.ForeignKey(
        User, related_name='secondary_user', on_delete=models.CASCADE, null=True)
    status = models.BooleanField(
        default=True, help_text="This tells us the connection between these two users")

    def __str__(self) -> str:
        return self.primary_user.username
        # return f"{self.primary_user.name}-{self.primary_user.age}"


class ViewProfile(models.Model):
    primary_user = models.ForeignKey(
        User, related_name='primary_user_view', on_delete=models.CASCADE, null=True)
    viewer = models.ForeignKey(
        User, related_name='viewer', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(
        verbose_name='View Profile Date', auto_now=True)

    def __str__(self) -> str:
        return self.primary_user.username


class Chat(models.Model):
    '''
    This class is used for the chatting between two users
    '''
    receiver = models.ForeignKey(
        User, related_name='receiver', on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(
        User, related_name='sender', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(verbose_name='Message Date', auto_now=True)
    text = models.TextField(max_length=1000)

class GroupChat(models.Model):
    '''
    This class is used for Group chatting
    '''
    sender = models.ForeignKey(
        User, related_name='group', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(verbose_name='Message Date', auto_now=True)
    text = models.TextField(max_length=1000)