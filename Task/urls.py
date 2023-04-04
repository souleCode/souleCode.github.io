

from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
    path('<int:my_id>/update',views.update,name='update'),
    path('<int:my_id>/delete',views.delete,name='delete')
]