from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ContactQueries, BlogCategory, OurTeam, SEOmeta, StaticContentHome, StaticContentContact, StaticContentAbout, Footer, WhyChooseMeSlider, AboutListItem, CallToAction
from .forms import CommentForm
import urllib.request
import json

def home(request):
    articles = Article.objects.all().order_by('-article_date')[:16]
    sliders = WhyChooseMeSlider.objects.all()
    static_content = StaticContentHome.objects.first()
    footer = Footer.objects.first()
    call2action = CallToAction.objects.first()

    try:
        seo_meta = SEOmeta.objects.get(page_name='home')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    active_home = 'active'
    return render(request, 'index.html', {
        'articles': articles,
        'seo_meta': seo_meta,
        'static_content': static_content,
        'sliders': sliders,
        'footer': footer,
        'call2action': call2action,
        'active_home': active_home,
    })

def contact(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'

    values = {
        'secret': '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',
        'response': recaptcha_response
    }

    data = urllib.parse.urlencode(values).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)

    success_message = None
    result = json.loads(response.read().decode())
    # if result['success']:

    if request.method == 'POST':
        name = request.POST.get('name')
        mailid = request.POST.get('mailid')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactQueries.objects.create(
            name=name,
            mailid=mailid,
            phone=phone,
            subject=subject,
            message=message
        )
        success_message = "Your message has been sent. Thank you!"

    try:
        seo_meta = SEOmeta.objects.get(page_name='contact')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    static_content = StaticContentContact.objects.first()
    footer = Footer.objects.first()

    active_contact = 'active'
    return render(request, 'contact.html', {
        'success_message': success_message,
        'seo_meta': seo_meta,
        'static_content': static_content,
        'footer': footer,
        'active_contact': active_contact,
    })

def category(request, category):
    category = get_object_or_404(BlogCategory, category_name=category)
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    articles = Article.objects.filter(category_name=category)
    categories = BlogCategory.objects.all()
    footer = Footer.objects.first()

    try:
        seo_meta = SEOmeta.objects.get(page_name='category')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    return render(request, 'category.html', {
        'articles': articles, 
        'categories': categories, 
        'category' : category,
        'recent_posts': recent_posts,
        'seo_meta': seo_meta,
        'footer': footer,
    })

def blogs(request):
    categories = BlogCategory.objects.all()
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    category_slug = request.GET.get('category')
    articles = Article.objects.all().order_by('-article_date')
    footer = Footer.objects.first()

    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        articles = articles.filter(category_name=category)

    try:
        seo_meta = SEOmeta.objects.get(page_name='blog')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    active_blogs = 'active'
    return render(request, 'blog.html', {
        'categories': categories,
        'recent_posts': recent_posts,
        'articles': articles,
        'seo_meta': seo_meta,
        'footer': footer,
        'active_blogs': active_blogs,
    })

def about(request):
    team_members = OurTeam.objects.all()
    sliders = WhyChooseMeSlider.objects.all()
    static_content = StaticContentAbout.objects.first()
    list_items = AboutListItem.objects.all()
    footer = Footer.objects.first()
    call2action = CallToAction.objects.first()

    try:
        seo_meta = SEOmeta.objects.get(page_name='about')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    active_about = 'active'
    return render(request, 'about.html', {
        'team_members': team_members,
        'seo_meta': seo_meta,
        'static_content': static_content,
        'sliders': sliders,
        'list_items': list_items,
        'footer': footer,
        'call2action': call2action,
        'active_about': active_about,
    })

def blog_details(request, article_slug):
    article = get_object_or_404(Article, article_slug=article_slug)
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    categories = BlogCategory.objects.all()
    footer = Footer.objects.first()

    comments = article.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', article_slug=article_slug)
    else:
        comment_form = CommentForm()

    try:
        seo_meta = SEOmeta.objects.get(page_name='blog_details')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    return render(request, 'blog-details.html', {
        'article': article,
        'recent_posts': recent_posts,
        'comments': comments,
        'categories': categories,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'seo_meta': seo_meta,
        'footer': footer,
    })
