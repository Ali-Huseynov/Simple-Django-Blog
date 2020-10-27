from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):

    name = models.CharField(max_length=15 )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Post(models.Model):
    
    author = models.ForeignKey( User , on_delete=models.CASCADE)
    title = models.CharField( max_length=20 )

    body = RichTextField( blank=True , null=True )
    date_time = models.DateTimeField( auto_now_add=True )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    likes = models.ManyToManyField(User,related_name='like_post')
    unlikes = models.ManyToManyField(User,related_name='unlike_post')


    def __str__(self):
        return  str(self.title) #+ ' | ' + str(self.date_time)

    def get_likes(self):
        return self.likes.count()
    
    def get_unlikes(self):
        return self.unlikes.count()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', kwargs={'pk': self.pk})



class Comments(models.Model):

    post = models.ForeignKey( Post , on_delete=models.CASCADE , related_name='comments'  ) # on delete post also delete Comment
    author = models.ForeignKey(User,on_delete=models.CASCADE )
    body = models.CharField(max_length=255)
    date_time = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return  f" Comment at  '{ self.post }' from { self.author } "

    class Meta:
        ordering = ['-date_time']
