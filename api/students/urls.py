from .views import StudentsViewSet, EmailAPI

from rest_framework.routers import DefaultRouter
from django.urls import re_path, include

router = DefaultRouter()
router.register('', StudentsViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    re_path('send-email', EmailAPI.as_view()),
]