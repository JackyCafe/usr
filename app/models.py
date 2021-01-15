from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
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
    slug = RandomCharField(length=32, unique=True, unique_for_date='created')
    category = models.CharField(max_length=32,default='')
    created = models.DateTimeField(auto_now=True,)
    content = RichTextField(verbose_name='內容',null=True)
    attachment = models.FileField(upload_to='healthes/%Y/%m/%d/')
    
    def __str__(self):
        return self.title
    
    def delete(self,*args,**kwargs):
        self.attachment.delete()
        super(Reading, self).delete(*args,**kwargs)

