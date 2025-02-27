from django.shortcuts import render,redirect
from .forms import SignUpForm,EditProfile,EditPro
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from myBlog.models import UserPost,Category
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_login')
    else:
        form = SignUpForm()
    context = {
        'form':form
    }
    return render(request,'User/sign_up.html',context)

class CustomLogout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request,"You have been Logged Out successfully!")
        return super().dispatch(request, *args, **kwargs)
    

@login_required
def userProfile(request):
    if request.method == "POST":
        u_form = EditProfile(request.POST or None,instance=request.user)
        p_form = EditPro(request.POST or None,request.FILES or None,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = EditProfile(instance=request.user)
        p_form = EditPro(instance=request.user.profile)

    blog_count = UserPost.objects.filter(author=request.user).count()
    category = Category.objects.filter(status = 0)
    context = {
        'u_form':u_form,
        'p_form':p_form,
        'blog_count':blog_count,
        'category':category
        
    }
    return render(request,'User/profile.html',context)