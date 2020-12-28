### Hi there, I'm Anish - 👋

## Python developer !!

<br />

# AMC (Django application)
> coordinate generator.

This web app converts Excel file containing one or more addresses and on submit, returns an updated Excel file with the addresses along with latitude and longitude for each address

![](header.png)

## Installation

Pandas:

```sh
pip install pandas
```

geopy:

```sh
pip install geopy
```

## Usage
1. created address as new app
```
$ python manage.py startapp address
```

2. Used geopy library for generating coordinated of given address

#geopy:

```sh
pip install geopy
```


```   

3. Used pandas library for reading and analysis of address from uploaded excel-sheet 
4. generating end result of excel-sheet using pandas libraries
5. created a model with field 'file' to save uploaded file in given path('media/uploaded_files')
6. created three function to handle uploading , downloading files as requested in statement (ref:views.py)
```
## Views.py

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
```
Sample Files used:
Book3.xlsx for sample upload (path:address/static/Book3.xlsx)