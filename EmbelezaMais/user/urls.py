from django.conf.urls import url
from .views import (
    register_client_view,
    register_company_view,
    register_confirm,
    remove_client_view,
    show_client_view,
    CompanyAction,
    LoginCompanyView,
    LogoutView,
    LoginClientView,
)

urlpatterns = (
    url(r'^login_company/', LoginCompanyView.as_view(), name='login_view'),
    url(r'^login_client/', LoginClientView.as_view(), name='login_client'),
    url(r'^logout_company/', LogoutView.as_view(), name='logout_view'),
    url(r'^register_client/', register_client_view,
        name='register_client_view'),
    url(r'^register_company/', register_company_view, name='register_view'),
    url(r'^confirm/(?P<activation_key>\w+)/', register_confirm, name='confirm_account'),
    url(r'^profile/(?P<email>[\w|\W]+)/', CompanyAction.company_profile, name='profile'),
    url(r'^edit/(?P<email>[\w|\W]+)/', CompanyAction.company_edit_profile_view, name='edit'),
    url(r'view_client/', show_client_view, name="show_client_view"),
    url(r'remove_client/', remove_client_view, name="remove_client_view"),

)
