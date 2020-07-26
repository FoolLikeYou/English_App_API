from django.http import HttpResponseForbidden
from django.http import HttpResponse

from django.conf import settings


def api_get_auth(get_response):
    def middleware(request):

        is_admin_page = ((request.path.find("/admin/") >= 0) or (request.path.find("/static/") >= 0) or (request.path.find("/media/") >= 0))

        if (('secret' not in request.headers) and not is_admin_page):
            return HttpResponse('Unauthorized!', status=401)

        if (settings.API_SECRET != '' and not is_admin_page):
                if (request.headers['secret'] != settings.API_SECRET):
                    return HttpResponseForbidden()

        response = get_response(request)
        return response

    def process_exception(request, exception):
        print(request.path)
        print(exception)
        return HttpResponse(exception, status=500)

    middleware.process_exception = process_exception
    return middleware
