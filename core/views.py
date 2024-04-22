from django.shortcuts import render, redirect
from core.models import Todo, Teacher, User
from django.http import HttpResponse
from django.core.exceptions import BadRequest
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView # CRUD views
import datetime
# Create your views here.
# Data Manipulation

def index(request):
    """
    Get all the todos in the application
    """
    todos = Todo.objects.all() # SELECT * FROM Todo -- select everything from todos
    context = {
        "todos_list": todos
    }
    return render(request,"index.html", context)

def display(request):
    return render(request, "index.html")

def create_teacher(request):
    if request.method == "POST":
        teacher = Teacher()
        teacher.first_name = request.POST["first_name"]
        teacher.last_name = request.POST["last_name"]
        teacher.school = request.POST["school"]
        teacher.hire = request.POST["hire_date"]
        teacher.salary = request.POST["salary"]
        teacher.save()
        print(teacher)
        return HttpResponse("Teachers Created Successfully")
    else:
        raise BadRequest()
    
def get_teachers(request):
    teachers = Teacher.objects.all() # SELECT * FROM teachers;
    print(teachers)
    return render(request,"teachers.html",{"teachers":teachers})


def my_todos(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user = request.user) # SELECT * FROM todos WHERE user  = request.user.id
        context = {
            'todos': todos # List[Dict(text,id,user)]
        }
        return render(request,"todos.html",context)
    else:
        return render(request,"not-authenticated.html")
    

def create_todo(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            task = request.POST["task"]
            todo = Todo()
            todo.text = task
            todo.user = request.user
            todo.save()
            return redirect("/todos")
        else:
            return redirect("/todos")
    else:
        return render(request,"not-authenticated.html")
    
def mark_todo(request, id):
    if request.user.is_authenticated:
        todo = Todo.objects.get(id =id)
        if todo.user == request.user:
            todo.completed = True
            todo.save()
        else:
            return render(request,"not-authorized.html")
        return redirect("/todos")
    else:
        return render(request,"not-authenicated.html")
            


class ProfileView(View):
    def get(self,request):
        user = request.user
        context = {
            'user':user # Dict
        }
        return render(request,"profile.html", context)
    


