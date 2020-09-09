from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('show/', views.show, name='show'),
	path('edit/<int:id>', views.edit, name='edit'),
	path('delete/<int:id>', views.delete, name='delete'),
	path('confirm/<int:id>', views.confirm, name = 'confirm'),
	path('login/', views.login, name='login'),
	path('forgotpwd/', views.forgotpwd, name= 'forgotpwd'),
	path('changepwd/', views.changepwd, name='changepwd')
]
