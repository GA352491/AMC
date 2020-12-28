
from django.shortcuts import render, redirect
from .models import FileUpload
import pandas as pd
from functools import partial
import ssl
from geopy.geocoders import Nominatim
from django.http import FileResponse

ssl._create_default_https_context = ssl._create_unverified_context

geolocator = Nominatim(user_agent="amc", timeout=10)
geocode = partial(geolocator.geocode, min_delay_seconds=1)


# Create your views here.

def home(request):
    return render(request, 'home.html')


def upload(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']
        FileUpload.objects.all().delete()
        doc = FileUpload.objects.create(file=upload_file)

    return redirect('download')


def download(request):
    files = FileUpload.objects.values('file')
    df = pd.DataFrame()
    for data in files:
        a = data['file']
        df2 = pd.read_excel(str('media') + '/' + a)
        lat = []
        lon = []
        for data in df2['address']:
            location = geolocator.geocode(data)
            if location is None:
                lat.append('Need more information')
                lon.append('Need more information')
            else:
                lat.append(location.latitude)
                lon.append(location.longitude)
        df['address'] = df2['address']
        df['latitude'] = lat
        df['longitude'] = lon
        df.to_excel('media/download/download.xlsx')
    response = FileResponse(open('media/download/download.xlsx', 'rb'))

    return response
