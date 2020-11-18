from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,

)
from posts.models import Comment
from .serializers import CommentSerializer


class CommentListView(ListAPIView):
    '''
    API View for Comment List
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveAPIView):
    '''
    API View for Comment Details
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateView(CreateAPIView):
    '''
    API View for to add a comment
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(UpdateAPIView):
    '''
    API View for Update a Comment
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDeleteView(DestroyAPIView):
    '''
    API View for to delete a comment
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
