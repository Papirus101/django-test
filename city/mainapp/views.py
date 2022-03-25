from django.shortcuts import render
from django.db.models import Count

from .models import City, People


def index(request):
    peoples = People.objects.all()
    top_citys = City.objects.annotate(count=Count('peoples__id')).order_by('-count')[:10]
    all_citys = City.objects.all()
    return render(request, 'mainapp/index.html', {'peoples': peoples, 
                                                   'objects': top_citys,
                                                   'all_city': all_citys})



def city(request, city_id):
    city_info = People.objects.filter(city__pk=city_id).select_related('city')
    return render(request, 'mainapp/detail.html', {'city_info': city_info})