from django.db import models

class MyPets(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    owner = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE,
        related_name='owner',
        verbose_name='Хозяин',
    )
    timeCreate = models.DateTimeField(auto_now_add=True)
    timeUpdate = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name