from django.shortcuts import render
from oauth2_provider.views import AuthorizationView


class CustomLoginUrlAuthorizationView(AuthorizationView):
    login_url = '/users/login/'  # TODO put it in the settings
