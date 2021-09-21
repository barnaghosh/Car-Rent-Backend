from rest_framework.viewsets import ModelViewSet
from CarRentApi.models import UserProfile,Test,Owner,Customer,Book
from CarRentApi.serailizers import OwnerProfileSerializer,CustomerProfileSerializer,BookSerializer
# Create your views here.
class OwnerProfileViewSet(ModelViewSet):
    serializer_class = OwnerProfileSerializer
    queryset = Owner.objects.all()

class CustomerProfileViewSet(ModelViewSet):
    serializer_class = CustomerProfileSerializer
    queryset = Customer.objects.all()

class OrderViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    def get_queryset(self):
        queryset = Book.objects.all()
        id = self.request.query_params.get("id", None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset
