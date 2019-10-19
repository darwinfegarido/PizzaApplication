from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Pizza, PizzaType, Transaction
from django.conf import settings
from  .forms import PizzaForm, TransactionForm, SearchForm


# Create your views here.
class HomeView(ListView):
    model = Transaction
    form_class = SearchForm
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timezone'] = settings.TIME_ZONE
        context['search_form'] = SearchForm
        return context

    def get_queryset(self): #search function
        name = self.form_class(self.request.GET)
        if name.is_valid():
            order_list = self.model.objects.filter(pizza_id__name__contains='{0}'.format(self.request.GET.get('name', '')))
            return order_list.order_by('-pk') #order by descending



class ManagementView(TemplateView):
    template_name = 'management.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form_pizza'] = PizzaForm
        context['form_transaction'] = TransactionForm
        return context

    def post(self, request):
        if request.method == 'POST':
            form = TransactionForm(request.POST) if 'pizza_id' in request.POST else PizzaForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponse('success!!!')
