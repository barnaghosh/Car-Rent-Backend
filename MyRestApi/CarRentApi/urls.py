from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from CarRentApi import views

router = DefaultRouter()
router.register(r"customer", views.CustomerProfileViewSet)
router.register(r"owner", views.OwnerProfileViewSet)
router.register(r"book", views.OrderViewSet)
urlpatterns = [
       path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
