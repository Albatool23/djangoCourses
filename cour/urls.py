
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addCourses',views.create),
    path('disply/<_id>',views.disply),
    path('delete/<_id>',views.delete,name='delete cour' )
]

