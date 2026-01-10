---
title: Django Model Fields – Common Use Cases and How They Work
subtitle: ''
author: Victoria (Burah) Poromon
co_authors: []
series: null
date: '2023-11-23T00:03:28.000Z'
originalURL: https://freecodecamp.org/news/common-django-model-fields-and-their-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Django-models-article-cover.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: null
seo_desc: 'Django model fields define the structure of a database within a Django
  web application. Using this essential component will keep your work organized and
  help you make fewer mistakes in your code.

  This article will discuss some common Django model fie...'
---

Django model fields define the structure of a database within a Django web application. Using this essential component will keep your work organized and help you make fewer mistakes in your code.

This article will discuss some common Django model fields and how to use them in your code.

To get the most out of this article, you should have at least a basic knowledge of Django and understand how object-oriented programming works.

## What is a Model Field?

A model field is a data type that stores a specific type of data. Each model field represents specific data, such as numbers, dates, texts, or even relationships with other models.

Fields contain in-built validations for specific types of data. Therefore, an IntegerField will not accept letters of the alphabet, for example. Every field is specific to its purpose.

## Common Django Model Fields

You need to import the models module from the Django database to use the Django fields. It will ensure that the data type you store in your database column is well-defined.

This section will discuss Django's common model field types and how to use them.

### The `CharField` Model Field

This field stores short-medium length characters or text strings, which makes it suitable to store an attribute like a name. `CharField` has a `max_length` parameter you must specify every time you use the field. But when you do not specify the field length, it defaults to 255 characters.

Below is an example of how to use `CharField` in your code:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
```

In the above code snippet, `max_length` sets the maximum length of the 'name' attribute to 20 characters.

### The `DateField` Model Field

This field stores dates in your model and has two optional parameters (`auto_now` and `auto_now_add`). The `auto_now` parameter sets the date every time you change or update data, while the `auto_now_add` sets the field's date only when you create the data. 

The following is an example of how you can use the date field:

```python
from django.db import models

class Product(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    
```

In the code snippet above, the product module has two `DateField`s. One sets the date when you create the data, and the other sets the date when you update the data.

### The `DateTimeField` Model Field

This field stores the date and time information in a model. Just like the `DateField`, the `DateTimeField` also has two parameters (`auto_now` and `auto_now_add`). They have the same function, except this field also sets the time.

### The `DecimalField` Model Field

This field stores decimal numbers in a database. You can use it to store numerical values like price, weight, and height. 

It has two parameters that you must specify when using it. They include:

* `max_digit`: This is the total number of digits allowed in the number. It includes all the digits to the left and right of the decimal point. This number must be greater than or equal to the decimal_places.
* `decimal_places`: This is the number of digits on the right side of the decimal point.

Here is an example of how to store data in the DecimalField:

```python
from django.db import models

class Product(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

In the above code snippet, the number of digits on both sides of the decimal point is 6. At the same time, the number of decimal places equals 2. Therefore, your program can only store prices like $2100.00.

### The `BooleanField` Model Field

This field stores boolean values. You can perform simple binary operations with this field.

For example:

```python
from django.db import models

class Product(models.Model):
    add_to_cart = models.BooleanField(default=False)
```

In the above product model, the `BooleanField` is set to a default value of False, which means that products are outside your cart by default. It also means you can click to add or remove a product from your cart anytime.

### The `EmailField` Model Field

The `EmailField` is a specialized form of `CharField` that stores email addresses. When you use this field, it makes sure that the value you provide is a valid email address. Otherwise, it returns an error. 

Here is how to use this field in your project:

```python
from django.db import models

class Customer(models.Model):
    email = models.EmailField()
```

The above program ensures that your customer enters a valid email address into the database.

### The `TextField` Model Field

A `TextField` stores large amounts of text data. This field is useful when storing text data that is too long for a `CharField`. It can handle long-form texts like paragraphs and even entire documents.

Here is an example of how you can use this field:

```python
from django.db import models

class Product(models.Model):
    comments = models.TextField()
```

In the above example, the Product model has a `TextField` named 'Comments'. This field will store the customer's comments on products.

### The `IntegerField` Model Field

This field stores integer values in the form of whole numbers. These values range from -2147483648 to 0 for negative integers and 0 to 2147483647 for positive integers. So it can store any integer value, either positive or negative.

According to your project's needs, you can constrain this field to only store a positive or a negative value by using `PositiveIntegerField` or `NegativeIntegerField`, respectively. 

Below is an example of how to store data in the IntegerField:

```python
from django.db import models

class Product(models.Model):
    available_quantity = models.PositiveIntegerField()
```

In this example, the model has a field that stores the number of available products. The `PositiveIntegerField` ensures that the available quantity is a non-negative integer and only valid quantities can be in the field

### The `TimeField` Model Field

The TimeField is a field that stores time information in your model. It has two parameters, just like the DateField. 

Here is an example of how to use this field:

```python
from django.db import models

class Order(models.Model):
    time_placed = models.TimeField(auto_now_add=True)
```

In the above example, the `time_placed` field automatically displays the current time whenever there is a new order.

### The `ForeignKeyField` Model Field

The `ForeignKey` field type creates a many-to-one relationship between two models. This field is helpful when one model (the child model) needs to reference another (the parent model). It has two required parameters, the class to which the model is related and the `on_delete` option. 

Below is an example of how to use the `ForeignKey`:

```python
from django.db import models

class Customer(models.Model):
    email = models.EmailField()

class Order(models.Model):
    order_number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
```

The `ForeignKey` links each order to a specific customer in the above code snippet. It also allows for one customer to be associated with many orders. The `on_delete` option specifies that if you delete a referenced customer, all orders relating to that customer should also leave the database.

### The `ManyToManyField` Model Field

This field type represents a Many-to-many relationship between two models. It implies that you can associate a record in one model with many records in another and vice versa. This field has a required parameter, the class to which the model is related.

Here is an example of how to use this field:

```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)

class Order(models.Model):
    order_number = models.CharField(max_length=10)
    products = models.ManyToManyField(Product)
```

In the preceding code, the 'order' model has a 'products' field that establishes a many-to-many relationship with the 'product' model. Therefore, an order can contain multiple products, and a product can be in multiple orders.

### The `OneToOneField` Model Field

The `OneToOne` field type creates a one-to-one relationship between two models. It means that each record in one model will correspond to exactly one record from another. This field has one required parameter, the class to which the model is related.

Below is an example of how to use the `OneToOneField`:

```python
from django.db import models

class Customer(models.Model):
    email = models.EmailField()

class CustomerProfile(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
```

In the above example, the `CustomerProfile` links to the customer through the `OneToOneField`. It ensures that each Customer can have exactly one `CustomerProfile` and each `CustomerProfile` is associated with only one Customer. The additional parameter `on_delete=models.CASCADE` simply tells the program to remove the `CustomerProfile` whenever the Customer is removed.

## Conclusion

Django model fields empower you to build efficient data structures for your web applications. Field types help you eliminate human errors by enforcing the kind of data in a particular field.

In this article, you have seen some of the common field types in Django and how to use them to store your data. As you continue to build your Django projects, the knowledge from understanding and implementing these model fields will be invaluable in creating reliable applications for your users.

