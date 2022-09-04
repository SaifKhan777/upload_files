from django.shortcuts import render , redirect, HttpResponse
from datetime import datetime
from .models import Data
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages
# Create your views here.
def index(request):
        list = Data.objects.all()
        return render (request, 'index.html',
        {'list': list})    


def addfile(request):
    if request.method=="POST":
        username = request.POST.get('username')
        filename = request.POST.get('filename')
        addedfiles = request.FILES.get('addedfiles')
        

        adding_file= Data(username=username,filename=filename,addedfiles=addedfiles,date=datetime.today())
        adding_file.save()

        

    return render(request,"addfile.html")   

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exixts(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/addedfiles")
            response['contents-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

def deletefile(request):
    if request.method=="POST":
        username = request.POST.get('username')
        filename = request.POST.get('filename')
        # deletefiles = Data(username=username, filename=filename)
        # deletefiles.delete()
        Data.objects.filter(username=username, filename=filename).delete()
    return render (request, 'deletefile.html')


def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username,email,password)
        myuser.name = username
        myuser.save()
        return redirect('home')
    else:
        return HttpResponse('404 -not found')   


def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username= loginusername, password=loginpassword)
        if user is not None:
            login(request)
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return render(request, "login.html")

def logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

