from django.shortcuts import render

def index(request):
    return render(request, 'build/index.html')

def adduser(request):
    print("golu")
    username=request.POST["username"]
    email=request.POST["email"]
    pwd=request.POST["pwd"]
    
    event_obj=users(username=username,email=email,pwd=pwd)
    event_obj.save()
   
    return redirect("/")

