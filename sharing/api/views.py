import json

from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    CreateAPIView

from sharing.api.serializers import ShareableFileListSerializer, ShareableFileDetailSerializer, \
    ShareableFileCreateSerializer
from sharing.models import ShareableFile


class ShareableFileListView(ListAPIView):
    """
    get:
    File list of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileListSerializer


class ShareableFileDetailView(RetrieveAPIView):
    """
    Get file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileDetailSerializer


class ShareableFileUpdateView(RetrieveUpdateAPIView):
    """
    Update file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileDetailSerializer


class ShareableFileDeleteView(RetrieveDestroyAPIView):
    """
    Delete file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileDetailSerializer


class ShareableFileCreateView(CreateAPIView):
    """
    Delete file of logged in user.
    """
    queryset = ShareableFile.objects.all()
    serializer_class = ShareableFileCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
