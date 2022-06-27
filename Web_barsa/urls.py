"""Web_barsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from barsa_app import views
#from django.conf.urls import url
from django.views.generic import TemplateView

#from barsa_app.views import EmployeeViewSet
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()

#router.register('employee', EmployeeViewSet, basename='employee')

#urlpatterns = router.urls
'''добавить + перед ='''
urlpatterns = [
    path('', views.get_game_calendar, name='home'),
    path('employee/', views.get_employee, name='employee'),
    path('footballer/', views.get_footballers, name='footballer'),
    re_path(r'^teams/$', views.TeamsListView.as_view(), name='teams'),
    re_path(r'^teams/(?P<pk>\d+)$', views.TeamsDetailView.as_view(), name='teams-detail'),
    re_path(r'^coach/$', views.CoachListViev.as_view(), name='coach'),
    re_path(r'^coach/(?P<pk>\d+)$', views.CoachDetailView.as_view(), name='coach-detail'),
    re_path(r'^contract/$', views.ContractListView.as_view(), name='contract'),
    re_path(r'^contract/(?P<pk>\d+)$', views.ContractDetailView.as_view(), name='contract-detail'),

    #url(r'^team/$', views.TeamsListView.as_view(), name='team'),
    #path('create/', views.create_employee),
    #path('update_employee/<int:id>/', views.update_employee),
    #path('delete_employee/<int:id>/', views.delete_employee),
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^myticket/$', views.TicketsByUserListView.as_view(), name='ticket'),
]
