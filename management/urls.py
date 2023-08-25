from django.urls import path
from . import views

app_nam = 'management'
urlpatterns =[
    path('',views.homepage, name="homepage"),
]