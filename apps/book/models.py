from django.db import models
from django.utils.text import slugify


class LibraryBranch(models.Model):
    Library_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.Library_name

class Catagory(models.Model):

    catagory_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.catagory_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.catagory_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag_name


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.author_name

class Publisher(models.Model):
    Publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Publisher_name



class Book(models.Model):

    # Basic Information
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    B_title = models.CharField(max_length=200,  default="Untitled")
    isbn = models.CharField(max_length=50, blank=True, unique=True)
    call_no = models.CharField(max_length=50, blank=True, unique=True)
    year = models.IntegerField(blank=True, null=True)
    ddc_no = models.CharField(max_length=50, blank=True)
    Description = models.TextField(blank=True, null=True)

    #Foreign Keys and Relations
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    library = models.ForeignKey(LibraryBranch, on_delete=models.SET_NULL, null=True, blank=True)


    # Status Info
    volume = models.IntegerField(default=1)
    pages = models.IntegerField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)

    # Librarty Spacific Fields
    shelf_no = models.IntegerField(blank=True, null=True)
    added_by = models.CharField(max_length=100, blank=True, null=True)
    date_of_inclusion = models.DateField(blank=True, null=True)
    no_of_copy = models.IntegerField(default=1)



    # Toocle Fields

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.B_title








    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    # language = models.CharField(max_length=100, blank=True)
    # library = models.ForeignKey(LibraryBranch, on_delete=models.SET_NULL, null=True)
    # total_volumes = models.PositiveIntegerField(null=True, blank=True)
    # status = models.CharField(max_length=20, choices=STATUS, default="draft")
    # # book_type = models.CharField(max_length=100, blank=True)
    # # edition = models.CharField(max_length=100, blank=True)
    # # publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    # # publishing_year = models.PositiveIntegerField(null=True, blank=True)
    # # isbn = models.CharField(max_length=20, blank=True)
    # # pages = models.PositiveIntegerField(null=True, blank=True)
    # # catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)
    # # ddc_no = models.CharField(max_length=20, blank=True)
    # # tags = models.ManyToManyField(Tag, blank=True)
    # # added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # # notes = models.TextField(blank=True)
    # # shelf_no = models.CharField(max_length=50, blank=True, null=True)




    # def __str__(self):
    #     return self.B_title


# Create your models here.
