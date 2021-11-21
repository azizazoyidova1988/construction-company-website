from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('service/', views.service, name='service'),
    path('project/', views.project, name='project'),
    path('project/<int:project_id>/single/', views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

]