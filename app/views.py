from django.shortcuts import render
# from django.http import HttpResponse

def home (request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [1,2, 3, 4, 5]
    }
    return render(request, 'app/home.html', context)