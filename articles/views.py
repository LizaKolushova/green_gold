from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from .tasks import send_email


def home(request):
    send_email.delay()
    return HttpResponse('<h1> отправка сообщения на почту </h1>')


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return ArticleCreateSerializer
        return ArticleSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return CommentCreateSerializer
        return CommentSerializer