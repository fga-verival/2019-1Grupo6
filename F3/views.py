from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import TransactionalFunction

class TransactionalFunctionCreate(CreateView):
    model = TransactionalFunction
    fields = ['name', 'f_type', 'qt_ALR', 'qt_DER', 'function_points', 'counter_name', 'complexity']
    success_url = reverse_lazy('admin/')


class TransactionalFunctionList(ListView):
    model = TransactionalFunction
