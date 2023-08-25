from django.shortcuts import render
from .models import Thru, Pascucci,Starbucks, Twosomeplace, Burgerking, Hollys, Ediya, Kfc, Lotteria, Mcdonalds,Angelinus
from django.views.generic import ListView
from django.core.paginator import Paginator

class ThruMain(ListView):
    model = Thru
    template_name = "thru/thru_main.html"

class PostSearch(ListView):
    # PostSearch에서는 검색된 결과를 한페이지에 보여주기 위하여 None으로 설정
    pagenate_by = None

def detail(request):

    mcs = Mcdonalds.objects.all()
    mcs = [mcdonalds.mc_json() for mcdonalds in mcs]

    tws = Twosomeplace.objects.all()
    tws = [twosome.to_json() for twosome in tws]

    sts = Starbucks.objects.all()
    sts = [starbucks.st_json() for starbucks in sts]

    pas = Pascucci.objects.all()
    pas = [pascucci.pa_json() for pascucci in pas]

    los = Lotteria.objects.all()
    los = [lotteria.lo_json() for lotteria in los]

    kfs = Kfc.objects.all()
    kfs = [kfc.kf_json() for kfc in kfs]

    hos = Hollys.objects.all()
    hos = [hollys.ho_json() for hollys in hos]

    eds = Ediya.objects.all()
    eds = [ediya.ed_json() for ediya in eds]

    ans = Angelinus.objects.all()
    ans = [angelinus.an_json() for angelinus in ans]

    bus = Burgerking.objects.all()
    bus = [burgerking.bu_json() for burgerking in bus]


    shopselect = request.GET.get('test')

    if shopselect == "mcs":
        shopselect = mcs

    if shopselect == "los":
        shopselect = los

    if shopselect == "bus":
        shopselect = bus

    if shopselect == "kfs":
        shopselect = kfs

    if shopselect == "tws":
        shopselect = tws

    if shopselect == "sts":
        shopselect = sts

    if shopselect == "pas":
        shopselect = pas

    if shopselect == "hos":
        shopselect = hos

    if shopselect == "eds":
        shopselect = eds

    if shopselect == "ans":
        shopselect = ans


    return render(request, "thru/detail.html", {"mcs": mcs, "tws": tws, "sts": sts, "pas": pas,
                                            "los": los, "kfs": kfs, "hos": hos, "eds": eds,
                                            "ans": ans, "bus": bus, "shopselect":page_obj})


