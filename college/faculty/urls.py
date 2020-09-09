from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='registerFaculty'),
	path('show/', views.show, name='showFaculty'),
	path('edit/<int:id>', views.edit, name='editFaculty'),
	path('delete/<int:id>', views.delete, name='deleteFaculty'),
	path('confirm/<int:id>', views.confirm, name='confirmFaculty')
]
