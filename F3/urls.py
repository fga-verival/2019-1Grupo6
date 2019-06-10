from django.urls import path

from .views import TransactionalFunctionList, TransactionalFunctionCreate, TransactionalFunctionUpdate

urlpatterns = [
    path('', TransactionalFunctionList.as_view(), name='ft_list'),
    path('new/', TransactionalFunctionCreate.as_view(), name='ft_new'),
    path('edit/<int:pk>', TransactionalFunctionUpdate.as_view(), name='ft_update')
]