from django.db import models

# Create your models here.
def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True)  
    debut = models.DateField()    
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, null=False, blank=False, on_delete=models.CASCADE, related_name='songs')  
    release = models.DateField()  
    content = models.TextField()