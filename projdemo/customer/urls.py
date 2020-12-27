from django.urls import path
from customer.api.v1.customer_info_api import CustomerInfoDetailApi, CustomerInfoListApi
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('info/', CustomerInfoListApi.as_view()),
    path('info/<int:id>/', CustomerInfoDetailApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)