from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_form, name='login'),
    path('success/',views.slogin),
    path('home',views.nav, name='home'),
    path('tf/',views.tFeature),
    path('aOne/',views.aOne),
    path('usercform/',views.usercform, name='registration'),
    path('logout/',views.logout_form, name='logout'),
    path('passc/',views.password_change, name='passwordchange'),
    path('withoutoldpassc/',views.without_old_password_change, name='withoutoldpass'),
]