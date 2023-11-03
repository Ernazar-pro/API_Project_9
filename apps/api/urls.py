from django.urls import path,include
from .views import PostAPIView, PostDetailAPIView

urlpatterns = [
    path('post/', PostAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
]