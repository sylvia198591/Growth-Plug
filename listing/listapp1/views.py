
from django.http import JsonResponse
from django.shortcuts import *
from django.views.generic import *
from django.urls import *
from listapp1.models import *
from listapp1.forms import *

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser, FileUploadParser
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from listapp1.models import *
from listapp1.serializers import *
import pyfacebook
# api=pyfacebook.Api(app_id="2773352989611930",app_secret="a5ceb9b7b928c55fd1f7922dc3737a33",application_only_auth=True)
# access_token=api.get_app_token(return_json=True)['access_token']
# print(api)
# print(api.get_app_token(return_json=True))
# print(access_token)
from facebook import GraphAPI
# graph=GraphAPI(access_token="EAAnaWYZCIV5oBAMtZCNEuMwsLpboSnyqLKRZBLyZBO3yGa3NZChXiZBoXV9LSEBkJn9REQMGGgGkom3aP6bOAbZAvpKZAVq8fejDUWmxv4ZAZAZAgWQJCM909dpVSAITZAWiX2ksNdpsZAbESSYaXnXiEuNexmwBTcORpmr5QWlkGyBEwYAs4EWSfLYOJANTKkBahpELdN3LwYAgIYgZDZD")
# objects1=graph.get_object("me",fields="accounts")
# user=graph.get_object("me",fields="id,name")
# print(user)
# userid=user['id']
# for page in objects1['accounts']['data']:
#     page_access_token=page['access_token']
#     pageid=page['id']
#     pagename=page['name']
#     pagecategory=page['category']
#     api=pyfacebook.Api(app_id="2773352989611930",app_secret="a5ceb9b7b928c55fd1f7922dc3737a33",short_token=page_access_token)
#     print(page_access_token,pageid,pagename,pagecategory)
#     print(api.get_page_info(page_id=pageid,return_json=True))
#     # qs1 = pgdtl.objects.create(pagename=pagename, pageid=pageid, pagecategory=pagecategory)
#     qs1=pgdtl(pagename=pagename, pageid=pageid, pagecategory=pagecategory)
#     print("d1")
#     # form.save(commit=False)
#     print("d2")
#     qs1.save()
class viewpgdtl(TemplateView):
    # graph = GraphAPI(\
    #     access_token="EAAnaWYZCIV5oBAMtZCNEuMwsLpboSnyqLKRZBLyZBO3yGa3NZChXiZBoXV9LSEBkJn9REQMGGgGkom3aP6bOAbZAvpKZAVq8fejDUWmxv4ZAZAZAgWQJCM909dpVSAITZAWiX2ksNdpsZAbESSYaXnXiEuNexmwBTcORpmr5QWlkGyBEwYAs4EWSfLYOJANTKkBahpELdN3LwYAgIYgZDZD")
    #
    # model_name=pgdtl
    # template_name = "listapp1/pgdtlview.html"
    # objects1=graph.get_object("me",fields="accounts")
    # user=graph.get_object("me",fields="id,name")
    # print(user)
    # userid=user['id']
    # for page in objects1['accounts']['data']:
    #     page_access_token = page['access_token']
    #     pageid = page['id']
    #     pagename = page['name']
    #     pagecategory = page['category']
    #     api = pyfacebook.Api(app_id="2773352989611930", app_secret="a5ceb9b7b928c55fd1f7922dc3737a33",
    #                          short_token=page_access_token)
    #     print(page_access_token, pageid, pagename, pagecategory)
    #     print(api.get_page_info(page_id=pageid, return_json=True))
    #     qs1 = pgdtl(pagename=pagename, pageid=pageid, pagecategory=pagecategory)
    #     qs1.save()
    model_name = pgdtl
    template_name = "listapp1/pgdtlview.html"
    def get(self, request, *args, **kwargs):
        # qs = Employee.objects.all()
        # form.fields['Paymode'].queryset = Account.objects.filter(Username=request.session["Username"])
        # objects1 = graph.get_object("me", fields="accounts")
        # user = graph.get_object("me", fields="id,name")
        # print(user)
        # userid = user['id']

        #
        graph = GraphAPI( \
            access_token="EAAnaWYZCIV5oBADaPaZAYHl7ovqdV0yKGVtZCWitnYYLagFbiWTstwGC5GKqqHLWL5yiBcMCLyIzeTlQc3J8XEOjNZAx0CC2Ov2p6mpO7yrud8zWkQyFnI9AnmyxRtbbmrzHiLLZB8OWkAT7lldPDPNBej8pgnFZAltsWB9FMVaHewhZCA45zirgRLr5ZCd0yVv100ZAFDloJywZDZD")


        objects1 = graph.get_object("me", fields="accounts")
        user = graph.get_object("me", fields="id,name")
        print(user)
        print("pggg")
        userid = user['id']
        context = {}
        dict={}
        # context=0
        for page in objects1['accounts']['data']:
            # print(page)
            page_access_token = page['access_token']
            pageid = page['id']
            pagename = page['name']
            pagecategory = page['category']
            api = pyfacebook.Api(app_id="2773352989611930", app_secret="a5ceb9b7b928c55fd1f7922dc3737a33",
                                 short_token=page_access_token)
            print(page_access_token, pageid, pagename, pagecategory)
            print(api.get_page_info(page_id=pageid, return_json=True))
            print("aaa111")
            # q=pgdtl.objects.all()
            q = pgdtl.objects.filter(pageid=pageid).count()
            # print("Hi")
            # print("Active:", qs.isActive)
            if ((q ==0)):
            # def post(self, request, *args, **kwargs):

                qs1 = pgdtl.objects.create(pagename=pagename, pageid=pageid, pagecategory=pagecategory)
                qs1.save()
                print("aaaaaaaasave")

            qs=pgdtl.objects.all()

            context['viewpgdtl'] = qs


        return render(request, self.template_name, context)
