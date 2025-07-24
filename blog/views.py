from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, UserRegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-date_created')  # Get all published posts, ordered by date
    editorschoice= Post.objects.filter(is_editorschoice=True).first()  # Get the first editor's choice post
    context = {
        'posts': posts,
        'editorschoice': editorschoice
    }
    return render(request, 'blog/home.html', context)


def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}. You can now login.")
            return redirect('login')
    else:
        form=UserRegistrationForm()
        context={
            'form':form
        }
        return render(request, 'blog/register.html', context)


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostDetail(DetailView):
    model = Post
    template_name='blog/post_detail.html'
    context_object_name = 'post'

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'blog/post_form.html', context)



class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        
    def form_valid(self, form): # <--- This is the method you need to override for POST logic
        post = self.get_object()

        if post.author != self.request.user:
            messages.error(self.request, 'You do not have permission to delete this post.')
            return redirect('post-detail', pk=post.pk)
        
        # If the user is authorized (is the author or a superuser), proceed with deletion
        return super().form_valid(form) # This will call self.object.delete() and redirect
    
