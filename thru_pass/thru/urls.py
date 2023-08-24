from django.urls import path
from . import views
urlpatterns = [
    # path("", views.index),
    path("", views.ThruMain.as_view()),
    path("pascucci/", views.ThruDetail_pascucci),
    path("starbucks/", views.ThruDetail_starbucks),
    path("twosome/", views.ThruDetail_twosome),
    path("ediya/", views.ThruDetail_ediya),
    path("hollys/", views.ThruDetail_hollys),
    path("angel/", views.ThruDetail_angel),
    path("burgerking/", views.ThruDetail_burgerking),
    path("lotteria/", views.ThruDetail_lotte),
    path("kfc/", views.ThruDetail_kfc),
    path("mcdo/", views.ThruDetail_mcdo),





]