from django.db import models
from django.urls import reverse


class Categories(models.Model):

    # Fields
    category_id = models.SmallIntegerField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    picture = models.BinaryField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'categories'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Categories_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Categories_update", args=(self.pk,))


class CustomerCustomerDemo(models.Model):
    customer = models.OneToOneField('Customers',  primary_key=True, on_delete=models.CASCADE)
    customer_type = models.ForeignKey('CustomerDemographics',  on_delete=models.CASCADE)

    class Meta:
        #managed = False
        db_table = 'customer_customer_demo'
        unique_together = (('customer', 'customer_type'),)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_CustomerCustomerDemo_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_CustomerCustomerDemo_update", args=(self.pk,))


class CustomerDemographics(models.Model):

    # Fields
    customer_type_id = models.CharField(primary_key=True, max_length=200)
    customer_desc = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'customer_demographics'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_CustomerDemographics_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_CustomerDemographics_update", args=(self.pk,))


class Customers(models.Model):

    # Fields
    customer_id = models.CharField(primary_key=True, max_length=200)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Customers_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Customers_update", args=(self.pk,))


class EmployeeTerritories(models.Model):
    employee = models.OneToOneField('Employees',  primary_key=True, on_delete=models.CASCADE)
    territory = models.ForeignKey('Territories',  on_delete=models.CASCADE)

    class Meta:
        #managed = False
        db_table = 'employee_territories'
        unique_together = (('employee', 'territory'),)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_EmployeeTerritories_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_EmployeeTerritories_update", args=(self.pk,))


class Employees(models.Model):

    # Fields
    employee_id = models.SmallIntegerField(primary_key=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=10)
    title = models.CharField(max_length=30, blank=True, null=True)
    title_of_courtesy = models.CharField(max_length=25, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    home_phone = models.CharField(max_length=24, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    photo = models.BinaryField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    reports_to = models.ForeignKey('self',  db_column='reports_to', blank=True, null=True, on_delete=models.CASCADE)
    photo_path = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'employees'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Employees_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Employees_update", args=(self.pk,))


class GeographyColumns(models.Model):

    # Fields
    f_table_catalog = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_schema = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_geography_column = models.TextField(blank=True, null=True)  # This field type is a guess.
    coord_dimension = models.BigIntegerField(blank=True, null=True)
    srid = models.BigIntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'geography_columns'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_GeographyColumns_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_GeographyColumns_update", args=(self.pk,))


class GeometryColumns(models.Model):
    f_table_catalog = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_schema = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_table_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    f_geometry_column = models.TextField(blank=True, null=True)  # This field type is a guess.
    coord_dimension = models.BigIntegerField(blank=True, null=True)
    srid = models.BigIntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'geometry_columns'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_GeometryColumns_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_GeometryColumns_update", args=(self.pk,))


class OrderDetails(models.Model):
    order = models.OneToOneField('Orders', primary_key=True, on_delete=models.CASCADE)
    product = models.ForeignKey('Products',  on_delete=models.CASCADE)
    unit_price = models.FloatField()
    quantity = models.SmallIntegerField()
    discount = models.FloatField()

    class Meta:
        #managed = False
        db_table = 'order_details'
        unique_together = (('order', 'product'),)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_OrderDetails_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_OrderDetails_update", args=(self.pk,))


class Orders(models.Model):
    order_id = models.SmallIntegerField(primary_key=True)
    customer = models.ForeignKey(Customers,  blank=True, null=True, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees,  blank=True, null=True, on_delete=models.CASCADE)
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    ship_via = models.ForeignKey('Shippers',  db_column='ship_via', blank=True, null=True, on_delete=models.CASCADE)
    freight = models.FloatField(blank=True, null=True)
    ship_name = models.CharField(max_length=40, blank=True, null=True)
    ship_address = models.CharField(max_length=60, blank=True, null=True)
    ship_city = models.CharField(max_length=15, blank=True, null=True)
    ship_region = models.CharField(max_length=15, blank=True, null=True)
    ship_postal_code = models.CharField(max_length=10, blank=True, null=True)
    ship_country = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'orders'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Orders_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Orders_update", args=(self.pk,))


class Products(models.Model):
    product_id = models.SmallIntegerField(primary_key=True)
    product_name = models.CharField(max_length=40)
    supplier = models.ForeignKey('Suppliers',  blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories,  blank=True, null=True, on_delete=models.CASCADE)
    quantity_per_unit = models.CharField(max_length=20, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    units_in_stock = models.SmallIntegerField(blank=True, null=True)
    units_on_order = models.SmallIntegerField(blank=True, null=True)
    reorder_level = models.SmallIntegerField(blank=True, null=True)
    discontinued = models.BigIntegerField()

    class Meta:
        #managed = False
        db_table = 'products'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Products_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Products_update", args=(self.pk,))


class Region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True)
    region_description = models.CharField(max_length=200)

    class Meta:
        #managed = False
        db_table = 'region'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Region_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Region_update", args=(self.pk,))


class Shippers(models.Model):
    shipper_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'shippers'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Shippers_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Shippers_update", args=(self.pk,))


class SpatialRefSys(models.Model):
    srid = models.BigIntegerField(blank=True, null=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.BigIntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'spatial_ref_sys'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_SpatialRefSys_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_SpatialRefSys_update", args=(self.pk,))


class Suppliers(models.Model):
    supplier_id = models.SmallIntegerField(primary_key=True)
    company_name = models.CharField(max_length=40)
    contact_name = models.CharField(max_length=30, blank=True, null=True)
    contact_title = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    region = models.CharField(max_length=15, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'suppliers'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Suppliers_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Suppliers_update", args=(self.pk,))


class Territories(models.Model):
    territory_id = models.CharField(primary_key=True, max_length=20)
    territory_description = models.CharField(max_length=200)
    region = models.ForeignKey(Region,  on_delete=models.CASCADE)

    class Meta:
        #managed = False
        db_table = 'territories'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_Territories_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_Territories_update", args=(self.pk,))


class UsStates(models.Model):
    state_id = models.SmallIntegerField(primary_key=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)
    state_abbr = models.CharField(max_length=2, blank=True, null=True)
    state_region = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'us_states'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("crm_UsStates_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("crm_UsStates_update", args=(self.pk,))
