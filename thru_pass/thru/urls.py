from django.urls import path
from . import views
urlpatterns = [

    path("", views.ThruMain.as_view()),
    path("detail/", views.detail, name="detail"),

]