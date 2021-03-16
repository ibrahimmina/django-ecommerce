from django import forms
from . import models


class user_profileForm(forms.ModelForm):
    class Meta:
        model = models.user_profile
        fields = [
            "date_of_birth",
            "user_image",
            "gender",
        ]


class Order_itemForm(forms.ModelForm):
    class Meta:
        model = models.Order_item
        fields = [
            "quantity",
            "order_id",
            "product_id",
        ]


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = models.Invoice
        fields = [
            "invoice_details",
            "order_id",
        ]


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = models.Shipment
        fields = [
            "shipment_date",
            "shipment_tracking_number",
            "other_shipment_details",
            "order_id",
            "invoice_number",
        ]


class Ref_Payment_MethodForm(forms.ModelForm):
    class Meta:
        model = models.Ref_Payment_Method
        fields = [
            "payment_method_name",
        ]


class Shipment_ItemForm(forms.ModelForm):
    class Meta:
        model = models.Shipment_Item
        fields = [
            "shipment_id",
            "order_item_id",
        ]


class Product_ImageForm(forms.ModelForm):
    class Meta:
        model = models.Product_Image
        fields = [
            "product_image",
            "product_id",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "product_name",
            "product_description",
            "sku",
            "product_price",
        ]


class User_AddressForm(forms.ModelForm):
    class Meta:
        model = models.User_Address
        fields = [
            "postal_code",
            "city",
            "country",
            "district",
            "address2",
            "full_name",
            "phone",
            "address1",
            "user_address",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "order_details",
            "order_status_code",
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = [
            "payment_method",
            "payment_amount",
            "invoice_number",
        ]


class Ref_Order_Item_Status_CodeForm(forms.ModelForm):
    class Meta:
        model = models.Ref_Order_Item_Status_Code
        fields = [
            "order_item_status_description",
        ]


class Ref_Order_Status_CodeForm(forms.ModelForm):
    class Meta:
        model = models.Ref_Order_Status_Code
        fields = [
            "order_status_description",
        ]


class Ref_Product_TypeForm(forms.ModelForm):
    class Meta:
        model = models.Ref_Product_Type
        fields = [
            "product_type_description",
        ]


class Ref_Invoice_Status_CodeForm(forms.ModelForm):
    class Meta:
        model = models.Ref_Invoice_Status_Code
        fields = [
            "invoice_status_description",
        ]
