# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.db import models


class Author(models.Model):
    authorid = models.AutoField(db_column='AuthorID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=45, blank=True, null=True)  # Field name made lowercase. 
    
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    class Meta:
        managed = True
        db_table = 'Author'


class Book(models.Model):
    bookid = models.AutoField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=45, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    pubdate = models.DateTimeField(db_column='PubDate', blank=True, null=True)  # Field name made lowercase.
    authorid = models.ForeignKey(Author, models.DO_NOTHING, db_column='AuthorID', blank=True, null=True)  # Field name made lowercase.
    publisherid = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='PublisherID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'Book'


class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CIty', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.
    discountpct = models.DecimalField(db_column='DiscountPct', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Customer'


class Price(models.Model):
    priceid = models.AutoField(db_column='PriceId', primary_key=True)  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID', blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='ListPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Price'


class Publisher(models.Model):
    publisherid = models.AutoField(db_column='PublisherID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=10, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Publisher'


class Sale(models.Model):
    saleid = models.AutoField(db_column='SaleID', primary_key=True)  # Field name made lowercase.
    saledate = models.DateTimeField(db_column='SaleDate', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='SalePrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID', blank=True, null=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Sale'
