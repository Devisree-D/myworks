from .forms import FruitAddForm,UserRegisterForm,LoginForm
from django.shortcuts import render,redirect
from Fruits.models import Fruits as FruitsModel
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.generic import TemplateView
from django.urls import reverse_lazy
# Create your views here.

class Fruits(TemplateView):
    model=FruitsModel
    template_name = "fruit/fruitadd.html"
    context = {}
    def get(self, request, *args, **kwargs):
        fruits=self.model.objects.all()
        self.context["fruits"]=fruits
        return render(request,self.template_name,self.context)

class Fruitcreate(TemplateView):
    model=FruitsModel
    form_class=FruitAddForm
    template_name = "fruit/fruitadd.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class()
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render (request,self.template_name,self.context)

class FruitUpdate(TemplateView):
    model = FruitsModel
    form_class = FruitAddForm
    template_name = "fruit/fruitupdate.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        fruit=self.get_object(kwargs["pk"])
        form=self.form_class(instance=fruit)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request, *args, **kwargs):
        fruit=self.get_object(kwargs["pk"])
        form=self.form_class(request.POST,instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request,self.template_name,self.context)

class FruitDetail(TemplateView):
    model=FruitsModel
    template_name = "fruit/fruitview.html"
    context={}
    def get(self, request, *args, **kwargs):
        fruit=self.model.objects.get(id=kwargs["pk"])
        self.context["fruit"]=fruit
        return render(request,self.template_name,self.context)

class Fruitdelete(TemplateView):
    model = FruitsModel
    template_name = "fruit/fruitdelete.html"
    context={}
    def get(self, request, *args, **kwargs):
        fruit=self.model.objects.get(id=kwargs["pk"])
        fruit.delete()
        return redirect("create")

def fruit_create(request):
    form=FruitAddForm()
    context={}
    context["form"]=form
    fruits=FruitsModel.objects.all()
    context["fruits"]=fruits
    if request.method == "POST":
        form = FruitAddForm(request.POST)
        if form.is_valid():
            form.save()
            print("Fruit saved")
            return redirect("create")
        else:
            form = FruitAddForm(request.POST)
            context["form"] = form
            return render(request, "fruit/fruitadd.html", context)


    return render(request, "fruit/fruitadd.html", context)

def fruit_view(request,id):
    fruit=FruitsModel.objects.get(id=id)
    context={}
    context["fruit"]=fruit
    return render(request, "fruit/fruitupdate", context)
def fruit_update(request,id):
    fruit=FruitsModel.objects.get(id=id)
    form=FruitAddForm(instance=fruit)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=FruitAddForm(request.POST,instance=fruit)
        if form.is_valid():
            form.save()
            return redirect("create")
    return render(request, "fruit/fruitupdate", context)

def fruit_delete(request,id):
    fruit=FruitsModel.objects.get(id=id)
    fruit.delete()
    return redirect("create")

def registration(request):
    form=UserRegisterForm()
    context={}
    context["form"]=form

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("registration success")
            return render(request, "fruit/userlog.html")
        else:
            form = UserRegisterForm(request.POST)
            context["form"] = form
            print("registration failed. recheck!")
            return render(request, "fruit/usereg.html", context)
    return render(request, "fruit/usereg.html", context)


def login_view(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return redirect("create")
            else:
                print("login failed")
                return render(request, "fruit/userlog.html", context)

    return render(request, "fruit/userlog.html",context)
def log_out(request):
    logout(request)
    form = LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return redirect("create")
            else:
                print("login failed")
                return render(request, "fruit/userlog.html", context)
    return render(request, "fruit/userlog.html",context)

