from django.shortcuts import render
from .models import Author

# Create your views here.
def author_list(request):
    authors = Author.objects.order_by('lastnane')
    return render(request, 'myapp/author_list.html',{'authors' : firstname + ' ' + lastname})
