---
title: Relations imbriquées dans les Serializers pour les champs OneToOne dans Django
  Rest Framework
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
seo_title: Relations imbriquées dans les Serializers pour les champs OneToOne dans
  Django Rest Framework
seo_desc: 'By Bharath Kallur

  The Django Rest Framework (DRF) is one of the effectively written frameworks around
  Django and helps build REST APIs for an application back-end.

  I was using it in one of my personal projects and stumbled upon this challenge of
  “ser...'
---

Par Bharath Kallur

Le Django Rest Framework ([DRF](http://www.django-rest-framework.org/)) est l'un des frameworks les mieux écrits autour de Django et aide à construire des API REST pour un backend d'application.

Je l'utilisais dans l'un de mes projets personnels et j'ai rencontré ce défi de « sérialiser un modèle qui référence un autre modèle via un [champ OneToOne](https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.OneToOneField) ».

`J'utilisais le modèle **User** de `[django.contrib.auth.models](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/)`. Je voulais écrire une API pour créer et mettre à jour un objet utilisateur via une seule API qui met également à jour les attributs de mon modèle. La solution était d'utiliser les **Relations Imbriquées** de DRF dans la sérialisation.

Je suppose que vous avez une connaissance de travail équitable de Python, virtualenv, pip, Django et DRF avant de continuer. Si ce n'est pas le cas, veuillez en apprendre davantage et n'hésitez pas à revenir si vous êtes bloqué sur les relations imbriquées dans la sérialisation.

L'exemple que je considère ici est un modèle **University Student**, référençant le modèle **User** via le champ OneToOne. Mon objectif est une seule API pour créer et obtenir les détails de l'utilisateur comme le nom, le nom d'utilisateur et l'email ainsi qu'un attribut étudiant tel que la matière principale.

Voici à quoi ressemble mon `**models.py**` :

```py
from django.db import models
from django.contrib.auth.models import User

class UnivStudent(models.Model):
    """
    Un modèle basé sur une classe pour stocker les enregistrements d'un étudiant universitaire
    Remarque : Une relation OneToOne est établie pour chaque étudiant avec le modèle User.
    """
    user = models.OneToOneField(User)
    subject_major = models.CharField(name="subject_major", max_length=60)
```

Ensuite, le serializer pour le modèle ci-dessus détermine les attributs à manipuler. Si vous observez ci-dessous, j'ai 2 classes de serializer, `**UserSerializer**` et `StudentSerializer`. C'est notre point d'intérêt.

J'ai déclaré un attribut `user` qui est un champ de serializer ici. Cet attribut `user` contiendra principalement toute la référence pour la classe `UserSerializer`. Dans les **fields** de `StudentSerializer`, nous voyons simplement '`user`' et '`subject_major`'. Cela nous permet de saisir les attributs de l'étudiant (ou de l'utilisateur) ainsi que le subject_major.

Une entrée utilisateur est créée qui est référencée par l'entrée étudiant. Nous remplaçons la méthode create de `StudentSerializer` pour créer un objet `user` d'abord, et utiliser celui-ci pour créer l'objet `student`.

Le `**serializer.py**` est le suivant :

```py
from rest_framework import serializers, status
from models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class StudentSerializer(serializers.ModelSerializer):
    """
    Un serializer d'étudiant pour retourner les détails de l'étudiant
    """
    user = UserSerializer(required=True)

    class Meta:
        model = UnivStudent
        fields = ('user', 'subject_major',)

    def create(self, validated_data):
        """
        Remplacement de la méthode create par défaut du Model serializer.
        :param validated_data: données contenant tous les détails de l'étudiant
        :return: retourne un enregistrement d'étudiant créé avec succès
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = UnivStudent.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return student
```

Le `**views.py**` devrait être assez simple si vous êtes déjà familier avec les [vues basées sur les classes](https://docs.djangoproject.com/en/1.11/topics/class-based-views/) de Django. Nous allons utiliser le serializer pour valider et créer les objets de modèle :

```py
from serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentRecordView(APIView):
    """
    Une vue basée sur une classe pour créer et récupérer des enregistrements d'étudiants
    """
    def get(self, format=None):
        """
        Obtenir tous les enregistrements d'étudiants
        :param format: Format des enregistrements d'étudiants à retourner
        :return: Retourne une liste d'enregistrements d'étudiants
        """
        students = UnivStudent.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Créer un enregistrement d'étudiant
        :param format: Format des enregistrements d'étudiants à retourner
        :param request: Objet de requête pour créer un étudiant
        :return: Retourne un enregistrement d'étudiant
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
```

J'ai inclus l'`url` `/univstud/` pour réaliser les requêtes `post` et `get` pour les étudiants universitaires.

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
    # API pour mapper l'enregistrement de l'étudiant
    url(r'^api/univstud/$',
        views.StudentRecordView.as_view(),
        name='students_list'),
])
```

L'appel de requête `**POST**` ressemblerait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*AxmyhgMuhoFfved4pSDUhw.png)
_appel post pour /univstud/_

L'appel de requête `**Get**` ressemblerait à ceci :



![Image](https://cdn-media-1.freecodecamp.org/images/1*FGXTNU4Fri9iTO2ab1mRqA.png)
_appel get pour /univstud/_

C'est tout!:)

La Relation Imbriquée est ainsi activée sur `**StudentSerializer**` pour référencer `user`.

Le code complet est dans mon [dépôt gitlab](https://gitlab.com/bharathkallurs/writeup/tree/master).

### Références :

1. [http://www.django-rest-framework.org/api-guide/relations/](http://www.django-rest-framework.org/api-guide/relations/)