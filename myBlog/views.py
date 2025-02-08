from django.shortcuts import render,redirect,get_object_or_404
from .models import UserPost,Catblog,Category
from django.contrib import messages
from django.utils.http import urlencode
from .forms import PostForm,CommentForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    posts = UserPost.objects.all()
    category = Category.objects.filter(status = 0)
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
        'form': form,
        'category':category
    }
    return render(request, 'index2.html', context)






def post_view(request,pk):
    category = Category.objects.filter(status = 0)
    post = get_object_or_404(UserPost,id=pk)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in to send a message.")
            login_url = f"{redirect('new_login').url}?{urlencode({'next': request.path})}"  # Preserve return URL
            return redirect(login_url)
        
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
        'c_form':c_form,
        'category':category
    }
    return render(request,'post_view.html',context)




@login_required
def post_edit(request,pk):
    post = UserPost.objects.get(id = pk)
    category = Category.objects.filter(status = 0)
    if request.method == "POST":
        form = PostForm(request.POST or None,request.FILES or None,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_view',pk=post.id)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form,
        'category':category
    }
    return render(request,'post_edit.html',context)





@login_required
def post_del(request,pk):
    post = get_object_or_404(UserPost,id=pk)
    category = Category.objects.filter(status = 0)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request,'post_del.html',{'post':post,'category':category})

@login_required
def your_post(request):
    category = Category.objects.filter(status = 0)
    blog = UserPost.objects.filter(author = request.user)
    context = {
        'blog':blog,
        'category':category
    }
    return render(request,'your_post.html',context)




def category_view(request,slug):
    category = Category.objects.filter(status = 0)
    categ = Category.objects.filter(slug=slug).first()
    blog = Catblog.objects.filter(category=categ)
    if categ:
        blog = Catblog.objects.filter(category=categ)
    if not categ:  
        return render(request, "category_view.html", {"error": "Category not found"})
    context = {
        'blog':blog,
        "name": categ.slug,
        'category':category
    }        
    return render(request,'category_view.html',context)




def search_results(request):
    category = Category.objects.filter(status = 0)
    query = request.GET.get("q", "").strip()  # Get the search input

    if query:  # If input is not empty
        matching_blog = Catblog.objects.filter(meta_keywords__icontains=query).first()

        if matching_blog:
            category_slug = matching_blog.category.slug  # Get the category slug associated with the blog
            return redirect("category_view", slug=category_slug)  # Redirect to the category page

    # If no blog matches the search keyword, display a "No results" page
    return render(request, "search_results.html", {"message": "No results found",'category':category})

def about(request):
    category = Category.objects.filter(status = 0)
    return render(request,'about.html',{'category':category})




def contact(request):
    category = Category.objects.filter(status = 0)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in to send a message.")
            login_url = f"{redirect('new_login').url}?{urlencode({'next': request.path})}"  # Preserve return URL
            return redirect(login_url)

        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.name = request.user.username
            instance.email = request.user.email 
            instance.save()
            messages.info(request, "Thank you for your interest! We will respond to you shortly.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form,'category':category})


def baseeee(request):
    category = Category.objects.filter(status=0)
    return render(request, 'sidebar.html', {'category': category})