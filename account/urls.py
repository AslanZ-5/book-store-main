from unicodedata import name
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from .forms import (UserLoginForm, PwdResetForm, PwdResetConfirmForm)
from .views import (account_register,
                    account_activate,
                    dashboard,
                    edit_details,
                    delete_user,
                    view_address,
                    add_address,
                    edit_address,
                    set_default,
                    delete_address,
                    add_to_wishlist,
                    wishlist
                    )

app_name = 'account'
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='login.html',
                                               form_class=UserLoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    path('register/',account_register,name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', account_activate, name='activate'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',
                                                                 success_url='password_reset_email_confirm',
                                                                 email_template_name='password_reset_email.html',
                                                                 form_class=PwdResetForm),name='pwdreset'),
    path('password_reset/password_reset_email_confirm/',auth_views.PasswordResetDoneView.as_view(template_name='reset_status.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(
                                                                    template_name='password_reset_confirm.html',
                                                                    success_url=reverse_lazy('account:password_reset_complete'),
                                                                    form_class=PwdResetConfirmForm),name='password_reset_confirm'),
    
    path('password_reset_complete/',
        auth_views.PasswordResetDoneView.as_view(template_name='reset_status.html'),name='password_reset_complete'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/edit/', edit_details, name='edit_details'),
    path('profile/delete_user/', delete_user, name='delete_user'),
    path('profile/delete_confirm', TemplateView.as_view(template_name='delete_confirm.html'),
                                                        name='delete_confirmation'),
    path("addresses/", view_address, name='addresses'),
    path("add_address/", add_address, name='add_address'),
    path("address/edit/<slug:id>/", edit_address, name='edit_address'),
    path("address/delete/<slug:id>/", delete_address, name='delete_address'),
    path("address/set_default/<slug:id>/", set_default, name='set_default'),
    # Wish list
    path('wishlist', wishlist, name='wishlist'),
    path('wishlist/add_to_whishlist/<int:id>/', add_to_wishlist, name='add_to_wishlist'),
    
    
]