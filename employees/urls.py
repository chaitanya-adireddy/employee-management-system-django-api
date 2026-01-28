from django.urls import path
from . views import employee_detail,add_employee,update_employee,delete_employee
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<int:pk>/',employee_detail,name="employee_detail"),
    path('add/',add_employee, name='add_employee'),
    path('<int:id>/update/', update_employee, name='update_employee'),
    path('<int:id>/delete/', delete_employee, name='delete_employee'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]