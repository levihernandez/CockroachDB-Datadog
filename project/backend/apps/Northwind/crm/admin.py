from django.contrib import admin
from django import forms

from . import models


class CategoriesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Categories
        fields = "__all__"


class CategoriesAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm
    list_display = [
        "category_id",
        "category_name",
        "description",
        "picture",
    ]
    readonly_fields = [
        "category_id",
        "category_name",
        "description",
        "picture",
    ]


class CustomerCustomerDemoAdminForm(forms.ModelForm):

    class Meta:
        model = models.CustomerCustomerDemo
        fields = "__all__"


class CustomerCustomerDemoAdmin(admin.ModelAdmin):
    form = CustomerCustomerDemoAdminForm
    list_display = [
    ]
    readonly_fields = [
    ]


class CustomerDemographicsAdminForm(forms.ModelForm):

    class Meta:
        model = models.CustomerDemographics
        fields = "__all__"


class CustomerDemographicsAdmin(admin.ModelAdmin):
    form = CustomerDemographicsAdminForm
    list_display = [
        "customer_type_id",
        "customer_desc",
    ]
    readonly_fields = [
        "customer_type_id",
        "customer_desc",
    ]


class CustomersAdminForm(forms.ModelForm):

    class Meta:
        model = models.Customers
        fields = "__all__"


class CustomersAdmin(admin.ModelAdmin):
    form = CustomersAdminForm
    list_display = [
        "customer_id",
        "company_name",
        "contact_name",
        "contact_title",
        "address",
        "city",
        "region",
        "postal_code",
        "country",
        "phone",
        "fax",
    ]
    readonly_fields = [
        "customer_id",
        "company_name",
        "contact_name",
        "contact_title",
        "address",
        "city",
        "region",
        "postal_code",
        "country",
        "phone",
        "fax",
    ]


class EmployeeTerritoriesAdminForm(forms.ModelForm):

    class Meta:
        model = models.EmployeeTerritories
        fields = "__all__"


class EmployeeTerritoriesAdmin(admin.ModelAdmin):
    form = EmployeeTerritoriesAdminForm
    list_display = [
    ]
    readonly_fields = [
    ]


class EmployeesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Employees
        fields = "__all__"


class EmployeesAdmin(admin.ModelAdmin):
    form = EmployeesAdminForm
    list_display = [
        "employee_id",
        "last_name",
        "first_name",
        "title",
        "title_of_courtesy",
        "birth_date",
        "hire_date",
        "address",
        "city",
        "region",
        "postal_code",
        "country",
        "home_phone",
        "extension",
        "photo",
        "notes",
        "photo_path",
    ]
    readonly_fields = [
        "employee_id",
        "last_name",
        "first_name",
        "title",
        "title_of_courtesy",
        "birth_date",
        "hire_date",
        "address",
        "city",
        "region",
        "postal_code",
        "country",
        "home_phone",
        "extension",
        "photo",
        "notes",
        "photo_path",
    ]


class GeographyColumnsAdminForm(forms.ModelForm):

    class Meta:
        model = models.GeographyColumns
        fields = "__all__"


class GeographyColumnsAdmin(admin.ModelAdmin):
    form = GeographyColumnsAdminForm
    list_display = [
        "coord_dimension",
        "srid",
        "type",
    ]
    readonly_fields = [
        "coord_dimension",
        "srid",
        "type",
    ]


class GeometryColumnsAdminForm(forms.ModelForm):

    class Meta:
        model = models.GeometryColumns
        fields = "__all__"


class GeometryColumnsAdmin(admin.ModelAdmin):
    form = GeometryColumnsAdminForm
    list_display = [
        "coord_dimension",
        "srid",
        "type",
    ]
    readonly_fields = [
        "coord_dimension",
        "srid",
        "type",
    ]


class OrderDetailsAdminForm(forms.ModelForm):

    class Meta:
        model = models.OrderDetails
        fields = "__all__"


class OrderDetailsAdmin(admin.ModelAdmin):
    form = OrderDetailsAdminForm
    list_display = [
        "unit_price",
        "quantity",
        "discount",
    ]
    readonly_fields = [
        "unit_price",
        "quantity",
        "discount",
    ]


class OrdersAdminForm(forms.ModelForm):

    class Meta:
        model = models.Orders
        fields = "__all__"


