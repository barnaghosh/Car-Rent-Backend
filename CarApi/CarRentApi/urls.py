from django.urls import path
from rest_framework.routers import DefaultRouter
from CarRentApi import views

router = DefaultRouter()
router.register(r"customer", views.CustomerProfileViewSet)
router.register(r"owner", views.OwnerProfileViewSet)

urlpatterns = [
     
] + router.urls
