from django.views.generic import TemplateView, ListView

from trendapp.models import NewModel


class BasicTemplateView(TemplateView):
    template_name = 'trendapp/base.html'


class TrendListView(ListView):
    template_name = 'trendapp/bukgu.html'
    model = NewModel