from django.urls import path
from .views import BlogLisView

urlpatterns=[
    path('',BlogLisView.as_view,name='main')
]