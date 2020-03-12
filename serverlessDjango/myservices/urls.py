from django.urls import path
from myservices.views import Home

urlpatterns=[
    path('/message',Home.as_view(),name='home'),
]