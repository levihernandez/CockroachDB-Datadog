from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CategoriesListView(generic.ListView):
    model = models.Categories
    form_class = forms.CategoriesForm


class CategoriesCreateView(generic.CreateView):
    model = models.Categories
    form_class = forms.CategoriesForm


class CategoriesDetailView(generic.DetailView):
    model = models.Categories
    form_class = forms.CategoriesForm


class CategoriesUpdateView(generic.UpdateView):
    model = models.Categories
    form_class = forms.CategoriesForm
    pk_url_kwarg = "pk"


class CategoriesDeleteView(generic.DeleteView):
    model = models.Categories
    success_url = reverse_lazy("crm_Categories_list")


class CustomerCustomerDemoListView(generic.ListView):
    model = models.CustomerCustomerDemo
    form_class = forms.CustomerCustomerDemoForm


class CustomerCustomerDemoCreateView(generic.CreateView):
    model = models.CustomerCustomerDemo
    form_class = forms.CustomerCustomerDemoForm


class CustomerCustomerDemoDetailView(generic.DetailView):
    model = models.CustomerCustomerDemo
    form_class = forms.CustomerCustomerDemoForm


class CustomerCustomerDemoUpdateView(generic.UpdateView):
    model = models.CustomerCustomerDemo
    form_class = forms.CustomerCustomerDemoForm
    pk_url_kwarg = "pk"


class CustomerCustomerDemoDeleteView(generic.DeleteView):
    model = models.CustomerCustomerDemo
    success_url = reverse_lazy("crm_CustomerCustomerDemo_list")


class CustomerDemographicsListView(generic.ListView):
    model = models.CustomerDemographics
    form_class = forms.CustomerDemographicsForm


class CustomerDemographicsCreateView(generic.CreateView):
    model = models.CustomerDemographics
    form_class = forms.CustomerDemographicsForm


class CustomerDemographicsDetailView(generic.DetailView):
    model = models.CustomerDemographics
    form_class = forms.CustomerDemographicsForm


class CustomerDemographicsUpdateView(generic.UpdateView):
    model = models.CustomerDemographics
    form_class = forms.CustomerDemographicsForm
    pk_url_kwarg = "pk"


class CustomerDemographicsDeleteView(generic.DeleteView):
    model = models.CustomerDemographics
    success_url = reverse_lazy("crm_CustomerDemographics_list")


class CustomersListView(generic.ListView):
    model = models.Customers
    form_class = forms.CustomersForm


class CustomersCreateView(generic.CreateView):
    model = models.Customers
    form_class = forms.CustomersForm


class CustomersDetailView(generic.DetailView):
    model = models.Customers
    form_class = forms.CustomersForm


class CustomersUpdateView(generic.UpdateView):
    model = models.Customers
    form_class = forms.CustomersForm
    pk_url_kwarg = "pk"


class CustomersDeleteView(generic.DeleteView):
    model = models.Customers
    success_url = reverse_lazy("crm_Customers_list")


class EmployeeTerritoriesListView(generic.ListView):
    model = models.EmployeeTerritories
    form_class = forms.EmployeeTerritoriesForm


class EmployeeTerritoriesCreateView(generic.CreateView):
    model = models.EmployeeTerritories
    form_class = forms.EmployeeTerritoriesForm


class EmployeeTerritoriesDetailView(generic.DetailView):
    model = models.EmployeeTerritories
    form_class = forms.EmployeeTerritoriesForm


class EmployeeTerritoriesUpdateView(generic.UpdateView):
    model = models.EmployeeTerritories
    form_class = forms.EmployeeTerritoriesForm
    pk_url_kwarg = "pk"


class EmployeeTerritoriesDeleteView(generic.DeleteView):
    model = models.EmployeeTerritories
    success_url = reverse_lazy("crm_EmployeeTerritories_list")


class EmployeesListView(generic.ListView):
    model = models.Employees
    form_class = forms.EmployeesForm


