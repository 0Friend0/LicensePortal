from django.shortcuts import render, redirect
from .models import Client, License
from .forms import LicenseForm, ClientForm
from django.views.generic import ListView, DetailView


class LicensesListView(ListView):
    model = License
    

class ClientsListView(ListView):
    model = Client

class LicenseDetailView(DetailView):

    model = License



def home(request):
    return render(request, 'home.html')

def licenses(request):
    licenses_list = License.objects.all()
    context={'licenses': licenses_list}
    return render(request, 'licenses/licenses.html', context=context)

def license(request, pk):
    license = License.objects.get(id=pk)
    context={'license': license}
    return render(request, 'licenses/license.html', context=context)

def license_add(request):
    form = LicenseForm()

    if request.method == 'POST':
        form = LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('licenses')

    context = {'form': form}
    return render(request, 'licenses/license_form.html', context=context)

def license_update(request, pk):
    license = License.objects.get(id=pk)
    form = LicenseForm(instance=license)

    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=license)
        if form.is_valid():
            form.save()
            return redirect('licenses')

    context = {'form': form}
    return render(request, 'licenses/license_form.html', context=context)

def license_delete(request, pk):
    license = License.objects.get(id=pk)
    if request.method == 'POST':
        license.delete()
        return redirect('licenses')

    context = {'object': license}
    return render(request, 'licenses/delete.html', context=context)

def clients(request):
    clients_list = Client.objects.order_by("name")
    context={'clients': clients_list}
    return render(request, 'licenses/clients.html', context=context)

def client(request, pk):
    client_data = Client.objects.get(id=pk)
    licenses_list = License.objects.filter(client=client_data.id)
    context={'client_data': client_data, 'licenses_list': licenses_list}
    return render(request, 'licenses/client.html', context=context)

def client_add(request):
    form = ClientForm()

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')

    context = {'form': form}
    return render(request, 'licenses/client_form.html', context=context)

def client_update(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients')

    context = {'form': form}
    return render(request, 'licenses/client_form.html', context=context)

def client_delete(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')

    context = {'object': client}
    return render(request, 'licenses/delete.html', context=context)
    