from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


from website_api.models import Article


def list_articles(request):
    state = get_random_string(32)
    print(request.user.id)
    cache.set(state, request.user.id, 6000)
    return render(request,'list-articles.html')


def get_articles(request, my_slug):
    article = Article.objects.get(slug=my_slug)
    return render(request,'get-articles.html', {'article': article})


@login_required()
def add_articles(request):
    title = ''
    content = ''
    error = False

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        if len(title) > 30:
            error = True
        else:
            author = request.user.detail[0].bio
            article = Article.objects.create(title=title, content=content, author=author)
            return redirect('website_web:article_get', article.slug)
    return render(request, 'add-articles.html', {'title': title, 'content': content, 'error': error})


def facebook_oauth(request):

    state=request.Get['state']
    grant=request.Get['code']
    user_id=cache.request.id
    client_id = ''
    client_secret = ''
    redirect_uri = 'http://127.0.0.1/api/articles'

    data = {'client_id': client_id, 'redirect_uri': redirect_uri,
            'client_secret': client_secret, 'code': grant}
    res= request.get('https://graph.facebook.com/v2.12/oauth/access_token',params=data).json()
    print(res)
    access_token = res['access_token']


def home_page(request):
    return render(request,'main.html')
