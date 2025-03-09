from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    role_description = models.TextField()
    role_team_position = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self) -> str:
        return self.role_name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=200)
    fte_savings = models.PositiveIntegerField()
    feedback = models.TextField()
    projectimgurl= models.CharField(max_length=255,unique=False,default="images/image_2.jpg")
    # Client Information
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Education(models.Model):
    Course = models.CharField(max_length=100)
    C_description = models.TextField()
    C_from= models.PositiveIntegerField()
    C_To = models.PositiveIntegerField()
    C_Place = models.TextField()
    

    def __str__(self):
        return self.Course    

class Experience(models.Model):
    Title = models.CharField(max_length=100)
    company = models.TextField()
    e_from= models.TextField()
    e_To = models.TextField()
    e_description = models.TextField()
    

    def __str__(self):
        return self.Title    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name   

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    imageurl = models.CharField(max_length=255,unique=False)
    tags = models.ManyToManyField(Tag, blank=True)  # Many-to-many relationship with tags
    categories = models.ManyToManyField(Category, blank=True)  # Many-to-many relationship with categories

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_post', args=[str(self.id)])

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

class Skill(models.Model):
    s_name = models.CharField(max_length=100)
    s_percentage= models.IntegerField()
    

    def __str__(self):
        return self.s_name    
