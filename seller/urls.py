from django.urls import path
from .views import register_vendor,vendors_list,vendor_detail,edit_vendor_view

urlpatterns =[
    path ("vendors/registration",register_vendor,name = "vendor_registration_view"),
    path ("vendors/list",vendors_list,name = "vendors_list_view"),
    path ("vendors/<int:id>/",vendor_detail,name = "vendor_detail_view"),
    path ("vendor/edit/<int:id>/",edit_vendor_view,name="vendor_edit_view"),

]
