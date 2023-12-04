from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    context={}
    api='be35cc5517d57c9f68c1cc0cd18a9d6d'
    city='kochi'


    if request.method=='POST':
        city=request.POST.get('city')




    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'
    response=requests.get(url)
    data=response.json()
  
    weather=data['weather'][0]['description']
    temp=data['main']['temp']
    temp_max=data['main']['temp_max']
    temp_min=data['main']['temp_min']
    feels=data['main']['feels_like']

    context['city']=city
    context['weather']=weather
    context['temp']=temp
    context['temp_max']=temp_max
    context['temp_min']=temp_min
    context['feels']=feels
    
    



    return render(request,'index.html',context)

