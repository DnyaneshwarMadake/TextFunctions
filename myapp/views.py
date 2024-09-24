from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Item  # Import your Item model
from django.contrib import messages  # To show success/failure messages


# views.py
from django.shortcuts import render, redirect
from .forms import ItemForm





def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('dashboard')  # Redirect to another view after saving
    else:
        form = ItemForm()  # Provide an empty form for GET requests

    return render(request, 'dashboard.html', {'form': form})
