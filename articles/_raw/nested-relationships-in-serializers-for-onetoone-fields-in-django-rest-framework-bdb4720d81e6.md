---
title: Nested Relationships in Serializers for OneToOne fields in Django Rest Framework
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-08T16:39:22.000Z'
originalURL: https://freecodecamp.org/news/nested-relationships-in-serializers-for-onetoone-fields-in-django-rest-framework-bdb4720d81e6
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb2fe740569d1a4cac5db.jpg
tags:
- name: Django
  slug: django
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bharath Kallur

  The Django Rest Framework (DRF) is one of the effectively written frameworks around
  Django and helps build REST APIs for an application back-end.

  I was using it in one of my personal projects and stumbled upon this challenge of
  “ser...'
---

By Bharath Kallur

The Django Rest Framework ([DRF](http://www.django-rest-framework.org/)) is one of the effectively written frameworks around Django and helps build REST APIs for an application back-end.

I was using it in one of my personal projects and stumbled upon this challenge of “serializing a model which is referencing another model via [OneToOne field](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.OneToOneField).”

`I was using the **User** model from `[django.contrib.auth.models](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/)`. I wanted to write an API to create and update a user object through a single API which also updates my model’s attributes. The solution was to use DRF’s **Nested Relationships** in serialization.

I shall assume you have a fair working knowledge of Python, virtualenv, pip, Django and DRF before proceeding. If not, please learn more and feel free to return if you are ever stuck on nested relationships in serialization.

The example I am considering here is a **University Student** model, referencing **User** model via the OneToOne field. My goal is a single API for creating and getting user details like name, username, and email along with a student attribute such as subject major.

Here is how my `**models.py**` looks:

```py
from django.db import models
from django.contrib.auth.models import User

class UnivStudent(models.Model):
    """
    A class based model for storing the records of a university student
    Note: A OneToOne relation is established for each student with User model.
    """
    user = models.OneToOneField(User)
    subject_major = models.CharField(name="subject_major", max_length=60)
```

Next, the serializer for the above model determines the attributes to manipulate. If you observe below, I have 2 serializer classes, `**UserSerializer**` and `StudentSerializer`. This is our point of interest.

I have declared a `user` attribute which is a serializer field here. That `user` attribute will primarily hold the entire reference for the `UserSerializer` class. In the **fields** of `StudentSerializer` , we just see ‘`user`’ and ‘`subject_major`’. This allows us to enter the student (or user) attributes along with the subject_major.

A user entry is created which is referenced by the student entry. We override the create method of `StudentSerializer` to create a `user` object first, and use that to create the `student` object.

The `**serializer.py**` is as follows:

```py
from rest_framework import serializers, status
from models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class StudentSerializer(serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserSerializer(required=True)

    class Meta:
        model = UnivStudent
        fields = ('user', 'subject_major',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = UnivStudent.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return student
```

The `**views.py**` should be quite straightforward if you are already familiar with the [class-based views](https://docs.djangoproject.com/en/1.11/topics/class-based-views/) of Django. We will be using the serializer to validate and create the model objects:

```py
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentRecordView(APIView):
    """
    A class based view for creating and fetching student records
    """
    def get(self, format=None):
        """
        Get all the student records
        :param format: Format of the student records to return to
        :return: Returns a list of student records
        """
        students = UnivStudent.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a student record
        :param format: Format of the student records to return to
        :param request: Request object for creating student
        :return: Returns a student record
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
```

I have included `/univstud/` `url` for achieving `post` and `get` requests for university student.

```py
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from OneToOne import views


admin.autodiscover()
router = routers.DefaultRouter()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns += format_suffix_patterns([
    # API to map the student record
    url(r'^api/univstud/$',
        views.StudentRecordView.as_view(),
        name='students_list'),
])
```

The `**POST**` request call would look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*AxmyhgMuhoFfved4pSDUhw.png)
_post call for /univstud/_

The `**Get**` request call would look something like this:



![Image](https://cdn-media-1.freecodecamp.org/images/1*FGXTNU4Fri9iTO2ab1mRqA.png)
_get call for /univstud/_

That’s all!:)

Nested Relationship is thus enabled on `**StudentSerializer**` to reference `user`.

Complete code is in [my gitlab](https://gitlab.com/bharathkallurs/writeup/tree/master) repository.

### References:

1. [http://www.django-rest-framework.org/api-guide/relations/](http://www.django-rest-framework.org/api-guide/relations/)

