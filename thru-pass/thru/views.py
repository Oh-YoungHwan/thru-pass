from django.shortcuts import render
from .models import Thru,Pascucci,Starbucks
from . import models
from django.views.generic import ListView
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