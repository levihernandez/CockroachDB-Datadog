from rest_framework import serializers

from . import models


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Categories
        fields = [
            "category_id",
            "category_name",
            "description",
            "picture",
        ]

class CustomerCustomerDemoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerCustomerDemo
        fields = [
        ]

class CustomerDemographicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomerDemographics
        fields = [
            "customer_type_id",
            "customer_desc",
        ]

class CustomersSerializer(serializers.ModelSerializer):

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

class EmployeeTerritoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmployeeTerritories
        fields = [
        ]

class EmployeesSerializer(serializers.ModelSerializer):

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
            "photo",
            "notes",
            "photo_path",
        ]

class GeographyColumnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GeographyColumns
        fields = [
            "coord_dimension",
            "srid",
            "type",
        ]

class GeometryColumnsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GeometryColumns
        fields = [
            "coord_dimension",
            "srid",
            "type",
        ]

class OrderDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderDetails
        fields = [
            "unit_price",
            "quantity",
            "discount",
        ]

class OrdersSerializer(serializers.ModelSerializer):

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

class ProductsSerializer(serializers.ModelSerializer):

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

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Region
        fields = [
            "region_id",
            "region_description",
        ]

class ShippersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Shippers
        fields = [
            "shipper_id",
            "company_name",
            "phone",
        ]

class SpatialRefSysSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SpatialRefSys
        fields = [
            "srid",
            "auth_name",
            "auth_srid",
            "srtext",
            "proj4text",
        ]

class SuppliersSerializer(serializers.ModelSerializer):

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

class TerritoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Territories
        fields = [
            "territory_id",
            "territory_description",
        ]

class UsStatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UsStates
        fields = [
            "state_id",
            "state_name",
            "state_abbr",
            "state_region",
        ]
