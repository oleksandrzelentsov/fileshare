from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.views import View

from sharing.models import ShareableFile


class LoginView(View):
    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username and password):
            return JsonResponse(data={
                'status': 'username and password parameters are required',
                'return_code': 400
            })
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse(data={
                'status': 'ok',
                'return_code': 200,
            })
        else:
            return JsonResponse(data={
                'status': 'wrong authentication data',
                'return_code': 403,
            })


class ShareableFileView(View):
    def get(self, request, file_id):
        response_data = {
            'status': 'ok',
            'return_code': 200,
        }

        if self.request.user.is_anonymous():
            response_data.update({
                'status': 'not authorized',
                'return_code': 401,
            })
        else:
            try:
                obj = ShareableFile.objects.get(pk=file_id)
                if obj.user != self.request.user:
                    raise ShareableFile.DoesNotExist
            except ShareableFile.DoesNotExist:
                response_data.update({
                    'status': "file does not exist or you don't have access to it",
                    'return_code': 404,
                })
            else:
                response_data['image'] = {
                    'id': obj.id,
                    'name': obj.name,
                    'url': obj.get_raw_url()
                }
                response_data['return_code'] = 200
        return JsonResponse(data=response_data)
