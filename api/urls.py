from django.urls import path
from .views import UrineStripColorDetectionView

urlpatterns = [
    path('upload/', UrineStripColorDetectionView.as_view(), name='upload'),
]
