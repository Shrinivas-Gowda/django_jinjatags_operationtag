from django.shortcuts import render

# Create your views here.

def forloop(request):
    details={
        'name':'shri',
        'age':22,
        'gender':'male'
    }

    return render(request,'index.html',details)


def ifcond(request):
    d={'a':10,'b':20,'c':30}

    return render(request,'index.html',d)
