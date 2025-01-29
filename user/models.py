from django.db import models
from django.contrib.auth.models import User
import os,datetime
from django.core.validators import FileExtensionValidator

# Create your models here.


def get_pic_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('pfp/',filename)



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(default='default.png',upload_to=get_pic_path,validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username
    

