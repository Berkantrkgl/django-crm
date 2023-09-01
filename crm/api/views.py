from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from crm.models import Customer
from crm.api.serializers import CustomerSerializer

# Class views
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from rest_framework.generics import get_object_or_404

from rest_framework import permissions
from crm.api.permissions import IsAdminUserOrReadOnly



class CustomerListCreateAPIViews(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    


# class CustomerListCreateAPIViews(ListModelMixin, CreateModelMixin ,GenericAPIView):

#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     #Listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)  
        

#     #Yaratabilmek
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)







# ESKI TIP VIEWSLER ASAGIDA.

# class CustomerListCreateAPIView(APIView):   
#     def get(self, request):
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(status= status.HTTP_400_BAD_REQUEST)
    
# class CustomerDetailAPIView(APIView):
#     def get_object(self, pk):
#         customer_instance = get_object_or_404(Customer, pk=pk)
#         return customer_instance

#     def get(self, request, pk):
#         customer = self.get_object(pk=pk)
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         customer = self.get_object(pk=pk)
#         serializer = CustomerSerializer(customer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         customer = self.get_object(pk=pk)
#         customer.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
    
