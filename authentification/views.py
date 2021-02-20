from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.views import View
# Create your views here.
from items.models import User

APPLICATION='authentification'

class SignInView(View):
    view_name='signin'
    template=f'{APPLICATION}/{view_name}.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('listitems')

        return render(request,self.template, {})
            

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        US=get_object_or_404(User,username=username, password=password)
        if US is not None:
             login(request,US)
             return redirect('listitems') 

        return redirect('signin')

def logout_view(request):
    logout(request) 
    return redirect('signin')       