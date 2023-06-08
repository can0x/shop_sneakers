from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(null=True, upload_to='images/users', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_admin=False, is_staff=False,
                    is_active=True):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)  # change password to hash
        user.profile_picture = profile_picture
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, profile_picture, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        user.profile_picture = profile_picture
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user


class Task(models.Model):
    title = models.CharField('name', max_length=50)
    task = models.TextField('Опис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = "Задачі"


class Sneakers(models.Model):
    sneakers_id = models.IntegerField()
    name = models.CharField('name', max_length=50)
    brand = models.CharField('brand', max_length=50)
    image = models.ImageField(null=True, upload_to='images/snicker', blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    info = models.TextField('Опис')

    def __str__(self):
        return self.name


class Account(models.Model):
    username = models.CharField(max_length=50, default='john_doe')
    email = models.EmailField(max_length=254, default='john.doe@example.com')
    password = models.CharField(max_length=50, default='password123')

    def str(self):
        return self.username

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password


class Orders(models.Model):
    customer_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="user")
    deliveryAddress = models.CharField(max_length=200, null=True)
    total_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    def order_items(self):
        order_items = OrderItem.objects.filter(order=self)
        return ', '.join(str(item.item.name) for item in order_items)

    order_items = property(order_items)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sneakers = models.ForeignKey(Sneakers, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def total_price(self):
        return self.quantity * self.item.price

    total_price = property(total_price)

# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.ForeignKey(
#         Category, on_delete=models.SET_NULL, null=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     details = models.TextField(null=True, blank=True,
#                                default="A moist, flavorful, cake with golden raisins, shredded carrots, This cake is /
#                                filled with a cream cheese filling. We also use this same recipe for our morning glory/
#                                that has a honey glaze on top instead of the frosting, great for breakfast.")
#     imagePath = models.CharField(max_length=200, default="f1.jpg")
#
#     def __str__(self) -> str:
#         return str(self.name)
# class Brands(models.Model):
#     name = models.CharField('name', max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Categories(models.Model):
#     name = models.CharField('name', max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Order_Details(models.Model):
#     name = models.CharField('name', max_length=50)
#     number = models.CharField('Код', max_length=50)
#     info = models.CharField('Інформація', max_length=255)
#     quantity = models.CharField('Кількість', max_length=10)
#     price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
#
#     def __str__(self):
#         return self.number
#
#
# class Customers(models.Model):
#     customer_id = models.CharField(max_length=50, default=1)
#     first_name = models.CharField('Name', max_length=255)
#     last_name = models.CharField('Surname', max_length=255)
#     email = models.CharField('email', max_length=255)
#     password = models.CharField('password', max_length=50)
#     address = models.CharField('address', max_length=50)
#     phone_number = models.CharField('phone_number', max_length=12)
#
#     def __str__(self):
#         return self.first_name, self.last_name
