from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rent_app.models import CAR
from .forms import SignUpForm,CarForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:

        form = SignUpForm()  # Only create a new form instance for GET requests

    return render(request, 'sign_up.html', {'form': form})



def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('view')  # Redirect to the home page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})




def log_out(request):
    logout(request)
    return render(request,'index.html')

@login_required
def my_cars(request):
    cars = CAR.objects.filter(owner=request.user) # Fetch cars added by the logged-in user
    return render(request, 'my_cars.html', {'cars': cars})



def view(request):
    return render(request,'view.html')

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            car = form.save(commit=False)
            car.owner.id = request.user.id  # Set the owner to the logged-in user
            car.save()  # Now save it to the database
            return redirect('my_cars') # Redirect to car list after saving
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(CAR, id=car_id, owner=request.user)  # Ensure the user is the owner
    car.delete()  # Delete the car
    return redirect('my_cars')

@login_required
def edit_car(request, car_id):
    car = get_object_or_404(CAR, id=car_id, owner=request.user)  # Ensure the user is the owner

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)  # Include request.FILES for image upload
        if form.is_valid():
            form.save()
            return redirect('my_cars')  # Adjust redirect as necessary
    else:
        form = CarForm(instance=car)

    return render(request, 'edit_car.html', {'form': form, 'car': car})