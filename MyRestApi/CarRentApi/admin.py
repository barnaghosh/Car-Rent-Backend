from django.contrib import admin
from CarRentApi.models import UserProfile,Owner,Customer,Book

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Owner)
admin.site.register(Customer)
admin.site.register(Book)