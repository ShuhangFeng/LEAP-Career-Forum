from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
]
