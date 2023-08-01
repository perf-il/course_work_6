from django.urls import path

from mail_sender import views as my_view
from mail_sender.apps import MailSenderConfig

app_name = MailSenderConfig.name

urlpatterns = [

    path('', my_view.home, name='home'),

    path('customers', my_view.CustomersView.as_view(), name='all_customers'),
    path('customer/<int:pk>', my_view.CustomerDetailView.as_view(), name='customer'),
    path('customer/create', my_view.CustomerCreateView.as_view(), name='customer_create'),
    path('customer/update/<int:pk>', my_view.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>', my_view.CustomerDeleteView.as_view(), name='customer_delete'),

    path('email-templates', my_view.ContentEmailView.as_view(), name='all_email_templates'),
    path('email-template/<int:pk>', my_view.ContentEmailDetailView.as_view(), name='email_template'),
    path('email-template/create', my_view.ContentEmailCreateView.as_view(), name='email_template_create'),
    path('email-template/update/<int:pk>', my_view.ContentEmailUpdateView.as_view(), name='email_template_update'),
    path('email-template/delete/<int:pk>', my_view.ContentEmailDeleteView.as_view(), name='email_template_delete'),

    path('email-settings', my_view.SetEmailingView.as_view(), name='all_emailing'),
    path('email-setting/<int:pk>', my_view.SetEmailingDetailView.as_view(), name='email_setting'),
    path('email-setting/create', my_view.SetEmailingCreateView.as_view(), name='email_setting_create'),
    path('email-setting/update/<int:pk>', my_view.SetEmailingUpdateView.as_view(), name='email_setting_update'),
    path('email-setting/delete/<int:pk>', my_view.SetEmailingDeleteView.as_view(), name='email_setting_delete'),

]