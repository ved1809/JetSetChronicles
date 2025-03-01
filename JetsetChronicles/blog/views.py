from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.models import Post,Category
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    #load all the post from db(10)
    posts= Post.objects.all()[:11]
    #print(posts)
    cats=Category.objects.all()
    data={
        'posts':posts,
        'cats':cats
    }
    return render(request,'home.html',data)



def post(request,url):
    post= Post.objects.get(url=url)
    cats=Category.objects.all()
    # print(post)
    return render(request,'posts.html',{'post':post,'cats':cats})

def category(request,url):
    cat= Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a different page after successful login
            return redirect('/admin')  # Replace 'home' with the URL name of your home page
        else:
            # Handle invalid login credentials
            return render(request, 'logout.html', {'error': 'Invalid username or password.'})
    else:
        # Render the login form for GET requests
        return render(request, 'logout.html')

