
from collections import namedtuple
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

ROLES_NAME = namedtuple('ROLES_NAME', 'user admin')
ROLES = ROLES_NAME('user', 'admin')
ROLE_CHOICES = (
    ('user', ROLES.user),
    ('admin', ROLES.admin),
)
class User(AbstractUser):
    """Castom model user."""
    role = models.CharField(
        verbose_name='Роль пользователя',
        choices=ROLE_CHOICES,
        default=ROLES.user,
        max_length=max(len(role) for _, role in ROLE_CHOICES),
    )
    first_name = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def is_admin(self) -> bool:
        return self.role == ROLES.admin

    def __str__(self) -> str:
        return self.username[:30]