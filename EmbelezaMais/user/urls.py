from django.conf.urls import url
from .views import (
    register_client_view,
    register_company_view,
    register_confirm,
    CompanyAction,
    LoginCompanyView,
    LogoutCompanyView,
)

urlpatterns = (
    url(r'^login_company/', LoginCompanyView.as_view(), name='login_view'),
    url(r'^logout_company/', LogoutCompanyView.as_view(), name='logout_view'),
    url(r'^register_client/', register_client_view, name='register_client_view'),
    url(r'^register_company/', register_company_view, name='register_view'),
    url(r'^confirm/(?P<activation_key>\w+)/', register_confirm, name='confirm_account'),
    url(r'^profile/(?P<email>[\w|\W]+)/', CompanyAction.company_profile, name='profile'),
    url(r'^edit/(?P<email>[\w|\W]+)/', CompanyAction.company_edit_profile_view, name='edit')
)
