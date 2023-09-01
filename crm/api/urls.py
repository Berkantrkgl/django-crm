from django.urls import path
from crm.api import views as api_views

urlpatterns = [
    path('customers/', api_views.CustomerListCreateAPIViews.as_view(), name='customer-list'),
    path('customers/<int:pk>/', api_views.CustomerDetailAPIView.as_view(), name='customer-detail'),
]
