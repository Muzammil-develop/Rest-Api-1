from django.urls import path , include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter ()
router.register ('list' , views.blog_viewset , basename='blog')

urlpatterns = [
#     path ('list' , views.blog_content_list.as_view () , name='blog_content_list'),
#     path ('list/<int:pk>' , views.blog_detail.as_view () , name='blog_detail'),
    path ('' , include (router.urls)),
]
