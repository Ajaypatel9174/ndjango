from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def landing(req):
    data={'name':'ajay',
          'email':'ajay@gmail.com',
         
    }
    
    return render(req,'landing.html',data)


def home1(req):
    return redirect('about')

def about(req):
    return HttpResponse("hello.....")


    






