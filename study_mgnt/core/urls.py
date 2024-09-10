from django.urls import path
from .import views



urlpatterns=[
    path('',views.index,name=" "),
    path('index',views.index, name="index"),
    path('Add_Study',views.add_study,name="Add_Study"),
    path('Edit_Study/<str:id>',views.edit_study,name="Edit_Study"),
    path('View/<str:id>',views.View,name="view"),
    path('Delete_Study',views.Delete_Study,name="Delete_Study")
]