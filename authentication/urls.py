from django.urls import path
from authentication.views import login, register, logout
from rest_framework_simplejwt import views as jwt_views
from .api import RegisterApi

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/register/', RegisterApi.as_view()),
]
