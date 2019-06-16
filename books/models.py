from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    # books = models.ForeignKey(Book, on_delete=models.CASCADE)
    # -- tohle udela dropdown, ale ja chci aby to vyistovalo automaticky vsechny knihy s timto autorem

    def author_get_absolute_url(self):
        return reverse('author_detail_view', kwargs={'id': self.id})


class Book(models.Model):
    title = models.CharField(max_length=60)
    year = models.DateField()
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)
    borrowed_by = models.CharField(max_length=60, blank=True, null=False)

    def book_get_absolute_url(self):
        return reverse('book_detail_view', kwargs={'id': self.id})
