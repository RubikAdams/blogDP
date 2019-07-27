from django.shortcuts import render
from .models import Post
from django.utils import timezone 

def post_list(request):
	posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
    # consulta  ala DB y guardando en la DB y pintando con render post list solo los publicados
# Create your views here.
