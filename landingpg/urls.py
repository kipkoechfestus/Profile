from landingpg.views import landingpgView

from django.urls import path


urlpatterns=[
	path('',landingpgView,name='landingpage'),
]