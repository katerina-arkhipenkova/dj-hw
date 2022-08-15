from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        rows = csv.DictReader(f)
        station_list = list(rows)

    paginator = Paginator(station_list, 10)
    page = paginator.get_page(page_number)
    context = {
        # 'bus_stations': station_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
