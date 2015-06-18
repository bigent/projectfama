import time, datetime
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.utils import timezone
import foursquare
from fama import settings
from django.utils.translation import ugettext_lazy as _


#---begin--- foursquare client id and client secret
client_id = "A3VXW30IK3MVYL3AYPA0GFXDK4VTPTSAT5SWANKDOJQVN0CY"
client_secret = "FTVVMZNWM4RRO2HI4RKEB3EH11AFPFAZTFKIKK5YCXGTLQ2A"
#---stop---


#foursquare config
client = foursquare.Foursquare(client_id=client_id, client_secret=client_secret, version=time.strftime("%Y%m%d"))

class Reporter(models.Model):
    user = models.OneToOneField(User)
    xp = models.PositiveIntegerField(default=100)
    profile_picture = models.ImageField(upload_to='images/avatars/', default='images/avatars/no_picture.jpg')

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.user.username

    def level_info(self):
        i=1
        level = 0
        xp = self.xp

        def total_level_xp(level):
            return level * (level+1) * 500

        while True:
            if xp < total_level_xp(i):
                level = i
                break
            elif xp > total_level_xp(i):
                i = i + 1

        next_level = level + 1

        total_next_level_xp = total_level_xp(next_level)

        left_xp = total_next_level_xp - xp

        percent = int( float(xp) / float(total_next_level_xp) * 100 )

        data = {
            'level': level,
            'next_level': next_level,
            'xp': xp,
            'left_xp': left_xp,
            'next_level_xp': total_next_level_xp,
            'percent': percent
        }

        return data

    def get_famas(self):
        return Fama.objects.filter(author=self.user)


class Fama(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=350)
    place = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

    def get_reporter(self):
        return Reporter.objects.filter(user=self.user)
    
    def get_place(self):
        return client.venues(self.place)['venue']['name']


class Ticket(models.Model):
    messagge = models.TextField(max_length=510)
    is_solved = models.BooleanField(default=False)
    send_date = models.DateTimeField(auto_now=True)
