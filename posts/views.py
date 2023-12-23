from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from django.db.models import Q
from .forms import PostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def random_response(request):
    # 아무 응답을 원하는 경우, 여기에서 응답을 생성합니다.
    response_data = {
        'message': '아무거나 응답합니다!'
    }
    return Response(response_data)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'blog/post.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'blog/delete.html', {'post': post})