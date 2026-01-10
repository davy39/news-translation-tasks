---
title: Python Attributes – Class and Instance Attribute Examples
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-12T02:17:19.000Z'
originalURL: https://freecodecamp.org/news/python-attributes-class-and-instance-attribute-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pyAttributes.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'When creating a class in Python, you''ll usually create attributes that
  may be shared across every object of a class or attributes that will be unique to
  each object of the class.

  In this article, we''ll see the difference between class attributes and ...'
---

When creating a `class` in Python, you'll usually create attributes that may be shared across every object of a class or attributes that will be unique to each object of the class.

In this article, we'll see the difference between class attributes and instance attributes in Python with examples.

Before we do that, let's see how to create a class in Python.

## How to Create a Class in Python

To create a class in Python, we use the `class` keyword followed by the name of the class. Here is an example:

```python
class Student:
    name = "Jane"
    course = "JavaScript"
```

In the code above, we created a class called `Student` with a `name` and `course` property. Now let's create new objects from this class.

```python
class Student:
    name = "Jane"
    course = "JavaScript"
    
Student1 = Student()

print(Student1.name)
# Jane
```

We've created a new object called `Student1` from the `Student` class.

When we printed `Student1.name`, we got "Jane" printed to the console. Recall that the value of Jane was stored in a variable in the original class created. 

This `name` and `course` variables are actually class attributes. We'll see more examples in the next section to help you understand better. 

## Class and Instance Attributes in Python

To give a basic definition of both terms, **class attributes** are class variables that are inherited by every object of a class. The value of class attributes remain the same for every new object. 

Like you will see in the examples in this section, class attributes are defined outside the `__init__()` function.

On the other hand, **instance attributes**, which are defined in the `__init__()` function, are class variables that allow us to define different values for each object of a class.

Here is an example:

```python
class Student:
    school = "freeCodeCamp.org"
    
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John

```

In the code above, we created a variable in the `Student` class called `school`.

We created two more variables but in the `__init__()` function – `name` and `course` – which we initialized using the `self` parameter. 

The first parameter in an `__init__()` function is used to initialize other parameters when creating variables in the function. You can call it whatever you want – by convention, `self` is mostly used. 

The `school` variable acts as a class attribute while `name` and `course` are instance attributes. Let's break the example above down to explain instance attributes.

```python
Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John
```

We created two objects from the `Student` class – `Student1` and `Student2`. Each of these objects, by default, will have all the variables created in the class. But each object is able to have its own `name` and `course` variable because they were created in the `__init__()` function. 

Now let's print the `school` variable for each object and see what happens.

```python
print(Student1.school) # freeCodeCamp.org
print(Student2.school) # freeCodeCamp.org
```

Both gave us the same value because the `school` variable is a class attribute.

## Conclusion

In this article, we saw how to create a class in Python and the differences between class and instance attributes.

In summary, **class attributes** remain the same for every object and are defined outside the `__init__()` function. **Instance attributes** are somewhat dynamic because they can have different values in each object.

**Instance attributes** are defined in the `__init__()` function.

Happy coding!

