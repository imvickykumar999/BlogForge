from django.contrib import admin
from .models import OurTeam, ContactQueries, BlogCategory, Article, ArticleDetails, Comment, SEOmeta, StaticContentHome, StaticContentContact, StaticContentAbout, WhyChooseMeSlider, AboutListItem, Footer, CallToAction

@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = ('calltoaction', 'calltoaction_p')
    search_fields = ('calltoaction', 'calltoaction_p')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('base_content', 'location', 'email', 'call', 'twitter_url', 'facebook_url', 'instagram_url', 'linkedin_url')
    search_fields = ('base_content', 'location', 'email', 'call', 'twitter_url', 'facebook_url', 'instagram_url', 'linkedin_url')

@admin.register(AboutListItem)
class AboutListItemAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)

@admin.register(WhyChooseMeSlider)
class WhyChooseMeSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description')
    search_fields = ('title', 'subtitle', 'description')

@admin.register(StaticContentAbout)
class StaticContentAboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content')
    search_fields = ('heading', 'content')

@admin.register(StaticContentContact)
class StaticContentContactAdmin(admin.ModelAdmin):
    list_display = ('location', 'email', 'call')
    search_fields = ('location', 'email', 'call')

@admin.register(StaticContentHome)
class StaticContentHomeAdmin(admin.ModelAdmin):
    list_display = ('heading', 'youtube_url')
    search_fields = ('heading', 'content_p1', 'content_p2', 'youtube_url')

@admin.register(SEOmeta)
class SEOmetaAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'description', 'keywords')
    search_fields = ('page_name', 'title', 'description', 'keywords')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'twitter_link', 'facebook_link', 'instagram_link', 'linkedin_link', 'image')

@admin.register(ContactQueries)
class ContactQueriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'mailid', 'phone', 'subject')
    search_fields = ('name', 'mailid', 'subject')

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('meta_title', 'author_name', 'article_title_h1', 'category_name', 'article_date')
    search_fields = ('meta_title', 'author_name', 'article_title_h1', 'category_name__category_name')
    prepopulated_fields = {'article_slug': ('article_title_h1',)}

@admin.register(ArticleDetails)
class ArticleDetailsAdmin(admin.ModelAdmin):
    list_display = ('article', 'title')
    search_fields = ('title', 'article__article_title_h1')
