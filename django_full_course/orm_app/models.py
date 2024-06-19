from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=80)


# one to many relationship a author can have n number of books
class Book(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


# many to many field-- shop can have n number of fruits as well as fruit can have n number shops
class Shop(models.Model):
    name = models.CharField(max_length=80)

    # Example Queries


class Fruits(models.Model):
    title = models.CharField(max_length=80)
    shop = models.ManyToManyField(Shop)

    # example queries
    """
     from orm_app.models import Shop, Fruits
    >>> shop1 = Shop.objects.create(name = "RK fruits")
    >>> shop2 = Shop.objects.create(name = "AI fruits center") 
    >>> fruit1 = Fruits.objects.create(title = "apple")      
    >>> fruit2 = Fruits.objects.create(title = "banana") 
    >>> fruit1.shop.add(shop1, shop2) 
    >>> fruit2.shop.add(shop1, shop2) 
    """


# one customer record can have one profile record as well as one profile record can only one customer record
class Customer(models.Model):
    name = models.CharField(max_length=80)


class Profile(models.Model):
    address = models.TextField()
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    # example queries
    """
    p1 = Profile.objects.create(address=)
    p1 = Profile.objects.create(address="blr, ka", customer = c1) 
    >>> p2 = Profile.objects.create(address = "hyd, ad", customer = c1) 
    """


class Blog(models.Model):
    name = models.CharField(max_length=80)
    tagline = models.TextField()


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=80)
    body_text = models.TextField()
    pub_date = models.DateField()
    author = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    rating = models.FloatField()

    # sample orm queries
    """
    from orm_app.models import Entry, Author, Blog 
>>> Entry.objects.filter(number_of_comments__gt=3).values()
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}, {'id': 2, 'blog_id': 1, 'headline': 'comiccon', 'body_text': 'movie details', 'pub_date': datetime.date(2024, 6, 19), 'number_of_comments': 7, 'rating': 5.0}, {'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}]>
>>> Entry.objects.filter(number_of_comments__lt=3).values() 
<QuerySet [{'id': 4, 'blog_id': 1, 'headline': 'venom', 'body_text': 'last dance', 'pub_date': datetime.date(2024, 6, 4), 'number_of_comments': 2, 'rating': 3.0}]>
>>> Entry.objects.filter(pub_date__year=2024).values()      
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}, {'id': 2, 'blog_id': 1, 'headline': 'comiccon', 'body_text': 'movie details', 'pub_date': datetime.date(2024, 6, 19), 'number_of_comments': 7, 'rating': 5.0}, {'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}, {'id': 4, 'blog_id': 1, 'headline': 'venom', 'body_text': 'last dance', 'pub_date': datetime.date(2024, 6, 4), 'number_of_comments': 2, 'rating': 3.0}]>
>>> Entry.objects.filter(pub_date__year=2023).values() 
<QuerySet []>
     Entry.objects.filter(id__in=[1,3,5,7]).values() 
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}, {'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}]>  
>>> Entry.objects.filter(headline__contains="man").values()       
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}]>
>>> Entry.objects.filter(headline__startswith="i").values()   
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}]>
>>> Entry.objects.filter(headline__endswith="s").values()   
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}]>
>>> Entry.objects.filter().values()[:3]                   
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}, {'id': 2, 'blog_id': 1, 'headline': 'comiccon', 'body_text': 'movie details', 'pub_date': datetime.date(2024, 6, 19), 'number_of_comments': 7, 'rating': 5.0}, {'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}]>
>>> Entry.objects.filter().values()[2:] 
<QuerySet [{'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}, {'id': 4, 'blog_id': 1, 'headline': 'venom', 'body_text': 'last dance', 'pub_date': datetime.date(2024, 6, 4), 'number_of_comments': 2, 'rating': 3.0}]>
>>> entry_data=Entry.objects.filter().values() 
>>> entry_data[1] 
{'id': 2, 'blog_id': 1, 'headline': 'comiccon', 'body_text': 'movie details', 'pub_date': datetime.date(2024, 6, 19), 'number_of_comments': 7, 'rating': 5.0}
>>> entry_data[2] 
{'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}
>>> entry_data[0] 
{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}
Entry.objects.filter(pub_date__day=5) 
<QuerySet []>
>>> Entry.objects.filter(pub_date__day=18) 
<QuerySet []>
>>> Entry.objects.filter(pub_date__day=19) 
<QuerySet [<Entry: Entry object (2)>]>
>>> Entry.objects.filter(pub_date__month=19) 
<QuerySet []>
>>> Entry.objects.filter(pub_date__month=06) 
  File "<console>", line 1
    Entry.objects.filter(pub_date__month=06)
                                         ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers   
>>> Entry.objects.filter(pub_date__month=6)  
<QuerySet [<Entry: Entry object (2)>, <Entry: Entry object (3)>, <Entry: Entry object (4)>]>
    
 from django.db.models import Avg, F  
>>> Entry.objects.filter(number_of_comments__gt=F("rating")).values()
<QuerySet [{'id': 2, 'blog_id': 1, 'headline': 'comiccon', 'body_text': 'movie details', 'pub_date': datetime.date(2024, 6, 19), 'number_of_comments': 7, 'rating': 5.0}, {'id': 3, 'blog_id': 1, 'headline': 'spider verse', 'body_text': 'beyond the spider verse', 'pub_date': datetime.date(2024, 6, 3), 'number_of_comments': 90, 'rating': 4.0}]>
>>> Entry.objects.filter(id=2, rating=5) 
<QuerySet [<Entry: Entry object (2)>]>
from django.db.models import Q
 Entry.objects.filter(Q(headline__startswith="i")|Q(body_text__startswith="m")).values() 
<QuerySet [{'id': 1, 'blog_id': 1, 'headline': 'ironman news', 'body_text': '', 'pub_date': datetime.date(2024, 5, 12), 'number_of_comments': 5, 'rating': 5.0}, {'id': 2, 'blog_id': 1, 'headline': 'comiccon', 'body_text': 'movie details', 'pub_date': datetime.date(2024, 6, 19), 'number_of_comments': 7, 'rating': 5.0}]>
>>> Entry.objects.filter(Q(headline__startswith="i")&Q(body_text__startswith="m")).values() 
<QuerySet []>
    """