class EmployeesCreateView(generic.CreateView):
    model = models.Employees
    form_class = forms.EmployeesForm


class EmployeesDetailView(generic.DetailView):
    model = models.Employees
    form_class = forms.EmployeesForm


class EmployeesUpdateView(generic.UpdateView):
    model = models.Employees
    form_class = forms.EmployeesForm
    pk_url_kwarg = "pk"


class EmployeesDeleteView(generic.DeleteView):
    model = models.Employees
    success_url = reverse_lazy("crm_Employees_list")


class GeographyColumnsListView(generic.ListView):
    model = models.GeographyColumns
    form_class = forms.GeographyColumnsForm


class GeographyColumnsCreateView(generic.CreateView):
    model = models.GeographyColumns
    form_class = forms.GeographyColumnsForm


class GeographyColumnsDetailView(generic.DetailView):
    model = models.GeographyColumns
    form_class = forms.GeographyColumnsForm


class GeographyColumnsUpdateView(generic.UpdateView):
    model = models.GeographyColumns
    form_class = forms.GeographyColumnsForm
    pk_url_kwarg = "pk"


class GeographyColumnsDeleteView(generic.DeleteView):
    model = models.GeographyColumns
    success_url = reverse_lazy("crm_GeographyColumns_list")


class GeometryColumnsListView(generic.ListView):
    model = models.GeometryColumns
    form_class = forms.GeometryColumnsForm


class GeometryColumnsCreateView(generic.CreateView):
    model = models.GeometryColumns
    form_class = forms.GeometryColumnsForm


class GeometryColumnsDetailView(generic.DetailView):
    model = models.GeometryColumns
    form_class = forms.GeometryColumnsForm


class GeometryColumnsUpdateView(generic.UpdateView):
    model = models.GeometryColumns
    form_class = forms.GeometryColumnsForm
    pk_url_kwarg = "pk"


class GeometryColumnsDeleteView(generic.DeleteView):
    model = models.GeometryColumns
    success_url = reverse_lazy("crm_GeometryColumns_list")


class OrderDetailsListView(generic.ListView):
    model = models.OrderDetails
    form_class = forms.OrderDetailsForm


class OrderDetailsCreateView(generic.CreateView):
    model = models.OrderDetails
    form_class = forms.OrderDetailsForm


class OrderDetailsDetailView(generic.DetailView):
    model = models.OrderDetails
    form_class = forms.OrderDetailsForm


class OrderDetailsUpdateView(generic.UpdateView):
    model = models.OrderDetails
    form_class = forms.OrderDetailsForm
    pk_url_kwarg = "pk"


class OrderDetailsDeleteView(generic.DeleteView):
    model = models.OrderDetails
    success_url = reverse_lazy("crm_OrderDetails_list")


class OrdersListView(generic.ListView):
    model = models.Orders
    form_class = forms.OrdersForm


class OrdersCreateView(generic.CreateView):
    model = models.Orders
    form_class = forms.OrdersForm


class OrdersDetailView(generic.DetailView):
    model = models.Orders
    form_class = forms.OrdersForm


class OrdersUpdateView(generic.UpdateView):
    model = models.Orders
    form_class = forms.OrdersForm
    pk_url_kwarg = "pk"


class OrdersDeleteView(generic.DeleteView):
    model = models.Orders
    success_url = reverse_lazy("crm_Orders_list")


class ProductsListView(generic.ListView):
    model = models.Products
    form_class = forms.ProductsForm


class ProductsCreateView(generic.CreateView):
    model = models.Products
    form_class = forms.ProductsForm


class ProductsDetailView(generic.DetailView):
    model = models.Products
    form_class = forms.ProductsForm


class ProductsUpdateView(generic.UpdateView):
    model = models.Products
    form_class = forms.ProductsForm
    pk_url_kwarg = "pk"


class ProductsDeleteView(generic.DeleteView):
    model = models.Products
    success_url = reverse_lazy("crm_Products_list")


