from django.shortcuts import render
from time import localtime
# Create your views here.
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Stock1,Useer,Dummy
from .serializers import StockSerializer ,  StockSerializer1 ,ProbSerializer
from django.views import generic
from django.views.generic.edit  import CreateView
from django.views.generic import  View
from .forms import StockForm
from django.http import  request
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
#Lists all stocks or create a new onedef transport_new(request):
   ##return render(request,'music/transport_edit.html',{'form':form})
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import NewForm
from django.shortcuts import render, redirect

@csrf_exempt
def transport_new(request):
    if request.method == "POST":
        print "hello"
        form = StockForm(request.POST)
        if form.is_valid():
            print "hello"
        #    instance = Transport(file_field=request.FILES['logo'])
         #   instance.save()
            Transport1 = form.save()
            Transport1.save()
            email1=str(request.POST['email1'])
            c1 = Stock1.objects.last()
            c=localtime()
            li=[]
            li.append(str(email1))
            li.append('ramuklinus369@gmail.com')
            send_mail('Thanks for Reporting the problem',
                    'Dear'+''+','+'\n'+'Your Problem token no. is'+' '+'PGAS'+str(c.tm_mday)+str(c.tm_mon)+str(c.tm_year)+str(c1.pk) +'\n'+'Sent From Admin of PGAS System',
                    'ramuklinus369@gmail.com',
                    li)

            return redirect('companies:index')
    else:
        form = StockForm()
    return render(request, 'companies/transport_edit.html', {'form': form})
@csrf_exempt
def index(request):
    all_albums = Stock1.objects.all()
    albums = {'s1':[],'s2':[],'s3':[]}
    for x in xrange(0,all_albums.count()):
        if  x % 3 == 0:
            albums['s1'].append(all_albums[x])
        elif  x % 3 == 1:
            albums['s2'].append(all_albums[x])
        else:
            albums['s3'].append(all_albums[x])

    return render(request, 'companies/index.html',{'albums':albums})

def albdetail(request, album_id):
    album =Stock1.objects.get(pk=album_id)

    return render(request, 'companies/imgdetail.html', {'album': album})

def test(request):
    return render(request,'companies/test.html')
def service(request):
    return render(request,'companies/service.html')
def team(request):
    return render(request,'companies/team.html')
def login(request):
    return render(request,'companies/newLogin.html')
@csrf_exempt
def register(request):
        if request.method=="POST":
            reg=Useer()
            l=Useer.objects.filter(email1=str(request.POST['email']))
            if len(l)>=1:
                redirect('companies:rregister')

            else :
                reg.user1=str(request.POST['first_name'])
                reg.pass1=str(request.POST['password'])
                reg.email1=str(request.POST['email'])
                reg.Adhar=str(request.POST['adhar_no'])
                reg.save()
                return redirect('companies:index')
        return render(request,'companies/newRegister.html')



def rregister(request):
    messages.success(request, 'Sorry, already registered')
    return render(request,'companies/newRegister.html',{'error': 'Already Registerd'})

def problems(request):
    all_albums = Stock1.objects.all()
    albums = {'s1':[],'s2':[],'s3':[]}
    for x in xrange(0,all_albums.count()):
        if  x % 3 == 0:
            albums['s1'].append(all_albums[x])
        elif  x % 3 == 1:
            albums['s2'].append(all_albums[x])
        else:
            albums['s3'].append(all_albums[x])

    return render(request,'companies/problems.html',{'albums':albums})
def contact(request):
    if request.method=="POST":
        li=[]
        li.append(str(request.POST['email']))
        li.append('ramuklinus369@gmail.com')
        try:
            spe=send_mail('From'+' '+str(request.POST['name'])+' '+'About'+' ' +str(request.POST['subject']),request.POST['message'],'ramuklinus369@gmail.com',li)
            return redirect('companies:test')
        except:
            return HttpResponse("Could not process your Request")
    else:
        # messages.success(request,'Send Mail Succesfullu')
        return render(request,'companies/contact.html')

def email_verify(request,emailto):
    l=Dummy.objects.all()
    flag=0
    for i in range(len(l)):
        if str(emailto) == str(l[i]):
            flag=2
            album1=Dummy.objects.get(pk=l[i].id)
            if album1.bf==0:
                album1.delete()
                formreq = Dummy()
                formreq.duser1=str(emailto)
                formreq.bf=1
                formreq.save()
                flag=1
                break
    if flag==1:
        return  HttpResponse("Email verification done")
    if flag==0:
        return  HttpResponse("Not Registered yet")
    if flag==2:
        return  HttpResponse("Already Registered")

class StockList0(APIView):
    def get(self,request):
        stocks=Stock1.objects.all()
        print stocks
        serializer=StockSerializer1(stocks,many=True)
        content = {'user_details': serializer.data}
        return Response(content)
    def post(self):
        pass




