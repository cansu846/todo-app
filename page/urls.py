from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hakkimizda/", views.about_us_view, name="about_us"),
    path("iletisim/", views.contact_us_view, name="contact_us"),
    path("vizyonumuz/", views.vision_view, name="vision"),
]
