import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RechargeProject.settings')

import random
import django
django.setup()

from app1.models import RechargeCardM
from faker import Faker

fakegen=Faker()

def populate(N):


    for values in range(N):
        name=[1,2,3,4]
        nums=[1,2,3,4]
        num1=random.choice(nums)
        name1=random.choice(name)
        fake_name=name1
        fake_code=fakegen.ssn()
        fake_price=num1
        var= RechargeCardM.objects.get_or_create(name=fake_name,price=fake_price,code=fake_code)[0]

populate(50)
