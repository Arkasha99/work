from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time,date


class Ticket(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    price=models.IntegerField()
    place=models.IntegerField()
    adate=models.DateField(default=date.today,blank=True)
    ddate=models.DateField(default=date.today,blank=True)
    atime=models.CharField(max_length=6)
    dtime=models.CharField(max_length=6)
    DIRECTION=(
        ('Moscow', 'm'),
        ('Saint-Petersburg', 'spb'),
        ('Kazan', 'k'),
        ('Perm', 'p'),
        ('Astana', 'a'),
        ('Vladivostok', 'v'),
        ('Surgut', 's'),
        ('Saratov', 's'),
        ('Tashkent', 't'),
        ('Kirov', 'k')
    )
    arpoint=models.CharField(max_length=20,choices=DIRECTION,blank=True,default='Moscow')
    dpoint=models.CharField(max_length=30,choices=DIRECTION,blank=True,default='Saint-Petersburg')
    BOOK_STATUS=(
        ('a','Active'),
        ('b','Booked')
    )
    status=models.CharField(max_length=10,choices=BOOK_STATUS,blank=True,default='a')
    def __str__(self):
        return self.arpoint+'-'+self.dpoint+', '+str(self.place)