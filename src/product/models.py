from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
# from django.core.urlresolvers import reverse

class Product(models.Model):
    PRDName = models.CharField(max_length=50,verbose_name=_("Product Name "))
    PRDCategory = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name=_("Product Category"), blank=True , null=True)
    PRDBrand = models.ForeignKey('settings.Brand',on_delete=models.CASCADE,verbose_name=_("Product Brand"), blank=True , null=True)
    PRDDesc = models.TextField(max_length=1000,verbose_name=_("Description"))
    PRDImage = models.ImageField(upload_to='product/' , verbose_name=_("Image"), blank=True , null=True)
    PRDCreated = models.DateTimeField(auto_now=True,verbose_name=_("Created At"))
    PRDPrice = models.DecimalField(max_digits=5 , decimal_places=2 ,verbose_name=_("Price"))
    PRDDiscountPrice = models.DecimalField(max_digits=5 , decimal_places=2 ,verbose_name=_("Discount Price"))
    PRDCost = models.DecimalField(max_digits=5, decimal_places=2,verbose_name=_("Cost"))
    PRDSLug = models.SlugField(blank=True, null=True , verbose_name=_("Product URL"))
    PRDISNew = models.BooleanField(default=True , verbose_name=_("New Product "))
    PRDISBestSeller = models.BooleanField(default=False , verbose_name=_("Best Sale"))

    def save(self , *args , **kwargs):
        if not self.PRDSLug : 
            self.PRDSLug = slugify(self.PRDName)
        super(Product , self).save(*args , **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.PRDSLug})

    def __str__(self):
        return self.PRDName

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
    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("Order_detail", kwargs={"pk": self.pk})




class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product , on_delete=models.CASCADE , verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product/' , verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model): #table 
    CATName = models.CharField(max_length=50,verbose_name=_("Category Name")) #column
    CATParent = models.ForeignKey('self',limit_choices_to={'CATParent__isnull':True}, on_delete=models.CASCADE, blank=True , null=True,verbose_name=_("Category Parent Name"))
    CATDesc = models.TextField(max_length=1000,verbose_name=_("Description"), blank=True , null=True)
    CATDImg = models.ImageField(upload_to='category/',verbose_name=_("Image"), blank=True , null=True)
    


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorios")


    def __str__(self):
        return self.CATName


class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='main_product' , verbose_name=_("Product"))
    PALNAlternatives = models.ManyToManyField(Product , related_name='alternative_products'  , verbose_name=_("Alternatives"))
    

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)


class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='mainAccessory_product' , verbose_name=_("Product"))
    PACCAlternatives = models.ManyToManyField(Product , related_name='accessories_products' , verbose_name=_("Accessories"))
    

    class Meta:
        verbose_name = _("Accessory")
        verbose_name_plural = _("Accessorios")

    def __str__(self):
        return str(self.PACCProduct)

    
