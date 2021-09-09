from django.db import models
import datetime
# Create your models here.


class ManageBook (models.Model):
    Authorname = models.CharField(max_length=100)
    Booktitle = models.CharField(max_length=100)
    Imprint = models.CharField(max_length=50)
    Publicationdate = models.DateField()

    class Meta:
        db_table = "managebook"
