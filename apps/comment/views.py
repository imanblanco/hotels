from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Like, Comment
from .permissions import IsCommentAuthor
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = IsCommentAuthor

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated]
        else:
            permissions = [IsCommentAuthor]
        return [permission() for permission in permissions]

    @action(detail=True, methods=["POST"])
    def like(self, request, *args, **kwargs):
        comment = self.get_object()
        like_obj, _ = Like.objects.get_or_create(comment=comment, user=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'like'
        if not like_obj.like:
            status = 'unlike'
        return Response({'status': status})