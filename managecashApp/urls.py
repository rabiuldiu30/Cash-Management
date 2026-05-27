from django.urls import path
from .views import *

urlpatterns = [
    path('',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('register',registerPage,name='register'),
    path('addcash/',addCashPage,name='addcash'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('expense/',expensePage,name='expense'),
]
