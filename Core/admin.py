from django.contrib import admin
from django import forms

from . import models


class user_profileAdminForm(forms.ModelForm):

    class Meta:
        model = models.user_profile
        fields = "__all__"


class user_profileAdmin(admin.ModelAdmin):
    form = user_profileAdminForm
    list_display = [
        "date_of_birth",
        "created",
        "last_updated",
        "user_image",
        "gender",
    ]
    readonly_fields = [
        "date_of_birth",
        "created",
        "last_updated",
        "user_image",
        "gender",
    ]


class Order_itemAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order_item
        fields = "__all__"


class Order_itemAdmin(admin.ModelAdmin):
    form = Order_itemAdminForm
    list_display = [
        "order_item_id",
        "quantity",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "order_item_id",
        "quantity",
        "created",
        "last_updated",
    ]


class InvoiceAdminForm(forms.ModelForm):

    class Meta:
        model = models.Invoice
        fields = "__all__"


class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm
    list_display = [
        "last_updated",
        "created",
        "invoice_details",
        "invoice_number",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "invoice_details",
        "invoice_number",
    ]


class ShipmentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Shipment
        fields = "__all__"


class ShipmentAdmin(admin.ModelAdmin):
    form = ShipmentAdminForm
    list_display = [
        "shipment_date",
        "shipment_tracking_number",
        "created",
        "last_updated",
        "other_shipment_details",
        "shipment_id",
    ]
    readonly_fields = [
        "shipment_date",
        "shipment_tracking_number",
        "created",
        "last_updated",
        "other_shipment_details",
        "shipment_id",
    ]


class Ref_Payment_MethodAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ref_Payment_Method
        fields = "__all__"


class Ref_Payment_MethodAdmin(admin.ModelAdmin):
    form = Ref_Payment_MethodAdminForm
    list_display = [
        "last_updated",
        "created",
        "payment_method_name",
        "payment_method_code",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "payment_method_name",
        "payment_method_code",
    ]


class Shipment_ItemAdminForm(forms.ModelForm):

    class Meta:
        model = models.Shipment_Item
        fields = "__all__"


class Shipment_ItemAdmin(admin.ModelAdmin):
    form = Shipment_ItemAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class Product_ImageAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product_Image
        fields = "__all__"


class Product_ImageAdmin(admin.ModelAdmin):
    form = Product_ImageAdminForm
    list_display = [
        "created",
        "last_updated",
        "product_image",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "product_image",
    ]


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "last_updated",
        "product_name",
        "product_description",
        "created",
        "sku",
        "product_id",
        "product_price",
    ]
    readonly_fields = [
        "last_updated",
        "product_name",
        "product_description",
        "created",
        "sku",
        "product_id",
        "product_price",
    ]


class User_AddressAdminForm(forms.ModelForm):

    class Meta:
        model = models.User_Address
        fields = "__all__"


class User_AddressAdmin(admin.ModelAdmin):
    form = User_AddressAdminForm
    list_display = [
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
    readonly_fields = [
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


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
        "created",
        "last_updated",
        "order_id",
        "order_details",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "order_id",
        "order_details",
    ]


class PaymentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Payment
        fields = "__all__"


class PaymentAdmin(admin.ModelAdmin):
    form = PaymentAdminForm
    list_display = [
        "created",
        "payment_method",
        "payment_id",
        "payment_amount",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "payment_method",
        "payment_id",
        "payment_amount",
        "last_updated",
    ]


class Ref_Order_Item_Status_CodeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ref_Order_Item_Status_Code
        fields = "__all__"


class Ref_Order_Item_Status_CodeAdmin(admin.ModelAdmin):
    form = Ref_Order_Item_Status_CodeAdminForm
    list_display = [
        "order_item_status_code",
        "created",
        "order_item_status_description",
        "last_updated",
    ]
    #readonly_fields = [
    #    "order_item_status_code",
    #    "created",
    #    "order_item_status_description",
    #    "last_updated",
    #]


class Ref_Order_Status_CodeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ref_Order_Status_Code
        fields = "__all__"


class Ref_Order_Status_CodeAdmin(admin.ModelAdmin):
    form = Ref_Order_Status_CodeAdminForm
    list_display = [
        "last_updated",
        "order_status_code",
        "order_status_description",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "order_status_code",
        "order_status_description",
        "created",
    ]


class Ref_Product_TypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ref_Product_Type
        fields = "__all__"


class Ref_Product_TypeAdmin(admin.ModelAdmin):
    form = Ref_Product_TypeAdminForm
    list_display = [
        "product_type_code",
        "product_type_description",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "product_type_code",
        "product_type_description",
        "last_updated",
        "created",
    ]


class Ref_Invoice_Status_CodeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ref_Invoice_Status_Code
        fields = "__all__"


class Ref_Invoice_Status_CodeAdmin(admin.ModelAdmin):
    form = Ref_Invoice_Status_CodeAdminForm
    list_display = [
        "invoice_status_code",
        "invoice_status_description",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "invoice_status_code",
        "invoice_status_description",
        "created",
        "last_updated",
    ]


admin.site.register(models.user_profile, user_profileAdmin)
admin.site.register(models.Order_item, Order_itemAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Shipment, ShipmentAdmin)
admin.site.register(models.Ref_Payment_Method, Ref_Payment_MethodAdmin)
admin.site.register(models.Shipment_Item, Shipment_ItemAdmin)
admin.site.register(models.Product_Image, Product_ImageAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.User_Address, User_AddressAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Ref_Order_Item_Status_Code, Ref_Order_Item_Status_CodeAdmin)
admin.site.register(models.Ref_Order_Status_Code, Ref_Order_Status_CodeAdmin)
admin.site.register(models.Ref_Product_Type, Ref_Product_TypeAdmin)
admin.site.register(models.Ref_Invoice_Status_Code, Ref_Invoice_Status_CodeAdmin)
