import json

from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView

from sharing.api.serializers import ShareableFileListSerializer
from sharing.models import ShareableFile


class ShareableFileListView(ListAPIView):
    """
    get:
    File list of logged in user.

    post:
    Create new file.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileListSerializer


class ShareableFileDetailView(RetrieveAPIView):
    """
        get:
        Get file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileListSerializer


class LoginView(View):
    def post(self, request):
        logout(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username and password):
            return JsonResponse(data={
                'status': 'username and password parameters are required',
            }, status=400)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse(data={
                'status': 'ok',
            }, status=200)
        else:
            return JsonResponse(data={
                'status': 'wrong authentication data',
            }, status=403)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return JsonResponse({'status': 'ok'})


class ShareableFileView(View):
    def get(self, request, file_id):
        response_data = {
            'status': 'ok',
        }
        return_code = 200

        if request.user.is_anonymous():
            response_data.update({
                'status': 'not authorized',
            })
            return_code = 401
        else:
            try:
                obj = ShareableFile.objects.get(pk=file_id)
                if obj.user != request.user and not obj.public:
                    raise ShareableFile.DoesNotExist
            except ShareableFile.DoesNotExist:
                response_data.update({
                    'status': "file does not exist or you don't have access to it",
                })
                return_code = 404
            else:
                response_data['file'] = obj.as_json()
        return JsonResponse(data=response_data, status=return_code)

    def delete(self, request, file_id):
        response_data = {
            'status': 'ok',
        }
        return_code = 200

        if request.user.is_anonymous():
            response_data.update({
                'status': 'not authorized',
            })
            return_code = 401
        else:
            try:
                obj = ShareableFile.objects.get(pk=file_id)
                if obj.user != request.user:
                    raise ShareableFile.DoesNotExist
            except ShareableFile.DoesNotExist:
                response_data.update({
                    'status': "file does not exist or you don't have access to it",
                })
                return_code = 404
            else:
                obj.delete()
        return JsonResponse(data=response_data, status=return_code)


class ShareableFilesView(View):
    def get(self, request):
        if request.user.is_anonymous():
            return JsonResponse(data={
                'status': 'not authorized',
            }, status=401)
        files = ShareableFile.objects.filter(user=request.user)
        response_data = {}
        response_data['files'] = []
        for file in files:
            response_data['files'].append(file.as_json())
        response_data['status'] = 'ok'
        return JsonResponse(data=response_data)

    def post(self, request):
        if request.user.is_anonymous():
            return JsonResponse(data={
                'status': 'not authorized',
            }, status=401)
        if len(request.FILES.keys()) != 1:
            return JsonResponse(data={
                'status': 'you have to send 1 file',
            }, status=400)
        filename = request.FILES['file'].name
        public = bool(int(request.POST.get('public')))
        obj = ShareableFile(file=request.FILES['file'], name=filename, user=request.user, public=public)
        obj.save()
        response_json = {'status': 'ok'}
        response_json.update(obj.as_json())
        return JsonResponse(data=response_json)
