from rest_framework import viewsets, permissions

from . import serializers
from . import models


class user_profileViewSet(viewsets.ModelViewSet):
    """ViewSet for the user_profile class"""

    queryset = models.user_profile.objects.all()
    serializer_class = serializers.user_profileSerializer
    permission_classes = [permissions.IsAuthenticated]


class Order_itemViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order_item class"""

    queryset = models.Order_item.objects.all()
    serializer_class = serializers.Order_itemSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Invoice class"""

    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShipmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Shipment class"""

    queryset = models.Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class Ref_Payment_MethodViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ref_Payment_Method class"""

    queryset = models.Ref_Payment_Method.objects.all()
    serializer_class = serializers.Ref_Payment_MethodSerializer
    permission_classes = [permissions.IsAuthenticated]


class Shipment_ItemViewSet(viewsets.ModelViewSet):
    """ViewSet for the Shipment_Item class"""

    queryset = models.Shipment_Item.objects.all()
    serializer_class = serializers.Shipment_ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class Product_ImageViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product_Image class"""

    queryset = models.Product_Image.objects.all()
    serializer_class = serializers.Product_ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class User_AddressViewSet(viewsets.ModelViewSet):
    """ViewSet for the User_Address class"""

    queryset = models.User_Address.objects.all()
    serializer_class = serializers.User_AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order class"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Payment class"""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class Ref_Order_Item_Status_CodeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ref_Order_Item_Status_Code class"""

    queryset = models.Ref_Order_Item_Status_Code.objects.all()
    serializer_class = serializers.Ref_Order_Item_Status_CodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class Ref_Order_Status_CodeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ref_Order_Status_Code class"""

    queryset = models.Ref_Order_Status_Code.objects.all()
    serializer_class = serializers.Ref_Order_Status_CodeSerializer
    permission_classes = [permissions.IsAuthenticated]


class Ref_Product_TypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ref_Product_Type class"""

    queryset = models.Ref_Product_Type.objects.all()
    serializer_class = serializers.Ref_Product_TypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class Ref_Invoice_Status_CodeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ref_Invoice_Status_Code class"""

    queryset = models.Ref_Invoice_Status_Code.objects.all()
    serializer_class = serializers.Ref_Invoice_Status_CodeSerializer
    permission_classes = [permissions.IsAuthenticated]
