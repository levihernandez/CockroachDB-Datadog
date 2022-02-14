from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CategoriesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Categories class"""

    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerCustomerDemoViewSet(viewsets.ModelViewSet):
    """ViewSet for the CustomerCustomerDemo class"""

    queryset = models.CustomerCustomerDemo.objects.all()
    serializer_class = serializers.CustomerCustomerDemoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerDemographicsViewSet(viewsets.ModelViewSet):
    """ViewSet for the CustomerDemographics class"""

    queryset = models.CustomerDemographics.objects.all()
    serializer_class = serializers.CustomerDemographicsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Customers class"""

    queryset = models.Customers.objects.all()
    serializer_class = serializers.CustomersSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeTerritoriesViewSet(viewsets.ModelViewSet):
    """ViewSet for the EmployeeTerritories class"""

    queryset = models.EmployeeTerritories.objects.all()
    serializer_class = serializers.EmployeeTerritoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Employees class"""

    queryset = models.Employees.objects.all()
    serializer_class = serializers.EmployeesSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeographyColumnsViewSet(viewsets.ModelViewSet):
    """ViewSet for the GeographyColumns class"""

    queryset = models.GeographyColumns.objects.all()
    serializer_class = serializers.GeographyColumnsSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeometryColumnsViewSet(viewsets.ModelViewSet):
    """ViewSet for the GeometryColumns class"""

    queryset = models.GeometryColumns.objects.all()
    serializer_class = serializers.GeometryColumnsSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailsViewSet(viewsets.ModelViewSet):
    """ViewSet for the OrderDetails class"""

    queryset = models.OrderDetails.objects.all()
    serializer_class = serializers.OrderDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Orders class"""

    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductsViewSet(viewsets.ModelViewSet):
    """ViewSet for the Products class"""

    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Region class"""

    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShippersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Shippers class"""

    queryset = models.Shippers.objects.all()
    serializer_class = serializers.ShippersSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpatialRefSysViewSet(viewsets.ModelViewSet):
    """ViewSet for the SpatialRefSys class"""

    queryset = models.SpatialRefSys.objects.all()
    serializer_class = serializers.SpatialRefSysSerializer
    permission_classes = [permissions.IsAuthenticated]


class SuppliersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Suppliers class"""

    queryset = models.Suppliers.objects.all()
    serializer_class = serializers.SuppliersSerializer
    permission_classes = [permissions.IsAuthenticated]


class TerritoriesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Territories class"""

    queryset = models.Territories.objects.all()
    serializer_class = serializers.TerritoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsStatesViewSet(viewsets.ModelViewSet):
    """ViewSet for the UsStates class"""

    queryset = models.UsStates.objects.all()
    serializer_class = serializers.UsStatesSerializer
    permission_classes = [permissions.IsAuthenticated]
