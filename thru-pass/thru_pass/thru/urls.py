from django.urls import path
from . import views
urlpatterns = [
    # path("", views.index),
    path("", views.ThruMain.as_view()),
    path("pascucci/", views.ThruDetail_pascucci),
    path("starbucks/", views.ThruDetail_starbucks),
    path("twosome/", views.ThruDetail_twosome),
    path("burgerking/", views.ThruDetail_burgerking),
    path("test/",views.thru_main),

]