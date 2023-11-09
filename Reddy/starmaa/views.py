from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import *

import random


def working(request):

    return HttpResponse('working')


def coin_toss(request):
    context = {'result': None}
    if request.method == "POST":
        output = random.choice(['Heads', 'Tails'])
        
        context = {'result': output,}
    
        

    return render(request, 'Toss.html', context=context)



def people_view(request):
    if request.method == "POST":
        data = request.POST
        fname = data['fname']
        lname = data['lname']
        image = request.FILES.get('image')

        
        People.objects.create(fname=fname,lname=lname,image=image)

        return redirect("/people_view")


    people = People.objects.all()

    context = {'people':people,'a':'abhi_new_contest'}
    return render(request,"People.html",context)
