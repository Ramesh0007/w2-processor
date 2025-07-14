from django.urls import path
from .views import async_upload_view
from .mock_views import mock_report, mock_upload

urlpatterns = [
    path("upload-w2/", async_upload_view, name="upload-w2"),
    path("mockapi/reports", mock_report, name="mock-report"),
    path("mockapi/files", mock_upload, name="mock-upload"),
]
