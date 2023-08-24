from django.shortcuts import render
from .models import Thru, Pascucci,Starbucks, Twosomeplace, Burgerking, Hollys, Ediya, Kfc, Lotteria, Mcdonalds,Angelinus
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


def ThruDetail_angel(request):
    angel = Angelinus.objects.all()
    context = {'angel' : angel}
    return render(request, "thru/angelinus_detail.html", context)

def ThruDetail_ediya(request):
    ediya = Ediya.objects.all()
    context = {'ediya' : ediya}
    return render(request, "thru/ediya_detail.html", context)


def ThruDetail_hollys(request):
    hollys = Hollys.objects.all()
    context = {'hollys' : hollys}
    return render(request, "thru/hollys_detail.html", context)


def ThruDetail_kfc(request):
    kfc = Kfc.objects.all()
    context = {'kfc' : kfc}
    return render(request, "thru/kfc_detail.html", context)

def ThruDetail_mcdo(request):
    mcdo = Mcdonalds.objects.all()
    context = {'mcdo' : mcdo}
    return render(request, "thru/mcdonalds_detail.html", context)

def ThruDetail_lotte(request):
    lotte = Lotteria.objects.all()
    context = {'lotte' : lotte}
    return render(request, "thru/lotteria_detail.html", context)





