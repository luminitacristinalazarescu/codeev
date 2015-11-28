from projects import views
from django.conf.urls import url
from projects.views import ProjectListView


urlpatterns = [

    url(r'^$', ProjectListView.as_view(), name='list_projects'),
    url(r'^upload/$', views.get_project),
]
