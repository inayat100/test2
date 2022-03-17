from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .forms import detail_form,user_form,singin_form,post_form
from .models import user_details,Post,Category
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        dd = Post.objects.filter(Publish=True)
        return render(request,'home.html',{'data':dd})
    return redirect('singin')

def singup(request):
    if request.method == 'POST':
        user = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_type = request.POST['User_Type']
        image = request.FILES['image']
        address = request.POST['address']
        if password1 != password2:
            messages.error(request,"both password is not same..")
            return redirect('/')
        us1 = User.objects.create_user(user, email, password1)
        us1.first_name=fname
        us1.last_name=lname
        us1.save()
        user = User.objects.get(username=user)
        us2 = user_details(user=user,User_Type=user_type, image=image, address=address)
        us2.save()
        messages.success(request,"singup successfully")
        return redirect('singin')
    return render(request,'singup.html',{'user_form':user_form,'detail_form':detail_form})

def singin(request):
    if request.method == "POST":
        username = request.POST['User_name']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "login successfully")
            return redirect('profile')
        else:
            messages.error(request, "something is wrong input")
            return redirect('/')
    else:
        fm = singin_form
        return render(request,'singin.html',{'form':fm})

def profile(request):
    if request.user.is_authenticated:
         us = User.objects.get(username=request.user)
         us1 = user_details.objects.get(user=request.user)
         print(us1)
         return render(request, 'dash.html', {'user': us, 'detail': us1})
    else:
        messages.warning(request,"you should have an authenticated user")
        return redirect('singin')

def post(request):
    if request.user.is_authenticated:
        obj = user_details.objects.get(user=request.user)
        chek = obj.User_Type
        if chek == 'Doctor':
            if request.method == "POST":
                title = request.POST.get('title')
                image = request.FILES.get('image')
                category = request.POST.get('category')
                summary = request.POST.get('summary')
                Publish = request.POST.get('Publish')
                content = request.POST.get('content')
                if Publish:
                    Publish = True
                else:
                    Publish = False
                c = Category.objects.get(pk=category)
                sb = Post(user=request.user,title=title,image=image,category=c,summary=summary,content=content,Publish=Publish)
                sb.save()
                return redirect('/')
            return render(request,'post.html',{'fm':post_form})
        else:
            messages.warning(request,"you are not a doctor")
            return redirect('/')
    else:
        messages.warning(request,"you should have an authenticated user")
        return redirect('singin')

def Up_post(request):
    if request.user.is_authenticated:
        obj = user_details.objects.get(user=request.user)
        chek = obj.User_Type
        if chek == 'Doctor':
            dd = Post.objects.filter(user=request.user,Publish=True)
            return  render(request,'showpost.html',{'data':dd})
        else:
            messages.warning(request, "you are not a doctor")
            return redirect('/')
    else:
        messages.warning(request,"you should have an authenticated user")
        return redirect('singin')

def Df_post(request):
    if request.user.is_authenticated:
        obj = user_details.objects.get(user=request.user)
        chek = obj.User_Type
        if chek == 'Doctor':
            dd = Post.objects.filter(user=request.user,Publish=False)
            return  render(request,'drf.html',{'data':dd})
        else:
            messages.warning(request, "you are not a doctor")
            return redirect('/')
    else:
        messages.warning(request,"you should have an authenticated")
        return redirect('singin')

def pub(request,pk):
    if request.user.is_authenticated:
        obj = user_details.objects.get(user=request.user)
        chek = obj.User_Type
        if chek == 'Doctor':
            obj = Post.objects.get(pk=pk)
            fm = post_form(instance=obj)
            if request.method == "POST":
                title = request.POST.get('title')
                image = request.FILES.get('image')
                category = request.POST.get('category')
                summary = request.POST.get('summary')
                Publish = request.POST.get('Publish')
                content = request.POST.get('content')
                if Publish:
                    Publish = True
                else:
                    Publish = False
                obj.title = title
                if image:
                    obj.image = image
                c = Category.objects.get(pk=category)
                obj.category = c
                obj.summary = summary
                obj.Publish = Publish
                obj.content = content
                obj.save()
                return redirect('show_post')
            return render(request,'pub.html',{'fm':fm})
        else:
            messages.warning(request, "you are not a doctor")
            return redirect('/')
    else:
        messages.warning(request,"you should have an authenticated user")
        return redirect('singin')

def full_post(request,pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        return render(request,'fullpost.html',{'post':post})
    else:
        messages.warning(request, "you should have an authenticated user")
        return redirect('singin')

def user_logout(request):
    logout(request)
    messages.success(request,"User successfully Logout... ")
    return redirect('/')