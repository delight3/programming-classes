from django.shortcuts import render
from .models import Posts
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView)
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'core/index.html', context)

# create a Listview details to list the  posts and display the post details
# use class because this is a class base view
class PostListView(ListView):
    model = Posts
    template_name = 'core/index.html'
    context_object_name = 'posts'

 
# display post details
class PostDetailView(DetailView):
    model = Posts 
     
class PostCreateView(LoginRequiredMixin, CreateView):
    model =  Posts
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def text_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView ):
    model = Posts
    success_url = '/'
    
    def text_func(self):  # to prevent a user from deleting other users post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
           
    
    
    
         