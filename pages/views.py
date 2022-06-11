from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return render(request, 'home.html')


def about_page_view(request):
    context = {
        'page_name': 'about',
        'description': 'this is s.th said in context',
        'button_value': "Dont click",
    }
    return render(request, 'pages/about.html', context)


def contact_page_view(request):
    return render(request, 'pages/contact.html')




