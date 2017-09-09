from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from sharing.api.views import LoginView, LogoutView, ShareableFileListView, ShareableFileDetailView

urlpatterns = [
    # url(r'^files/$', ShareableFilesView.as_view(), name='files'),
    url(r'^files/$', ShareableFileListView.as_view(), name='files'),
    # url(r'^files/(?P<file_id>\d+)/$', ShareableFileView.as_view(), name='file'),
    url(r'^files/(?P<pk>\d+)/$', ShareableFileDetailView.as_view(), name='file'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='login'),
]