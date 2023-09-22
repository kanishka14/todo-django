from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks = Task.objects.filter(is_compleated=False).order_by('-updated_at') # "-" in orderby will order in decending order
    compleated_tasks = Task.objects.filter(is_compleated=True)
    context= {
        'tasks':tasks,
        'compleated_tasks':compleated_tasks,
    }
    return render(request, 'home.html', context)