from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist.models import Tasklist
from todolist.Form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
def todolist(request):
    if request.method=='POST':
        form=TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'New Task Added!')
        return redirect('todolist')
    else:
       all_task=Tasklist.objects.all()
       paginator=Paginator(all_task,5)
       page=request.GET.get('pg')
       all_task=paginator.get_page(page)

       return render(request,'todolist.html',{'mt':all_task})
def index(request):
    return render(request,'index.html',{'mt':'Home'})
def about(request):

    return render(request,'ab.html',{'mt':'about'})
def delete_task(request,task_id):
    task=Tasklist.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')
def edit_task(request,task_id):
    if request.method=='POST':
        task = Tasklist.objects.get(pk=task_id)
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'New Task Edited!')
        return redirect('todolist')
    else:
       all_task=Tasklist.objects.get(pk=task_id)

       return render(request,'edit.html',{'mt':all_task})
def complete_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done=True
    task.save()
    return redirect('todolist')
def pending_task(request,task_id):
    task = Tasklist.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')
def contact(request):

    return render(request,'tell.html',{'mt':'contact'})


# Create your views here.
