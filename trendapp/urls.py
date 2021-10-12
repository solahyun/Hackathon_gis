from django.urls import path

from trendapp.views import BasicTemplateView, TrendListView, let_write

app_name = 'trendapp'

urlpatterns = [
    path('info/', BasicTemplateView.as_view(), name='info'),
    path('list/', TrendListView.as_view(), name='list'),
    path('let_write/', let_write, name='let_write'),
]