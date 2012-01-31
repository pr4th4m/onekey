from django.db import models

# Create your models here.


class Test(models.Model) :
    ''' Just a test model
    '''
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    test_field = models.CharField(max_length =100)


TITLE_CHOICES = (
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
        )

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def full_clean(self):
        """ """
        debug()

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
