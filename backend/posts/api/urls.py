from django.urls import path, include
from .api import (
    CommentListView,
    CommentDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    path('add/', CommentCreateView.as_view()),
    path('', CommentListView.as_view()),
    path('<pk>/', CommentDetailView.as_view()),
    path('<pk>/update/', CommentUpdateView.as_view()),
    path('<pk>/delete/', CommentDeleteView.as_view()),



]
