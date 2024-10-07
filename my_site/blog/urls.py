from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageListView.as_view(), name="starting-page"),
    path("posts", views.AllPostsViews.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
