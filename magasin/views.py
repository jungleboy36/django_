from django.http import HttpResponse
from django.template import loader
from magasin.models import Article
def index(request):
 art = Article.objects.all().values()
 template = loader.get_template('home.html')
 context = {
 'art': art,
 }
 return HttpResponse(template.render(context, request))