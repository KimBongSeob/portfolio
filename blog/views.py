from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def index(request):
    #posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
    )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post':post,
#         }
#     )

class PostList(ListView):
    model = Post
    # template_name = 'blog/post_list.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
