#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse("Hello World!")

def current_datetime(request):
  current_date = datetime.datetime.now()
  return render_to_response('test/current_datetime.html', locals())

  #now = datetime.datetime.now()
  #return render_to_response('current_datetime.html',{'current_date':now})
  
  #t = get_template('current_datetime.html')
  #html = t.render(Context({'current_date':now}))
  #return HttpResponse(html)

#def current_datetime(request):
#  now = datetime.datetime.now()
#  html = "<html><body>It is now %s.</body></html>" % now
#  return HttpResponse(html)

#def hours_ahead(request, hour_offset):
  #try:
  #  hour_offset = int(hour_offset)
  #except ValueError:
  #  raise Http404()
  #next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
  #return render_to_response('test/hours)ahead.html',{'hour_offset':hour_offset,'next_time':next_time})
  #return render_to_response('test/hours_ahead.html', locals())
  #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
  #return HttpResponse(html)
def hours_ahead(request, hour_offset):
  try:
    hour_offset = int(hour_offset)
  except ValueError:
    raise Http404()
  next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
  return render_to_response('test/hours_ahead.html', ({'hour_offset':hour_offset,'next_time':next_time}))
