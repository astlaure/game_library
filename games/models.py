from django.db import models


class Game(models.Model):
    GamePlatform = [
        ('PC', 'PC'),
        ('PS4', 'PS4'),
        ('SWITCH', 'Switch'),
        ('XBOX_ONE', 'Xbox One')
    ]

    title = models.CharField(max_length=200, null=False)
    platform = models.CharField(max_length=10, choices=GamePlatform, null=False)
    release_date = models.DateField(null=False)
    owned = models.BooleanField(default=True)
    watched = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.platform, self.title)
