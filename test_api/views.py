
from django.views import View

from test_api.controllers.access_controller import AccessController


class AccessCheckView(View):
    def get(self, request):
        return AccessController.handle_request(request)