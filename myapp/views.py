from django.shortcuts import render, reverse, redirect, get_object_or_404
from myapp.models import Client
from .forms import ClientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView

def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('showclient'))

    else:
        form = ClientForm()
    return render(request, 'myapp/client_form.html', {'form': form})


def client_update(request, pk, template_name='myapp/edit_client.html'):
    client= get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('showclient')
    return render(request, template_name, {'form':form})


def home(request):
    return render(request, 'home.html')


def search(request):
    query = request.GET.get('q')
    object_list = Client.objects.filter(
        Q(client_name__icontains=query) | Q(email_address__icontains=query) | Q(phone_number__icontains=query) | Q(suburb__icontains=query)
    )
    return render(request, 'show.html', {'object_list': object_list})


def delete(request, pk):
    query = Client.objects.get(pk=pk)
    query.delete()
    return HttpResponseRedirect(reverse('showclient'))


def sort(request):
    orderBy = request.GET.get('order_by')
    direction = 'desc'
    if request.GET.get('direction'):
        direction = request.GET.get('direction')
        if direction == 'desc':
            orderBy = "-" + orderBy   
            direction = 'asc'
        elif direction == 'asc':
            orderBy = orderBy   
            direction = 'desc'

    if orderBy is None:
        object_list = Client.objects.all().order_by('id')
        return render(request, 'show.html', {'object_list': object_list})

    else:
        object_list = Client.objects.all().order_by(orderBy)
        return render(request, 'show.html', {"object_list": object_list, "direction": direction})


# class ShowClient(ListView):
#     model = Client
#     template_name = 'show.html'

#     def get_queryset(self):
#         orderBy = self.request.GET.get('order_by')
#         self.direction = 'desc'
#         if self.request.GET.get('direction'):
#             direction = self.request.GET.get('direction')
#             if direction == 'desc':
#                 orderBy = "-" + orderBy   
#                 self.direction = 'asc'
        
#         if orderBy is None:
#             return Client.objects.all().order_by('client_name')
#         else:
#             return Client.objects.all().order_by(orderBy)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['direction'] = self.direction
#         return context