
from django.urls import path, include
from whois_app.views import home
from whois_app.addCvViews import addCv

urlpatterns = [
    path('', home, name='getCv'), # hongoroo
    path('addCv/', addCv, name='addCv') ,# boldoo
]
