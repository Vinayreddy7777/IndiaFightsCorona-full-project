"""IndiaFightsCorona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#created apps
from mainapp import views as main_views
from adminapp import views as admin_views
from hospitalapp import views as hospital_views
from oxygensupplierapp import views as oxygensupplier_views
from userapp import views as user_views
#resources for files
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admins/', admin.site.urls),

    #main
    path('',main_views.main_home, name='main_home'),
    path('main-about',main_views.main_about, name='main_about'),
    path('main-hospital-beds',main_views.main_hospital_beds, name='main_hospital_beds'),
    path('main-ventilators',main_views.main_ventilators, name='main_ventilators'),
    path('main-oxygen-cylinders',main_views.main_oxygen_cylinders, name='main_oxygen_cylinders'),
    path('main-plasma',main_views.main_plasma, name='main_plasma'),
    path('main-ration-help',main_views.main_ration_help, name='main_ration_help'),
    path('main-contact',main_views.main_contact, name='main_contact'),
    path('main-booking',main_views.main_booking, name='main_booking'),


    #admin
    path('admin-login',admin_views.admin_login, name='admin_login'),
    path('admin-dashboard',admin_views.admin_dashboard, name='admin_dashboard'),
    path('admin-view-hospitals',admin_views.admin_view_hospitals, name='admin_view_hospitals'),
    path('accept_hospitals/<int:id>/',admin_views.accept_hospitals, name='accept_hospitals'),
    path('reject_hospitals/<int:id>/',admin_views.reject_hospitals, name='reject_hospitals'),
    path('admin-view-hospital_beds',admin_views.admin_view_hospital_beds, name='admin_view_hospital_beds'),
    path('admin-view-ventilators',admin_views.admin_view_ventilators, name='admin_view_ventilators'),
    path('admin-view-plasma',admin_views.admin_view_plasma, name='admin_view_plasma'),
    # path('admin_users_request_plasma',admin_views.admin_users_request_plasma, name='admin_users_request_plasma'),
    path('admin-view-ration',admin_views.admin_view_ration, name='admin_view_ration'),
    # path('admin_users_request_ration',admin_views.admin_users_request_ration, name='admin_users_request_ration'),
    path('admin-view-o2-suppliers',admin_views.admin_view_o2_suppliers, name='admin_view_o2_suppliers'),
    path('accept_o2supplier/<int:id>/',admin_views.accept_o2supplier, name='accept_o2supplier'),
    path('reject_o2supplier/<int:id>/',admin_views.reject_o2supplier, name='reject_o2supplier'),
    path('admin-view-o2-cylinders',admin_views.admin_view_o2_cylinders, name='admin_view_o2_cylinders'),
    path('admin-view-users',admin_views.admin_view_users, name='admin_view_users'),
    path('admin-view-help-requests',admin_views.admin_view_help_requests, name='admin_view_help_requests'),
    path('admin-view-feedback',admin_views.admin_view_feedback, name='admin_view_feedback'),
    path('admin-contact-us',admin_views.admin_contact_us, name='admin_contact_us'),
    path('admin-logout',main_views.main_home, name='logout'),


    #hospital
    path('hospital-login',hospital_views.hospital_login, name='hospital_login'),
    path('hospital-registration',hospital_views.hospital_registration, name='hospital_registration'),
    path('hospital-dashboard',hospital_views.hospital_dashboard, name='hospital_dashboard'),
    path('hospital-add-bed',hospital_views.hospital_add_bed, name='hospital_add_bed'),
    path('hospital_view_beds',hospital_views.hospital_view_beds, name='hospital_view_beds'),
    path('hospital_edit_bed/<int:id>/',hospital_views.hospital_edit_bed, name='hospital_edit_bed'),
    path('delete_bed/<int:id>/',hospital_views.delete_bed ,name='delete_bed'),
    path('hospital-add-ventilator',hospital_views.hospital_add_ventilator, name='hospital_add_ventilator'),
    path('hospital-view-ventilators',hospital_views.hospital_view_ventilators, name='hospital_view_ventilators'),
    path('hospital_edit_ventilator/<int:id>/',hospital_views.hospital_edit_ventilator, name='hospital_edit_ventilator'),
    path('delete_ventilator/<int:id>/',hospital_views.delete_ventilator ,name='delete_ventilator'),
    path('hospital-logout',hospital_views.hospital_logout, name='hospital_logout'),


    #oxygensupplier
    path('oxygensupplier-login',oxygensupplier_views.oxygensupplier_login, name='oxygensupplier_login'),
    path('oxygensupplier-registration',oxygensupplier_views.oxygensupplier_registration, name='oxygensupplier_registration'),
    path('oxygensupplier-dashboard',oxygensupplier_views.oxygensupplier_dashboard, name='oxygensupplier_dashboard'),
    path('oxygensupplier-add-o2cylinder',oxygensupplier_views.oxygensupplier_add_o2cylinder, name='oxygensupplier_add_o2cylinder'),
    path('oxygensupplier-view-o2cylinder',oxygensupplier_views.oxygensupplier_view_o2cylinder, name='oxygensupplier_view_o2cylinder'),
    path('oxygensupplier-edit-o2cylinder/<int:id>/',oxygensupplier_views.oxygensupplier_edit_o2cylinder, name='oxygensupplier-edit-o2cylinder'),
    path('delete_o2cylinder/<int:id>/',oxygensupplier_views.delete_o2cylinder ,name='delete_o2cylinder'),
    path('oxygensupplier-logout',main_views.main_home, name='logout'),


    #user
    path('user-login',user_views.user_login, name='user_login'),
    path('user-registration',user_views.user_registration, name='user_registration'),
    path('user-home',user_views.user_home, name='user_home'),
    path('user-donate-plasma',user_views.user_donate_plasma, name='user_donate_plasma'),
    path('user-donate-ration',user_views.user_donate_ration, name='user_donate_ration'),
    path('user-request-help',user_views.user_request_help, name='user_request_help'),
    path('user-feedback',user_views.user_feedback, name='user_feedback'),
    path('user-logout',main_views.main_home, name='logout'),
    path('user-hospital-beds',user_views.user_hospital_beds, name='user_hospital_beds'),
    path('user-ventilators',user_views.user_ventilators, name='user_ventilators'),
    path('user-oxy-cylinders',user_views.user_oxy_cylinders, name='user_oxy_cylinders'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


