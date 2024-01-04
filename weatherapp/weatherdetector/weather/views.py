from django.shortcuts import render
import json
import urllib.request 
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=f5568dcc450b8b44c12ee52edb977dc2').read()
        json_data=json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }
    else:
        data={}
    return render(request,'index.html',{'data':data,'city':city})

# Create your views here.
