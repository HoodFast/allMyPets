from django.db import models

class MyPets(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    owner = models.ForeignKey(
        to='users.CastomUser',
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Хозяин',
    )
    photo = models.ImageField(upload_to='photo/',blank=True)
    video = models.FileField(upload_to='video/',blank=True)
    # categories = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    timeCreate = models.DateTimeField(auto_now_add=True)
    timeUpdate = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    

class Likes(models.Model):
    ownerLikes=models.ForeignKey(
        to='users.CastomUser',
        on_delete=models.CASCADE,
        related_name='Ownlikes',
        verbose_name='Хозяин',
    )
    petsLikes = models.ForeignKey(
        to='pets.MyPets',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Лайк',
    )