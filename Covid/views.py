from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    data=True
    result=True
    globalSum=None

    try:
        while(data):
            try:
                result=requests.get('https://api.covid19api.com/summary')
                globalSum=result.json()['Global']
                data=False
            except:
                data=True
        return render(request,'index.html',{"globalSum":globalSum})
    except print(0):
        pass
