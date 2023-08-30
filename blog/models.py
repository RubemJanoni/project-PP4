from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    # Vou usar o title para nomear os tipos de cafe
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True) # No momento que o usuario registrar uma postagem, a data será salva.  Salva uma unica vez. Só salva quando cria a postagem
    updated_on = models.DateTimeField(auto_now=True) # Sempre que o registro for alterado, a data tambem será atualizada. 
    content = models.TextField(max_length=500)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True) # related_name = Nome dado à relação de chave extrangeira.

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