class fbupdate(TemplateView):

    model_name = pgdtl
    form_class=fbupdateform
    template_name = "listapp1/fb_update.html"
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        p_k=self.kwargs.get('pk')
        form = self.form_class(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]

            graph = GraphAPI( \
                access_token="EAAnaWYZCIV5oBADaPaZAYHl7ovqdV0yKGVtZCWitnYYLagFbiWTstwGC5GKqqHLWL5yiBcMCLyIzeTlQc3J8XEOjNZAx0CC2Ov2p6mpO7yrud8zWkQyFnI9AnmyxRtbbmrzHiLLZB8OWkAT7lldPDPNBej8pgnFZAltsWB9FMVaHewhZCA45zirgRLr5ZCd0yVv100ZAFDloJywZDZD")


            objects1 = graph.get_object("me", fields="accounts")
            user = graph.get_object("me", fields="id,name")
            print(user)
            print("pggg")
            userid = user['id']
            context = {}
            dict={}
            # context=0
            for page in objects1['accounts']['data']:
                # print(page)
                page_access_token = page['access_token']
                pageid = p_k
                pagename = page['name']
                pagecategory = page['category']
                api = pyfacebook.Api(app_id="2773352989611930", app_secret="a5ceb9b7b928c55fd1f7922dc3737a33",
                                     short_token=page_access_token)
                print(page_access_token, pageid, pagename, pagecategory)
                print(api.get_page_info(page_id=p_k, return_json=True))
                print("aaa111")

                # def post(self, request, *args, **kwargs):
                subgraph = GraphAPI(access_token=page_access_token)
                subgraph.put_object(pageid, "feed", message=f'{message} {pagename}')
                return redirect("pgdtl_view")


class createEmployee(TemplateView):
    form_class=Employeecreateform
    model_name=Employee
    template_name = "listapp1/Employeecreate.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data["Name"]
            Telephone = form.cleaned_data["Telephone"]
            Age = form.cleaned_data["Age"]
            # if 'Profile_pic' in request.FILES:
            #     Profile_pic = request.FILES['Profile_pic']
            # Profile_pic = form.cleaned_data["Profile_pic"]
            Email = form.cleaned_data["Email"]
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            # isActive=True
            qs = Employee.objects.create(Name=Name, Telephone=Telephone,Age=Age,\
                    Email=Email,Username=Username,Password=Password,isActive=True)
            print("d1")
            # form.save(commit=False)
            print("d2")
            qs.save()
            print("d3")
            return JsonResponse({"message": "loginSuccess", 'status': 200})

        else:
            return render(request, self.template_name,{"form":form})

class loginEmployee(TemplateView):
    form_class=Employeelogin
    model_name=Employee
    template_name = "listapp1/Employeelogin.html"
    template_name1 = "listapp1/home.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        print("Hi0000")
        if form.is_valid():
            print("Hi1111")
            Username = form.cleaned_data["Username"]
            Password = form.cleaned_data["Password"]
            qs=Employee.objects.get(Username=Username)
            print("Hi")
            print("Active:",qs.isActive)
            if((qs.Username==Username)&(qs.Password==Password)):
                request.session['Username']=Username
                context = {}
                context["qs"] = qs
                print(qs)
                print(context)
                # context["user"] = user
                print("hiiiiiiiiiiiiii")
                return render(request, self.template_name1, context)
                # return HttpResponseNotFound('<h1>Page not found</h1>')
            else:
                print("Hi2222")
                return redirect("User_login")
                # return HttpResponse('<h1>Page was not found</h1>')

        else:
            print("Hi33333")
            return render(request, self.template_name,{"form":form})

class viewEmployee(TemplateView):
    model_name=Employee
    template_name = "listapp1/Employeeview.html"
    # Username = request.session["Username"]
    # def get_queryset(self):
    #
    #     return self.model_name.objects.filter(Username=request.session["Username"])
    def get(self, request, *args, **kwargs):
        # form.fields['Paymode'].queryset = Account.objects.filter(Username=request.session["Username"])
        qs=Employee.objects.all()
        print("ddddd")
        context={}
        print(context)
        context["viewemployee"]=qs
        print(context)
        return render(request,self.template_name,context)

def logoutEmployee(request):
        del request.session['Username']
        return redirect("Employee_login")
class updateEmployee(UpdateView):
    model=Employee
    fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password"]
    success_url = '/Employeeview'
    # success_url = reverse_lazy('getRes')
    #context_object_name = "form"
    template_name = 'listapp1/Employee_update.html'
class deleteEmployee(DeleteView):
    model = Employee
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    fields = ["Name", "Telephone", "Age",  "Email", "Username", "Password"]
    # template_name_suffix = "_del"
    success_url = '/Employeeview'
class EmployeeList(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self,request):
        serializer = EmployeeSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.data, status=400)

class EmployeeListCreateAPIView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    serializer_class =  EmployeeSerializer
    queryset = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        documents = Employee.objects.all()
        serializer = EmployeeSerializer(documents,many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)