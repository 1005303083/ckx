from django.db import models


# 基础类
class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

# 轮播图
# insert into axf_wheel(img,name,trackid)
class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'


# 导航
class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'


# 每日必购
class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'


# 部分商品
class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


# 商品列表
class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'


# 分类
class Foodtype(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'


# 商品
class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=256)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    marketprice = models.DecimalField(max_digits=6, decimal_places=2)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=10)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


class User(models.Model):
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=40, default='axf.png')
    rank = models.IntegerField(default=1)

    class Meta:
         db_table = 'axf_user'