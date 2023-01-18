import factory
from django.contrib.auth.models import User 
from blog import models 


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = 'admin'
    password = 'admin'
    is_superuser = True 
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Post

    title = 'null'
    subtitle = 'null'
    slug = 'null'
    author = factory.SubFactory(UserFactory)
    content = 'null'
    status = 'published'