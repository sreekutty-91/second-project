from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from mailapp.forms import StudentForm

# Create your views here.
def stdform(request):
    form = StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            subject='Learning Python'
            message = 'Dear Candidate,\n We are pleased to offer an internship at our company in Python Django session. If you are interested ,please reply with this mail .Hope you are interested to join with us.\n Regards,\n Infox Technologies.'
            recipient = form.cleaned_data.get('Email')
            send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient])
            return redirect('/')
    return render(request,'index.html',{'form':form})        

