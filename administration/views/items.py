from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib import messages

import cloudinary
from items.models import Item,ItemImage

APPLICATION="administration"

class ItemsView(View):
    view_name='items'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        context={
            'items':Item.objects.all()
        }
        return render(request, self.template,context)


class ItemView(View):
    view_name='item'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        item_reference=kwargs.get('item_reference')
        context={
            'item':get_object_or_404(Item,reference=item_reference)
        }
        return render(request, self.template,context)
        
class CreateItemView(View):
    view_name='createitem'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
        
    def post(self, request, *args, **kwargs):
        title=request.POST.get('title')
        big_desc=request.POST.get('big_desc')
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        image3=request.FILES['image3']
        image4=request.FILES['image4']
        image5=request.FILES['image5']
        try:
            images=[image1,image2,image3,image4,image5]
            urls=[]
            item=Item.objects.create(title=title,big_desc=big_desc)
            for image in images:
                response=cloudinary.uploader.upload(image)
                urls.append(response['secure_url'])
            for url in urls:
                ItemImage.objects.create(item=item,image=url,miniature=urls[0])  
        except:
            redirect('createitem')
            messages.error(request,'error from backend')  


        messages.success(request,'item added successfuly')  
        return redirect('listitems')


class UpdateItemView(View):
    view_name='updateitem'
    template=f'{APPLICATION}/items/{view_name}.html'    
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
        

    def post(self, request, *args, **kwargs):


        messages.success(request,'item updated successfuly')
        return HttpResponse('POST request!')

class DeleteItemView(View):
    def get(self, request, *args, **kwargs):
        item_reference=kwargs.get('item_reference')
        item=get_object_or_404(Item,reference=item_reference)
        item.delete()
        messages.success(request,'item deleted successfuly')
        return redirect('listitems')

