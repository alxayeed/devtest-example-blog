from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .api import RegisterApi

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('register/', RegisterApi.as_view()),
]
