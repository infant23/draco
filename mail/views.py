from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.core.mail import BadHeaderError, send_mail
from django.views.generic import View


from blog.models import Category, Post, Tag, Comment

def index(request):
    return HttpResponse("Hi, bro. This is mail.")


class PostMan(View):
    template = 'mail/contacts.html'

    def get(self, request):
        tags = Tag.objects.all()
        categories = Category.objects.all()
        context = {
            'tags': tags,
            'categories': categories
        }
        return render(request, self.template, context=context)

    def post(self, request):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        sender = request.POST.get('sender', '')
        if subject and message and sender:
            try:
                mail_content = 'You have receive feedback from email {} on the Draco site.\nThe subject is:\n{}\nThe message is:\n{}'.format(sender, subject, message)
                send_mail('New feedback on Draco site', mail_content, 'testforbkc@gmail.com', ['infant23@ex.ua'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('mail:index', permanent=True)
