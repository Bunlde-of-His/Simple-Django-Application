from django.views.generic import ListView
from simple_app.models import Employee


class EmployeeListView(ListView):
    model = Employee
    template_name = 'home_page.html'
    context_object_name = 'employees'
