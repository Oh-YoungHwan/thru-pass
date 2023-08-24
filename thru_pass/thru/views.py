from django.shortcuts import render
from .models import Thru, Pascucci,Starbucks, Twosomeplace, Burgerking, Hollys, Ediya, Kfc, Lotteria, Mcdonalds,Angelinus
from . import models
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
class ThruMain(ListView):
    model = Thru
    template_name = "thru/thru_main.html"


def ThruDetail_pascucci(request):
    pascucci = Pascucci.objects.all()  # 데이터베이스에서 모든 Pascucci 위치 정보 가져오기
    paginator = Paginator(pascucci, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/pascucci_detail.html", {'pascucci' : page_obj})
def ThruDetail_starbucks(request):
    starbucks = Starbucks.objects.all()
    paginator = Paginator(starbucks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/starbucks_detail.html", {'starbucks' : page_obj})


def ThruDetail_twosome(request):
    twosome = Twosomeplace.objects.all()
    paginator = Paginator(twosome, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/twosome_detail.html", {'twosome' : page_obj})

def ThruDetail_burgerking(request):
    burgerk = Burgerking.objects.all()
    paginator = Paginator(burgerk, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/burgerk_detail.html", {'burgerk' : page_obj})


def ThruDetail_angel(request):
    angel = Angelinus.objects.all()
    paginator = Paginator(angel, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/angelinus_detail.html", {'angel' : page_obj})

def ThruDetail_ediya(request):
    ediya = Ediya.objects.all()
    paginator = Paginator(ediya, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/ediya_detail.html", {'ediya' : page_obj})


def ThruDetail_hollys(request):
    hollys = Hollys.objects.all()
    paginator = Paginator(hollys, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/hollys_detail.html", {'hollys' : page_obj})


def ThruDetail_kfc(request):
    kfc = Kfc.objects.all()
    paginator = Paginator(kfc, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/kfc_detail.html", {'kfc' : page_obj})

def ThruDetail_mcdo(request):
    mcdo = Mcdonalds.objects.all()
    paginator = Paginator(mcdo, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/mcdonalds_detail.html", {'mcdo' : page_obj})

def ThruDetail_lotte(request):
    lotte = Lotteria.objects.all()
    paginator = Paginator(lotte, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "thru/lotteria_detail.html", {'lotte' : page_obj})



