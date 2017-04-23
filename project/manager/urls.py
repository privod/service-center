from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.AtmListView.as_view(), name='atm-list'),
]