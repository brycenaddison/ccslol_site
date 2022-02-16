from django.shortcuts import render, redirect

# Create your views here.

def root(request):
    return redirect('https://docs.google.com/spreadsheets/d/1cvBNafAxgwnJhwyTWmk3V7R8-lkgNElzbvi16W76wbA/edit#gid=1806252028')
    return render(request, 'page_schedule_html/main.html')
