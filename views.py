

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from LitTalkIndex.models import *
from LitTalk import settings
from django.core.mail import send_mail

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django.core.exceptions import  ObjectDoesNotExist



def index(request):
    if request.session.has_key('username'):
        username = request.session['username']

        return render(request, 'index.html', {"username": username})
    else:

        template = loader.get_template('index.html')
        return HttpResponse(template.render())
def login(request):

    if request.method == 'POST':
        username = request.POST['email']

        password = request.POST['pswd']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                request.session['username'] =   username
                auth.login(request, user)
                print(" data validation is done")
                return HttpResponseRedirect('/LitTalkIndex/index/')
            else:

                messages.error(request, 'invalid usernamae or password')
                return render(request, 'login.html')
        except auth.objectNotExist:
            print("some errror ")
            return  render(request,'login.html')
    else:
        return render(request, 'login.html')




   # return HttpResponse(template.render())




def home(request):

     return redirect(index(request))


def register(request):

    if request.method == 'POST':
        form=userform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            EmailId=form.cleaned_data['EmailId']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            password=form.cleaned_data['password']
            User.objects.create_user(username= username,email=EmailId,first_name= first_name,last_name= last_name,
                                     password=password)
            return HttpResponseRedirect('/LitTalkIndex/login/')
    else:
        form=userform()
        return render(request, 'register.html', {'form': form})

def logout(request):
   try:
      msg="You are sucessfully Loged out"
      del request.session['username']


   except:
      pass
   return render(request,"login.html",{'msg':msg})

def hindipoem(request):
     # template = loader.get_template('')

      poem =  HindiPoem.objects.all()
      return render(request, "Hindipoem.html", {'poem': poem})

def AddPoem(request):
    if request.session.get('username') is None:
        msg = "please login first to add poem"
        return render(request, "login.html", {'msg': msg})
    else:
        if request.method == 'POST':
            form = AddHindiPoemForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'added sucessfully.......')
                return HttpResponseRedirect('/LitTalkIndex/AddPoem/')

        else:
            form = AddHindiPoemForm()
            return render(request, 'AddPoem.html', {'form': form})


    return  render(request , 'AddPoem.html')

def mail(request):
    subject = "Greetings"
    msg     = "Congratulations for your success"
    to      = "tripathyajit9@gmail.com"
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)













