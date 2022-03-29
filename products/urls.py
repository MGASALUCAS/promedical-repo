from django.urls import path, include
from . import views

urlpatterns = [
    path('GetYourDoctor', views.GetYourDoctor, name='GetYourDoctor'),
    path('blog', views.blog, name='blog'),
    path('GoogleMap', views.GoogleMap, name='GoogleMap'),
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index4', views.index4, name='index4'),
    path('UserInfo', views.UserInfo, name='UserInfo'),
    path('LabTest', views.LabTest, name='LabTest'),
    path('detail', views.detail, name='detail'),
    path('<int:product_id>', views.blog, name='blog'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]
