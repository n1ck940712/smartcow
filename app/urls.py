from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('annotate/<int:img_id>/', views.annotate, name='annotate'),
    path('save_annotation', views.save_annotation, name='save_annotation'),
    path('myannotated', views.myannotated, name='myannotated'),
    path('checkannotate/<int:img_id>/', views.checkannotate, name='checkannotate'),
    path('download_csv', views.download_csv, name='download_csv'),
    
    # signin signout
    path('signin', views.signin, name='signin'),
    path('signinfirst', views.signinfirst, name='signinfirst'),
    path('signout', views.signout, name='signout'),
    path('register', views.register, name='register'),


]
