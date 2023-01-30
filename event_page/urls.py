from django.urls import path
from .views import event_list, event_detail ,info 
urlpatterns = [
    path('', event_list, name='event_list'),
    path('<int:pk>/', event_detail, name='event_detail'),
    path('info',info, name='info'),

]