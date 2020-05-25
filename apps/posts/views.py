from django.shortcuts import render,redirect
from django.views.generic import View, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

# class HomeView(LoginRequiredMixin,ListView):
#     model = Post
#     template_name = 'posts/index.html'
#     context_object_name = 'posts'
#     ordering = ['-date']
#     paginate_by = 20
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = PostForm()
#         context = {
#             'form':form
#         }
#         return context
    
class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        postsss = Post.objects.all()
        form = PostForm()
        titles = Post.objects.all().order_by('id')[:10]
        page = request.GET.get('page', 1)
        paginator = Paginator(postsss, 10)

        count = Post.objects.all().count()
        if count>10:
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
        else:
            posts = postsss
        context={
            'posts':posts,
            'form':form,
            'titles':titles,
            'paginator':paginator,
        }
        return render(request, 'posts/index.html',context)
    def post(self,request):
        data = PostForm(request.POST, request.FILES)
        if data.is_valid():
            data.instance.author = self.request.user
            data.save()
            return redirect('home')

class SinglePostView(LoginRequiredMixin,View):
    def get(self,request,pk):
        post = Post.objects.filter(pk=pk)
        titles = Post.objects.all().order_by('id')[:10]
        context={
            'posts':post,
            'titles':titles,
        }
        return render(request, 'posts/single.html', context)

class SinglePostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','image','content']
    template_name = 'posts/index.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
            
class SinglePostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    template_name = 'posts/delete.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SingleUserPost(LoginRequiredMixin,View):
    def get(self,request,id):
        user_post=Post.objects.filter(author=id)

        user_det=Post.objects.filter(author=id)[:1]

        context={
            'posts':user_post,
            'users':user_det,
        }
        return render(request,'posts/user_post.html',context)