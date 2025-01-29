from django.shortcuts import render,redirect,get_object_or_404
from .models import UserPost
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    posts = UserPost.objects.all()
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
        else:
            print("Form errors:", form.errors)  # Debugging
    
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'index.html', context)





@login_required
def post_view(request,pk):
    post = get_object_or_404(UserPost,id=pk)
    if request.method == "POST":
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('post_view',pk=post.id)
    else:
        c_form = CommentForm()


    context={
        'post':post,
        'c_form':c_form
    }
    return render(request,'post_view.html',context)




@login_required
def post_edit(request,pk):
    post = UserPost.objects.get(id = pk)
    if request.method == "POST":
        form = PostForm(request.POST or None,request.FILES or None,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_view',pk=post.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request,'post_edit.html',context)





@login_required
def post_del(request,pk):
    post = get_object_or_404(UserPost,id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request,'post_del.html',{'post':post})

@login_required
def your_post(request):
    blog = UserPost.objects.filter(author = request.user)
    context = {
        'blog':blog
    }
    return render(request,'your_post.html',context)


