from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    settings = models.JSONField(default=dict)

    def change_theme_preference(self, theme):
        self.settings['theme'] = theme
        self.save()

    def get_theme_preference(self):
        return self.settings.get('theme', 'auto')
