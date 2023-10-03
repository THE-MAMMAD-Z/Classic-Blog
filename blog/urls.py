from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('blog/',views.blog,name='blog'),
    path('todo',views.todo,name="todo"),
    path('post-detail/<int:num>/',views.post_detail , name='detail')
]
