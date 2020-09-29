from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    food = ['apples', 'oranges', 'bananas']

    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]
    context = {
        'user' : user,
        'subjects': subjects,
        'food': food
    }

    return render(request, 'home.html', context)