from django.db import models
import json
# Create your models here.
class Thru(models.Model):
    pass

class Angelinus(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'angelinus'



class Burgerking(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'burgerking'


class Ediya(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ediya'
class Hollys(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hollys'
class Kfc(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'kfc'
class Lotteria(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'lotteria'
class Mcdonalds(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'mcdonalds'
class Twosomeplace(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'twosomeplace'
class Pascucci(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'pascucci'
class Starbucks(models.Model):
    num = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    addr1 = models.CharField(max_length=40)
    addr2 = models.CharField(max_length=40)
    addrx = models.CharField(max_length=40, blank=True, null=True)
    addry = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    star = models.CharField(max_length=6, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'starbucks'


