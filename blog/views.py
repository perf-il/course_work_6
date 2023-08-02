from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic


from blog.forms import BlogForm
from blog.models import Blog


class BlogView(generic.ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        queryset = queryset.order_by('-data_creating')
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_object(self, *args, **kwargs):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(queryset, slug=slug)
        return obj

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']

        return context_data


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'Написать статью'
    }

    def form_valid(self, form):
        if form.is_valid():
            fields = form.save(commit=False)
            fields.autor = self.request.user
            fields.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'Редактировать статью'
    }


class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog')
    extra_context = {
        'title': 'Удалить статью'
    }

