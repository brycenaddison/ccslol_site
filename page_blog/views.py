from django.contrib import messages
from django.shortcuts import render, redirect, reverse

# Create your views here.

def root(request):
    return render(request, 'page_blog_html/main.html')


def write(request):
    if request.user.is_authenticated:
        return render(request, 'page_blog_html/write.html')
    messages.add_message(request, messages.WARNING, 'You must be signed in to do that!')
    return redirect(reverse("page_home:root"))