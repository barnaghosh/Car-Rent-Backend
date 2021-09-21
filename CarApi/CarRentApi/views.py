from rest_framework.viewsets import ModelViewSet
from CarRentApi.models import UserProfile
from CarRentApi.serializers import CustomerProfileSerializer,OwnerProfileSerializer

# Create your views here.
class OwnerProfileViewSet(ModelViewSet):
    serializer_class = OwnerProfileSerializer
    queryset = UserProfile.objects.all()

class CustomerProfileViewSet(ModelViewSet):
    serializer_class = CustomerProfileSerializer
    queryset = UserProfile.objects.all()



