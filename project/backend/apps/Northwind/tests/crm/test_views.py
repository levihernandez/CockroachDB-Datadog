import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Categories_list_view():
    instance1 = test_helpers.create_crm_Categories()
    instance2 = test_helpers.create_crm_Categories()
    client = Client()
    url = reverse("crm_Categories_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Categories_create_view():
    client = Client()
    url = reverse("crm_Categories_create")
    data = {
        "category_id": 1,
        "category_name": "text",
        "description": "text",
        "picture": b'bytes',
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Categories_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Categories()
    url = reverse("crm_Categories_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Categories_update_view():
    client = Client()
    instance = test_helpers.create_crm_Categories()
    url = reverse("crm_Categories_update", args=[instance.pk, ])
    data = {
        "category_id": 1,
        "category_name": "text",
        "description": "text",
        "picture": b'bytes',
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomerCustomerDemo_list_view():
    instance1 = test_helpers.create_crm_CustomerCustomerDemo()
    instance2 = test_helpers.create_crm_CustomerCustomerDemo()
    client = Client()
    url = reverse("crm_CustomerCustomerDemo_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CustomerCustomerDemo_create_view():
    client = Client()
    url = reverse("crm_CustomerCustomerDemo_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomerCustomerDemo_detail_view():
    client = Client()
    instance = test_helpers.create_crm_CustomerCustomerDemo()
    url = reverse("crm_CustomerCustomerDemo_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CustomerCustomerDemo_update_view():
    client = Client()
    instance = test_helpers.create_crm_CustomerCustomerDemo()
    url = reverse("crm_CustomerCustomerDemo_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomerDemographics_list_view():
    instance1 = test_helpers.create_crm_CustomerDemographics()
    instance2 = test_helpers.create_crm_CustomerDemographics()
    client = Client()
    url = reverse("crm_CustomerDemographics_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_CustomerDemographics_create_view():
    client = Client()
    url = reverse("crm_CustomerDemographics_create")
    data = {
        "customer_type_id": "text",
        "customer_desc": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_CustomerDemographics_detail_view():
    client = Client()
    instance = test_helpers.create_crm_CustomerDemographics()
    url = reverse("crm_CustomerDemographics_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_CustomerDemographics_update_view():
    client = Client()
    instance = test_helpers.create_crm_CustomerDemographics()
    url = reverse("crm_CustomerDemographics_update", args=[instance.pk, ])
    data = {
        "customer_type_id": "text",
        "customer_desc": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Customers_list_view():
    instance1 = test_helpers.create_crm_Customers()
    instance2 = test_helpers.create_crm_Customers()
    client = Client()
    url = reverse("crm_Customers_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Customers_create_view():
    client = Client()
    url = reverse("crm_Customers_create")
    data = {
        "customer_id": "text",
        "company_name": "text",
        "contact_name": "text",
        "contact_title": "text",
        "address": "text",
        "city": "text",
        "region": "text",
        "postal_code": "text",
        "country": "text",
        "phone": "text",
        "fax": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Customers_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Customers()
    url = reverse("crm_Customers_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Customers_update_view():
    client = Client()
    instance = test_helpers.create_crm_Customers()
    url = reverse("crm_Customers_update", args=[instance.pk, ])
    data = {
        "customer_id": "text",
        "company_name": "text",
        "contact_name": "text",
        "contact_title": "text",
        "address": "text",
        "city": "text",
        "region": "text",
        "postal_code": "text",
        "country": "text",
        "phone": "text",
        "fax": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_EmployeeTerritories_list_view():
    instance1 = test_helpers.create_crm_EmployeeTerritories()
    instance2 = test_helpers.create_crm_EmployeeTerritories()
    client = Client()
    url = reverse("crm_EmployeeTerritories_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_EmployeeTerritories_create_view():
    client = Client()
    url = reverse("crm_EmployeeTerritories_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_EmployeeTerritories_detail_view():
    client = Client()
    instance = test_helpers.create_crm_EmployeeTerritories()
    url = reverse("crm_EmployeeTerritories_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_EmployeeTerritories_update_view():
    client = Client()
    instance = test_helpers.create_crm_EmployeeTerritories()
    url = reverse("crm_EmployeeTerritories_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Employees_list_view():
    instance1 = test_helpers.create_crm_Employees()
    instance2 = test_helpers.create_crm_Employees()
    client = Client()
    url = reverse("crm_Employees_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Employees_create_view():
    client = Client()
    url = reverse("crm_Employees_create")
    data = {
        "employee_id": 1,
        "last_name": "text",
        "first_name": "text",
        "title": "text",
        "title_of_courtesy": "text",
        "birth_date": datetime.now(),
        "hire_date": datetime.now(),
        "address": "text",
        "city": "text",
        "region": "text",
        "postal_code": "text",
        "country": "text",
        "home_phone": "text",
        "extension": "text",
        "photo": b'bytes',
        "notes": "text",
        "photo_path": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Employees_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Employees()
    url = reverse("crm_Employees_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Employees_update_view():
    client = Client()
    instance = test_helpers.create_crm_Employees()
    url = reverse("crm_Employees_update", args=[instance.pk, ])
    data = {
        "employee_id": 1,
        "last_name": "text",
        "first_name": "text",
        "title": "text",
        "title_of_courtesy": "text",
        "birth_date": datetime.now(),
        "hire_date": datetime.now(),
        "address": "text",
        "city": "text",
        "region": "text",
        "postal_code": "text",
        "country": "text",
        "home_phone": "text",
        "extension": "text",
        "photo": b'bytes',
        "notes": "text",
        "photo_path": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_GeographyColumns_list_view():
    instance1 = test_helpers.create_crm_GeographyColumns()
    instance2 = test_helpers.create_crm_GeographyColumns()
    client = Client()
    url = reverse("crm_GeographyColumns_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_GeographyColumns_create_view():
    client = Client()
    url = reverse("crm_GeographyColumns_create")
    data = {
        "coord_dimension": 1,
        "srid": 1,
        "type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_GeographyColumns_detail_view():
    client = Client()
    instance = test_helpers.create_crm_GeographyColumns()
    url = reverse("crm_GeographyColumns_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_GeographyColumns_update_view():
    client = Client()
    instance = test_helpers.create_crm_GeographyColumns()
    url = reverse("crm_GeographyColumns_update", args=[instance.pk, ])
    data = {
        "coord_dimension": 1,
        "srid": 1,
        "type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_GeometryColumns_list_view():
    instance1 = test_helpers.create_crm_GeometryColumns()
    instance2 = test_helpers.create_crm_GeometryColumns()
    client = Client()
    url = reverse("crm_GeometryColumns_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_GeometryColumns_create_view():
    client = Client()
    url = reverse("crm_GeometryColumns_create")
    data = {
        "coord_dimension": 1,
        "srid": 1,
        "type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_GeometryColumns_detail_view():
    client = Client()
    instance = test_helpers.create_crm_GeometryColumns()
    url = reverse("crm_GeometryColumns_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_GeometryColumns_update_view():
    client = Client()
    instance = test_helpers.create_crm_GeometryColumns()
    url = reverse("crm_GeometryColumns_update", args=[instance.pk, ])
    data = {
        "coord_dimension": 1,
        "srid": 1,
        "type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderDetails_list_view():
    instance1 = test_helpers.create_crm_OrderDetails()
    instance2 = test_helpers.create_crm_OrderDetails()
    client = Client()
    url = reverse("crm_OrderDetails_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_OrderDetails_create_view():
    client = Client()
    url = reverse("crm_OrderDetails_create")
    data = {
        "unit_price": 1.0f,
        "quantity": 1,
        "discount": 1.0f,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_OrderDetails_detail_view():
    client = Client()
    instance = test_helpers.create_crm_OrderDetails()
    url = reverse("crm_OrderDetails_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_OrderDetails_update_view():
    client = Client()
    instance = test_helpers.create_crm_OrderDetails()
    url = reverse("crm_OrderDetails_update", args=[instance.pk, ])
    data = {
        "unit_price": 1.0f,
        "quantity": 1,
        "discount": 1.0f,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Orders_list_view():
    instance1 = test_helpers.create_crm_Orders()
    instance2 = test_helpers.create_crm_Orders()
    client = Client()
    url = reverse("crm_Orders_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Orders_create_view():
    client = Client()
    url = reverse("crm_Orders_create")
    data = {
        "order_id": 1,
        "order_date": datetime.now(),
        "required_date": datetime.now(),
        "shipped_date": datetime.now(),
        "freight": 1.0f,
        "ship_name": "text",
        "ship_address": "text",
        "ship_city": "text",
        "ship_region": "text",
        "ship_postal_code": "text",
        "ship_country": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Orders_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Orders()
    url = reverse("crm_Orders_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Orders_update_view():
    client = Client()
    instance = test_helpers.create_crm_Orders()
    url = reverse("crm_Orders_update", args=[instance.pk, ])
    data = {
        "order_id": 1,
        "order_date": datetime.now(),
        "required_date": datetime.now(),
        "shipped_date": datetime.now(),
        "freight": 1.0f,
        "ship_name": "text",
        "ship_address": "text",
        "ship_city": "text",
        "ship_region": "text",
        "ship_postal_code": "text",
        "ship_country": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Products_list_view():
    instance1 = test_helpers.create_crm_Products()
    instance2 = test_helpers.create_crm_Products()
    client = Client()
    url = reverse("crm_Products_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Products_create_view():
    client = Client()
    url = reverse("crm_Products_create")
    data = {
        "product_id": 1,
        "product_name": "text",
        "quantity_per_unit": "text",
        "unit_price": 1.0f,
        "units_in_stock": 1,
        "units_on_order": 1,
        "reorder_level": 1,
        "discontinued": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Products_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Products()
    url = reverse("crm_Products_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Products_update_view():
    client = Client()
    instance = test_helpers.create_crm_Products()
    url = reverse("crm_Products_update", args=[instance.pk, ])
    data = {
        "product_id": 1,
        "product_name": "text",
        "quantity_per_unit": "text",
        "unit_price": 1.0f,
        "units_in_stock": 1,
        "units_on_order": 1,
        "reorder_level": 1,
        "discontinued": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Region_list_view():
    instance1 = test_helpers.create_crm_Region()
    instance2 = test_helpers.create_crm_Region()
    client = Client()
    url = reverse("crm_Region_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Region_create_view():
    client = Client()
    url = reverse("crm_Region_create")
    data = {
        "region_id": 1,
        "region_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Region_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Region()
    url = reverse("crm_Region_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Region_update_view():
    client = Client()
    instance = test_helpers.create_crm_Region()
    url = reverse("crm_Region_update", args=[instance.pk, ])
    data = {
        "region_id": 1,
        "region_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Shippers_list_view():
    instance1 = test_helpers.create_crm_Shippers()
    instance2 = test_helpers.create_crm_Shippers()
    client = Client()
    url = reverse("crm_Shippers_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Shippers_create_view():
    client = Client()
    url = reverse("crm_Shippers_create")
    data = {
        "shipper_id": 1,
        "company_name": "text",
        "phone": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Shippers_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Shippers()
    url = reverse("crm_Shippers_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Shippers_update_view():
    client = Client()
    instance = test_helpers.create_crm_Shippers()
    url = reverse("crm_Shippers_update", args=[instance.pk, ])
    data = {
        "shipper_id": 1,
        "company_name": "text",
        "phone": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SpatialRefSys_list_view():
    instance1 = test_helpers.create_crm_SpatialRefSys()
    instance2 = test_helpers.create_crm_SpatialRefSys()
    client = Client()
    url = reverse("crm_SpatialRefSys_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_SpatialRefSys_create_view():
    client = Client()
    url = reverse("crm_SpatialRefSys_create")
    data = {
        "srid": 1,
        "auth_name": "text",
        "auth_srid": 1,
        "srtext": "text",
        "proj4text": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_SpatialRefSys_detail_view():
    client = Client()
    instance = test_helpers.create_crm_SpatialRefSys()
    url = reverse("crm_SpatialRefSys_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_SpatialRefSys_update_view():
    client = Client()
    instance = test_helpers.create_crm_SpatialRefSys()
    url = reverse("crm_SpatialRefSys_update", args=[instance.pk, ])
    data = {
        "srid": 1,
        "auth_name": "text",
        "auth_srid": 1,
        "srtext": "text",
        "proj4text": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Suppliers_list_view():
    instance1 = test_helpers.create_crm_Suppliers()
    instance2 = test_helpers.create_crm_Suppliers()
    client = Client()
    url = reverse("crm_Suppliers_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Suppliers_create_view():
    client = Client()
    url = reverse("crm_Suppliers_create")
    data = {
        "supplier_id": 1,
        "company_name": "text",
        "contact_name": "text",
        "contact_title": "text",
        "address": "text",
        "city": "text",
        "region": "text",
        "postal_code": "text",
        "country": "text",
        "phone": "text",
        "fax": "text",
        "homepage": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Suppliers_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Suppliers()
    url = reverse("crm_Suppliers_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Suppliers_update_view():
    client = Client()
    instance = test_helpers.create_crm_Suppliers()
    url = reverse("crm_Suppliers_update", args=[instance.pk, ])
    data = {
        "supplier_id": 1,
        "company_name": "text",
        "contact_name": "text",
        "contact_title": "text",
        "address": "text",
        "city": "text",
        "region": "text",
        "postal_code": "text",
        "country": "text",
        "phone": "text",
        "fax": "text",
        "homepage": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Territories_list_view():
    instance1 = test_helpers.create_crm_Territories()
    instance2 = test_helpers.create_crm_Territories()
    client = Client()
    url = reverse("crm_Territories_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Territories_create_view():
    client = Client()
    url = reverse("crm_Territories_create")
    data = {
        "territory_id": "text",
        "territory_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Territories_detail_view():
    client = Client()
    instance = test_helpers.create_crm_Territories()
    url = reverse("crm_Territories_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Territories_update_view():
    client = Client()
    instance = test_helpers.create_crm_Territories()
    url = reverse("crm_Territories_update", args=[instance.pk, ])
    data = {
        "territory_id": "text",
        "territory_description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_UsStates_list_view():
    instance1 = test_helpers.create_crm_UsStates()
    instance2 = test_helpers.create_crm_UsStates()
    client = Client()
    url = reverse("crm_UsStates_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_UsStates_create_view():
    client = Client()
    url = reverse("crm_UsStates_create")
    data = {
        "state_id": 1,
        "state_name": "text",
        "state_abbr": "text",
        "state_region": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_UsStates_detail_view():
    client = Client()
    instance = test_helpers.create_crm_UsStates()
    url = reverse("crm_UsStates_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_UsStates_update_view():
    client = Client()
    instance = test_helpers.create_crm_UsStates()
    url = reverse("crm_UsStates_update", args=[instance.pk, ])
    data = {
        "state_id": 1,
        "state_name": "text",
        "state_abbr": "text",
        "state_region": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
