from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import EmployeeForm,EmployeeModelForm,RegistrationForm,LoginForm
from crm.models import Employees
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout 
# Create your views here.
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeModelForm()
        return render(request,"emp_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"employee has been added")
            # Employes.objects.create(**form.cleaned_data)
            print("created")
            return render(request,"emp_add.html",{"form":form})
        else:
            messages.error(request,"failed to add employee")
            return render(request,"emp_add.html",{"form":form})




            

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})


class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        return render(request,"emp_list.html",{"data":qs})

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):                    #localhost:8000/employees/{id}/change
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        #messages.success(request,"employee removed")
        return redirect("emp-all")

class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        form=EmployeeModelForm(instance=obj)
        return render(request,"emp_edit.html",{"form":form})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employees.objects.get(id=id)
        #messages.success(request,"employee changed")
        form=EmployeeModelForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            Employees.objects.create(**form.cleaned_data)
            print("updated")
            return redirect("emp-all")
        else:
            messages.error(request,"failed to change")
            return render(request,"emp_add.html",{"form":form})

#class SignUpView(View):
 #   def get(self,request,*args,**kwargs):
  #      form=RegistrationForm()
    #    return render(request,"register.html",{"form":form})
   # def post(self,request,*args,**kwargs):
     #   form=RegistrationForm(request.POST)
   # if form.is_valid():
    #    User.objects.create_user(**form.cleaned_data)
     #   form.save()
      #  messages.success(request,"Account has been created")
          
       # return render(request,"register.html",{"form":form})
   # else:
    #    messages.error(request,"Failed to create account")
            
     #   return render(request,"register.html",{"form":form})

#class SignInView(View):
 #   def get(self,request,*args,**kwargs):
  #      form=LoginForm()
   #     return render(request,"login.html",{"form":form})
    #def post(self,request,*args,**kwargs):
     #   form=LoginForm(request.POST)

        #if form.is_valid():
         #   u_name=form.cleaned_data.get("username")
          #  pwd=form.cleaned_data.get("password")
           # print(u_name,pwd)
          #  user_obj=authenticate(request,username=u_name,password=pwd)
           # if user_obj:
            #    print("valid credential")
             #   login(request,user_obj)
              #  return redirect("emp-lst")

#        messages.error(request,"invalid credential")


#class SignOutView(View):
 #     def get(self,request,*args,**kwargs):
  #      logout(request)
   #     return redirect("signin")