from django.shortcuts import render

# Create your views here.
def author_list(request):
    return render(request, 'myapp/author_list.html',{})
