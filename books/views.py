from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def search(request):
  if 'q' in request.GET:
    message = "You searched for : %r' % request.GET['q']"
  else:
    message = "You submitted an empty form."
  return HttpResponse(message)

def search_form(request):
  return render_to_response('books/search_form.html',)
