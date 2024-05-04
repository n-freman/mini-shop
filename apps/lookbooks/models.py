from django.db import models


class LookBook(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = 'lookbooks'

    def __str__(self):
        return self.title


class LookBookImage(models.Model):
    lookbook = models.ForeignKey(LookBook, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lookbooks')

    class Meta:
        db_table = 'lookbook_images'

