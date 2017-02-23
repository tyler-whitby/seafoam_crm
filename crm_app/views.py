from django.http import HttpResponse
from django.views.generic.base import TemplateView

class mainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(mainView, self).get_context_data(**kwargs)

        return context

