from django.urls import path
from .views import upload_review


urlpatterns =[
    path ("reviews/upload",upload_review,name = "review_upload_view"),
]
