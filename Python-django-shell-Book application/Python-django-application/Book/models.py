from django.db import models

class Author(models.Model):
    name = fields.CharField(max_length=100)
    country_code_choices = [
        ('GB', 'United Kingdom'),
        ('US', 'United States'),
        # ...
    ]
    country_code = fields.CharField(max_length=2, choices=country_code_choices)


class Book(models.Model):
    author = fields.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = fields.CharField(max_length=300)
