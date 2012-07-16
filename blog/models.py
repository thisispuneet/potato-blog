# models.py in blog project for potato
# created by Puneet Chawla (pchawla@buffalo.edu)

from django.db import models

# Create your models here.
# creating table myblog with title and content as fields
# title is the primark key and limited to length 40
# content can be blank
class myblog(models.Model):
    title=models.CharField(max_length=40, primary_key=True)
    content=models.TextField(blank=True)
#    pub_date = models.DateTimeField('date published')

# returning title (pk) as unicode
    def __unicode__(self):
        return self.title
