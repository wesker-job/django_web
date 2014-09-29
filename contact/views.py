from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from contact.forms import ContactForm

# Create your views here.
def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      return render_to_response('contact/thanks.html',{'subject':cd['subject']})
      #send_mail(cd['subject'],cd['message'],cd.get('email','noreply@exam.com'),['site@exam.com'],)
      #return HttpResponseRedirect('thanks/',{'subject':cd['subject']})
  else:
    form = ContactForm(initial={'subject':'Test site'})
  return render_to_response('contact/contact_form.html',{'form':form}, context_instance=RequestContext(request))
  #errors = []
  #if request.method == 'POST':
  #  subject = request.POST['subject']
  #  message = request.POST['message']
  #  email = request.POST.get('email','noreply@example.com')
  #  if not request.POST.get('subject',''):
  #    errors.append('Enter a subject')
  #  if not request.POST.get('message',''):
  #    errors.append('Enter a message')
  #  if request.POST.get('email') and '@' not in request.POST['email']:
  #    errors.append('Enter a valid e-mail address')
  #if not errors:
  #  errors.append('no errors')
    ##return HttpResponseRedirect('/contact/thanks/')
    ##send_mail(subject, message, email ,['weiren0516@gmail.com'],)
  #return render_to_response('contact/contact_form.html', {'errors':errors,'subject': request.POST.get('subject', ''),'message': request.POST.get('message', ''),'email': request.POST.get('email', '')}, context_instance=RequestContext(request))

def thanks(request):
  return render_to_response('contact/thanks.html')
