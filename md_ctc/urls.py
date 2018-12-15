from django.conf.urls import url
from md_ctc import views

urlpatterns = [
               url(r'^$',  views.index, name='index'),
               url(r'^profile/$', views.update_profile, name='profile'),
               url(r'^logout/$', views.Logout, name='logout'),
            ]
