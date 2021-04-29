from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'home.html', {'hello': 'Hello!'})

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    string_count = len(user_text.split())
    return render(request, 'reverse.html', {'user_text': user_text, 'reversed_text': reversed_text, 'string_count': string_count})
