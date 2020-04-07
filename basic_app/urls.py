from django.conf.urls import url
from basic_app import views

urlpatterns = [
    url(r'^schools/$', views.SchoolListView.as_view(), name='list'),
    url(r'^$',
        views.IndexView.as_view(template_name='index.html'),
        name='index'),
    url(r'^schools/(?P<pk>\d+)/$',
        views.SchoolDetailView.as_view(),
        name='detail'),
    url(r'^schools/create/$', views.SchoolCreateView.as_view(), name="create"),
    url(r'^schools/update/(?P<pk>\d+)/$',
        views.SchoolUpdateView.as_view(),
        name="update"),
    url(r'^schools/delete/(?P<pk>\d+)/$',
        views.SchoolDeleteView.as_view(),
        name="delete"),
]
