from string import punctuation

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from pyexpat.errors import messages




#from .models import Item  # Import your Item model
# from django.contrib import messages  # To show success/failure messages


def index(request):
    return render(request, 'index.html')
    # file = open("1.txt", 'r+')
    # return HttpResponse(file.read())


def analyze(request):
    # return render(request,'index.html')
    # check checkbox
    ttext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount', 'off')
    print("Name is: ", ttext)

    if removepunc == "on":
        punctuations = '''*^%.$#,?!:;'""()—-…[]/{ }'''
        analyzed = ""
        for char in ttext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removed Punctuation", 'analyzed_text': analyzed}
        ttext = analyzed
        # return render(request,'analyze.html',params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in ttext:
            analyzed = analyzed + char.upper()
        params = {'purpose': "Changed to Uppercase", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        ttext = analyzed

    if (charcount == "on"):
        char_count = {}
        for char in set(ttext):
            char_count[char] = ttext.count(char)

        # Pass the dictionary to the template context
        return render(request, 'analyze.html', {'char_count': char_count})

    if removepunc != "on" and charcount != "on" and fullcaps != "on":
        return HttpResponse("Error please choose any option")

    return render(request, 'analyze.html', params)


def navigator(request):
    return HttpResponse('''<h1>webSite Navigator </h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Code with Harry </a>> <br></br> 
     <h1> Geeks for Geeks </h1> <a href ="https://www.geeksforgeeks.org/batch/devops-23/track/DevOps-SRE-Fundamentals/article/MTEzMzg%3D"> Geeks For Geeks</a>>
     <h1>Facebook Profile </h1> <a href ="https://www.facebook.com/login/"> Facebook Profile</a>>
     <a href='/'> back </a>

''')


def dashboard(request):
    return render(request, 'Dashboard.html')


def about(request):
    return HttpResponse(''' <h1>In about page </h1> <a href='/'> back </a>
''')


#
def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_price = request.POST.get('item_price')
        category = request.POST.get('category')

        # Save the new item to the database
        from mysite.myapp.models import Item
        new_item = Item(name=item_name, price=item_price, category=category)
        new_item.save()

        # Show a success message and redirect to the same page
        messages.success(request, 'Item added successfully!')
        return redirect('dashboard')  # Replace 'dashboard' with the name of your dashboard view

    # If not POST, render the add item form
    return render(request, 'dashboard.html')
