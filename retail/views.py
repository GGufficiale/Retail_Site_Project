import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.functional import SimpleLazyObject
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from config.settings import EMAIL_HOST_USER
from retail.forms import ProductForm, ProductModeratorForm
from retail.models import Product
from users.models import User


class HomeView(TemplateView):
    """Класс, отображающий базовую страницу"""
    template_name = 'retail/index.html'


class ProductListView(LoginRequiredMixin, ListView):
    """Класс, заменяющий функцию product_list (FBV на CBV)"""
    model = Product
    template_name = 'retail/product_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Product.objects.all()
        else:
            return Product.objects.filter(owner=self.request.user)


class ProductDetailView(DetailView):
    """Класс, заменяющий функцию product_detail (FBV на CBV)"""
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('retail:product_list')

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse('retail:product_list')
        else:
            return reverse('retail:index')

    # def form_valid(self, form):
    #     """Метод для """
    #     ...


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # template_name = 'retail/product_create.html'
    success_url = reverse_lazy('retail:product_list')

    def get_success_url(self):
        return reverse('retail:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        """Метод для работы с правами доступа"""
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('product.can_cancel_publication') and user.has_perm(
                'product.can_edit_description') and user.has_perm('product.can_change_category'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'retail/product_confirm_delete.html'
    success_url = reverse_lazy('retail:product_list')


class ContactPageView(TemplateView):
    """Класс для отображения страницы с контактами"""
    template_name = 'retail/contact.html'

    def post(self, request, *args, **kwargs):
        """Метод для приема инфы с фронтэнда в контактах и ее вывода в консоль"""
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(f'{name} ({email}): {message}')
        return render(request, 'retail/contact.html')

    def get(self, request):
        return render(request, 'retail/contact.html')


class InfoPageView(TemplateView):
    """Класс для отображения страницы с информацией о ресторане"""
    template_name = 'retail/info.html'

    def get(self, request):
        return render(request, 'retail/info.html')
