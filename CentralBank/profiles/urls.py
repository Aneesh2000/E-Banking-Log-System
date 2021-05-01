from django.conf.urls import url
from . import views

app_name = "profiles"

urlpatterns = [
    url(r"^account_status/$", views.index, name = "account_status"),
    url(r"^money_transfer/", views.money_transfer, name = "money_transfer"),
    url(r"edit_details/", views.edit_details, name = "edit_details")

]
