from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import HttpResponse
from django.template import loader
from .models import userlogin
from django.contrib import messages
from .forms import ContactForm
#from .forms import LoginForm
from .forms import HomeForm
from django.views.generic import View
import json
# Create your views here.


def index(request):
    all_users = userlogin.objects.all()
    return render(request, "userlogin/formnew.html", {'Users': all_users})

def loginview(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get("password")
            if userlogin.objects.filter(username=username, password=password).exists():
                data = userlogin.objects.all()

                return render(request, 'userlogin/home.html', {'userlogin': data})
            else:
                return HttpResponse('username or password are not correct')
            #return render(request, 'userlogin/home.html', stu, {'form': form})
            #response = redirect('../homecreate/')
            #return response
    else:
        return render(request, 'userlogin/login.html')

# def login(request):
#     if request.method == 'POST':
#         # POST, generate form with data from the request
#         form = LoginForm(request.POST)
#     else:
#         # GET, generate blank form
#         form = LoginForm()
#     return render(request, 'userlogin/login.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
    else:
        # GET, generate blank form
        form = ContactForm()
    return render(request, 'userlogin/formnew.html', {'form': form})


def articlespage(request):
    return render(request, 'userlogin/formnew.html')


def successpage(request):
    data = json.dumps(request.POST)
    print(data)

    return render(request, 'userlogin/successpage.html', context={'data': data})


# class ContactView(View):
#      template_name = 'userlogin/formnew.html'
#
#      def get(self, request):
#          return render(request, self.template_name)
#          #response = redirect('../homecreate/')
#
#      def post(self, request):
#          form = ContactForm(request.POST)
#          if form.is_valid():
#              text = form.cleaned_data['post']
#
#          args = {'form': form, 'text': text}
#          return render(request, self.template_name, args)


def register(request):

    if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            mail = request.POST.get('mail')
            address = request.POST.get('address')
            phonenumber = request.POST.get('phonenumber')

            return render(request, 'userlogin/formnew', context={"data": data})
    else:
        form = ContactForm(request.POST)
        return render(request, 'userlogin/formnew.html', {'form': form})

