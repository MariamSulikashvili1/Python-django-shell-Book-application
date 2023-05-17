from Book import models
from Book import book_list

author_book_subquery = Book.objects.filter(author_id=OuterRef('id'))
Author.objects.annotate(
    has_book=Exists(author_book_subquery)
).annotate(
    has_book_as_int=Case(
        When(has_book=True, then=Value(1)),
        default=Value(0),
        output_field=IntegerField(),
    )
).values(
    'country_code'
).annotate(
    num_authors=Count('*'),
    num_authors_with_book=Sum(has_book_as_int),
