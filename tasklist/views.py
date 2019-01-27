from django.shortcuts import render
import datetime

# Create your views here.
from django.shortcuts import render,redirect
from .models import TodoList, Category
def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
          try:  
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            if date == '' :
               date=datetime.datetime.today().strftime('%Y-%m-%d')
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
          except NameError as ec: 
             raise NameError(
            "Please check your values"
             ) from ec
          return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete()
        if "taskEdit" in request.POST: #checking if there is a request to edit a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be edited
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
            context = {
                           "description": todo.title,
                           "date": todo.due_date,
                           "category": todo.category,
                           "content": todo.content,
                      }
            return render(request, "index.html", todo.context)             
            todo.save() #save  todo     

    return render(request, "index.html", {"todos": todos, "categories":categories})