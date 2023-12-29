from django.contrib import admin
from django.urls import path
from simple_app.views import EmployeeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EmployeeListView.as_view(), name='home_page')
]
