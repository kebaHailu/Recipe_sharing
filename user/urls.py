from django.urls import path
from .views import CustomUserCreateView, CustomTokenObtainPairView

urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name='create_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
