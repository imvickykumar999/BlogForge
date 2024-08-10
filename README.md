# `Blog`

    Google Adsense, Robots.txt, Ads.txt, reCaptcha, 
    KYC, Admin, Like, Comment, Share, Profile, SEO Meta

```py
class Blog(models.Model):
    blogid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title_tegs = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    url_structure = models.CharField(
        max_length=500, unique=True, blank=True, null=True)
    title = models.CharField(
        max_length=500, unique=True, blank=True, null=True)
    blog_categories = models.CharField(max_length=100, blank=True, null=True)
    short_discription = models.CharField(max_length=300, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    alttext = models.CharField(max_length=100, blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.blogid)+' '+str(self.url_structure)

class Blogcontent(models.Model):
    blogcontentid = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, models.DO_NOTHING)
    title = models.CharField(
        max_length=500, unique=True, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    alttext = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.title)

class BlogsCate(models.Model):
    blogscateid = models.AutoField(primary_key=True)
    blogscategory = models.TextField()
    page_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    h1_tag = models.CharField(max_length=150, blank=True, null=True,default=None)
    h2_tag = models.CharField(max_length=150, blank=True, null=True,default=None)
    h3_tag = models.CharField(max_length=150, blank=True, null=True,default=None)
    h4_tag = models.CharField(max_length=150, blank=True, null=True,default=None)

    def __str__(self):
        return str(self.blogscategory)

class BlogCategory(models.Model):
    blogcategoryid = models.AutoField(primary_key=True)
    blogcategory = models.TextField()
    blogcategory_count = models.TextField()

    def __str__(self):
        return str(self.blogcategoryid)


class BlogComments(models.Model):
    commentid = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, models.DO_NOTHING)
    Commenttext = models.TextField()
    name = models.CharField(max_length=20)
    totallikes = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    isapproved = models.BooleanField(default=False, blank=True, null=True)
    approveuserid = models.ForeignKey(
        Allusers, models.DO_NOTHING, db_column='approveuserid', to_field='id', blank=True, null=True)

    def __str__(self):
        return str(self.commentid)
```
