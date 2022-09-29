from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as OrigUserAdmin





# Register your models here.


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['receiver', 'sender', 'date', 'text']

@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ['sender', 'date', 'text']


@admin.register(ViewProfile)
class ViewProfileAdmin(admin.ModelAdmin):
    list_display = ['primary_user', 'viewer', 'date']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'object_id', 'content_object']


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['primary_user', 'secondary_user', 'status']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date',
                    'end_date', 'position', 'company_name']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'institute', 'start_date', 'end_date', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'text']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'date', 'text']


@admin.register(User)
class UserAdmin(OrigUserAdmin):
    list_display = ['username', 'age', 'email', 'password', 'is_staff',
                    'mobile', 'address', 'website', 'profile_pic', 'about', 'headlines']



