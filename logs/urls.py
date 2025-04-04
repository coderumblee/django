from django.urls import path
from .views import LogListView

urlpatterns = [
    path('api/logs/', LogListView.as_view(), name='log-list'),
]
