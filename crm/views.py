from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddCustomerForm
from .models import Customer

# Import Pagination Stuff
from django.core.paginator import Paginator

# Import Q for multiple Queries
from django.db.models import Q


# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home') 
        else :
            messages.error(request, "There was an error! Please check your password or username!")
            return redirect('home')
    else :
        p = Paginator(Customer.objects.all().order_by('-created_at'), 15)
        page = request.GET.get('page')
        customers = p.get_page(page)
        return render(request, 'home.html', {'customers' : customers})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfluy registered!")
            return redirect('home')
    else :
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up Record
        customer_record = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer_record':customer_record})
    else :
        messages.success(request, "You must be logged in to view that page!!!")
        return redirect('home')


def delete_customer(request, pk):

    if request.user.is_authenticated:
        delete_it = Customer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Customer Deleted Successfully!!")
        return redirect('home')
    else :
        messages.success(request, "You must be logged in to delet customer!!!")
        return redirect('home')
    

def add_customer(request):
    form = AddCustomerForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_customer = form.save()
                messages.success(request, "Customer Added...")
                return redirect('home')
            
        return render(request, 'add_customer.html', {'form':form})
    else :
        messages.success(request, "You must be logged in")
        return redirect('home')
    

def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)

        if form.is_valid():
            form.save()
            messages.success(request, "Customer has been updated...")
            return redirect('home')
        return render(request, 'update_customer.html', {'form':form})
    else :
        messages.success(request, "You must be logged in")
        return redirect('home') 
    

def search_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            searched = request.POST.get('searched')
            customers = Customer.objects.all()
            if searched:     
                customers = customers.filter(
                    Q(first_name__contains=searched) | 
                    Q(last_name__contains=searched) |
                    Q(city__contains=searched) |
                    Q(district__contains=searched)
                    )
            customers = customers.order_by('-created_at')
           
        else :
            messages.success(request, "You must be search something")
            customers = Customer.objects.all()
            
        p = Paginator(customers, 15)
        page = request.GET.get('page')
        customers = p.get_page(page)
        return render(request, 'search_customer.html', {'customers':customers})


    else :
        messages.success(request, "You must be logged in")
        return redirect('home') 
