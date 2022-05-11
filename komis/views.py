from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from komis.models import Samochod
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def search(request):
    samochod_list = Samochod.objects.all()
    paginator = Paginator(samochod_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html',  {'page_obj': page_obj})


def offer_img(request):
    return HttpResponse(request, content_type="../media/{{samochod.image}}")


class SamochodCreateView(CreateView):
    model = Samochod
    fields = ('marka', 'model', 'przebieg', 'rok_produkcji', 'moc', 'pojemnosc', 'cena', 'paliwo', 'image')
