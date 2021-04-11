from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View

from apps.api.models import Server


class Home(TemplateView):
    template_name = 'index.html'


class ServerView(View):

    def get(self, request, name, *args, **kwargs):
        server = get_object_or_404(Server, name=name)

        context = {
            'server': server
        }

        return render(request, 'server.html', context=context)


def handler404(request, exception):
    return render(request, '404.html', status=404)