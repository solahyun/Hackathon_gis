from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from trendapp.models import NewModel


class BasicTemplateView(TemplateView):
    template_name = 'trendapp/base.html'


class TrendListView(ListView):
    template_name = 'trendapp/bukgu.html'
    model = NewModel


def let_write(request):
    if request.method == "POST":
        if request.POST.get(""):

            return render(request, 'trendapp/bukgu.html')
    else:
        return render(request, 'trendapp/bukgu.html')