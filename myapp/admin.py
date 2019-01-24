#load tables
from django.contrib import admin
from .models import Author
from .models import Book
from .models import Sale
from .models import Publisher
from .models import Customer
from .models import Price


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Sale)
admin.site.register(Publisher)
admin.site.register(Customer)
admin.site.register(Price)
# Register your models here.
