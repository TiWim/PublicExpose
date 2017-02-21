from django.db import models

# Create your models here.

#class Question(models.Model):
#   question_text = models.CharField(max_length=200)
#   pub_date = models.DateTimeField('date published')

class Host(models.Model):
    fqdn = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=39)
    inScope = models.IntegerField(default=2)  # 0 if unknown, 1 if in scope, -1 if not
    censys = models.BooleanField(default=False)
    nmap = models.BooleanField(default=False)
    shodan = models.BooleanField(default=False)
    whois = models.BooleanField(default=False)
    nameserver = models.BooleanField(default=False)
    mailserver = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

    module = models.CharField(max_length=200)  # module used to find item
    derivativeKeyword = models.CharField(max_length=200)
    creation = models.DatetimeField()
    modification = models.DatetimeField()

class Email(models.Model):
    email_addr = models.CharField(max_length=200)
    whoisology_status = models.BooleanField(default=False)
    module = models.CharField(max_length=200)  # module used to find item
    derivativeKeyword = models.CharField(max_length=200)
    creation = models.DatetimeField()
    modification = models.DatetimeField()

class Whois(models.Model):
    domainname = models.CharField(max_length=200)
    ip_addr = models.CharField(max_length=200)
    result = models.CharField(max_length=2000)
    creation = models.DatetimeField()
    modification = models.DatetimeField()

class Censys(models.Model):
    domainname = models.CharField(max_length=200)
    result = models.CharField(max_length=2000)
    creation = models.DatetimeField()
    modification = models.DatetimeField()

class Scan(models.Model):
    ip_addr = models.CharField(max_length=200)
    port = models.CharField(max_length=200)
    protocol = models.CharField(max_length=200)
    banner = models.CharField(max_length=200)
    type_scan = models.CharField(max_length=100)  # nmap , shodan
    creation = models.DatetimeField()
    modification = models.DatetimeField()

