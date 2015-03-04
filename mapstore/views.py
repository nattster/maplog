from django.shortcuts import render
from django.http import HttpResponse
from models import Location

# Create your views here.
def index(request):
    l = Location.objects.all()
    return render(request, 'index.html', {
        'locations': l
    })

def add(request):
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    title = request.GET.get('title', '')
    color = request.GET.get('color', 'FF0000')
    if lat and lng:
        l = Location()
        l.latitude = lat
        l.longitude = lng
        l.title = title
        l.color = color
        l.save()
        return HttpResponse('Successfully saved')
    else:
        return HttpResponse('Invalid input, missing lat and lng',
                status=400)
