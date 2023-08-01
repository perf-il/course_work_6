from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mail_sender import models as my_models
from mail_sender import forms as my_forms
from blog.models import Blog
from mail_sender.services import get_cache


def home(request):
    customers = my_models.Customer.objects.all()
    settings = my_models.SendSettings.objects.all()
    act_settings = my_models.SendSettings.objects.filter(status='CR')
    blog_posts = Blog.objects.filter(is_published=True)
    blog_posts_random = blog_posts.order_by('?')[:3]
    context = {
        'customers': customers,
        'settings': settings,
        'act_settings': act_settings,
        'blog_posts': blog_posts,
        'blog_posts_random': get_cache('posts', blog_posts_random),
        'title': 'Главная'
    }
    return render(request, 'mail_sender/home.html', context)


class CheckPermEditMixin:
    """Mixin для проверки владельца или суперпользователя"""
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.created_by != self.request.user and not self.request.user.is_superuser:
            raise Http404('Недостаточно прав доступа - только владелец может редактировать эту страницу')
        return self.object


class CustomersView(LoginRequiredMixin, generic.ListView):
    model = my_models.Customer
    extra_context = {
        'title': 'Получатели'
    }

    def get_queryset(self, *args, **kwargs):
        """выборка активных пользователей из всех"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_blocked=False)
        return queryset


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    model = my_models.Customer

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class CustomerCreateView(LoginRequiredMixin, generic.CreateView):
    model = my_models.Customer
    form_class = my_forms.CustomerForm
    success_url = reverse_lazy('mailsender:all_customers')


class CustomerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = my_models.Customer
    form_class = my_forms.CustomerForm
    success_url = reverse_lazy('mailsender:all_customers')


class CustomerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = my_models.Customer
    success_url = reverse_lazy('mailsender:all_customers')
    extra_context = {
        'title': 'Удалить получателя'
    }


class ContentEmailView(LoginRequiredMixin, generic.ListView):
    model = my_models.ContentEmail
    extra_context = {
        'title': 'Шаблоны писем'
    }


class ContentEmailDetailView(LoginRequiredMixin, generic.DetailView):
    model = my_models.ContentEmail

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ContentEmailCreateView(LoginRequiredMixin, generic.CreateView):
    model = my_models.ContentEmail
    form_class = my_forms.WriteEmailForm
    success_url = reverse_lazy('mailsender:all_email_templates')

    def form_valid(self, form):
        """заполнение поля владельца при валидации формы"""
        if form.is_valid():
            fields = form.save(commit=False)
            fields.created_by = self.request.user
        return super().form_valid(form)


class ContentEmailUpdateView(LoginRequiredMixin, CheckPermEditMixin, generic.UpdateView):
    model = my_models.ContentEmail
    form_class = my_forms.WriteEmailForm
    success_url = reverse_lazy('mailsender:all_email_templates')


class ContentEmailDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = my_models.ContentEmail
    success_url = reverse_lazy('mailsender:all_email_templates')
    extra_context = {
        'title': 'Удалить шаблон письма'
    }


class SetEmailingView(LoginRequiredMixin, generic.ListView):
    model = my_models.SendSettings
    extra_context = {
        'title': 'Настройки рассылок'
    }


class SetEmailingDetailView(LoginRequiredMixin, generic.DetailView):
    model = my_models.SendSettings

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        return context_data


class SetEmailingCreateView(LoginRequiredMixin, generic.CreateView):
    model = my_models.SendSettings
    form_class = my_forms.SendSettingsForm
    success_url = reverse_lazy('mailsender:all_emailing')

    def form_valid(self, form):
        """заполнение поля владельца при валидации формы"""
        if form.is_valid():
            fields = form.save(commit=False)
            fields.created_by = self.request.user
        return super().form_valid(form)


class SetEmailingUpdateView(LoginRequiredMixin, CheckPermEditMixin, generic.UpdateView):
    model = my_models.SendSettings
    form_class = my_forms.SendSettingsForm
    success_url = reverse_lazy('mailsender:all_emailing')


class SetEmailingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = my_models.SendSettings
    success_url = reverse_lazy('mailsender:all_emailing')
    extra_context = {
        'title': 'Удалить настройки рассылки'
    }


