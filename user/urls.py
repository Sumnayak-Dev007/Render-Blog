from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('sign_up',views.index,name="sign_up"),
    path('login/', auth_view.LoginView.as_view(template_name='User/login_form.html'), name='login'),
    path('new_login/', auth_view.LoginView.as_view(template_name='User/login.html'), name='new_login'),
    path('new_logout/', views.CustomLogout.as_view(next_page='home'), name='logout'),
    path('profile/',views.userProfile,name='profile'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='User/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='User/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='User/password_reset_confirm.html'), name='password_reset_confirm'),
    path('done/',auth_view.PasswordResetCompleteView.as_view(template_name='User/password_reset_complete.html'),name='password_reset_complete'),
]

