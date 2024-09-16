from django.urls import path
from .import views
#from .views import home, add_employee, update_employee, delete_employee

urlpatterns = [
    path('', views.login_view, name='login_first'),
    path('home', views.home, name='home'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:pk>/', views.update_employee, name='update_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path("login/", views.login_view, name = "login_view"),
    path('logout/', views.logout_view, name='logout_view'),
    path('password/', views.change_password, name='change_password'),

]