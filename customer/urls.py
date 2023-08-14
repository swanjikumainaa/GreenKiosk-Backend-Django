from django.urls import path
from .views import register_user,users_list,user_detail,edit_user_view


urlpatterns =[
path ("users/registration",register_user,name = "user_registration_view"),
path ("users/list",users_list,name = "users_list_view"),
path ("users/<int:id>/",user_detail,name = "user_detail_view"),
path ("user/edit/<int:id>/",edit_user_view,name="user_edit_view"),

]
