
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

# Create your views here.
class LandingPageView(TemplateView):

    template_name='landing.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home_page')
        return super(LandingPageView, self).dispatch(request, *args, **kwargs)


class FeaturesPageView(TemplateView):
    template_name = 'features.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('dashboards:overview')
    #     return super(FeaturesPageView, self).dispatch(request, *args, **kwargs)

class NewsPageView(TemplateView):
    template_name = 'news.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return redirect('login')
    #     return super(NewsPageView, self).dispatch(request, *args, **kwargs)
