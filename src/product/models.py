from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
# from django.core.urlresolvers import reverse

class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name=_("Product Name "))
    category = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name=_("Product Category"), blank=True , null=True)
    brand = models.ForeignKey('settings.Brand',on_delete=models.CASCADE,verbose_name=_("Product Brand"), blank=True , null=True)
    desc = models.TextField(max_length=1000,verbose_name=_("Description"))
    image = models.ImageField(upload_to='product/' , verbose_name=_("Image"), blank=True , null=True)
    created = models.DateTimeField(auto_now=True,verbose_name=_("Created At"))
    price = models.DecimalField(max_digits=5 , decimal_places=2 ,verbose_name=_("Price"))
    discountprice = models.DecimalField(max_digits=5 , decimal_places=2 ,verbose_name=_("Discount Price"))
    cost = models.DecimalField(max_digits=5, decimal_places=2,verbose_name=_("Cost"))
    slug = models.SlugField(blank=True, null=True , verbose_name=_("Product URL"))
    newproduct = models.BooleanField(default=True , verbose_name=_("New Product "))
    bestseller = models.BooleanField(default=False , verbose_name=_("Best Sale"))

    def save(self , *args , **kwargs):
        if not self.slug : 
            self.slug = slugify(self.name)
        super(Product , self).save(*args , **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class ProductOrder(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = _("ProductOrder")
        verbose_name_plural = _("ProductOrders")

    def __str__(self):
        return str(self.PRDName)

    # def get_absolute_url(self):
    #     return reverse("ProductOrder_detail", kwargs={'slug': self.slug})


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
        
    items = models.ManyToManyField(ProductOrder)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("Order_detail", kwargs={"pk": self.pk})


class ProductImage(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=_("Product"))
    productimage = models.ImageField(upload_to='product/' , verbose_name=_("Image"))

    def __str__(self):
        return str(self.product)


class Category(models.Model): #table 
    name = models.CharField(max_length=50,verbose_name=_("Category Name")) #column
    parent = models.ForeignKey('self',limit_choices_to={'parent__isnull':True}, on_delete=models.CASCADE, blank=True , null=True,verbose_name=_("Category Parent Name"))
    desc = models.TextField(max_length=1000,verbose_name=_("Description"), blank=True , null=True)
    categoryimge = models.ImageField(upload_to='category/',verbose_name=_("Image"), blank=True , null=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorios")


    def __str__(self):
        return self.name


class Product_Alternative(models.Model):
    alternativeproduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_product' , verbose_name=_("Product"))
    alternatives = models.ManyToManyField(Product , related_name='alternative_products'  , verbose_name=_("Alternatives"))
    

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.alternativeproduct)


class Product_Accessories(models.Model):
    accessoriesproduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='mainAccessory_product' , verbose_name=_("Accessories"))
    accessoriesalternatives = models.ManyToManyField(Product , related_name='accessories_products' , verbose_name=_("Products"))
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.accessoriesproduct)
        super(Product_Accessories,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Accessory")
        verbose_name_plural = _("Accessorios")

    def __str__(self):
        return str(self.accessoriesproduct)

    
