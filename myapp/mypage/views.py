from django.shortcuts import render
from .models import Bookmark
from .forms import BookmarkForm
from django.db.models import Q

# Create your views here.
def display(request):
	bookmark = Bookmark.objects.all()
	return render(request, 'display.html', {'bookmark' : bookmark})

def insert_page(request):
	if request.method == "POST":
		form = BookmarkForm(request.POST)
		form.save()
		return render(request, 'display1.html', {'form' : form})
	else:
		form = BookmarkForm()
		return render(request, 'display1.html', {'form' : form})

def search(request, keyword):
	bookmark = Bookmark.objects.filter(Q(name__contains = keyword) | Q(link__contains = keyword))
	return render(request, 'display.html', {'bookmark' : bookmark})