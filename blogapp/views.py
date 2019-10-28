from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.views.generic import View
from blogapp.models import Realuser
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import Realuser
from django.contrib.auth.hashers import check_password
from .forms import Signupform, LoginForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
import datetime
import json

class Home(View):


    def get(self, request):
        form = Signupform()
        login = LoginForm()
        return render(request, "index.html",{'id':form,'log': login})

    def linkmail(request):
        token=request.GET['token']
        mail=request.GET['email']
        ob = Realuser.objects.get(email=mail)
        if ob.token == token:
                ob.is_active=True
                ob.save()
                return redirect("/")
        else:
                return HttpResponse("Invalid Token")
        #return HttpResponse("token="+token+" email="+mail)


    def post(self,request):
        dict1 = {}
        form = Signupform(request.POST)
        if form.is_valid():
               try:
                    print(self.request.POST)
                    name = form.cleaned_data['name']
                    address = form.cleaned_data['address']
                    email = form.cleaned_data['email']
                    pwd = form.cleaned_data['pwd']
                    cpwd = form.cleaned_data['cpwd']
                    print("name----->", name,"email------>" , email)

                    if pwd == cpwd :
                       timestamp=datetime.datetime.timestamp(datetime.datetime.now())

                       obj = Realuser.objects.create_user(is_superuser="0", username=name, address=address, email=email, password=pwd)
                       token=account_activation_token._make_hash_value(obj,timestamp)
                       obj.token=token
                       msg="http://127.0.0.1:8000/email/?token="+token+"&email="+email
                       send_mail('Please confirm your mail id',msg,'anugeorge.cst@gmail.com',[email,],fail_silently=False)
                       obj.save()
                       dict1['val'] = "Success"

                    else:
                        dict1['val'] = "failure"

               except Exception as e:
                    print("Error: ", e)
                    dict1['result'] = "Error"


        else:
            print("form eroors: ---------------->", form.errors)
            dict1['val'] = "Error in forms"
            dict1['dict1']=form.errors
            print("non field-----------", form.non_field_errors())
            dict1['nonfield'] = form.non_field_errors()
        return HttpResponse(json.dumps(dict1), content_type="application/json")

class Login(View):

    def post(self, request):
        print("-------------------------------------------------------->login")
        dict2 = {}
        login = LoginForm(request.POST)
        if login.is_valid():
            uname = login.cleaned_data['uname']
            pwd = login.cleaned_data['pwd']
            print("uname: ", uname, "password: ", pwd)


            try:

                obj = Realuser.objects.get(username=uname)
                u = obj.username
                p = obj.password
                matchcheck = check_password(pwd, obj.password)
                if matchcheck and uname == u:
                    print("----------------------------------------->", matchcheck)
                    dict2['val'] = "success"

                else:
                    dict2['val'] = "failed"
                return HttpResponse(json.dumps(dict2), content_type="application/json")
            except Exception as e:
                print(e)

	


# class Category(View):
#     def get_name(request):
#        obj = CategoryForm()
#
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#
#        else:
#             form = NameForm()
#
#         return render(request, 'name.html',{'form': form})

