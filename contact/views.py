from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def contact(request):
  errors = []
  if request.method == 'POST':
    subject = request.POST['subject']
    message = request.POST['message']
    email = request.POST.get('email','noreply@example.com')
    #errors.append(str(subject))
    #errors.append(str(message))
    #errors.append(str(email))
    if not request.POST.get('subject',''):
      errors.append('Enter a subject')
    if not request.POST.get('message',''):
      errors.append('Enter a message')
    if request.POST.get('email') and '@' not in request.POST['email']:
      errors.append('Enter a valid e-mail address')
  if not errors:
    errors.append('no errors')
    #return HttpResponseRedirect('/contact/thanks/')
    #send_mail(subject, message, email ,['weiren0516@gmail.com'],)
  return render_to_response('contact/contact_form.html', {'errors':errors,'subject': request.POST.get('subject', ''),'message': request.POST.get('message', ''),'email': request.POST.get('email', '')}, context_instance=RequestContext(request))

def thanks(request):
  return render_to_response('contact/thanks.html')
