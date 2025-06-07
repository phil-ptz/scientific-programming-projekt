from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('intro/', views.introduction, name='introduction'),
    path('training/', views.training, name='training'),
    path('classify/', views.classify, name='classify'),
    path('klassifizieren/<int:bild_id>/', views.classify_existing_image, name='klassifizieren_bild'),
    path('database/', views.database, name='database'),
]