from django.views import generic
from . import models
from . import forms


class user_profileListView(generic.ListView):
    model = models.user_profile
    form_class = forms.user_profileForm


class user_profileCreateView(generic.CreateView):
    model = models.user_profile
    form_class = forms.user_profileForm


class user_profileDetailView(generic.DetailView):
    model = models.user_profile
    form_class = forms.user_profileForm


class user_profileUpdateView(generic.UpdateView):
    model = models.user_profile
    form_class = forms.user_profileForm
    pk_url_kwarg = "pk"


class Order_itemListView(generic.ListView):
    model = models.Order_item
    form_class = forms.Order_itemForm


class Order_itemCreateView(generic.CreateView):
    model = models.Order_item
    form_class = forms.Order_itemForm


class Order_itemDetailView(generic.DetailView):
    model = models.Order_item
    form_class = forms.Order_itemForm
    pk_url_kwarg = "order_item_id"


class Order_itemUpdateView(generic.UpdateView):
    model = models.Order_item
    form_class = forms.Order_itemForm
    pk_url_kwarg = "order_item_id"


class InvoiceListView(generic.ListView):
    model = models.Invoice
    form_class = forms.InvoiceForm


class InvoiceCreateView(generic.CreateView):
    model = models.Invoice
    form_class = forms.InvoiceForm


class InvoiceDetailView(generic.DetailView):
    model = models.Invoice
    form_class = forms.InvoiceForm
    pk_url_kwarg = "invoice_number"


class InvoiceUpdateView(generic.UpdateView):
    model = models.Invoice
    form_class = forms.InvoiceForm
    pk_url_kwarg = "invoice_number"


class ShipmentListView(generic.ListView):
    model = models.Shipment
    form_class = forms.ShipmentForm


class ShipmentCreateView(generic.CreateView):
    model = models.Shipment
    form_class = forms.ShipmentForm


class ShipmentDetailView(generic.DetailView):
    model = models.Shipment
    form_class = forms.ShipmentForm
    pk_url_kwarg = "shipment_id"


class ShipmentUpdateView(generic.UpdateView):
    model = models.Shipment
    form_class = forms.ShipmentForm
    pk_url_kwarg = "shipment_id"


class Ref_Payment_MethodListView(generic.ListView):
    model = models.Ref_Payment_Method
    form_class = forms.Ref_Payment_MethodForm


class Ref_Payment_MethodCreateView(generic.CreateView):
    model = models.Ref_Payment_Method
    form_class = forms.Ref_Payment_MethodForm


class Ref_Payment_MethodDetailView(generic.DetailView):
    model = models.Ref_Payment_Method
    form_class = forms.Ref_Payment_MethodForm
    pk_url_kwarg = "payment_method_code"


class Ref_Payment_MethodUpdateView(generic.UpdateView):
    model = models.Ref_Payment_Method
    form_class = forms.Ref_Payment_MethodForm
    pk_url_kwarg = "payment_method_code"


class Shipment_ItemListView(generic.ListView):
    model = models.Shipment_Item
    form_class = forms.Shipment_ItemForm


class Shipment_ItemCreateView(generic.CreateView):
    model = models.Shipment_Item
    form_class = forms.Shipment_ItemForm


class Shipment_ItemDetailView(generic.DetailView):
    model = models.Shipment_Item
    form_class = forms.Shipment_ItemForm


class Shipment_ItemUpdateView(generic.UpdateView):
    model = models.Shipment_Item
    form_class = forms.Shipment_ItemForm
    pk_url_kwarg = "pk"


class Product_ImageListView(generic.ListView):
    model = models.Product_Image
    form_class = forms.Product_ImageForm


class Product_ImageCreateView(generic.CreateView):
    model = models.Product_Image
    form_class = forms.Product_ImageForm


class Product_ImageDetailView(generic.DetailView):
    model = models.Product_Image
    form_class = forms.Product_ImageForm


class Product_ImageUpdateView(generic.UpdateView):
    model = models.Product_Image
    form_class = forms.Product_ImageForm
    pk_url_kwarg = "pk"


class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "product_id"


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "product_id"


class User_AddressListView(generic.ListView):
    model = models.User_Address
    form_class = forms.User_AddressForm


