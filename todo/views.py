from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Todo

# Display the Todo list
def todo_list(request):
    todos = Todo.objects.all()  # Fetch all Todo items from the database
    return render(request, 'todo/todo_list.html', {'todos': todos})

# Add a new Todo
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todo(title=title, description=description)
        todo.save()
        return redirect('todo_list')  # Redirect to the todo list page after adding
    return render(request, 'todo/add_todo.html')

# Mark a Todo as complete
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

