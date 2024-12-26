from django.urls import path
from app import views

urlpatterns = [
      path('',views.index, name='index'),
      path('contact',views.contact, name='contact'),
      path('about',views.about, name='about'),
      path('checkout/',views.Checkout, name='Checkout'),
      path('handlerequest/', views.handlerequest, name='HandleRequest'),
      # path('',views., name='')


]