from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import requests
import os
from urllib.parse import urlencode
# Create your views here.

def home(request):
    return render(request,'Home.html')


def About(request):
    return render(request,'About.html')

def memeDeatails(request):
    
    
    if(request.method=='POST'):
        template_id=request.POST['id']
        t1=request.POST['t1']
        t2=request.POST['t2']
        t3=request.POST['t3']
        t4=request.POST['t4']
       
                
         
     
 
        params = {
    "template_id": template_id,
    "username": "MemeSachin",
    "password": "Meme@2023",
   
    
    "boxes[0][type]": "text",
    "boxes[0][text]":t1,
    "boxes[0][font]": "arial",
  
   
    "boxes[1][type]": "text",
    "boxes[1][text]":t2,
    "boxes[1][font]": "arial",
    
    "boxes[2][type]": "text",
    "boxes[2][text]":t3,
    "boxes[2][font]": "arial",
    
    
    "boxes[3][type]": "text",
    "boxes[3][text]":t4,
    "boxes[3][font]": "arial",

}

        
        
     
        Result=requests.post('https://api.imgflip.com/caption_image',data=params)
        
        Response=Result.json()

        Link=Response['data']['url']
        
        
        
        # Download the image data from the URL
        response = requests.get(Link)
        image_data = response.content
        


        # Create a temporary file to store the image data
        tmp_filename = 'temp.png'
        with open(tmp_filename, 'wb') as f:
            f.write(image_data)

        # Return the image as a file download response
        response = FileResponse(open(tmp_filename, 'rb'), as_attachment=True, filename=os.path.basename(Link))
        return response  
        

    return render(request,'Edit.html')    
    
    




def editmeme(request):
    template_id =request.GET['id']
    print(template_id)
    context={
        'meme_id':template_id
    }
    return render(request,'Edit.html',context=context)
   
   
   
 
def create(request):
    r=requests.get('https://api.imgflip.com/get_memes')
   

   #define a dict name as context define data as form 
   # in json format and send to html direct using inbuilt varible 
   #name as a context
   
    context={
        'meme_data':r.json()['data']['memes']
    }

  
    return render(request,'create.html',context=context)    



