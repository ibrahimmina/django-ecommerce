import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from Core import models as Core_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_Core_user_profile(**kwargs):
    defaults = {}
    defaults["date_of_birth"] = datetime.now()
    defaults["user_image"] = ""
    defaults["gender"] = ""
    defaults.update(**kwargs)
    return Core_models.user_profile.objects.create(**defaults)
def create_Core_Order_item(**kwargs):
    defaults = {}
    defaults["quantity"] = ""
    if "order_id" not in kwargs:
        defaults["order_id"] = create_Core_Order()
    if "product_id" not in kwargs:
        defaults["product_id"] = create_Core_Product()
    defaults.update(**kwargs)
    return Core_models.Order_item.objects.create(**defaults)
def create_Core_Invoice(**kwargs):
    defaults = {}
    defaults["invoice_details"] = ""
    if "order_id" not in kwargs:
        defaults["order_id"] = create_Core_Order()
    defaults.update(**kwargs)
    return Core_models.Invoice.objects.create(**defaults)
def create_Core_Shipment(**kwargs):
    defaults = {}
    defaults["shipment_date"] = datetime.now()
    defaults["shipment_tracking_number"] = ""
    defaults["other_shipment_details"] = ""
    if "order_id" not in kwargs:
        defaults["order_id"] = create_Core_Order()
    if "invoice_number" not in kwargs:
        defaults["invoice_number"] = create_Core_Invoice()
    defaults.update(**kwargs)
    return Core_models.Shipment.objects.create(**defaults)
def create_Core_Ref_Payment_Method(**kwargs):
    defaults = {}
    defaults["payment_method_name"] = ""
    defaults.update(**kwargs)
    return Core_models.Ref_Payment_Method.objects.create(**defaults)
def create_Core_Shipment_Item(**kwargs):
    defaults = {}
    if "shipment_id" not in kwargs:
        defaults["shipment_id"] = create_Core_Shipment()
    if "order_item_id" not in kwargs:
        defaults["order_item_id"] = create_Core_Order_item()
    defaults.update(**kwargs)
    return Core_models.Shipment_Item.objects.create(**defaults)
def create_Core_Product_Image(**kwargs):
    defaults = {}
    defaults["product_image"] = ""
    if "product_id" not in kwargs:
        defaults["product_id"] = create_Core_Product()
    defaults.update(**kwargs)
    return Core_models.Product_Image.objects.create(**defaults)
def create_Core_Product(**kwargs):
    defaults = {}
    defaults["product_name"] = ""
    defaults["product_description"] = ""
    defaults["sku"] = ""
    defaults["product_price"] = ""
    defaults.update(**kwargs)
    return Core_models.Product.objects.create(**defaults)
def create_Core_User_Address(**kwargs):
    defaults = {}
    defaults["postal_code"] = ""
    defaults["city"] = ""
    defaults["country"] = ""
    defaults["district"] = ""
    defaults["address2"] = ""
    defaults["full_name"] = ""
    defaults["phone"] = ""
    defaults["address1"] = ""
    if "user_address" not in kwargs:
        defaults["user_address"] = create_User()
    defaults.update(**kwargs)
    return Core_models.User_Address.objects.create(**defaults)
def create_Core_Order(**kwargs):
    defaults = {}
    defaults["order_details"] = ""
    if "order_status_code" not in kwargs:
        defaults["order_status_code"] = create_Core_Ref_Order_Status_Code()
    defaults.update(**kwargs)
    return Core_models.Order.objects.create(**defaults)
def create_Core_Payment(**kwargs):
    defaults = {}
    defaults["payment_method"] = ""
    defaults["payment_amount"] = ""
    if "invoice_number" not in kwargs:
        defaults["invoice_number"] = create_Core_Invoice()
    defaults.update(**kwargs)
    return Core_models.Payment.objects.create(**defaults)
def create_Core_Ref_Order_Item_Status_Code(**kwargs):
    defaults = {}
    defaults["order_item_status_description"] = ""
    defaults.update(**kwargs)
    return Core_models.Ref_Order_Item_Status_Code.objects.create(**defaults)
def create_Core_Ref_Order_Status_Code(**kwargs):
    defaults = {}
    defaults["order_status_description"] = ""
    defaults.update(**kwargs)
    return Core_models.Ref_Order_Status_Code.objects.create(**defaults)
def create_Core_Ref_Product_Type(**kwargs):
    defaults = {}
    defaults["product_type_description"] = ""
    defaults.update(**kwargs)
    return Core_models.Ref_Product_Type.objects.create(**defaults)
def create_Core_Ref_Invoice_Status_Code(**kwargs):
    defaults = {}
    defaults["invoice_status_description"] = ""
    defaults.update(**kwargs)
    return Core_models.Ref_Invoice_Status_Code.objects.create(**defaults)
