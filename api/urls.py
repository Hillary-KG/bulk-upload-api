from django.urls import path, include
from rest_framework import routers
from .views import UploadViewSet, UserRecordView

router = routers.DefaultRouter()
router.register(r"upload", UploadViewSet, basename="upload")
router.register(r"users", UserRecordView, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
