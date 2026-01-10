---
title: Comment comprendre les modèles Django de manière simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T15:03:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-django-models-the-simple-way-20c39d234870
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lVq4xiiufKeBVM-lMkfp4w.jpeg
tags:
- name: Django
  slug: django
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment comprendre les modèles Django de manière simple
seo_desc: 'By Tim

  Have you ever tried to learn models by going through Django Docs? Did you leave
  with answers, or with even more questions?

  Personally, I started doubting whether programming was really for me.


  I wrote this post to help you understand Django m...'
---

Par Tim

Avez-vous déjà essayé d'apprendre les modèles en parcourant la documentation de Django ? Êtes-vous reparti avec des réponses, ou avec encore plus de questions ?

Personnellement, j'ai commencé à douter que la programmation était vraiment faite pour moi.

![Image](https://cdn-media-1.freecodecamp.org/images/JYSUn5CYYdtqeizDCoFRLj0TuITQ9vtyc1jJ)

J'ai écrit cet article pour vous aider à comprendre les modèles Django afin que vous puissiez effectuer des opérations de base avec eux. Les modèles sont une excellente façon de travailler avec les données.

Disons que nous voulons garder une trace de nos chats incroyables. Nous pourrions créer un modèle `Cat` — mais qu'est-ce qu'un modèle, au fait ?

Il s'avère qu'un modèle est en quelque sorte trois choses en une :

![Image](https://cdn-media-1.freecodecamp.org/images/GuS7UajURN4a0FobnqcMoZEnzM0bHFOnyNKD)

Maintenant, parcourons chaque bloc.

### Table avec les chats dans la base de données

![Image](https://cdn-media-1.freecodecamp.org/images/jU6jTPJj2rP4845S04dllZ436k5FhqwRkp23)

Nous avons créé une classe (= un modèle) nommée `Cat`.

Lorsque nous ajoutons des colonnes, nous devons indiquer à Django quel type de données sera dans chacune d'elles. Cela peut être du texte, des chiffres ou des booléens, entre autres.

Dans ce cas, le nom du chat doit être en texte — c'est un `CharField` dans Django. N'oubliez pas de définir la longueur maximale pour ce champ, car la base de données doit la connaître. Le poids du chat en grammes est un entier — nous utilisons donc un `IntegerField`. Juste une note : la colonne `id` est générée automatiquement.

Enfin, `null` permet de laisser une colonne vide. Par exemple, nous ne connaissons peut-être pas le poids. Notez que n'importe quel champ peut être marqué comme `null`.

Pour la touche finale, nous allons propager les changements (comme la création d'un modèle ou l'ajout d'une colonne) dans notre schéma de base de données. Pour cela, nous utilisons `python manage.py makemigrations` puis `python manage.py migrate`. Il est important de faire cela chaque fois que vous changez quelque chose dans les modèles.

Maintenant, nous avons une table, mais elle est vide. Corrigons cela.

### Opérations avec tous les chats

#### Créer une entrée

![Image](https://cdn-media-1.freecodecamp.org/images/TtimGYiyb1dYv0SwkEXjMwmBeFXpvKVBHmXO)

La fonction `create()` nous aide à créer des lignes. Nous devons simplement lui passer tous les détails poilus.

#### Trouver un chat en particulier

![Image](https://cdn-media-1.freecodecamp.org/images/cJuSzgi52alAYcSrHnFl6gYmany7bXjTzeMw)

Si vous voulez obtenir le dossier du FBI du chat — miaou-xcusez-moi, je veux dire les informations du chat — utilisez simplement la fonction `get()` avec l'un des paramètres du chat. Dans l'exemple, j'utilise `pk` qui signifie « clé primaire ». Le plus souvent, cela serait la même chose que d'utiliser `id`.

`get()` trouvera toutes les lignes correspondant aux paramètres et ne retournera que la première.

#### Trouver tous les enregistrements

![Image](https://cdn-media-1.freecodecamp.org/images/Lp3fYKZLOfUdZ2Nbyd7qsfpQGiLQsTSC5J4m)

En plus de cela, vous pouvez accéder à tous les chats de la base de données en utilisant la fonction `all()`.

#### Filtrer

![Image](https://cdn-media-1.freecodecamp.org/images/VRzM3BkoKNR-2pOhocUCalrq2UztpjJvKNZ2)

Ou avez-vous besoin de chats pesant moins de 3000g ?

Une fonction nommée `filter` est prête à vous aider avec cela.

Nous lui passons `field__lookuptype = 'value'` pour filtrer les chats.

Dans l'exemple, `lt` signifie « moins que ». Donc `weight_g__lt=3000` signifie « le poids est inférieur à 3000g ».

### Opérations avec un chat

#### Mettre à jour

![Image](https://cdn-media-1.freecodecamp.org/images/r1zJmKtyA5pWgNzah3AfPjXKOal2LQDVjkb1)

La dernière fois que nous avons pesé Luna, elle pesait 3200g. Mais maintenant, son poids est de 3100g. Il est très facile de changer cela.

Nous récupérons simplement Luna de la base de données par son nom, puis nous changeons son poids à 3100. C'est aussi simple que cela. Juste une chose — nous devons appeler `.save()` lorsque nous avons terminé les modifications.

#### Supprimer, pour de bon

![Image](https://cdn-media-1.freecodecamp.org/images/5Yh2AvxsVYbUBmSGzV6FRCc4hlpYQv5cm9bG)

Nous pouvons supprimer l'un de nos chats. Nous récupérons le chat et appelons la fonction `.delete()`.

Très triste. Mais c'est la vie.

Avez-vous aimé cet article ? Donnez-moi quelques applaudissements pour que plus de gens le voient. Merci !

L'article a été publié à l'origine sur [mon blog](https://arevej.me/django-models/).

[Abonnez-vous à la fin de l'article original](https://arevej.me/django-models/) pour recevoir mes nouveaux articles dans votre boîte de réception et apprendre Django ensemble.