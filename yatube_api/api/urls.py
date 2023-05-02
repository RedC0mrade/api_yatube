from django.urls import path
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='Groups')
router.register('posts/<int:pk>/comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
