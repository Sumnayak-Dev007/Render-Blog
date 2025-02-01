from django.db import models
from django.contrib.auth.models import User
import datetime,os
# Create your models here.


def get_image_path(instance, filename):  # `request` → `instance`
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # Removed `:`
    filename = f"{nowTime}_{original_filename}"
    return f"images/{filename}"  # Removed `os.path.join()`


class UserPost(models.Model):
    title = models.CharField(max_length=150,null=False)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_image_path )

    class Meta:
        ordering = ('-created_at',)

    def cmnt_count(self):
        return self.comments_set.all().count()

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content
    
    
