from django.conf.urls import url
from . import views  

urlpatterns = [
  url(r'^$', views.home),
  url(r'^menu$', views.menu),
  url(r'^breakfast$', views.breakfast_menu),
  url(r'^lunch$', views.lunch_menu),
  url(r'^dinner$', views.dinner_menu),
  url(r'^dessert$', views.dessert_menu),
  url(r'^reservations$', views.reservations),
  url(r'^process_reservation$', views.process_reservation),
  url(r'^process_inquery$', views.process_inquery),
  url(r'^process_feedback$', views.process_feedback),
  url(r'^about$', views.team),
  url(r'^contact$', views.contact),
  url(r'^coffee$', views.coffee),
  url(r'^drinks$', views.drinks)

]