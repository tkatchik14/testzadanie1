from django.db import models


# Create your models here.
class Dictionary(models.Model):
    id = models.TextField(primary_key=True)
    sprid = models.TextField()
    name = models.TextField()
    shortname = models.TextField()
    description = models.TextField()
    version = models.TextField()
    datefrom = models.DateField()
    dateto = models.DateField()

    class Meta:
        db_table = 'nsi\".\"dictionary'
        managed = False

    def __str__(self):
        return self.sprid


class DictionaryItem(models.Model):
    id = models.TextField(primary_key=True)
    dictionary_id = models.ForeignKey(Dictionary, on_delete=models.CASCADE, db_column='dictionary_id')
    parent_id = models.IntegerField()
    item_code = models.TextField()
    item_value = models.TextField()

    class Meta:
        db_table = 'nsi\".\"dictionary_item'
        managed = False

    def __str__(self):
        return self.id
