from django.urls import path
from . import views
urlpatterns = [
    # path("", views.index),
    path("", views.ThruMain.as_view()),
    path("pascucci/", views.ThruDetail_pascucci),
    path("starbucks/", views.ThruDetail_starbucks),
]