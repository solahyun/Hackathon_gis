from django.conf.urls import url
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
        if request.POST.get("input_text"):
            image = "{% static 'img/1.png' %}"

            return render(request, context={'text': image})
    else:
        return render(request, context={'text': ""})