<h1>Concepts I learnt in this Web Application </h1>


#Create Profile automatically when user Signs in

from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender = User)
def create_prfile(sender,instance,created,*args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

<b>Inform the apps.py that you are using signals</b>

def ready(self):
    import user.signals



<br>
<h4>Removing Help Text from forms</h4>
<br>
    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'email']:
                self.fields[fieldname].help_text = None

<h2>Modifying Admin Model View</h2>
<br>
from django.contrib import admin
from .models import UserPost


class UserPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at') 


admin.site.register(UserPost,UserPostAdmin)

<h1>Reverse Relationship in Django Models</h1>
ForeignKeyField:
Django uses the model name+_set:

author = Author.objects.get(id=1)
books = author.book_set.all() 

OneToOneField:
lowercase name of related models:

user = User.objects.get(id=1)
print(user.profile.bio)  # Default reverse

ManyToManyField:

Without related_name, Django uses the model name+_set:

student = Student.objects.get(id=1)
courses = student.course_set.all()

<h1>Comment Section</h1>
Accordion design from in Tailwind 
Comment model with Foreignkey to User and UserPost model
now To show number of comments on a post:
Using reverse relation to the comment model from UserPost modal to coutn the comments as well as showing all comments on a post in the template:
def cmnt_count(self):
        return self.comments_set.all().count()


Creating Form in forms.py for userd to send/write comment on a post
passing comment form in the context for rendering


<h1>To use Enviroment Variable to hide Sensitive Data</h1>
contron panel >> systems and security >> System >> Advanced System Setting >> Edit Enviroment Variable >> User Variable >> New >> Var_name >> Var_value >> OK*3 >> import os >> key = os.environ.get('var_name') >> Done

