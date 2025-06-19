from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    ## 반복되는 패턴을 재사용
    ## 코드 재사용 -> CreateView, ListView, DetailView, UpdateView, DeleteView 내장
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
