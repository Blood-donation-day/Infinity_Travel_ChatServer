from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanionViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'list', CompanionViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]