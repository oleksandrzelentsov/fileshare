from django.conf.urls import url

from sharing.api.views import ShareableFileView, LoginView, LogoutView, ShareableFilesView

urlpatterns = [
    url(r'^files/$', ShareableFilesView.as_view(), name='files'),
    url(r'^files/(?P<file_id>\d+)/$', ShareableFileView.as_view(), name='file'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='login'),
]