from django.urls import path

from .views import TransactionalFunctionList, TransactionalFunctionCreate

urlpatterns = [
    path('', TransactionalFunctionList.as_view(), name='ft_list'),
    path('new/', TransactionalFunctionCreate.as_view(), name='ft_new')
]