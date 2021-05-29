from django.shortcuts import render
from .models import Myurl
from .forms import MyurlForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

#Importing the required libraries
import contextlib
# from __future__ import with_statement
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys


#Defining the function to shorten a URL
def make_shorten(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


# Create your views here.
# List all course order by 'code' field
def myurl_list(request):
    c = Myurl.objects.all()
    print(c)
    return render(request, 'short/myurl_list.html', {'myurl': c})

# Create new myurl
def myurl_create(request):
    if request.method == "POST":
        form = MyurlForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            # print(make_shorten(m.longurl))
            m.shorturl = make_shorten(m.longurl)
            m.save()
            messages.success(request, 'Myurl ' + m.desc + ' has been successfully created!')
            return redirect(reverse_lazy('myurl_list'))
    else:
        form = MyurlForm()
    return render(request, 'short/myurl_create.html', {'form': form})

