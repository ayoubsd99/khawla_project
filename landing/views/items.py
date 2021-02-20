from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse
import simplejson as JSON
from django.core.mail import send_mail
from django.contrib import messages

from project.settings import EMAIL_HOST_USER
from items.models import Item,ItemImage
APPLICATION='landing'

class HomeView(View):
    view_name='home'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template)
        
class AboutView(View):
    view_name='about'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
        

        
class ContactView(View):
    view_name='contact'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(request.POST)
        send_mail(
        name,
        message,
        email,
        [EMAIL_HOST_USER],
        fail_silently=False,
        )
        messages.success(request,'email send successfuly')
        return redirect('contact')    



class CatalogView(View):
    view_name='catalog'
    template=f'{APPLICATION}/items/{view_name}.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template)


class ItemView(View):
    view_name='item'
    template=f'{APPLICATION}/items/{view_name}.html'    
    def get(self, request, *args, **kwargs):
        return render(request, self.template)


@csrf_exempt
def send_email(request):

    return redirect('home')

def item_data(item):
    image=ItemImage.objects.filter(item=item)[0]
    return{
        'reference':item.reference,
        'title':item.title,
        'big_desc':item.big_desc,
        'miniature':image.miniature,
    }
@csrf_exempt
def items_list(request):
    data={}
    items_list=[]
    items_data=Item.objects.filter(deleted=False)

    for item in items_data:
        items_list.append(item_data(item))
    data['items']=items_list
    data['response_code']=0  
    return HttpResponse(JSON.dumps(data))
