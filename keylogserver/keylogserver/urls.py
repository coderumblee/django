from django.urls import path
from logs.views import LogListView  # Make sure you have a view called LogListView

urlpatterns = [
    path('api/logs/', LogListView.as_view(), name='log-list'),
    # Other URL patterns
]