class RegionListView(generic.ListView):
    model = models.Region
    form_class = forms.RegionForm


class RegionCreateView(generic.CreateView):
    model = models.Region
    form_class = forms.RegionForm


class RegionDetailView(generic.DetailView):
    model = models.Region
    form_class = forms.RegionForm


class RegionUpdateView(generic.UpdateView):
    model = models.Region
    form_class = forms.RegionForm
    pk_url_kwarg = "pk"


class RegionDeleteView(generic.DeleteView):
    model = models.Region
    success_url = reverse_lazy("crm_Region_list")


class ShippersListView(generic.ListView):
    model = models.Shippers
    form_class = forms.ShippersForm


class ShippersCreateView(generic.CreateView):
    model = models.Shippers
    form_class = forms.ShippersForm


class ShippersDetailView(generic.DetailView):
    model = models.Shippers
    form_class = forms.ShippersForm


class ShippersUpdateView(generic.UpdateView):
    model = models.Shippers
    form_class = forms.ShippersForm
    pk_url_kwarg = "pk"


class ShippersDeleteView(generic.DeleteView):
    model = models.Shippers
    success_url = reverse_lazy("crm_Shippers_list")


class SpatialRefSysListView(generic.ListView):
    model = models.SpatialRefSys
    form_class = forms.SpatialRefSysForm


class SpatialRefSysCreateView(generic.CreateView):
    model = models.SpatialRefSys
    form_class = forms.SpatialRefSysForm


class SpatialRefSysDetailView(generic.DetailView):
    model = models.SpatialRefSys
    form_class = forms.SpatialRefSysForm


class SpatialRefSysUpdateView(generic.UpdateView):
    model = models.SpatialRefSys
    form_class = forms.SpatialRefSysForm
    pk_url_kwarg = "pk"


class SpatialRefSysDeleteView(generic.DeleteView):
    model = models.SpatialRefSys
    success_url = reverse_lazy("crm_SpatialRefSys_list")


class SuppliersListView(generic.ListView):
    model = models.Suppliers
    form_class = forms.SuppliersForm


class SuppliersCreateView(generic.CreateView):
    model = models.Suppliers
    form_class = forms.SuppliersForm


class SuppliersDetailView(generic.DetailView):
    model = models.Suppliers
    form_class = forms.SuppliersForm


class SuppliersUpdateView(generic.UpdateView):
    model = models.Suppliers
    form_class = forms.SuppliersForm
    pk_url_kwarg = "pk"


class SuppliersDeleteView(generic.DeleteView):
    model = models.Suppliers
    success_url = reverse_lazy("crm_Suppliers_list")


class TerritoriesListView(generic.ListView):
    model = models.Territories
    form_class = forms.TerritoriesForm


class TerritoriesCreateView(generic.CreateView):
    model = models.Territories
    form_class = forms.TerritoriesForm


class TerritoriesDetailView(generic.DetailView):
    model = models.Territories
    form_class = forms.TerritoriesForm


class TerritoriesUpdateView(generic.UpdateView):
    model = models.Territories
    form_class = forms.TerritoriesForm
    pk_url_kwarg = "pk"


class TerritoriesDeleteView(generic.DeleteView):
    model = models.Territories
    success_url = reverse_lazy("crm_Territories_list")


class UsStatesListView(generic.ListView):
    model = models.UsStates
    form_class = forms.UsStatesForm


class UsStatesCreateView(generic.CreateView):
    model = models.UsStates
    form_class = forms.UsStatesForm


class UsStatesDetailView(generic.DetailView):
    model = models.UsStates
    form_class = forms.UsStatesForm


class UsStatesUpdateView(generic.UpdateView):
    model = models.UsStates
    form_class = forms.UsStatesForm
    pk_url_kwarg = "pk"


class UsStatesDeleteView(generic.DeleteView):
    model = models.UsStates
    success_url = reverse_lazy("crm_UsStates_list")
