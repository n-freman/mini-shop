from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.title

