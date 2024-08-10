from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class CallToAction(models.Model):
    calltoaction = models.CharField(max_length=255)
    calltoaction_p = models.TextField()

    def __str__(self):
        return self.calltoaction

class AboutListItem(models.Model):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content

class WhyChooseMeSlider(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Footer(models.Model):
    base_content = models.TextField(default="")
    location = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    call = models.CharField(max_length=255, default="")
    twitter_url = models.URLField(max_length=255, default="")
    facebook_url = models.URLField(max_length=255, default="")
    instagram_url = models.URLField(max_length=255, default="")
    linkedin_url = models.URLField(max_length=255, default="")

    def __str__(self):
        return "Footer Content"

class StaticContentContact(models.Model):
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    call = models.CharField(max_length=255)
    def __str__(self):
        return "Contact Page Content"

class StaticContentAbout(models.Model):
    heading = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.heading
    
class StaticContentHome(models.Model):
    heading = models.CharField(max_length=500)
    content_p1 = models.TextField()
    content_p2 = models.TextField()
    youtube_url = models.CharField(max_length=255)

class SEOmeta(models.Model):
    page_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.TextField()
    og_title = models.CharField(max_length=255)
    og_url = models.CharField(max_length=255)
    og_image = models.CharField(max_length=255)
    og_image_type = models.CharField(max_length=255)
    og_image_width = models.CharField(max_length=255)
    og_image_height = models.CharField(max_length=255)
    og_type = models.CharField(max_length=255)
    og_locale = models.CharField(max_length=255)
    og_image_url = models.CharField(max_length=255)
    og_image_secure_url = models.CharField(max_length=255)
    og_site_name = models.CharField(max_length=255)
    og_see_also = models.CharField(max_length=255)
    article_author = models.CharField(max_length=255)
    format_detection = models.CharField(max_length=255)

class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return f"{self.name} - {self.designation}"

class ContactQueries(models.Model):
    name = models.CharField(max_length=255)
    mailid = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.subject

class BlogCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    def article_count(self):
        return self.article_set.count()

class Article(models.Model):
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    article_slug = models.SlugField(unique=True, max_length=255)
    author_name = models.CharField(max_length=255)
    article_title_h1 = models.CharField(max_length=255)
    category_name = models.ForeignKey('BlogCategory', on_delete=models.CASCADE)
    article_short_description = models.CharField(max_length=200) 
    article_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    thoughts = models.TextField()
    description = RichTextField()
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.article_title_h1

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'

class ArticleDetails(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='article_images/')

    def __str__(self):
        return self.title
