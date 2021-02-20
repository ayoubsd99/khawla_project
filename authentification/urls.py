from django.urls import path

from authentification.views import SignInView,logout_view

urlpatterns = [
    path('signin/' ,SignInView.as_view(),name='signin'),
    path('logout/' ,logout_view,name='logout'),

]
