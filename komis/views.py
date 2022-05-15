from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from komis.models import Samochod
from django.core.paginator import Paginator
import csv
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


def search(request, **kwargs):
    if request.method == 'POST':
        return redirect('oferty', marka=request.POST['marka'],
                        price_min=request.POST['price_min'],
                        price_max=request.POST['price_max'])

    if kwargs['marka'] == 'all':
        samochod_list = Samochod.objects.filter(cena__gte=kwargs['price_min'],
                                                cena__lte=kwargs['price_max'])
    else:
        samochod_list = Samochod.objects.filter(cena__gte=kwargs['price_min'],
                                                cena__lte=kwargs['price_max'],
                                                marka__icontains=kwargs['marka'])
    paginator = Paginator(samochod_list, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'page_obj': page_obj})


def offer_img(request):
    return HttpResponse(request, content_type='../media/{{samochod.image}}')


class SamochodCreateView(CreateView):
    model = Samochod
    fields = ('marka', 'model', 'przebieg', 'rok_produkcji', 'moc', 'pojemnosc', 'cena', 'paliwo', 'image')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['marka', 'model', 'przebieg', 'rok_produkcji', 'moc', 'pojemnosc', 'cena', 'paliwo'])

    for samochod in Samochod.objects.all().values_list('marka', 'model', 'przebieg', 'rok_produkcji', 'moc',
                                                       'pojemnosc', 'cena', 'paliwo'):
        writer.writerow(samochod)

    response['Content-Disposition'] = 'attachment; filename="samochod.csv"'

    return response
