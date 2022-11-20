from django.shortcuts import redirect, render
from .models import Task
from .forms import TodoForm
def todofn(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    task1=Task.objects.all()
        
    return render(request,'home.html',{'task1':task1})
# Create your views here.
def deletefn(request,tid):
    task=Task.objects.get(id=tid)
    
    if request.method=='POST':
        de=Task.objects.get(id=tid)
        de.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    to=TodoForm(request.POST or None , instance=task)
    if to.is_valid():
        to.save()
        return redirect('/')
    return render(request,'edit.html',{'to':to,'task':task})