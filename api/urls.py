from django.urls import path , include
from .views import *


app_name = 'api'
urlpatterns = [
    path("",PostList.as_view(),name='list'),
    path("<int:pk>",PostDetail.as_view(),name='detail'),
    path("user/",UserList.as_view(),name='user'),
    path("user/<int:pk>",UserDetail.as_view(),name='user-detail'),
]
