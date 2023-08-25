from django.urls import path
from . import views

app_name = 'management'
urlpatterns =[
    path('',views.homepage, name="homepage"),
     path('/add',views.addpage, name="add"),
]