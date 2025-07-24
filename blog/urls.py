from django.contrib import admin
from django.urls import path, include
from blog import views
from .views import PostDetail, PostCreate, PostDelete

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('blog/new/', PostCreate.as_view(), name='post-create'),
    path('blog/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('blog/<int:pk>/update/', views.post_update, name='post-update'),
    path('blog/<int:pk>/delete/', PostDelete.as_view(), name='post-delete' ),
]
