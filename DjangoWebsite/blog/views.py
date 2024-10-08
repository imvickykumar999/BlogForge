from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, ContactForm

from .models import (
    Article, 
    ContactQueries, 
    BlogCategory, 
    OurTeam, 
    SEOmeta, 
    StaticContentHome, 
    StaticContentContact, 
    StaticContentAbout, 
    Footer, 
    WhyChooseMeSlider, 
    AboutListItem, 
    CallToAction
)

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
    success_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        
        if form.is_valid():
            ContactQueries.objects.create(
                name=form.cleaned_data['name'],
                mailid=form.cleaned_data['mailid'],
                phone=form.cleaned_data['phone'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            success_message = "Your message has been sent. Thank you!"
        else:
            success_message = "reCAPTCHA Failed!"
    else:
        form = ContactForm() 

    try:
        seo_meta = SEOmeta.objects.get(page_name='contact')
    except SEOmeta.DoesNotExist:
        seo_meta = None

    static_content = StaticContentContact.objects.first()
    footer = Footer.objects.first()

    active_contact = 'active'
    return render(request, 'contact.html', {
        'form': form,
        'success_message': success_message,
        'seo_meta': seo_meta,
        'static_content': static_content,
        'footer': footer,
        'active_contact': active_contact,
    })

def category(request, category):
    try:
        category = get_object_or_404(BlogCategory, category_name=category)
    except:
        return redirect('https://imvickykumar999.pythonanywhere.com/')

    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    categories = BlogCategory.objects.all()
    footer = Footer.objects.first()
    query = request.GET.get('q', '')
    articles = Article.objects.filter(category_name=category)
    
    if query:
        articles = articles.filter(article_title_h1__icontains=query)

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

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
        'query': query,
    })

def blogs(request):
    categories = BlogCategory.objects.all()
    recent_posts = Article.objects.all().order_by('-article_date')[:10]
    category_slug = request.GET.get('category')
    query = request.GET.get('q', '')
    articles = Article.objects.all().order_by('-article_date')
    footer = Footer.objects.first()

    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        articles = articles.filter(category_name=category)

    if query:
        articles = articles.filter(article_title_h1__icontains=query)

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

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
        'query': query,
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
    try:
        article = get_object_or_404(Article, article_slug=article_slug)
    except:
        return redirect('https://imvickykumar999.pythonanywhere.com/')

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
