from django.urls import path, include
from .api import CommentListView, CommentDetailView, CommentCreateView

urlpatterns = [
    path('add/', CommentCreateView.as_view()),
    path('', CommentListView.as_view()),
    path('<pk>/', CommentDetailView.as_view()),



]
