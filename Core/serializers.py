from rest_framework import serializers

from . import models


class user_profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.user_profile
        fields = [
            "date_of_birth",
            "created",
            "last_updated",
            "user_image",
            "gender",
        ]

class Order_itemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order_item
        fields = [
            "order_item_id",
            "quantity",
            "created",
            "last_updated",
        ]

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Invoice
        fields = [
            "last_updated",
            "created",
            "invoice_details",
            "invoice_number",
        ]

class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Shipment
        fields = [
            "shipment_date",
            "shipment_tracking_number",
            "created",
            "last_updated",
            "other_shipment_details",
            "shipment_id",
        ]

class Ref_Payment_MethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ref_Payment_Method
        fields = [
            "last_updated",
            "created",
            "payment_method_name",
            "payment_method_code",
        ]

class Shipment_ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Shipment_Item
        fields = [
            "last_updated",
            "created",
        ]

class Product_ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product_Image
        fields = [
            "created",
            "last_updated",
            "product_image",
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "last_updated",
            "product_name",
            "product_description",
            "created",
            "sku",
            "product_id",
            "product_price",
        ]

class User_AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User_Address
        fields = [
            "last_updated",
            "created",
            "postal_code",
            "city",
            "country",
            "district",
            "address2",
            "full_name",
            "phone",
            "address1",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "created",
            "last_updated",
            "order_id",
            "order_details",
        ]

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = [
            "created",
            "payment_method",
            "payment_id",
            "payment_amount",
            "last_updated",
        ]

class Ref_Order_Item_Status_CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ref_Order_Item_Status_Code
        fields = [
            "order_item_status_code",
            "created",
            "order_item_status_description",
            "last_updated",
        ]

class Ref_Order_Status_CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ref_Order_Status_Code
        fields = [
            "last_updated",
            "order_status_code",
            "order_status_description",
            "created",
        ]

class Ref_Product_TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ref_Product_Type
        fields = [
            "product_type_code",
            "product_type_description",
            "last_updated",
            "created",
        ]

class Ref_Invoice_Status_CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ref_Invoice_Status_Code
        fields = [
            "invoice_status_code",
            "invoice_status_description",
            "created",
            "last_updated",
        ]
