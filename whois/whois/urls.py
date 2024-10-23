
from django.urls import path, include
from whois.whois_app.views import home
from whois.whois_app.addCvViews import addCv

urlpatterns = [
    path('api/', home,name='getCv'),
    path('api/addCv/', addCv,name='addCv')
]
