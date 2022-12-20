from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.todofn,name='todofn'),

    path('delete/<int:tid>/',views.deletefn,name='deletefn'),
    path('edit/<int:pk>/',views.update ,name='update'),
   
   
]
