from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
<<<<<<< HEAD
    email = models.EmailField(blank=True, null=True, verbose_name='郵件')
    #email = models.EmailField()
=======
<<<<<<< HEAD
    email = models.EmailField(blank=True, null=True, verbose_name='郵件')
=======
    email = models.EmailField()
>>>>>>> ad73372fd623d7ef61c6f5a331067ca592d7e73c
>>>>>>> 1b3c135edc7def09d57ec00017704174beb30e57

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
