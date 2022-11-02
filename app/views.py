from django.shortcuts import render

from django.http import HttpResponse
from app.forms import *

# Create your views here.
def validate_data(request):
    SF=StudentForm()
    d={'form':SF}
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            #return HttpResponse('Validate')
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'validate_data.html',d)