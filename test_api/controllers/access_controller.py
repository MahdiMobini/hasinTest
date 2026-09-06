from django.http import HttpRequest, HttpResponse

from test_api.services.access_service import AccessDecisionService


class AccessController:
    @staticmethod
    def handle_request(request: HttpRequest) -> HttpResponse:
        if not AccessDecisionService.can_access_for_request(request):
            return HttpResponse('Access Denied', status=403)

        return HttpResponse('Hello, world!')
