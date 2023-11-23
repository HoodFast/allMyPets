from django.db import models

class MyPets(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    owner = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='user',
        verbose_name='Хозяин',
    )
    photo = models.ImageField(upload_to='photo/')
    video = models.FileField(upload_to='video/')
    # likes = models.ForeignKey(
    #     to='likes.Like',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name='likes',)
    # categories = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    timeCreate = models.DateTimeField(auto_now_add=True)
    timeUpdate = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name