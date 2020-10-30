from rest_framework import viewsets
from .serializers import Author, AuthorSerializer

class AuthorViewset(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()