from django.urls import path
from .views import Note_List_view, Note_detail_view, Note_create_view, Note_edit_view, Note_delete_view

urlpatterns = [
    path('', Note_List_view.as_view(), name='list_view'),
    path('detail/<int:pk>/', Note_detail_view.as_view(), name='detail_view'),
    path('create/', Note_create_view.as_view(), name='create_view'),
    path('edit/<int:pk>',Note_edit_view.as_view(), name='edit_view'),
    path('delete/<int:pk>', Note_delete_view.as_view(), name='delete_view'),
]