import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from crm import models as crm_models


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


def create_crm_Categories(**kwargs):
    defaults = {}
    defaults["category_id"] = ""
    defaults["category_name"] = ""
    defaults["description"] = ""
    defaults["picture"] = ""
    defaults.update(**kwargs)
    return crm_models.Categories.objects.create(**defaults)
def create_crm_CustomerCustomerDemo(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return crm_models.CustomerCustomerDemo.objects.create(**defaults)
def create_crm_CustomerDemographics(**kwargs):
    defaults = {}
    defaults["customer_type_id"] = ""
    defaults["customer_desc"] = ""
    defaults.update(**kwargs)
    return crm_models.CustomerDemographics.objects.create(**defaults)
def create_crm_Customers(**kwargs):
    defaults = {}
    defaults["customer_id"] = ""
    defaults["company_name"] = ""
    defaults["contact_name"] = ""
    defaults["contact_title"] = ""
    defaults["address"] = ""
    defaults["city"] = ""
    defaults["region"] = ""
    defaults["postal_code"] = ""
    defaults["country"] = ""
    defaults["phone"] = ""
    defaults["fax"] = ""
    defaults.update(**kwargs)
    return crm_models.Customers.objects.create(**defaults)
def create_crm_EmployeeTerritories(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return crm_models.EmployeeTerritories.objects.create(**defaults)
def create_crm_Employees(**kwargs):
    defaults = {}
    defaults["employee_id"] = ""
    defaults["last_name"] = ""
    defaults["first_name"] = ""
    defaults["title"] = ""
    defaults["title_of_courtesy"] = ""
    defaults["birth_date"] = datetime.now()
    defaults["hire_date"] = datetime.now()
    defaults["address"] = ""
    defaults["city"] = ""
    defaults["region"] = ""
    defaults["postal_code"] = ""
    defaults["country"] = ""
    defaults["home_phone"] = ""
    defaults["extension"] = ""
    defaults["photo"] = ""
    defaults["notes"] = ""
    defaults["photo_path"] = ""
    defaults.update(**kwargs)
    return crm_models.Employees.objects.create(**defaults)
def create_crm_GeographyColumns(**kwargs):
    defaults = {}
    defaults["coord_dimension"] = ""
    defaults["srid"] = ""
    defaults["type"] = ""
    defaults.update(**kwargs)
    return crm_models.GeographyColumns.objects.create(**defaults)
def create_crm_GeometryColumns(**kwargs):
    defaults = {}
    defaults["coord_dimension"] = ""
    defaults["srid"] = ""
    defaults["type"] = ""
    defaults.update(**kwargs)
    return crm_models.GeometryColumns.objects.create(**defaults)
def create_crm_OrderDetails(**kwargs):
    defaults = {}
    defaults["unit_price"] = ""
    defaults["quantity"] = ""
    defaults["discount"] = ""
    defaults.update(**kwargs)
    return crm_models.OrderDetails.objects.create(**defaults)
def create_crm_Orders(**kwargs):
    defaults = {}
    defaults["order_id"] = ""
    defaults["order_date"] = datetime.now()
    defaults["required_date"] = datetime.now()
    defaults["shipped_date"] = datetime.now()
    defaults["freight"] = ""
    defaults["ship_name"] = ""
    defaults["ship_address"] = ""
    defaults["ship_city"] = ""
    defaults["ship_region"] = ""
    defaults["ship_postal_code"] = ""
    defaults["ship_country"] = ""
    defaults.update(**kwargs)
    return crm_models.Orders.objects.create(**defaults)
def create_crm_Products(**kwargs):
    defaults = {}
    defaults["product_id"] = ""
    defaults["product_name"] = ""
    defaults["quantity_per_unit"] = ""
    defaults["unit_price"] = ""
    defaults["units_in_stock"] = ""
    defaults["units_on_order"] = ""
    defaults["reorder_level"] = ""
    defaults["discontinued"] = ""
    defaults.update(**kwargs)
    return crm_models.Products.objects.create(**defaults)
def create_crm_Region(**kwargs):
    defaults = {}
    defaults["region_id"] = ""
    defaults["region_description"] = ""
    defaults.update(**kwargs)
    return crm_models.Region.objects.create(**defaults)
def create_crm_Shippers(**kwargs):
    defaults = {}
    defaults["shipper_id"] = ""
    defaults["company_name"] = ""
    defaults["phone"] = ""
    defaults.update(**kwargs)
    return crm_models.Shippers.objects.create(**defaults)
def create_crm_SpatialRefSys(**kwargs):
    defaults = {}
    defaults["srid"] = ""
    defaults["auth_name"] = ""
    defaults["auth_srid"] = ""
    defaults["srtext"] = ""
    defaults["proj4text"] = ""
    defaults.update(**kwargs)
    return crm_models.SpatialRefSys.objects.create(**defaults)
def create_crm_Suppliers(**kwargs):
    defaults = {}
    defaults["supplier_id"] = ""
    defaults["company_name"] = ""
    defaults["contact_name"] = ""
    defaults["contact_title"] = ""
    defaults["address"] = ""
    defaults["city"] = ""
    defaults["region"] = ""
    defaults["postal_code"] = ""
    defaults["country"] = ""
    defaults["phone"] = ""
    defaults["fax"] = ""
    defaults["homepage"] = ""
    defaults.update(**kwargs)
    return crm_models.Suppliers.objects.create(**defaults)
def create_crm_Territories(**kwargs):
    defaults = {}
    defaults["territory_id"] = ""
    defaults["territory_description"] = ""
    defaults.update(**kwargs)
    return crm_models.Territories.objects.create(**defaults)
def create_crm_UsStates(**kwargs):
    defaults = {}
    defaults["state_id"] = ""
    defaults["state_name"] = ""
    defaults["state_abbr"] = ""
    defaults["state_region"] = ""
    defaults.update(**kwargs)
    return crm_models.UsStates.objects.create(**defaults)
