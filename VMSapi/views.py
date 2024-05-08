from django.shortcuts import render
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from .models import Vendor, Purchase_Order,Historical_performance
from .serializers import AcknowledgeSerializer, HistoricalPerformanceOrderSerializer, PurchaseOrderSerializers, VendorSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics



# List all vendors or create a new vendor
class VendorListCreate(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No vendors found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve details or update or delete a specific vendor
class VendorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# List all purchase orders or create a new purchase order
class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = Purchase_Order.objects.all()
    serializer_class = PurchaseOrderSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No purchase order found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Retrieve details or update or delete a specific purchase order
class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset =Purchase_Order.objects.all()
    serializer_class = PurchaseOrderSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Acknowledge the receipt of a purchase order.
class AcknowledgeUpdate(generics.UpdateAPIView):
    queryset = Purchase_Order.objects.all()
    serializer_class = AcknowledgeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.validated_data['acknowledgment_date'] = timezone.now()
        super().perform_update(serializer)
        return Response(serializer.data)

# Retrieve performance details of a specific vendor
class VendorPerformance(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = HistoricalPerformanceOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
