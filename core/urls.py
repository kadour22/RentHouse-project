from django.urls import path
from . import views

urlpatterns = [
    path("create-account/" , views.CreatetenantView.as_view() , name="create-tenant"),
    path("tenant-list/" , views.ListTenantView.as_view() , name="list-tenant"),
    path("rent-house/" , views.RentHouseView.as_view() , name="rent-house"),
    path("create-depart/" , views.AddDepartmentView.as_view() , name="create-depart"),
    path("add-house/" , views.AddHouseView.as_view() , name="add-house"),
    path("houses-list/" , views.ListHouseView.as_view() , name="houses-list"),
    path("house/<int:house_id>/" , views.RetrieveHouseView.as_view() , name="house"),
]

