from django import forms
from . import models


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = models.Categories
        fields = [
            "category_id",
            "category_name",
            "description",

        ]


class CustomerCustomerDemoForm(forms.ModelForm):
    class Meta:
        model = models.CustomerCustomerDemo
        fields = [
            "customer",
            "customer_type",
        ]



class CustomerDemographicsForm(forms.ModelForm):
    class Meta:
        model = models.CustomerDemographics
        fields = [
            "customer_type_id",
            "customer_desc",
        ]


class CustomersForm(forms.ModelForm):
    class Meta:
        model = models.Customers
        fields = [
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


class EmployeeTerritoriesForm(forms.ModelForm):
    class Meta:
        model = models.EmployeeTerritories
        fields = []



class EmployeesForm(forms.ModelForm):
    class Meta:
        model = models.Employees
        fields = [
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
            "notes",
            "photo_path",
        ]


class GeographyColumnsForm(forms.ModelForm):
    class Meta:
        model = models.GeographyColumns
        fields = [
            "coord_dimension",
            "srid",
            "type",
        ]


class GeometryColumnsForm(forms.ModelForm):
    class Meta:
        model = models.GeometryColumns
        fields = [
            "coord_dimension",
            "srid",
            "type",
        ]


class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = models.OrderDetails
        fields = [
            "unit_price",
            "quantity",
            "discount",
        ]


class OrdersForm(forms.ModelForm):
    class Meta:
        model = models.Orders
        fields = [
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


class ProductsForm(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = [
            "product_id",
            "product_name",
            "quantity_per_unit",
            "unit_price",
            "units_in_stock",
            "units_on_order",
            "reorder_level",
            "discontinued",
        ]


class RegionForm(forms.ModelForm):
    class Meta:
        model = models.Region
        fields = [
            "region_id",
            "region_description",
        ]


class ShippersForm(forms.ModelForm):
    class Meta:
        model = models.Shippers
        fields = [
            "shipper_id",
            "company_name",
            "phone",
        ]


class SpatialRefSysForm(forms.ModelForm):
    class Meta:
        model = models.SpatialRefSys
        fields = [
            "srid",
            "auth_name",
            "auth_srid",
            "srtext",
            "proj4text",
        ]


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = models.Suppliers
        fields = [
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


class TerritoriesForm(forms.ModelForm):
    class Meta:
        model = models.Territories
        fields = [
            "territory_id",
            "territory_description",
        ]


class UsStatesForm(forms.ModelForm):
    class Meta:
        model = models.UsStates
        fields = [
            "state_id",
            "state_name",
            "state_abbr",
            "state_region",
        ]
