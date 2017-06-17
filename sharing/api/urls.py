from django.conf.urls import url

from sharing.api.views import ShareableFileView, LoginView

urlpatterns = [
    url(r'^file/(?P<file_id>\d+)/$', ShareableFileView.as_view(), name='file'),
    url(r'^login/$', LoginView.as_view(), name='login'),
]