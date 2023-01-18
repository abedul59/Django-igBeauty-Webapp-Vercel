from django.shortcuts import render
from module import func

# Create your views here.
def showigpic(request):  

    id, Url = func.sendImageURL()      



    return render(request, "showigpic.html", locals())

def index(request):  
     



    return render(request, "index.html", locals())