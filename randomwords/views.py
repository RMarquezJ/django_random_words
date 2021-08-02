from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):

  if 'counter' not in request.session:
    request.session['counter'] = 0
  
  context = {
    'random': get_random_string(length=14)
  }
  return render(request, 'index.html', context)

def random(request):

  request.session['counter'] += 1
  return redirect('/')

def reset(request):

  request.session['counter'] = 0
  return redirect('/')