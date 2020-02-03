from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Item(models.Model):
    kind = models.CharField(max_length = 200, default = 'Lost',
            choices = [('Lost', 'Lost'), ('Found', 'Found')],
            verbose_name = 'Lost/Found')
    location = models.CharField(max_length = 200)
    date = models.DateField(default = now)
    category = models.CharField(max_length = 200, verbose_name='Category')
    desc = models.TextField(verbose_name = 'Description of the Item')
    image = models.ImageField(upload_to='images', null = True)
    claimed = models.BooleanField(default = False)
    submitter = models.CharField(max_length = 200, verbose_name = 'Your Name')
    email = models.EmailField(verbose_name = 'Your Email Address')

    class Meta:
        ordering = ['-date', 'submitter']

    def __str__(self):
        return (self.kind + ' ' + str(self.category)
                          + ' at ' + self.location + ' on '
                          + self.date.strftime("%a, %d %b %Y"))
    def name(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('main:item', kwargs={'pk': self.pk})
