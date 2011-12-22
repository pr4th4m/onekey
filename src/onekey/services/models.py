from django.db import models

# Create your models here.


class Test(models.Model) :
    ''' Just a test model
    '''
    test_field = models.CharField(max_length =100)

