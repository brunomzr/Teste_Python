from django.urls import path

from .views import EmployeeView

app_name = "employee"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', EmployeeView.as_view()),
]
