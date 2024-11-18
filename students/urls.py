from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('student_detail/', views.student_detail, name='student_detail'),

    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/create/', views.MyModelCreatView.as_view(), name='mymodel_create'),
]
