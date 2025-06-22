from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from .forms import MurojaatForm
# Create your views here.


DEFAULT_ABOUT = {
    "title": "O'zbekistonda eng katta IT jamiyat",
    "text": "Digital Generation Uzbekistan NNM ning asosiy vazifasi yoshlarni bilim va ilmga chorlash, axborot, texnologiyalari soxasida ayollarni o'rnini ko'paytirish, yoshlarni mamlakatda amalga oshirilayotgan axborot kommunikatsiya islohotlarini chuqurlashtirishda faol ishtirok etishga jalb qilish.",
    "tizer": "https://www.youtube.com/watch?v=GkD7frg0nLk"
}

DEFAULT_MAP = {
    'embeded': "https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d1059.2053788673786!2d69.21860131180253!3d41.33310910350248!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sru!2s!4v1706543496574!5m2!1sru!2s"
}

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['about'] = list(About.objects.all() or [DEFAULT_ABOUT])[0]
        context['news'] = list(News.objects.order_by('-date'))[:4]
        context['future'] = list(Plans.objects.order_by('-data'))[:4]
        context['team'] = list(TeamMember.objects.all())

        gallary = Gallary.objects.all()

        context['gallary_row_1'] = gallary[0:3]
        context['gallary_row_2'] = gallary[3:6]
        context['latest_gallary'] = Gallary.objects.all().order_by('-id')[:3]
        context['partners'] = Partner.objects.all()
        context['map'] = Map.objects.first() or DEFAULT_MAP
        return context


class ListNews(ListView):
    paginate_by = 16
    template_name = 'list-news.html'
    model = News


class ListGallary(ListView):
    paginate_by = 16
    template_name = 'list-gallary.html'
    model = Gallary
    def get_queryset(self):
        return Gallary.objects.all().order_by('-id')
class NewsView(DetailView):
    template_name = 'new.html'
    model = News


class GallaryView(DetailView):
    template_name = 'gallary.html'
    model = Gallary
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_gallary'] = Gallary.objects.all().order_by('-id')[:3]
        return context

def accept_murojaat(request):
    if request.method == "POST":
        form = MurojaatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('/')
