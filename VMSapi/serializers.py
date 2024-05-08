from rest_framework import serializers
from .models import Vendor, Purchase_Order, Historical_performance


class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields=['name','contact_details','address','vendor_code']
        
class PurchaseOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields= ['po_number','vendor','delivery_date','items','quantity','status','quality_rating','issue_date','acknowledgment_date']
        

class AcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        fields = ['acknowledgment_date']
        
class HistoricalPerformanceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name','vendor_code','on_time_delivery','quality_rating_avg','average_response_time','fulfillment_rate']
        