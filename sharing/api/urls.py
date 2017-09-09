from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from sharing.api.views import LoginView, LogoutView, ShareableFileListView, ShareableFileDetailView, \
    ShareableFileUpdateView, ShareableFileDeleteView, ShareableFileCreateView

urlpatterns = [
    url(r'^files/$', ShareableFileListView.as_view(), name='files-list'),
    url(r'^files/create/$', ShareableFileCreateView.as_view(), name='file-create'),
    url(r'^files/(?P<pk>\d+)/$', ShareableFileDetailView.as_view(), name='file-retrieve'),
    url(r'^files/(?P<pk>\d+)/update/$', ShareableFileUpdateView.as_view(), name='file-update'),
    url(r'^files/(?P<pk>\d+)/delete/$', ShareableFileDeleteView.as_view(), name='file-delete'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='login'),
]