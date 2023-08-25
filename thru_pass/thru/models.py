from django.db import models
import json
# Create your models here.
class Thru(models.Model):
    pass

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

    def mc_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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
        db_table = 'twosome'

    def to_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def st_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def pa_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def lo_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def kf_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def ho_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def ed_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }

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

    def an_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }


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

    def bu_json(self):
    	return {
            "num": self.num,
            "name": self.name,
            "addr1": self.addr1,
            "addr2": self.addr2,
            "addrx": self.addrx,
            "addry": self.addry,
            "phone": self.phone,
            "star": self.star
        }
