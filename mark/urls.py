from django.urls import path

from mark.views import MarkCountView

urlpatterns = [
    path('count/', MarkCountView.as_view(), name='mark_count'),
]