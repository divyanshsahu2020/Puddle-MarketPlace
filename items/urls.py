from django.urls import path
from . import views
app_name='apps'
urlpatterns=[
    path("<int:pk>/",views.detail,name='detail'),
    path('new/',views.new,name='new'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('',views.items,name='items'),
]