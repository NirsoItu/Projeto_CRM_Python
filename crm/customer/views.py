from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Classe da função de listagem
class CustomerListView(ListView):
    template_name = "customer/customer_list.html"
    paginate_by = 5
    model = Customer
    queryset = Customer.objects.all()

# Classe da função de criação
class CustomerCreateView(CreateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    # Função de validação do formulário
    def form_valid(self, form):
        return super().form_valid(form)

    # Indica qual o url será redirecionado ao dslvsr formulário com sucesso usando o reverse
    def get_success_url(self):
        return reverse('customer-list')

# Classe da função de edição
class CustomerUpdateView(UpdateView):
    template_name = "customer/customer.html"
    form_class = CustomerForm

    # Função para buscar o id,caso não ache, retorna erro 404
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    # Função de validação do formulário
    def form_valid(self, form):
        return super().form_valid(form)

    # Indica qual o url será redirecionado ao dslvsr formulário com sucesso usando o reverse
    def get_success_url(self):
        return reverse('customer-list')

# Classe da função de exclusão
class CustomerDeleteView(DeleteView):
    # Função para buscar o id,caso não ache, retorna erro 404
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id)

    # Indica qual o url será redirecionado ao dslvsr formulário com sucesso usando o reverse
    def get_success_url(self):
        return reverse('customer-list')