class User_AddressCreateView(generic.CreateView):
    model = models.User_Address
    form_class = forms.User_AddressForm


class User_AddressDetailView(generic.DetailView):
    model = models.User_Address
    form_class = forms.User_AddressForm


class User_AddressUpdateView(generic.UpdateView):
    model = models.User_Address
    form_class = forms.User_AddressForm
    pk_url_kwarg = "pk"


class OrderListView(generic.ListView):
    model = models.Order
    form_class = forms.OrderForm


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "order_id"


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "order_id"


class PaymentListView(generic.ListView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentCreateView(generic.CreateView):
    model = models.Payment
    form_class = forms.PaymentForm


class PaymentDetailView(generic.DetailView):
    model = models.Payment
    form_class = forms.PaymentForm
    pk_url_kwarg = "payment_id"


class PaymentUpdateView(generic.UpdateView):
    model = models.Payment
    form_class = forms.PaymentForm
    pk_url_kwarg = "payment_id"


class Ref_Order_Item_Status_CodeListView(generic.ListView):
    model = models.Ref_Order_Item_Status_Code
    form_class = forms.Ref_Order_Item_Status_CodeForm


class Ref_Order_Item_Status_CodeCreateView(generic.CreateView):
    model = models.Ref_Order_Item_Status_Code
    form_class = forms.Ref_Order_Item_Status_CodeForm


class Ref_Order_Item_Status_CodeDetailView(generic.DetailView):
    model = models.Ref_Order_Item_Status_Code
    form_class = forms.Ref_Order_Item_Status_CodeForm
    pk_url_kwarg = "order_item_status_code"


class Ref_Order_Item_Status_CodeUpdateView(generic.UpdateView):
    model = models.Ref_Order_Item_Status_Code
    form_class = forms.Ref_Order_Item_Status_CodeForm
    pk_url_kwarg = "order_item_status_code"


class Ref_Order_Status_CodeListView(generic.ListView):
    model = models.Ref_Order_Status_Code
    form_class = forms.Ref_Order_Status_CodeForm


class Ref_Order_Status_CodeCreateView(generic.CreateView):
    model = models.Ref_Order_Status_Code
    form_class = forms.Ref_Order_Status_CodeForm


class Ref_Order_Status_CodeDetailView(generic.DetailView):
    model = models.Ref_Order_Status_Code
    form_class = forms.Ref_Order_Status_CodeForm
    pk_url_kwarg = "order_status_code"


class Ref_Order_Status_CodeUpdateView(generic.UpdateView):
    model = models.Ref_Order_Status_Code
    form_class = forms.Ref_Order_Status_CodeForm
    pk_url_kwarg = "order_status_code"


class Ref_Product_TypeListView(generic.ListView):
    model = models.Ref_Product_Type
    form_class = forms.Ref_Product_TypeForm


class Ref_Product_TypeCreateView(generic.CreateView):
    model = models.Ref_Product_Type
    form_class = forms.Ref_Product_TypeForm


class Ref_Product_TypeDetailView(generic.DetailView):
    model = models.Ref_Product_Type
    form_class = forms.Ref_Product_TypeForm
    pk_url_kwarg = "product_type_code"


class Ref_Product_TypeUpdateView(generic.UpdateView):
    model = models.Ref_Product_Type
    form_class = forms.Ref_Product_TypeForm
    pk_url_kwarg = "product_type_code"


class Ref_Invoice_Status_CodeListView(generic.ListView):
    model = models.Ref_Invoice_Status_Code
    form_class = forms.Ref_Invoice_Status_CodeForm


class Ref_Invoice_Status_CodeCreateView(generic.CreateView):
    model = models.Ref_Invoice_Status_Code
    form_class = forms.Ref_Invoice_Status_CodeForm


class Ref_Invoice_Status_CodeDetailView(generic.DetailView):
    model = models.Ref_Invoice_Status_Code
    form_class = forms.Ref_Invoice_Status_CodeForm
    pk_url_kwarg = "invoice_status_code"


class Ref_Invoice_Status_CodeUpdateView(generic.UpdateView):
    model = models.Ref_Invoice_Status_Code
    form_class = forms.Ref_Invoice_Status_CodeForm
    pk_url_kwarg = "invoice_status_code"
