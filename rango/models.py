from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

MAX_TITLE_LEN = 128


class Category(models.Model):
    #set name to unique, so that two Category entries cannot have the same name
    name = models.CharField(max_length=MAX_TITLE_LEN, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    #slug will be a safe name of the category to use in urls
    slug = models.SlugField(unique=True) #wil be used for urls, so should be unique
    
    # override the save method of model
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # delete pages associated to category when category is deleted
    title = models.CharField(max_length=MAX_TITLE_LEN)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    #link user profile to a user model page
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # the additionial attributes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True) # proj_root/mdeia/profile_images/

    def __str__(self):
        return self.user.username
