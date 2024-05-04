from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='blog_posts')
    description = models.TextField()

    class Meta:
        db_table = 'posts'

