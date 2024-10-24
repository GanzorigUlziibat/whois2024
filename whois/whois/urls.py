
from django.urls import path, include
from whois_app.views import home
from whois_app.addCvViews import addCv

urlpatterns = [
    path('api/', home, name='getCv'), # hongoroo
    path('api/addCv/', addCv, name='addCv') ,# boldoo
]
