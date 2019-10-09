from django.shortcuts import render, reverse, redirect, get_object_or_404
from myapp.models import Client
from .forms import ClientForm
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q


def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('showclient'))

    else:
        form = ClientForm()
    return render(request, 'myapp/client_form.html', {'form': form})


def show(request):
    object_list = Client.objects.all().order_by('client_name', 'email_address', 'phone_number', 'suburb')
    return render(request, 'show.html', {'object_list': object_list})


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
