from rest_framework import serializers
from posts.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    '''
    serializer for Comment
    '''
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment = Comment.objects.create(post_id=validated_data['post_id'],
                                         name=validated_data['name'],
                                         email=validated_data['email'],
                                         body=validated_data['body'])
        return comment
