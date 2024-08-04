from .views import PostListCreateView, CommentListCreateView
from django.urls import path



urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='posts-list'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list')
]
