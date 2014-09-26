from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def contact(request):
  errors = []
  if request.method == 'POST':
    if not request.POST.get('subject',False):
      errors.append('Enter a subject')
    if not request.POST.get('message',False):
      errors.append('Enter a message')
    if request.POST.get('email') and '@' not in request.POST['mail']:
      errors.append('Enter a valid e-mail address')
  #if not errors:
  #  send_mail(request.POST['subject'],request.POST['message'],request.POST.get('email','noreply@example.com'),['weiren0516@gmail.com'],)
  return HttpResponseRedirect('/contact/thanks/')
  return render_to_response('books/contact_form.html', {'errors':errors})
