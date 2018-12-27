from django.db import models

# Create your models here.
class RechargeCardM(models.Model):
    name=models.CharField(max_length=245,choices=((1,'MTN'),(2,'GLO'),(3,'Etisalat'),(4,'Airtel')))
    code=models.CharField(max_length=10)
    price=models.IntegerField(choices=((1,100),(2,200),(3,500),(4,1000)))

class CreditCardM(models.Model):
    cardnumber=models.CharField(verbose_name='Card Number', max_length=10)
    zipcode=models.CharField(verbose_name='Zipcode',max_length=5)
    securitycode=models.CharField(verbose_name='Security Code',max_length=3)
    nameofcardholder=models.CharField(verbose_name='Name Of Cardholder',max_length=245)
    expirydate=models.DateField(verbose_name='Expiry Date')
