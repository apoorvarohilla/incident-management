from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, IncidentListCreateView, IncidentDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('incidents/', IncidentListCreateView.as_view(), name='incident_list'),
    path('incidents/<int:pk>/', IncidentDetailView.as_view(), name='incident_detail'),
]
