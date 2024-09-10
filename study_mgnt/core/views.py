from django.shortcuts import render,redirect,get_object_or_404
from .models import Study
from .forms import StudyForm

def index(request):
    studies=Study.objects.all()
    context={'studies':studies}
    return render(request,'index.html',context)

def edit_study(request, id):
    study = get_object_or_404(Study, pk=id)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = StudyForm(instance=study)
    return render(request, 'edit_study.html', {'form': form})


def Delete_Study(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_studies') 
        Study.objects.filter(id__in=selected_ids).delete()
        data=Study.objects.all()
        context={'studies':data}
        return render(request,'index.html',context)  

def View(request,id):
    data=Study.objects.get(id=id)
    context={'data':data}
    return render(request,'view.html',context)

def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = StudyForm()

    spon = Study.objects.values_list('Sponser_Name', flat=True).distinct()
    return render(request, 'add_study.html', {'form': form,'spon':spon})
