from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Categories", api.CategoriesViewSet)
router.register("CustomerCustomerDemo", api.CustomerCustomerDemoViewSet)
router.register("CustomerDemographics", api.CustomerDemographicsViewSet)
router.register("Customers", api.CustomersViewSet)
router.register("EmployeeTerritories", api.EmployeeTerritoriesViewSet)
router.register("Employees", api.EmployeesViewSet)
router.register("GeographyColumns", api.GeographyColumnsViewSet)
router.register("GeometryColumns", api.GeometryColumnsViewSet)
router.register("OrderDetails", api.OrderDetailsViewSet)
router.register("Orders", api.OrdersViewSet)
router.register("Products", api.ProductsViewSet)
router.register("Region", api.RegionViewSet)
router.register("Shippers", api.ShippersViewSet)
router.register("SpatialRefSys", api.SpatialRefSysViewSet)
router.register("Suppliers", api.SuppliersViewSet)
router.register("Territories", api.TerritoriesViewSet)
router.register("UsStates", api.UsStatesViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("crm/Categories/", views.CategoriesListView.as_view(), name="crm_Categories_list"),
    path("crm/Categories/create/", views.CategoriesCreateView.as_view(), name="crm_Categories_create"),
    path("crm/Categories/detail/<int:pk>/", views.CategoriesDetailView.as_view(), name="crm_Categories_detail"),
    path("crm/Categories/update/<int:pk>/", views.CategoriesUpdateView.as_view(), name="crm_Categories_update"),
    path("crm/Categories/delete/<int:pk>/", views.CategoriesDeleteView.as_view(), name="crm_Categories_delete"),
    path("crm/CustomerCustomerDemo/", views.CustomerCustomerDemoListView.as_view(), name="crm_CustomerCustomerDemo_list"),
    path("crm/CustomerCustomerDemo/create/", views.CustomerCustomerDemoCreateView.as_view(), name="crm_CustomerCustomerDemo_create"),
    path("crm/CustomerCustomerDemo/detail/<int:pk>/", views.CustomerCustomerDemoDetailView.as_view(), name="crm_CustomerCustomerDemo_detail"),
    path("crm/CustomerCustomerDemo/update/<int:pk>/", views.CustomerCustomerDemoUpdateView.as_view(), name="crm_CustomerCustomerDemo_update"),
    path("crm/CustomerCustomerDemo/delete/<int:pk>/", views.CustomerCustomerDemoDeleteView.as_view(), name="crm_CustomerCustomerDemo_delete"),
    path("crm/CustomerDemographics/", views.CustomerDemographicsListView.as_view(), name="crm_CustomerDemographics_list"),
    path("crm/CustomerDemographics/create/", views.CustomerDemographicsCreateView.as_view(), name="crm_CustomerDemographics_create"),
    path("crm/CustomerDemographics/detail/<int:pk>/", views.CustomerDemographicsDetailView.as_view(), name="crm_CustomerDemographics_detail"),
    path("crm/CustomerDemographics/update/<int:pk>/", views.CustomerDemographicsUpdateView.as_view(), name="crm_CustomerDemographics_update"),
    path("crm/CustomerDemographics/delete/<int:pk>/", views.CustomerDemographicsDeleteView.as_view(), name="crm_CustomerDemographics_delete"),
    path("crm/Customers/", views.CustomersListView.as_view(), name="crm_Customers_list"),
    path("crm/Customers/create/", views.CustomersCreateView.as_view(), name="crm_Customers_create"),
    path("crm/Customers/detail/<int:pk>/", views.CustomersDetailView.as_view(), name="crm_Customers_detail"),
    path("crm/Customers/update/<int:pk>/", views.CustomersUpdateView.as_view(), name="crm_Customers_update"),
    path("crm/Customers/delete/<int:pk>/", views.CustomersDeleteView.as_view(), name="crm_Customers_delete"),
    path("crm/EmployeeTerritories/", views.EmployeeTerritoriesListView.as_view(), name="crm_EmployeeTerritories_list"),
    path("crm/EmployeeTerritories/create/", views.EmployeeTerritoriesCreateView.as_view(), name="crm_EmployeeTerritories_create"),
    path("crm/EmployeeTerritories/detail/<int:pk>/", views.EmployeeTerritoriesDetailView.as_view(), name="crm_EmployeeTerritories_detail"),
    path("crm/EmployeeTerritories/update/<int:pk>/", views.EmployeeTerritoriesUpdateView.as_view(), name="crm_EmployeeTerritories_update"),
    path("crm/EmployeeTerritories/delete/<int:pk>/", views.EmployeeTerritoriesDeleteView.as_view(), name="crm_EmployeeTerritories_delete"),
    path("crm/Employees/", views.EmployeesListView.as_view(), name="crm_Employees_list"),
    path("crm/Employees/create/", views.EmployeesCreateView.as_view(), name="crm_Employees_create"),
    path("crm/Employees/detail/<int:pk>/", views.EmployeesDetailView.as_view(), name="crm_Employees_detail"),
    path("crm/Employees/update/<int:pk>/", views.EmployeesUpdateView.as_view(), name="crm_Employees_update"),
    path("crm/Employees/delete/<int:pk>/", views.EmployeesDeleteView.as_view(), name="crm_Employees_delete"),
    path("crm/GeographyColumns/", views.GeographyColumnsListView.as_view(), name="crm_GeographyColumns_list"),
    path("crm/GeographyColumns/create/", views.GeographyColumnsCreateView.as_view(), name="crm_GeographyColumns_create"),
    path("crm/GeographyColumns/detail/<int:pk>/", views.GeographyColumnsDetailView.as_view(), name="crm_GeographyColumns_detail"),
    path("crm/GeographyColumns/update/<int:pk>/", views.GeographyColumnsUpdateView.as_view(), name="crm_GeographyColumns_update"),
    path("crm/GeographyColumns/delete/<int:pk>/", views.GeographyColumnsDeleteView.as_view(), name="crm_GeographyColumns_delete"),
    path("crm/GeometryColumns/", views.GeometryColumnsListView.as_view(), name="crm_GeometryColumns_list"),
    path("crm/GeometryColumns/create/", views.GeometryColumnsCreateView.as_view(), name="crm_GeometryColumns_create"),
    path("crm/GeometryColumns/detail/<int:pk>/", views.GeometryColumnsDetailView.as_view(), name="crm_GeometryColumns_detail"),
    path("crm/GeometryColumns/update/<int:pk>/", views.GeometryColumnsUpdateView.as_view(), name="crm_GeometryColumns_update"),
    path("crm/GeometryColumns/delete/<int:pk>/", views.GeometryColumnsDeleteView.as_view(), name="crm_GeometryColumns_delete"),
    path("crm/OrderDetails/", views.OrderDetailsListView.as_view(), name="crm_OrderDetails_list"),
    path("crm/OrderDetails/create/", views.OrderDetailsCreateView.as_view(), name="crm_OrderDetails_create"),
    path("crm/OrderDetails/detail/<int:pk>/", views.OrderDetailsDetailView.as_view(), name="crm_OrderDetails_detail"),
    path("crm/OrderDetails/update/<int:pk>/", views.OrderDetailsUpdateView.as_view(), name="crm_OrderDetails_update"),
    path("crm/OrderDetails/delete/<int:pk>/", views.OrderDetailsDeleteView.as_view(), name="crm_OrderDetails_delete"),
    path("crm/Orders/", views.OrdersListView.as_view(), name="crm_Orders_list"),
    path("crm/Orders/create/", views.OrdersCreateView.as_view(), name="crm_Orders_create"),
    path("crm/Orders/detail/<int:pk>/", views.OrdersDetailView.as_view(), name="crm_Orders_detail"),
    path("crm/Orders/update/<int:pk>/", views.OrdersUpdateView.as_view(), name="crm_Orders_update"),
    path("crm/Orders/delete/<int:pk>/", views.OrdersDeleteView.as_view(), name="crm_Orders_delete"),
    path("crm/Products/", views.ProductsListView.as_view(), name="crm_Products_list"),
    path("crm/Products/create/", views.ProductsCreateView.as_view(), name="crm_Products_create"),
    path("crm/Products/detail/<int:pk>/", views.ProductsDetailView.as_view(), name="crm_Products_detail"),
    path("crm/Products/update/<int:pk>/", views.ProductsUpdateView.as_view(), name="crm_Products_update"),
    path("crm/Products/delete/<int:pk>/", views.ProductsDeleteView.as_view(), name="crm_Products_delete"),
    path("crm/Region/", views.RegionListView.as_view(), name="crm_Region_list"),
    path("crm/Region/create/", views.RegionCreateView.as_view(), name="crm_Region_create"),
    path("crm/Region/detail/<int:pk>/", views.RegionDetailView.as_view(), name="crm_Region_detail"),
    path("crm/Region/update/<int:pk>/", views.RegionUpdateView.as_view(), name="crm_Region_update"),
    path("crm/Region/delete/<int:pk>/", views.RegionDeleteView.as_view(), name="crm_Region_delete"),
    path("crm/Shippers/", views.ShippersListView.as_view(), name="crm_Shippers_list"),
    path("crm/Shippers/create/", views.ShippersCreateView.as_view(), name="crm_Shippers_create"),
    path("crm/Shippers/detail/<int:pk>/", views.ShippersDetailView.as_view(), name="crm_Shippers_detail"),
    path("crm/Shippers/update/<int:pk>/", views.ShippersUpdateView.as_view(), name="crm_Shippers_update"),
    path("crm/Shippers/delete/<int:pk>/", views.ShippersDeleteView.as_view(), name="crm_Shippers_delete"),
    path("crm/SpatialRefSys/", views.SpatialRefSysListView.as_view(), name="crm_SpatialRefSys_list"),
    path("crm/SpatialRefSys/create/", views.SpatialRefSysCreateView.as_view(), name="crm_SpatialRefSys_create"),
    path("crm/SpatialRefSys/detail/<int:pk>/", views.SpatialRefSysDetailView.as_view(), name="crm_SpatialRefSys_detail"),
    path("crm/SpatialRefSys/update/<int:pk>/", views.SpatialRefSysUpdateView.as_view(), name="crm_SpatialRefSys_update"),
    path("crm/SpatialRefSys/delete/<int:pk>/", views.SpatialRefSysDeleteView.as_view(), name="crm_SpatialRefSys_delete"),
    path("crm/Suppliers/", views.SuppliersListView.as_view(), name="crm_Suppliers_list"),
    path("crm/Suppliers/create/", views.SuppliersCreateView.as_view(), name="crm_Suppliers_create"),
    path("crm/Suppliers/detail/<int:pk>/", views.SuppliersDetailView.as_view(), name="crm_Suppliers_detail"),
    path("crm/Suppliers/update/<int:pk>/", views.SuppliersUpdateView.as_view(), name="crm_Suppliers_update"),
    path("crm/Suppliers/delete/<int:pk>/", views.SuppliersDeleteView.as_view(), name="crm_Suppliers_delete"),
    path("crm/Territories/", views.TerritoriesListView.as_view(), name="crm_Territories_list"),
    path("crm/Territories/create/", views.TerritoriesCreateView.as_view(), name="crm_Territories_create"),
    path("crm/Territories/detail/<int:pk>/", views.TerritoriesDetailView.as_view(), name="crm_Territories_detail"),
    path("crm/Territories/update/<int:pk>/", views.TerritoriesUpdateView.as_view(), name="crm_Territories_update"),
    path("crm/Territories/delete/<int:pk>/", views.TerritoriesDeleteView.as_view(), name="crm_Territories_delete"),
    path("crm/UsStates/", views.UsStatesListView.as_view(), name="crm_UsStates_list"),
    path("crm/UsStates/create/", views.UsStatesCreateView.as_view(), name="crm_UsStates_create"),
    path("crm/UsStates/detail/<int:pk>/", views.UsStatesDetailView.as_view(), name="crm_UsStates_detail"),
    path("crm/UsStates/update/<int:pk>/", views.UsStatesUpdateView.as_view(), name="crm_UsStates_update"),
    path("crm/UsStates/delete/<int:pk>/", views.UsStatesDeleteView.as_view(), name="crm_UsStates_delete"),
)
