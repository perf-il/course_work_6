from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mail_sender import models as my_models
from mail_sender import forms as my_forms


class CustomersView(generic.ListView):
    model = my_models.Customer
    extra_context = {
        'title': 'Получатели'
    }

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_published=True)
    #     queryset = queryset.order_by('-data_creating')
    #     return queryset


class CustomerDetailView(generic.DetailView):
    model = my_models.Customer

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class CustomerCreateView(generic.CreateView):
    model = my_models.Customer
    form_class = my_forms.CustomerForm
    success_url = reverse_lazy('mailsender:all_customers')


class CustomerUpdateView(generic.UpdateView):
    model = my_models.Customer
    form_class = my_forms.CustomerForm
    success_url = reverse_lazy('mailsender:all_customers')


class CustomerDeleteView(generic.DeleteView):
    model = my_models.Customer
    success_url = reverse_lazy('mailsender:all_customers')
    extra_context = {
        'title': 'Удалить получателя'
    }


class ContentEmailView(generic.ListView):
    model = my_models.ContentEmail
    extra_context = {
        'title': 'Шаблоны писем'
    }

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_published=True)
    #     queryset = queryset.order_by('-data_creating')
    #     return queryset


class ContentEmailDetailView(generic.DetailView):
    model = my_models.ContentEmail

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ContentEmailCreateView(generic.CreateView):
    model = my_models.ContentEmail
    form_class = my_forms.WriteEmailForm
    success_url = reverse_lazy('mailsender:all_email_templates')


class ContentEmailUpdateView(generic.UpdateView):
    model = my_models.ContentEmail
    form_class = my_forms.WriteEmailForm
    success_url = reverse_lazy('mailsender:all_email_templates')


class ContentEmailDeleteView(generic.DeleteView):
    model = my_models.ContentEmail
    success_url = reverse_lazy('mailsender:all_email_templates')
    extra_context = {
        'title': 'Удалить шаблон письма'
    }


class SetEmailingView(generic.ListView):
    model = my_models.SendSettings
    extra_context = {
        'title': 'Настройки рассылок'
    }

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_published=True)
    #     queryset = queryset.order_by('-data_creating')
    #     return queryset


class SetEmailingDetailView(generic.DetailView):
    model = my_models.SendSettings

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class SetEmailingCreateView(generic.CreateView):
    model = my_models.SendSettings
    form_class = my_forms.SendSettingsForm
    success_url = reverse_lazy('mailsender:all_emailing')


class SetEmailingUpdateView(generic.UpdateView):
    model = my_models.SendSettings
    form_class = my_forms.SendSettingsForm
    success_url = reverse_lazy('mailsender:all_emailing')


class SetEmailingDeleteView(generic.DeleteView):
    model = my_models.SendSettings
    success_url = reverse_lazy('mailsender:all_emailing')
    extra_context = {
        'title': 'Удалить настройки рассылки'
    }


