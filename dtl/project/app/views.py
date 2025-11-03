from django.shortcuts import render

# Create your views here.

def home(req):
    data ={'name':'Ajay',
           'email':'ajay@gmail.com',
             'l':['python','java','php'] }
            
    return render(req,'home.html',data)

    
