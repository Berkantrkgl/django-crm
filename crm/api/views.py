from crm.models import Customer
from crm.api.serializers import CustomerSerializer

# Import API generics
from rest_framework import generics
from crm.api.permissions import IsAdminUserOrReadOnly

# For Pagination
from crm.api.pagination import SmallPagination

# Qeuryset import
from django.db.models import Q


class CustomerListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination

    # Custom search function
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.method == "GET":
            search_str = self.request.query_params.get("search")
            if search_str:
                #import ipdb; ipdb.set_trace()
                search_str = search_str.lower()
                queryset = queryset.filter(
                    Q(first_name__contains=search_str) | 
                    Q(last_name__contains=search_str) 
                )
        return queryset


class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUserOrReadOnly]
