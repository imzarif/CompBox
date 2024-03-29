from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Complain
from django.utils import timezone

def home(request):
    return render(request,'complain/home.html')


def mhome(request):
    complains = Complain.objects
    return render(request, 'complain/mhome.html', {'complains': complains})

@login_required()
def create(request):
    if request.method == 'POST':
        if request.POST['address'] and  request.POST['description'] and request.POST['ministry']  and request.FILES['image']:
            complain= Complain()

            complain.address= request.POST['address']
            complain.description = request.POST['description']
            complain.ministry = request.POST['ministry']
            complain.image = request.FILES['image']
            complain.pub_date = timezone.datetime.now()
            complain.user = request.user

            complain.save()
            return redirect('home')

        else:
            return render(request, 'complain/create.html', {'error': 'All fields are required'})

    else:
        return render(request, 'complain/create.html')

@login_required()
def detail(request,complain_id):
    complain=get_object_or_404(Complain,pk=complain_id)
    return render(request,'complain/detail.html',{'complain':complain})


@login_required()
def mdetail(request,complain_id):
    complain=get_object_or_404(Complain,pk=complain_id)
    return render(request,'complain/mdetail.html',{'complain':complain})

@login_required()
def clist(request):
    complains = Complain.objects
    return render(request,'complain/clist.html',{'complains':complains})