from django.shortcuts import render
from .models import blogcontentlist
from .api_file.serializer import blogSerializer
from rest_framework import generics
from rest_framework import mixins 
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class blog_content_list (mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = blogcontentlist.objects.all ()
    serializer_class = blogSerializer

    def get (self , request , *args , **kwargs):
        return self.list (request , *args , **kwargs)
    
    def post (self , request , *args , **kwargs):
        return self.create (request , *args , **kwargs) 
    
class blog_detail (mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = blogcontentlist.objects.all ()
    serializer_class = blogSerializer

    def get (self , request , *args , **kwargs):
        return self.retrieve (request , *args , **kwargs)
    
    def delete (self , request , *args , **kwargs):
        return self.destroy (request , *args , **kwargs)
    
class blog_viewset (viewsets.ModelViewSet):
    queryset = blogcontentlist.objects.all ()
    serializer_class = blogSerializer
    
    

