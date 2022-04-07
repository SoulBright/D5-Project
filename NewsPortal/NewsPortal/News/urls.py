from django.urls import path
from .views import *


urlpatterns = [
    path("", PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path("search", post_filter),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author'),
    path('author/<int:pk>/edit/', UserUpdate.as_view(), name='user_update'),
]
