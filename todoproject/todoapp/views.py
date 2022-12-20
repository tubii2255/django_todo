from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


# class todocreate(CreateView):
#     model= Task
#     # template_name= 'home.html'
    
#     fields = ['name','priority','date']
#     sucess_url = reverse_lazy('todofn')
    


# class TodoListview(ListView):
#     model=Task
#     template_name='home.html'
#     context_object_name= 'task1'
    
    
    
# class Todoupdate(UpdateView):
#     model= Task
#     template_name='edit.html'
#     context_object_name='task'
#     fields= ['name','priority','date']
#     def get_success_url(self) :
#         return reverse_lazy('todofn')
#         # ,kwargs={'pk':self.object.id}
    

# class tododelete(DeleteView):
#     model= Task
#     template_name= 'delete.html'
#     sucess_url = reverse_lazy('todofn')

# class TodoDetail(DetailView):
    # model = Task
    # template_name = 'home.html'
    # context_object_name = 'task1'


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