from django.db import models
from django.urls import reverse


class user_profile(models.Model):

    # Fields
    date_of_birth = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    user_image = models.ImageField(upload_to="upload/user_images/",blank=True)
    gender = models.CharField(max_length=1,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_user_profile_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Core_user_profile_update", args=(self.pk,))


class Order_item(models.Model):

    # Relationships
    order_id = models.ForeignKey("Core.Order", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Core.Product", on_delete=models.CASCADE)

    # Fields
    order_item_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Order_item_detail", args=(self.order_item_id,))

    def get_update_url(self):
        return reverse("Core_Order_item_update", args=(self.order_item_id,))


class Invoice(models.Model):

    # Relationships
    order_id = models.OneToOneField("Core.Order", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    invoice_details = models.TextField(max_length=100)
    invoice_number = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Invoice_detail", args=(self.invoice_number,))

    def get_update_url(self):
        return reverse("Core_Invoice_update", args=(self.invoice_number,))


class Shipment(models.Model):

    # Relationships
    order_id = models.ForeignKey("Core.Order", on_delete=models.CASCADE)
    invoice_number = models.ForeignKey("Core.Invoice", on_delete=models.CASCADE)

    # Fields
    shipment_date = models.DateField()
    shipment_tracking_number = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    other_shipment_details = models.TextField(max_length=100)
    shipment_id = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Shipment_detail", args=(self.shipment_id,))

    def get_update_url(self):
        return reverse("Core_Shipment_update", args=(self.shipment_id,))


class Ref_Payment_Method(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    payment_method_name = models.CharField(max_length=30)
    payment_method_code = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Ref_Payment_Method_detail", args=(self.payment_method_code,))

    def get_update_url(self):
        return reverse("Core_Ref_Payment_Method_update", args=(self.payment_method_code,))


class Shipment_Item(models.Model):

    # Relationships
    shipment_id = models.ForeignKey("Core.Shipment", on_delete=models.CASCADE)
    order_item_id = models.ForeignKey("Core.Order_item", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Shipment_Item_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Core_Shipment_Item_update", args=(self.pk,))


class Product_Image(models.Model):

    # Relationships
    product_id = models.ForeignKey("Core.Product", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    product_image = models.ImageField(upload_to="upload/product_images/")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Product_Image_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Core_Product_Image_update", args=(self.pk,))


class Product(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    product_name = models.CharField(max_length=30)
    product_description = models.TextField(max_length=100,blank=True,)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sku = models.CharField(max_length=255,blank=True,)
    product_id = models.AutoField(primary_key=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Product_detail", args=(self.product_id,))

    def get_update_url(self):
        return reverse("Core_Product_update", args=(self.product_id,))


class User_Address(models.Model):

    # Relationships
    user_address = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    postal_code = models.CharField(max_length=30,blank=True)
    city = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    district = models.TextField(max_length=100)
    address2 = models.TextField(max_length=100)
    full_name = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    address1 = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_User_Address_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Core_User_Address_update", args=(self.pk,))


class Order(models.Model):

    # Relationships
    order_status_code = models.OneToOneField("Core.Ref_Order_Status_Code", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    order_id = models.AutoField(primary_key=True)
    order_details = models.TextField(max_length=100,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Order_detail", args=(self.order_id,))

    def get_update_url(self):
        return reverse("Core_Order_update", args=(self.order_id,))


class Payment(models.Model):

    # Relationships
    invoice_number = models.ForeignKey("Core.Invoice", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    payment_method = models.TextField(max_length=100)
    payment_id = models.AutoField(primary_key=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Payment_detail", args=(self.payment_id,))

    def get_update_url(self):
        return reverse("Core_Payment_update", args=(self.payment_id,))


class Ref_Order_Item_Status_Code(models.Model):

    # Fields
    order_item_status_code = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    order_item_status_description = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Ref_Order_Item_Status_Code_detail", args=(self.order_item_status_code,))

    def get_update_url(self):
        return reverse("Core_Ref_Order_Item_Status_Code_update", args=(self.order_item_status_code,))


class Ref_Order_Status_Code(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    order_status_code = models.AutoField(primary_key=True)
    order_status_description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Ref_Order_Status_Code_detail", args=(self.order_status_code,))

    def get_update_url(self):
        return reverse("Core_Ref_Order_Status_Code_update", args=(self.order_status_code,))


class Ref_Product_Type(models.Model):

    # Fields
    product_type_code = models.AutoField(primary_key=True)
    product_type_description = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Ref_Product_Type_detail", args=(self.product_type_code,))

    def get_update_url(self):
        return reverse("Core_Ref_Product_Type_update", args=(self.product_type_code,))


class Ref_Invoice_Status_Code(models.Model):

    # Fields
    invoice_status_code = models.AutoField(primary_key=True)
    invoice_status_description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Core_Ref_Invoice_Status_Code_detail", args=(self.invoice_status_code,))

    def get_update_url(self):
        return reverse("Core_Ref_Invoice_Status_Code_update", args=(self.invoice_status_code,))
