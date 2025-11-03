from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def select1(req):
    print("hello")
    print(req.method)
    print(req.GET)

    x=req.GET.get('selectoption')
    print(x)
    

    # return render(req,'select1.html')
def radio(req):
     return render(req,'radio.html')



def radio1(req):
    print("hello")
    print(req.method)
    print(req.GET)

    x=req.GET.get('gender')
    print(x)

def form(req):
    return render(req,'form.html')

def form1(req):
    print("hello")
    print(req.FILES)
    print(req.GET)
    print(req.COOKIES)
    print(req.META)
    print(req.POST)

    n = req.POST.get('name')
    e = req.POST.get('email')
    nm = req.POST.get('number')
    i = req.FILES.get('image')
    v = req.FILES.get('video')
    a = req.FILES.get('audio')

    print(n,e,nm,i,v,a),
    


