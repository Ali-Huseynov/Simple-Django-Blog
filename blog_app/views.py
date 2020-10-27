from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,get_list_or_404 , Http404
from django.http import HttpResponseNotFound
from django.views.generic import  ListView, DetailView , CreateView, UpdateView , DeleteView 
from .models import Post , Category ,Comments
from .forms import PostForm,UpdateForm,CreateCommentForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime
from users.models import Profile


# Add User profile


@login_required(login_url='login')
def LikePostView(request,pk):

    post = get_object_or_404(Post, id = pk)

    if post.likes.filter(id=request.user.id):   # also can use  '.exists()'
        post.likes.remove(request.user)
    elif post.unlikes.filter(id=request.user.id) :
        post.likes.add(request.user)
        post.unlikes.remove(request.user)
    else:
        post.likes.add(request.user)


    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))


@login_required(login_url='login')
def UnlikePostView(request,pk):

    post = get_object_or_404(Post, id = pk)

    if post.unlikes.filter(id=request.user.id):
        post.unlikes.remove(request.user)
    elif post.likes.filter(id=request.user.id):
        post.unlikes.add(request.user)
        post.likes.remove(request.user)
    else:
        post.unlikes.add(request.user)


    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))


@login_required( login_url='login' )
def CreateCommentView(request , pk):
    
    if request.method == 'POST':
        
        form = CreateCommentForm( request.POST )
        
        if form.is_valid():
            post = get_object_or_404( Post , pk = pk  )

            comment = Comments.objects.create( author = request.user , body= form['body'].value() , post = post , date_time= datetime.now() )

            comment.save()

            return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))
        else:
            raise Http404
    else:
        raise Http404



class LikeListView(ListView):
    model = Post
    template_name = 'blog_app/like_list.html'
    
    def get_queryset(self):
        
        post = get_object_or_404(Post , pk = self.kwargs['pk'] )

        return post.likes.all()


class UnlikeListView(ListView):
    model = Post
    template_name = 'blog_app/like_list.html'
    
    def get_queryset(self):
        
        post = get_object_or_404(Post , pk = self.kwargs['pk'] )

        return post.unlikes.all()



class HomeView(ListView):
    
    model = Post
    template_name = 'blog_app/home.html'
    ordering = ['-date_time']

    paginate_by = 6

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # ip = get_client_ip(self.request)[0]
        # context['ip'] = ip

        

        context['category_list'] = Category.objects.all()
        
        return context


class CategoryView(ListView):

    template_name = 'blog_app/category.html' # here still you can use 'home.html' 
    paginate_by = 2

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['category_list'] = Category.objects.all()
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, name= ( self.kwargs['categ'])  ) # you can also slugify it and add    ( ' '.join( self.kwargs['categ'].split('-') ).title()  ) )
        return Post.objects.filter(category=self.category).order_by('-date_time')



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = get_object_or_404(Post, id = self.kwargs['pk'] )

        context['form'] = CreateCommentForm

        if post.likes.filter(id= self.request.user.id):
            context['like_color'] = 'green'
            context['unlike_color'] = 'gray'
        elif post.unlikes.filter(id= self.request.user.id):
            context['like_color'] = 'gray'
            context['unlike_color'] = 'red'
        else:
            context['unlike_color'] = 'gray'
            context['like_color'] = 'gray'

        return context



class AddPostView(LoginRequiredMixin,CreateView):
    login_url = 'login'

    model = Post
    form_class = PostForm
    template_name = 'blog_app/add_post.html'
    #fields = '__all__'
    #fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = 'login'

    model = Post
    form_class = UpdateForm
    template_name = 'blog_app/update_post.html'

    def test_func(self):
        post = self.get_object()
        return (self.request.user == post.author)


class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    login_url = 'login'

    model = Post
    template_name = 'blog_app/delete_post.html'

    success_url = reverse_lazy('home') # 1 method
    #def get_success_url(self, **kwargs): # 2 method
    #    return reverse('home')

    def test_func(self):
        post = self.get_object()
        return (self.request.user == post.author)


