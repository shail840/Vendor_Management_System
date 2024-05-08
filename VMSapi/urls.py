from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/vendors/', views.VendorListCreate.as_view()),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view()),
    path('api/purchase-orders/', views.PurchaseOrderListCreate.as_view()),
    path('api/purchase-orders/<int:pk>/',views.PurchaseOrderRetrieveUpdateDestroy.as_view()),
    path('api/purchase-orders/<int:pk>/acknowledge/',views.AcknowledgeUpdate.as_view()),
    path('api/vendors/<int:pk>/performance/',views.VendorPerformance.as_view()),
    path('apitoken/', obtain_auth_token),
]
