from django.shortcuts import render
from .forms import FileForm,BindingForm
from .models import files,Binding

from django.core.files.storage import FileSystemStorage
import random
import string
# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the main index.")
    
        
    return render(request, 'index.html' )
def randString(length=10):
    #put your letters in the following string
    your_letters='1abcdef2ghi3jklmnopq5rstuv9wx4yzABCDE6FGHIJK8LMNOPQRSTU7VWXYZ_-0'
    return ''.join((random.choice(your_letters) for i in range(length)))

def panel(request):
    #return HttpResponse("Hello, world. You're at the main index.")
    context = {"panel_page": "active"} # new info here
    return render(request, 'panel.html',context)
def table(request):

    if request.method == 'POST': 
        print("in Post method ---------------------------->")
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            from .models import files
            #student.fname=request.POST.get('fname')
            #60iSm9Bzm0c
            fs_doc = FileSystemStorage(location='/media/doc')
            
            filen = request.FILES['file']
             
            print('--',filen.name)
            print(filen.size)
            name = fs_doc.save(filen.name, filen)

             
            print((randString()))
            files=files()
            files.title=filen.name
            files.file=filen
            print(files.file)
            files.size=filen.size
            files.user_id=random.randrange(20, 50, 3)
            #xx=SimpleUploadedFile(request.FILES.values)
            #print(xx)
            
            files = files.save()
            data = {'is_valid': True}#, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}

        return render(request,"table.html")
    else:
        from .models import files
        files_list = files.objects.all()
        xfile = FileForm() 
        print(xfile.media) 
        context = {"table_page": "active", "form":xfile,"files_list":files_list}
        print("In the get method--------------")
        return render(request,"table.html",context)
   # return render(request,"table.html")

    
