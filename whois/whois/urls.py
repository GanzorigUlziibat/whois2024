
from django.urls import path, include
from whois_app import authView, addCvViews, views


urlpatterns = [
    path('api/', views.home, name='getCv'),  # hongoroo
    path('api/addCv/', addCvViews.addCv, name='addCv'),  # boldoo
    path('api/auth/', authView.authCheckService),
]