class OrdersAdmin(admin.ModelAdmin):
    form = OrdersAdminForm
    list_display = [
        "order_id",
        "order_date",
        "required_date",
        "shipped_date",
        "freight",
        "ship_name",
        "ship_address",
        "ship_city",
        "ship_region",
        "ship_postal_code",
        "ship_country",
    ]
    readonly_fields = [
        "order_id",
        "order_date",
        "required_date",
        "shipped_date",
        "freight",
        "ship_name",
        "ship_address",
        "ship_city",
        "ship_region",
        "ship_postal_code",
        "ship_country",
    ]


class ProductsAdminForm(forms.ModelForm):

    class Meta:
        model = models.Products
        fields = "__all__"


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = [
        "product_id",
        "product_name",
        "quantity_per_unit",
        "unit_price",
        "units_in_stock",
        "units_on_order",
        "reorder_level",
        "discontinued",
    ]
    readonly_fields = [
        "product_id",
        "product_name",
        "quantity_per_unit",
        "unit_price",
        "units_in_stock",
        "units_on_order",
        "reorder_level",
        "discontinued",
    ]


class RegionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Region
        fields = "__all__"


class RegionAdmin(admin.ModelAdmin):
    form = RegionAdminForm
    list_display = [
        "region_id",
        "region_description",
    ]
    readonly_fields = [
        "region_id",
        "region_description",
    ]


class ShippersAdminForm(forms.ModelForm):

    class Meta:
        model = models.Shippers
        fields = "__all__"


class ShippersAdmin(admin.ModelAdmin):
    form = ShippersAdminForm
    list_display = [
        "shipper_id",
        "company_name",
        "phone",
    ]
    readonly_fields = [
        "shipper_id",
        "company_name",
        "phone",
    ]


class SpatialRefSysAdminForm(forms.ModelForm):

    class Meta:
        model = models.SpatialRefSys
        fields = "__all__"


class SpatialRefSysAdmin(admin.ModelAdmin):
    form = SpatialRefSysAdminForm
    list_display = [
        "srid",
        "auth_name",
        "auth_srid",
        "srtext",
        "proj4text",
    ]
    readonly_fields = [
        "srid",
        "auth_name",
        "auth_srid",
        "srtext",
        "proj4text",
    ]


class SuppliersAdminForm(forms.ModelForm):

    class Meta:
        model = models.Suppliers
        fields = "__all__"


class SuppliersAdmin(admin.ModelAdmin):
    form = SuppliersAdminForm
    list_display = [
        "supplier_id",
        "company_name",
        "contact_name",
        "contact_title",
        "address",
        "city",
        "region",
        "postal_code",
        "country",
        "phone",
        "fax",
        "homepage",
    ]
    readonly_fields = [
        "supplier_id",
        "company_name",
        "contact_name",
        "contact_title",
        "address",
        "city",
        "region",
        "postal_code",
        "country",
        "phone",
        "fax",
        "homepage",
    ]


class TerritoriesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Territories
        fields = "__all__"


class TerritoriesAdmin(admin.ModelAdmin):
    form = TerritoriesAdminForm
    list_display = [
        "territory_id",
        "territory_description",
    ]
    readonly_fields = [
        "territory_id",
        "territory_description",
    ]


class UsStatesAdminForm(forms.ModelForm):

    class Meta:
        model = models.UsStates
        fields = "__all__"


class UsStatesAdmin(admin.ModelAdmin):
    form = UsStatesAdminForm
    list_display = [
        "state_id",
        "state_name",
        "state_abbr",
        "state_region",
    ]
    readonly_fields = [
        "state_id",
        "state_name",
        "state_abbr",
        "state_region",
    ]


admin.site.register(models.Categories, CategoriesAdmin)
admin.site.register(models.CustomerCustomerDemo, CustomerCustomerDemoAdmin)
admin.site.register(models.CustomerDemographics, CustomerDemographicsAdmin)
admin.site.register(models.Customers, CustomersAdmin)
admin.site.register(models.EmployeeTerritories, EmployeeTerritoriesAdmin)
admin.site.register(models.Employees, EmployeesAdmin)
admin.site.register(models.GeographyColumns, GeographyColumnsAdmin)
admin.site.register(models.GeometryColumns, GeometryColumnsAdmin)
admin.site.register(models.OrderDetails, OrderDetailsAdmin)
admin.site.register(models.Orders, OrdersAdmin)
admin.site.register(models.Products, ProductsAdmin)
admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.Shippers, ShippersAdmin)
admin.site.register(models.SpatialRefSys, SpatialRefSysAdmin)
admin.site.register(models.Suppliers, SuppliersAdmin)
admin.site.register(models.Territories, TerritoriesAdmin)
admin.site.register(models.UsStates, UsStatesAdmin)
