import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_user_profile_list_view():
    instance1 = test_helpers.create_Core_user_profile()
    instance2 = test_helpers.create_Core_user_profile()
    client = Client()
    url = reverse("Core_user_profile_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_user_profile_create_view():
    client = Client()
    url = reverse("Core_user_profile_create")
    data = {
        "date_of_birth": datetime.now(),
        "user_image": "anImage",
        "gender": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_user_profile_detail_view():
    client = Client()
    instance = test_helpers.create_Core_user_profile()
    url = reverse("Core_user_profile_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_user_profile_update_view():
    client = Client()
    instance = test_helpers.create_Core_user_profile()
    url = reverse("Core_user_profile_update", args=[instance.pk, ])
    data = {
        "date_of_birth": datetime.now(),
        "user_image": "anImage",
        "gender": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_item_list_view():
    instance1 = test_helpers.create_Core_Order_item()
    instance2 = test_helpers.create_Core_Order_item()
    client = Client()
    url = reverse("Core_Order_item_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Order_item_create_view():
    order_id = test_helpers.create_Core_Order()
    product_id = test_helpers.create_Core_Product()
    client = Client()
    url = reverse("Core_Order_item_create")
    data = {
        "quantity": 1,
        "order_id": order_id.pk,
        "product_id": product_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_item_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Order_item()
    url = reverse("Core_Order_item_detail", args=[instance.order_item_id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Order_item_update_view():
    order_id = test_helpers.create_Core_Order()
    product_id = test_helpers.create_Core_Product()
    client = Client()
    instance = test_helpers.create_Core_Order_item()
    url = reverse("Core_Order_item_update", args=[instance.order_item_id, ])
    data = {
        "quantity": 1,
        "order_id": order_id.pk,
        "product_id": product_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Invoice_list_view():
    instance1 = test_helpers.create_Core_Invoice()
    instance2 = test_helpers.create_Core_Invoice()
    client = Client()
    url = reverse("Core_Invoice_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Invoice_create_view():
    order_id = test_helpers.create_Core_Order()
    client = Client()
    url = reverse("Core_Invoice_create")
    data = {
        "invoice_details": "text",
        "order_id": order_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Invoice_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Invoice()
    url = reverse("Core_Invoice_detail", args=[instance.invoice_number, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Invoice_update_view():
    order_id = test_helpers.create_Core_Order()
    client = Client()
    instance = test_helpers.create_Core_Invoice()
    url = reverse("Core_Invoice_update", args=[instance.invoice_number, ])
    data = {
        "invoice_details": "text",
        "order_id": order_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Shipment_list_view():
    instance1 = test_helpers.create_Core_Shipment()
    instance2 = test_helpers.create_Core_Shipment()
    client = Client()
    url = reverse("Core_Shipment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Shipment_create_view():
    order_id = test_helpers.create_Core_Order()
    invoice_number = test_helpers.create_Core_Invoice()
    client = Client()
    url = reverse("Core_Shipment_create")
    data = {
        "shipment_date": datetime.now(),
        "shipment_tracking_number": "text",
        "other_shipment_details": "text",
        "order_id": order_id.pk,
        "invoice_number": invoice_number.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Shipment_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Shipment()
    url = reverse("Core_Shipment_detail", args=[instance.shipment_id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Shipment_update_view():
    order_id = test_helpers.create_Core_Order()
    invoice_number = test_helpers.create_Core_Invoice()
    client = Client()
    instance = test_helpers.create_Core_Shipment()
    url = reverse("Core_Shipment_update", args=[instance.shipment_id, ])
    data = {
        "shipment_date": datetime.now(),
        "shipment_tracking_number": "text",
        "other_shipment_details": "text",
        "order_id": order_id.pk,
        "invoice_number": invoice_number.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Payment_Method_list_view():
    instance1 = test_helpers.create_Core_Ref_Payment_Method()
    instance2 = test_helpers.create_Core_Ref_Payment_Method()
    client = Client()
    url = reverse("Core_Ref_Payment_Method_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ref_Payment_Method_create_view():
    client = Client()
    url = reverse("Core_Ref_Payment_Method_create")
    data = {
        "payment_method_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Payment_Method_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Payment_Method()
    url = reverse("Core_Ref_Payment_Method_detail", args=[instance.payment_method_code, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ref_Payment_Method_update_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Payment_Method()
    url = reverse("Core_Ref_Payment_Method_update", args=[instance.payment_method_code, ])
    data = {
        "payment_method_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Shipment_Item_list_view():
    instance1 = test_helpers.create_Core_Shipment_Item()
    instance2 = test_helpers.create_Core_Shipment_Item()
    client = Client()
    url = reverse("Core_Shipment_Item_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Shipment_Item_create_view():
    shipment_id = test_helpers.create_Core_Shipment()
    order_item_id = test_helpers.create_Core_Order_item()
    client = Client()
    url = reverse("Core_Shipment_Item_create")
    data = {
        "shipment_id": shipment_id.pk,
        "order_item_id": order_item_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Shipment_Item_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Shipment_Item()
    url = reverse("Core_Shipment_Item_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Shipment_Item_update_view():
    shipment_id = test_helpers.create_Core_Shipment()
    order_item_id = test_helpers.create_Core_Order_item()
    client = Client()
    instance = test_helpers.create_Core_Shipment_Item()
    url = reverse("Core_Shipment_Item_update", args=[instance.pk, ])
    data = {
        "shipment_id": shipment_id.pk,
        "order_item_id": order_item_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_Image_list_view():
    instance1 = test_helpers.create_Core_Product_Image()
    instance2 = test_helpers.create_Core_Product_Image()
    client = Client()
    url = reverse("Core_Product_Image_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Product_Image_create_view():
    product_id = test_helpers.create_Core_Product()
    client = Client()
    url = reverse("Core_Product_Image_create")
    data = {
        "product_image": "anImage",
        "product_id": product_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_Image_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Product_Image()
    url = reverse("Core_Product_Image_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Product_Image_update_view():
    product_id = test_helpers.create_Core_Product()
    client = Client()
    instance = test_helpers.create_Core_Product_Image()
    url = reverse("Core_Product_Image_update", args=[instance.pk, ])
    data = {
        "product_image": "anImage",
        "product_id": product_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_list_view():
    instance1 = test_helpers.create_Core_Product()
    instance2 = test_helpers.create_Core_Product()
    client = Client()
    url = reverse("Core_Product_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Product_create_view():
    client = Client()
    url = reverse("Core_Product_create")
    data = {
        "product_name": "text",
        "product_description": "text",
        "sku": "text",
        "product_price": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Product_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Product()
    url = reverse("Core_Product_detail", args=[instance.product_id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Product_update_view():
    client = Client()
    instance = test_helpers.create_Core_Product()
    url = reverse("Core_Product_update", args=[instance.product_id, ])
    data = {
        "product_name": "text",
        "product_description": "text",
        "sku": "text",
        "product_price": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_Address_list_view():
    instance1 = test_helpers.create_Core_User_Address()
    instance2 = test_helpers.create_Core_User_Address()
    client = Client()
    url = reverse("Core_User_Address_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_User_Address_create_view():
    user_address = test_helpers.create_User()
    client = Client()
    url = reverse("Core_User_Address_create")
    data = {
        "postal_code": "text",
        "city": "text",
        "country": "text",
        "district": "text",
        "address2": "text",
        "full_name": "text",
        "phone": "text",
        "address1": "text",
        "user_address": user_address.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_User_Address_detail_view():
    client = Client()
    instance = test_helpers.create_Core_User_Address()
    url = reverse("Core_User_Address_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_User_Address_update_view():
    user_address = test_helpers.create_User()
    client = Client()
    instance = test_helpers.create_Core_User_Address()
    url = reverse("Core_User_Address_update", args=[instance.pk, ])
    data = {
        "postal_code": "text",
        "city": "text",
        "country": "text",
        "district": "text",
        "address2": "text",
        "full_name": "text",
        "phone": "text",
        "address1": "text",
        "user_address": user_address.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_list_view():
    instance1 = test_helpers.create_Core_Order()
    instance2 = test_helpers.create_Core_Order()
    client = Client()
    url = reverse("Core_Order_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Order_create_view():
    order_status_code = test_helpers.create_Core_Ref_Order_Status_Code()
    client = Client()
    url = reverse("Core_Order_create")
    data = {
        "order_details": "text",
        "order_status_code": order_status_code.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Order_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Order()
    url = reverse("Core_Order_detail", args=[instance.order_id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Order_update_view():
    order_status_code = test_helpers.create_Core_Ref_Order_Status_Code()
    client = Client()
    instance = test_helpers.create_Core_Order()
    url = reverse("Core_Order_update", args=[instance.order_id, ])
    data = {
        "order_details": "text",
        "order_status_code": order_status_code.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Payment_list_view():
    instance1 = test_helpers.create_Core_Payment()
    instance2 = test_helpers.create_Core_Payment()
    client = Client()
    url = reverse("Core_Payment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Payment_create_view():
    invoice_number = test_helpers.create_Core_Invoice()
    client = Client()
    url = reverse("Core_Payment_create")
    data = {
        "payment_method": "text",
        "payment_amount": 1.0,
        "invoice_number": invoice_number.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Payment_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Payment()
    url = reverse("Core_Payment_detail", args=[instance.payment_id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Payment_update_view():
    invoice_number = test_helpers.create_Core_Invoice()
    client = Client()
    instance = test_helpers.create_Core_Payment()
    url = reverse("Core_Payment_update", args=[instance.payment_id, ])
    data = {
        "payment_method": "text",
        "payment_amount": 1.0,
        "invoice_number": invoice_number.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Order_Item_Status_Code_list_view():
    instance1 = test_helpers.create_Core_Ref_Order_Item_Status_Code()
    instance2 = test_helpers.create_Core_Ref_Order_Item_Status_Code()
    client = Client()
    url = reverse("Core_Ref_Order_Item_Status_Code_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ref_Order_Item_Status_Code_create_view():
    client = Client()
    url = reverse("Core_Ref_Order_Item_Status_Code_create")
    data = {
        "order_item_status_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Order_Item_Status_Code_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Order_Item_Status_Code()
    url = reverse("Core_Ref_Order_Item_Status_Code_detail", args=[instance.order_item_status_code, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ref_Order_Item_Status_Code_update_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Order_Item_Status_Code()
    url = reverse("Core_Ref_Order_Item_Status_Code_update", args=[instance.order_item_status_code, ])
    data = {
        "order_item_status_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Order_Status_Code_list_view():
    instance1 = test_helpers.create_Core_Ref_Order_Status_Code()
    instance2 = test_helpers.create_Core_Ref_Order_Status_Code()
    client = Client()
    url = reverse("Core_Ref_Order_Status_Code_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ref_Order_Status_Code_create_view():
    client = Client()
    url = reverse("Core_Ref_Order_Status_Code_create")
    data = {
        "order_status_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Order_Status_Code_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Order_Status_Code()
    url = reverse("Core_Ref_Order_Status_Code_detail", args=[instance.order_status_code, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ref_Order_Status_Code_update_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Order_Status_Code()
    url = reverse("Core_Ref_Order_Status_Code_update", args=[instance.order_status_code, ])
    data = {
        "order_status_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Product_Type_list_view():
    instance1 = test_helpers.create_Core_Ref_Product_Type()
    instance2 = test_helpers.create_Core_Ref_Product_Type()
    client = Client()
    url = reverse("Core_Ref_Product_Type_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ref_Product_Type_create_view():
    client = Client()
    url = reverse("Core_Ref_Product_Type_create")
    data = {
        "product_type_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Product_Type_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Product_Type()
    url = reverse("Core_Ref_Product_Type_detail", args=[instance.product_type_code, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ref_Product_Type_update_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Product_Type()
    url = reverse("Core_Ref_Product_Type_update", args=[instance.product_type_code, ])
    data = {
        "product_type_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Invoice_Status_Code_list_view():
    instance1 = test_helpers.create_Core_Ref_Invoice_Status_Code()
    instance2 = test_helpers.create_Core_Ref_Invoice_Status_Code()
    client = Client()
    url = reverse("Core_Ref_Invoice_Status_Code_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ref_Invoice_Status_Code_create_view():
    client = Client()
    url = reverse("Core_Ref_Invoice_Status_Code_create")
    data = {
        "invoice_status_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ref_Invoice_Status_Code_detail_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Invoice_Status_Code()
    url = reverse("Core_Ref_Invoice_Status_Code_detail", args=[instance.invoice_status_code, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ref_Invoice_Status_Code_update_view():
    client = Client()
    instance = test_helpers.create_Core_Ref_Invoice_Status_Code()
    url = reverse("Core_Ref_Invoice_Status_Code_update", args=[instance.invoice_status_code, ])
    data = {
        "invoice_status_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
