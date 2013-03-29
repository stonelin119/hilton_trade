# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ProductCategory(models.Model):
    id            = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=384)
    description   = models.CharField(max_length=3072)
    create_time   = models.DateTimeField(auto_now_add=True)
    update_time   = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u'product_category'

class ProductType(models.Model):
    id          = models.IntegerField(primary_key=True)
    category    = models.ForeignKey(ProductCategory)
    type_name   = models.CharField(max_length=384)
    description = models.CharField(max_length=3072)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u'product_type'

class ProductInfo(models.Model):
    id               = models.IntegerField(primary_key=True)
    product_type     = models.ForeignKey(ProductType)
    product_name     = models.CharField(max_length=384)
    description      = models.CharField(max_length=3072)
    photo            = models.CharField(max_length=3072)
    model            = models.CharField(max_length=384)
    product_package          = models.CharField(max_length=384)
    min_order_amount = models.CharField(max_length=384)
    create_time      = models.DateTimeField(auto_now_add=True)
    update_time      = models.DateTimeField(auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return ('product_detail', [str(self.id)])

    class Meta:
        db_table = u'product_info'

class ProductInfoDetail(models.Model):
    DETAIL_INFO_TYPE = (
        (1, 'Detail'),
        (2, 'Feature'),
        (3, 'Usage Method'),
        (4, 'Usage Scope'),
        )

    id                = models.IntegerField(primary_key=True)
    product_info_type = models.IntegerField(choices=DETAIL_INFO_TYPE, default=1)
    product_info      = models.ForeignKey(ProductInfo)
    description       = models.CharField(max_length=3072)
    create_time       = models.DateTimeField(auto_now_add=True)
    update_time       = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = u'product_info_detail'

