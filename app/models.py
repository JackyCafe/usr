from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.text import slugify
from django_extensions.db.fields import RandomCharField


class UserProfile(models.Model):
    AUTHORITY_CHOICE = (('admin', '管理者'),
                        ('general', '一般民眾'),

                        )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    actual_name = models.CharField(max_length=10, verbose_name='姓名')
    authority = models.CharField(max_length=20, verbose_name='身分', choices=AUTHORITY_CHOICE, default='resident')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', null=True, blank=True, verbose_name='照片')

    def __str__(self):
        return self.actual_name


class Reading(models.Model):
    title = models.CharField(max_length=20)
    slug = RandomCharField(length=32,blank=True,null=True)
    category = models.CharField(max_length=32,default='')
    created = models.DateTimeField(auto_now=True,)
    content = RichTextField(verbose_name='內容',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='reading',default=1)

    def __str__(self):
        return self.title
    
   
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    slug = RandomCharField(length=32, blank=True, null=True)
    category = models.CharField(max_length=32, default='')
    created = models.DateTimeField(auto_now=True, )
    content = RichTextField(verbose_name='內容', null=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Activity(models.Model):
    title = models.CharField(max_length=32,verbose_name='活動名稱')
    content = models.TextField(verbose_name='活動內容')
    point = models.IntegerField(default=0,verbose_name='點數')

    def __str__(self):
        return self.title

class myActivity(models.Model):
    ac_date=models.DateField(auto_now=True)
    user = models.ForeignKey(User,verbose_name='使用者',on_delete=models.CASCADE,related_name='my_activity')
    title = models.ForeignKey(Activity,verbose_name='活動名稱',default='',on_delete=models.CASCADE,related_name='activity')
    point = models.IntegerField(default=0,verbose_name='點數')