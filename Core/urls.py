from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("user_profile", api.user_profileViewSet)
router.register("Order_item", api.Order_itemViewSet)
router.register("Invoice", api.InvoiceViewSet)
router.register("Shipment", api.ShipmentViewSet)
router.register("Ref_Payment_Method", api.Ref_Payment_MethodViewSet)
router.register("Shipment_Item", api.Shipment_ItemViewSet)
router.register("Product_Image", api.Product_ImageViewSet)
router.register("Product", api.ProductViewSet)
router.register("User_Address", api.User_AddressViewSet)
router.register("Order", api.OrderViewSet)
router.register("Payment", api.PaymentViewSet)
router.register("Ref_Order_Item_Status_Code", api.Ref_Order_Item_Status_CodeViewSet)
router.register("Ref_Order_Status_Code", api.Ref_Order_Status_CodeViewSet)
router.register("Ref_Product_Type", api.Ref_Product_TypeViewSet)
router.register("Ref_Invoice_Status_Code", api.Ref_Invoice_Status_CodeViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Core/user_profile/", views.user_profileListView.as_view(), name="Core_user_profile_list"),
    path("Core/user_profile/create/", views.user_profileCreateView.as_view(), name="Core_user_profile_create"),
    path("Core/user_profile/detail/<int:pk>/", views.user_profileDetailView.as_view(), name="Core_user_profile_detail"),
    path("Core/user_profile/update/<int:pk>/", views.user_profileUpdateView.as_view(), name="Core_user_profile_update"),
    path("Core/Order_item/", views.Order_itemListView.as_view(), name="Core_Order_item_list"),
    path("Core/Order_item/create/", views.Order_itemCreateView.as_view(), name="Core_Order_item_create"),
    path("Core/Order_item/detail/<int:order_item_id>/", views.Order_itemDetailView.as_view(), name="Core_Order_item_detail"),
    path("Core/Order_item/update/<int:order_item_id>/", views.Order_itemUpdateView.as_view(), name="Core_Order_item_update"),
    path("Core/Invoice/", views.InvoiceListView.as_view(), name="Core_Invoice_list"),
    path("Core/Invoice/create/", views.InvoiceCreateView.as_view(), name="Core_Invoice_create"),
    path("Core/Invoice/detail/<int:invoice_number>/", views.InvoiceDetailView.as_view(), name="Core_Invoice_detail"),
    path("Core/Invoice/update/<int:invoice_number>/", views.InvoiceUpdateView.as_view(), name="Core_Invoice_update"),
    path("Core/Shipment/", views.ShipmentListView.as_view(), name="Core_Shipment_list"),
    path("Core/Shipment/create/", views.ShipmentCreateView.as_view(), name="Core_Shipment_create"),
    path("Core/Shipment/detail/<int:shipment_id>/", views.ShipmentDetailView.as_view(), name="Core_Shipment_detail"),
    path("Core/Shipment/update/<int:shipment_id>/", views.ShipmentUpdateView.as_view(), name="Core_Shipment_update"),
    path("Core/Ref_Payment_Method/", views.Ref_Payment_MethodListView.as_view(), name="Core_Ref_Payment_Method_list"),
    path("Core/Ref_Payment_Method/create/", views.Ref_Payment_MethodCreateView.as_view(), name="Core_Ref_Payment_Method_create"),
    path("Core/Ref_Payment_Method/detail/<int:payment_method_code>/", views.Ref_Payment_MethodDetailView.as_view(), name="Core_Ref_Payment_Method_detail"),
    path("Core/Ref_Payment_Method/update/<int:payment_method_code>/", views.Ref_Payment_MethodUpdateView.as_view(), name="Core_Ref_Payment_Method_update"),
    path("Core/Shipment_Item/", views.Shipment_ItemListView.as_view(), name="Core_Shipment_Item_list"),
    path("Core/Shipment_Item/create/", views.Shipment_ItemCreateView.as_view(), name="Core_Shipment_Item_create"),
    path("Core/Shipment_Item/detail/<int:pk>/", views.Shipment_ItemDetailView.as_view(), name="Core_Shipment_Item_detail"),
    path("Core/Shipment_Item/update/<int:pk>/", views.Shipment_ItemUpdateView.as_view(), name="Core_Shipment_Item_update"),
    path("Core/Product_Image/", views.Product_ImageListView.as_view(), name="Core_Product_Image_list"),
    path("Core/Product_Image/create/", views.Product_ImageCreateView.as_view(), name="Core_Product_Image_create"),
    path("Core/Product_Image/detail/<int:pk>/", views.Product_ImageDetailView.as_view(), name="Core_Product_Image_detail"),
    path("Core/Product_Image/update/<int:pk>/", views.Product_ImageUpdateView.as_view(), name="Core_Product_Image_update"),
    path("Core/Product/", views.ProductListView.as_view(), name="Core_Product_list"),
    path("Core/Product/create/", views.ProductCreateView.as_view(), name="Core_Product_create"),
    path("Core/Product/detail/<int:product_id>/", views.ProductDetailView.as_view(), name="Core_Product_detail"),
    path("Core/Product/update/<int:product_id>/", views.ProductUpdateView.as_view(), name="Core_Product_update"),
    path("Core/User_Address/", views.User_AddressListView.as_view(), name="Core_User_Address_list"),
    path("Core/User_Address/create/", views.User_AddressCreateView.as_view(), name="Core_User_Address_create"),
    path("Core/User_Address/detail/<int:pk>/", views.User_AddressDetailView.as_view(), name="Core_User_Address_detail"),
    path("Core/User_Address/update/<int:pk>/", views.User_AddressUpdateView.as_view(), name="Core_User_Address_update"),
    path("Core/Order/", views.OrderListView.as_view(), name="Core_Order_list"),
    path("Core/Order/create/", views.OrderCreateView.as_view(), name="Core_Order_create"),
    path("Core/Order/detail/<int:order_id>/", views.OrderDetailView.as_view(), name="Core_Order_detail"),
    path("Core/Order/update/<int:order_id>/", views.OrderUpdateView.as_view(), name="Core_Order_update"),
    path("Core/Payment/", views.PaymentListView.as_view(), name="Core_Payment_list"),
    path("Core/Payment/create/", views.PaymentCreateView.as_view(), name="Core_Payment_create"),
    path("Core/Payment/detail/<int:payment_id>/", views.PaymentDetailView.as_view(), name="Core_Payment_detail"),
    path("Core/Payment/update/<int:payment_id>/", views.PaymentUpdateView.as_view(), name="Core_Payment_update"),
    path("Core/Ref_Order_Item_Status_Code/", views.Ref_Order_Item_Status_CodeListView.as_view(), name="Core_Ref_Order_Item_Status_Code_list"),
    path("Core/Ref_Order_Item_Status_Code/create/", views.Ref_Order_Item_Status_CodeCreateView.as_view(), name="Core_Ref_Order_Item_Status_Code_create"),
    path("Core/Ref_Order_Item_Status_Code/detail/<int:order_item_status_code>/", views.Ref_Order_Item_Status_CodeDetailView.as_view(), name="Core_Ref_Order_Item_Status_Code_detail"),
    path("Core/Ref_Order_Item_Status_Code/update/<int:order_item_status_code>/", views.Ref_Order_Item_Status_CodeUpdateView.as_view(), name="Core_Ref_Order_Item_Status_Code_update"),
    path("Core/Ref_Order_Status_Code/", views.Ref_Order_Status_CodeListView.as_view(), name="Core_Ref_Order_Status_Code_list"),
    path("Core/Ref_Order_Status_Code/create/", views.Ref_Order_Status_CodeCreateView.as_view(), name="Core_Ref_Order_Status_Code_create"),
    path("Core/Ref_Order_Status_Code/detail/<int:order_status_code>/", views.Ref_Order_Status_CodeDetailView.as_view(), name="Core_Ref_Order_Status_Code_detail"),
    path("Core/Ref_Order_Status_Code/update/<int:order_status_code>/", views.Ref_Order_Status_CodeUpdateView.as_view(), name="Core_Ref_Order_Status_Code_update"),
    path("Core/Ref_Product_Type/", views.Ref_Product_TypeListView.as_view(), name="Core_Ref_Product_Type_list"),
    path("Core/Ref_Product_Type/create/", views.Ref_Product_TypeCreateView.as_view(), name="Core_Ref_Product_Type_create"),
    path("Core/Ref_Product_Type/detail/<int:product_type_code>/", views.Ref_Product_TypeDetailView.as_view(), name="Core_Ref_Product_Type_detail"),
    path("Core/Ref_Product_Type/update/<int:product_type_code>/", views.Ref_Product_TypeUpdateView.as_view(), name="Core_Ref_Product_Type_update"),
    path("Core/Ref_Invoice_Status_Code/", views.Ref_Invoice_Status_CodeListView.as_view(), name="Core_Ref_Invoice_Status_Code_list"),
    path("Core/Ref_Invoice_Status_Code/create/", views.Ref_Invoice_Status_CodeCreateView.as_view(), name="Core_Ref_Invoice_Status_Code_create"),
    path("Core/Ref_Invoice_Status_Code/detail/<int:invoice_status_code>/", views.Ref_Invoice_Status_CodeDetailView.as_view(), name="Core_Ref_Invoice_Status_Code_detail"),
    path("Core/Ref_Invoice_Status_Code/update/<int:invoice_status_code>/", views.Ref_Invoice_Status_CodeUpdateView.as_view(), name="Core_Ref_Invoice_Status_Code_update"),
)
