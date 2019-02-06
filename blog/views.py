from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Category, Post, Tag, Comment
from .forms import CommentForm

def index(request):
    return HttpResponse("Hi, bro. This is blog.")


class PostList(View):
    template = 'blog/list_post.html'
    page_value = 10

    def get(self, request):
        categories = Category.objects.all()
        search_query = request.GET.get('search', '')
        tag_query = request.GET.get('tag', '')
        category_query = request.GET.get('category', '')
        if search_query:
            posts = Post.objects.filter(
                Q(title__icontains=search_query) |
                Q(preview__icontains=search_query) |
                Q(content__icontains=search_query)
            )
        elif tag_query:
            tag = Tag.objects.get(
                title__iexact=tag_query
            )
            posts = Post.objects.filter(
              tags=tag.pk
            )
        elif category_query:
            category = Category.objects.get(
                title__iexact=category_query
            )
            posts = Post.objects.filter(
            	category=category.pk
            )
        else:
            posts = Post.objects.all()
        paginator = Paginator(posts, self.page_value)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context = {
            'categories': categories,
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url
        }
        return render(request, self.template, context=context)

class PostDetail(View):
    template = 'blog/detail_post.html'
    page_value = 3
    model_form = CommentForm

    def get(self, request, pk):
        categories = Category.objects.all()
        post = get_object_or_404(Post, pk__iexact=pk)
        comments = Comment.objects.filter(post=post.pk)
        paginator = Paginator(comments, self.page_value)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context = {
            'categories': categories,
            'post': post,
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'form': self.model_form
        }
        return render(request, self.template, context=context)

    def post(self, request, pk):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save(commit=False)
            new_obj.post = Post.objects.get(pk=pk)
            new_obj.save()
        return redirect(reverse('blog:post_detail_url', kwargs={'pk': pk}))
