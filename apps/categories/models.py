from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=120)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='subcategories',
        null=True,
        blank=True,
    )

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.title

