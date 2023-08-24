from django.shortcuts import render
from .models import Thru,Pascucci,Starbucks, Twosomeplace, Burgerking
from . import models
from django.views.generic import ListView
from rest_framework.views import APIView
# Create your views here.
class ThruMain(ListView):
    model = Thru
    template_name = "thru/thru_main.html"
def ThruDetail_pascucci(request):
    pascucci = Pascucci.objects.all()  # 데이터베이스에서 모든 Pascucci 위치 정보 가져오기
    context = {'pascucci': pascucci}
    return render(request, "thru/pascucci_detail.html", context)
def ThruDetail_starbucks(request):
    starbucks = Starbucks.objects.all()
    context = {'starbucks' : starbucks}
    return render(request, "thru/starbucks_detail.html", context)

def ThruDetail_twosome(request):
    twosome = Twosomeplace.objects.all()
    context = {'twosome' : twosome}
    return render(request, "thru/twosome_detail.html", context)

def ThruDetail_burgerking(request):
    burgerk = Burgerking.objects.all()
    context = {'burgerk' : burgerk}
    return render(request, "thru/burgerking_detail.html", context)

def thru_main(request) :
    data_list = Burgerking.objects.all()
    return render(request, "thru/test.html",
                  {"data_list" : data_list})

class Main(APIView) :
    def get_db(self, request):
        return render(request, "thru/thru_detail.html",
                               context=dict(data_list=Pascucci.objects.all()))