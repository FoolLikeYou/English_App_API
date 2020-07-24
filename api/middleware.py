from django.http import HttpResponseForbidden
from django.http import HttpResponse

from django.conf import settings


def api_get_auth(get_response):
    def middleware(request):

        if ('secret' not in request.headers):
            return HttpResponse('Unauthorized', status=401)
        is_admin_page = (request.path.find("/admin/") >= 0)

        if (settings.API_SECRET != '' and (is_admin_page == False)):
                if (request.headers['secret'] != settings.API_SECRET):
                    return HttpResponseForbidden()

        response = get_response(request)
        return response

    def process_exception(request, exception):
        print(request.path)
        print(exception)
        return HttpResponseForbidden()

    middleware.process_exception = process_exception
    return middleware
