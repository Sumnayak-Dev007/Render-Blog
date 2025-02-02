from django.db import models
from django.contrib.auth.models import User
import os,datetime
from django.core.validators import FileExtensionValidator

# Create your models here.


def get_pic_path(request,filename):
    original_filename=filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # Removed `:`
    filename = f"{nowTime}_{original_filename}"
    return f"pfp/{filename}"



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(default='default.png',upload_to=get_pic_path,validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username
    

# [Unit]
# Description=gunicorn service
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/Project/Render-Blog
# ExecStart=/home/ubuntu/Project/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/Project/Render-Blog/DjangoBlog.sock DjangoBlog.wsgi:application
# Environment="my_email=nsumankumari225@gmail.com"
# Environment="epass=byqu kyge gbqb ygzi"
# [Install]
# WantedBy=multi-user.target


# server {
#        listen 80;    
#        server_name 13.233.133.43;
#        location = /favicon.ico {access_log off;log_not_found off;} 
    
    
#         location / {
#             include proxy_params;
#             proxy_pass http://unix:/home/ubuntu/Project/Render-Blog/DjangoBlog.sock
#         }
#      }

# server {
#     listen 80;
#     server_name 13.233.133.43;
    
#     location = /favicon.ico {
#         access_log off;
#         log_not_found off;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/home/ubuntu/Project/Render-Blog/DjangoBlog.sock;
#     }
# }