class StockList(APIView):
    def get(self,request):
        stocks=Stock1.objects.all()
        serializer=StockSerializer(stocks,many=True)
        content = {'user_count': serializer.data}
        return Response(content)
    def post(self):
        pass
class StockList1(APIView):
    def get(self,request,album_id):
        stocks=Stock1.objects.get(id=album_id)
        serializer=StockSerializer(stocks)
        ls=[]
        #s.append(serializer.data)
        m=serializer.data

        k=str(m['data'])
        m=k.replace("\n","")
        m=m.replace('\r','')
        #ls.append(k)
        #ls.append(type(k))
        return Response(m)
        #content = {'user_count': ls}
        #return Response(content)
    def post(self):
        pass

class Login1(APIView):
    def post(self,request):
        reg=Useer()
        l=Useer.objects.filter(email1=str(request.POST['email']))

        if len(l)>=1:
           n=1
           k=[{"error":"false","dup":n}]
           return Response(k)
        else :
            reg.user1=="none"
            reg.pass1=str(request.POST['password'])
            reg.email1=str(request.POST['email'])
            reg.Adhar="none"
            reg.save()
            k=[{"error":"false","dup":0}]
            return Response(k)

    def get(self,request):
        form = LoginForm()
        return render(request, 'companies/login_new.html', {'form': form})

class Login1copy(APIView):
    def post(self,request):
        reg=Useer()
        l=Useer.objects.filter(email1=str(request.POST['email']))

        if len(l)>=1:
           n=1
           k=[{"error":"false","dup":n}]
           return Response(k)
        else :
            reg.user1=="none"
            reg.pass1=str(request.POST['password'])
            reg.email1=str(request.POST['email'])
            reg.Adhar="none"
            reg.save()
            email1=str(request.POST['email'])
            formreq = Dummy()
            formreq.duser1=str(email1)
            formreq.bf=0
            formreq.save()
            li=[]
            li.append(str(email1))
            li.append('ramuklinus369@gmail.com')
            str1='http://ramuk369.pythonanywhere.com/companies/email_verify/'+str(email1)
            spe=send_mail('From sunil',str1,'ramuklinus369@gmail.com',li)
            k=[{"error":"false","dup":0}]
            return Response(k)

    def get(self,request):
        form = LoginForm()
        return render(request, 'companies/login_new.html', {'form': form})


class Loginc(APIView):
    def post(self,request):
        reg=Useer()
        l=Useer.objects.filter(email1=str(request.POST['email']),pass1=str(request.POST['password']))

        if len(l)>=1:
           k=[{"error":1}]
           return Response(k)
        else :
            k=[{"error":0}]
            return Response(k)

    def get(self,request):
        form = LoginForm()
        return render(request, 'companies/login_new.html', {'form': form})

class Logincopy(APIView):
    def post(self,request):
        reg=Useer()
        email2=str(request.POST['email'])
        l=Useer.objects.filter(email1=str(request.POST['email']),pass1=str(request.POST['password']))
        flag=0
        l2=Dummy.objects.all()
        for i in range(len(l2)):
            if email2 == str(l2[i]):
                album1=Dummy.objects.get(pk=l2[i].id)
                if album1.bf==1:
                    flag=1
                    break
        if len(l)>=1 and flag==1:
            k=[{"error":1}]
            return Response(k)
        else:
            k=[{"error":0}]
            return Response(k)
    def get(self,request):
        form = LoginForm()
        return render(request, 'companies/login_new.html', {'form': form})

@login_required
def home(request):
    Problem1 = Stock1.objects.all()
    return render(request,'companies/try1.html',{'Problem': Problem1})
     #return  HttpResponse("Suceesfully logined")

def signup(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            deptid=form.cleaned_data.get('deptid')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('companies:home')
    else:
        form =NewForm()
    return render(request, 'companies/signup.html', {'form': form})


def deleteProblem(request,getPid):
    temp = Stock1.objects.get(pk=getPid)
    temp.delete()
    #Problem1 = Stock1.objects.all()
   # return render(request,'companies/try1.html',{'Problem': Problem1})
    return HttpResponseRedirect('/companies/')
def display(request,getPid):
    temp=Stock1.objects.get(pk=getPid)
    return render(request,'companies/display.html',{'Problem':temp})


def updateStatus(request):
    if request.method == 'POST':
        Status = int(request.POST['status'])
        Pid = int(request.POST['pid'])
        pri=int(request.POST['priority'])
        temp = Stock1.objects.get(pk=Pid)
        temp.status = Status
        temp.priority=pri
        temp.save()
    return HttpResponseRedirect('/companies/')

class ProbList(APIView):
    def get(self,request):
        probs=Stock1.objects.all()
        serializer=ProbSerializer(probs,many=True)
        content={'user_details':serializer.data}
        return Response(content)
    def post(self):
        pass
