from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from books.models import Book

# Create your views here.
def search(request):
  error = []
  if 'q' in request.GET:
    q = request.GET['q']
    if not q:
      error.append('Enter a search term')
    elif len(q) > 20:
      error.append('Please enter at most 20 characters')
    else:
      books = Book.objects.filter(title__icontains=q)
      return render_to_response('books/search_results.html',{'books':books, 'query':q})
  return render_to_response('books/search_form.html',{'error':error})
  #if 'q' in request.GET and request.GET['q']:
  #  q = request.GET['q']
  #  books = Book.objects.filter(title__icontains=q)
  #  return render_to_response('books/search_results.html', {'books':books, 'query':q})
    #message = "You searched for : %r" % request.GET['q']
  #else:
  #  return render_to_response('books/search_form.html', {'error':True})
    #return HttpResponse('Please submit a search term')
    #message = "You submitted an empty form."
  #return HttpResponse(message)

def search_form(request):
  return render_to_response('books/search_form.html',)
