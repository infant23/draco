from django.db import models
from django.shortcuts import reverse
from tinymce import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    preview = HTMLField(blank=True, max_length=200, db_index=True)
    content = HTMLField(blank=True, max_length=2000, db_index=True)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_detail_url(self):
        return reverse('blog:post_detail_url', kwargs={'pk': self.pk})

    def get_add_comment_url(self):
        return reverse('blog:add_comment_url', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    content = HTMLField(max_length=500, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-pub_date']
