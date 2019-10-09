from django.shortcuts import render, reverse, redirect, get_object_or_404
from myapp.models import Client
from .forms import ClientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView
from django.db.models import Q



class clientView(CreateView):
    model = Client
    form_class = ClientForm   

    def get_success_url(self):
        return reverse('showclient')


def show(request):
    # send_email()
    object_list = Client.objects.all().order_by('client_name', 'email_address', 'phone_number', 'suburb')
    return render(request, 'show.html', {'object_list': object_list})


class SearchResultsView(ListView):
    model = Client
    template_name = 'show.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Client.objects.filter(
            Q(client_name__icontains=query) | Q(email_address__icontains=query) | Q(phone_number__icontains=query) | Q(suburb__icontains=query)
        )
        return object_list


def edit_client(request):
    args = {}
    if request.method == "POST":
        form = ClientForm(data=request.POST, instance=request.user)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return HttpResponseRedirect(reverse('showclient'))
    else:
        form = ClientForm(instance=request.user)
        args['form'] = form
        return render(request, 'myapp/edit_client.html', args)

def client_update(request, pk, template_name='myapp/edit_client.html'):
    client= get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('showclient')
    return render(request, template_name, {'form':form})


class ClientDelete(DeleteView):
    model = Client
    template_name = 'myapp/delete.html'
    
    def get_context_data(self, **kwargs):
        context = super(ClientDelete, self).get_context_data(**kwargs)
        context["id"] = self.kwargs['pk']
        return context
    def get_success_url(self):
        return reverse('showclient')


class ViewClient(ListView):
    model = Client
    template_name = 'show.html'
    context_object_name = 'client'
    paginate_by = 5
    #queryset = model.objects.all().order_by('id')
    
    def get_queryset(self):
        orderBy = self.request.GET.get('order_by')
        self.direction = 'desc'
        if self.request.GET.get('direction'):
            direction = self.request.GET.get('direction')
            if direction == 'desc':
                orderBy = "-" + orderBy   
                self.direction = 'asc'
                
        
        if orderBy is None:
            return Client.objects.all().order_by('id')
        else:
            return Client.objects.all().order_by(orderBy)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direction'] = self.direction
        return context


def home(request):
    return render(request, 'home.html')
