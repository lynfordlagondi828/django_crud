from django.urls import path
from .views import list_person, add_person, update_person, delete_person


urlpatterns = [

    path('', list_person, name='list_person'),
    path('new', add_person, name='add_person'),
    path('update/<int:id>/', update_person, name='update_person'),
    path('delete/<int:id>/', delete_person, name='delete_person'),


]