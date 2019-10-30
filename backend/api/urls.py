from django.urls import include, path, re_path
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)
from allauth.account.views import confirm_email

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    re_path(r'^rest-auth/registration/verify-email/(?P<key>\w+)/$',
            confirm_email,
            name="account_confirm_email"),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]
