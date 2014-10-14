from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.shortcuts import render_to_response
from blogengine.models import Post
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from forms import NewPostForm, CommentForm
from forms import SignUpForm, LoginForm
from models import User,Post,Comment
from django.template.defaultfilters import slugify




def user_login_required(f):
        def wrap(request, *args, **kwargs):
                #this check the session if username key exist, if not it will redirect to login page
                if 'username' not in request.session.keys():
                        return HttpResponseRedirect("/login")
                return f(request, *args, **kwargs)
        wrap.__doc__=f.__doc__
        wrap.__name__=f.__name__
        return wrap

def welcome(request):
    ''' for signup or login '''
    return  render_to_response('welcome.html')

def signUp(request):
    ''' create new user '''
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           
            #print postSlug,post_id
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print name,email,password
            
            
            p = User( user_name = name, email = email, password = password)
            p.save()
            return redirect('/home')

    return render(request,'signin.html',{'form': form})

def logIn(request):
    '''check for usename & password set session username'''
    form = LoginForm()
    if request.method == 'POST':
        
      try:
       
        m = User.objects.get(user_name=request.POST['name'])
        if m.password == request.POST['password']:
            request.session['username'] = m.user_name
            return redirect('/home')
      except User.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")
    
    return render(request,'login.html',{'form': form})


def logOut(request):
    ''' clear session.username'''
    print "in logout"
    try:
        del request.session['username']
    except KeyError:
        pass
    return  render_to_response('welcome.html')


def getPosts(request, selected_page=1):
    ''' lists all blog posts as 3 in one page'''    
    posts = Post.objects.all().order_by('-pub_date')
    pages = Paginator(posts, 3)
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)

    return render_to_response('posts.html', { 'posts':returned_page.object_list, 'page':returned_page})


def getPost(request, postSlug):
    ''' show singlepost and comment form'''
    post = Post.objects.filter(slug=postSlug)
    post_id = post.values_list()[0][0]
    comments = Comment.objects.filter(comment_for_id = post_id)
   
    form = CommentForm() 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print postSlug
            #print postSlug,post_id
            name = form.cleaned_data['name']
            content = form.cleaned_data['comment']
            post_id = post.values_list()[0][0]
            p = Comment( commentor = name, comment_text = content, comment_for_id = post_id)
            p.save()
            #print name,content
    return render(request,'singlepost.html', { 'posts':post,'comments':comments,'form': form})


@user_login_required
def newpost(request):
    ''' create new post'''
    if request.POST == {}:
        form = NewPostForm()
        return render(request,'newpost.html', {'form': form})
    print request
    form = NewPostForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        content = form.cleaned_data['text']
        author_id = 1
        slug = slugify(title)
        p = Post( title = title, text = content, author_id = author_id, slug = slug)
        p.save()
        message = 'sucess'
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)



