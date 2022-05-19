from . import views
from django.urls import path


urlpatterns=[
            path('create',views.create,name='create'),
            path('<int:complain_id>', views.detail, name='detail'),
            path('m<int:complain_id>', views.mdetail, name='mdetail'),
            path('clist', views.clist, name='clist'),
            path('mhome', views.mhome, name='mhome'),

]