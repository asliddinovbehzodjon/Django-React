from django.urls import path
from .views import *
urlpatterns = [
    path('allmenu',AllMenu.as_view()),
    path('all',AllMahsulot.as_view())
]
