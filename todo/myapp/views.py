from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Task

# Create your views here.

def task_list(request):
    tasks=Task.objects.all()
    return render(request,'task_list.html',{'tasks':tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        is_completed = request.POST.get('is_completed') == 'on'
        task = Task(title=title, description=description, due_date=due_date, is_completed=is_completed)
        task.save()
        return redirect('task_list')
    return render(request,'task_form.html')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'delete_task.html', {'task': task})
