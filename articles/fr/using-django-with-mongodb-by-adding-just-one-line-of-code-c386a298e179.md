---
title: Comment utiliser Django avec MongoDB en ajoutant une seule ligne de code.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-04T10:40:40.000Z'
originalURL: https://freecodecamp.org/news/using-django-with-mongodb-by-adding-just-one-line-of-code-c386a298e179
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eu9UNWEULdOQb9K1XvDmhg.png
tags:
- name: Django
  slug: django
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Django avec MongoDB en ajoutant une seule ligne de code.
seo_desc: 'By Siddy Zen

  To use MongoDB as your backend database in your Django project, just add this one
  line into your settings.py file:

  DATABASES = {   ‘default’: {      ‘ENGINE’: ‘djongo’,      ‘NAME’: ‘your-db-name’,   }}

  It’s that simple!

  Next, login to y...'
---

Par Siddy Zen

Pour utiliser [MongoDB comme base de données backend dans votre projet Django](http://nesdis.github.io/djongo/), ajoutez simplement **cette ligne** dans votre fichier settings.py :

```
DATABASES = {   'default': {      'ENGINE': 'djongo',      'NAME': 'your-db-name',   }}
```

C'est aussi simple que cela !

Ensuite, connectez-vous à votre page d'administration (localhost:8000/admin/) et commencez à ajouter des "documents intégrés" dans MongoDB en utilisant l'interface graphique de l'Admin :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZkPNUvkWB5VoMn6bEoKxPA.jpeg)

En octobre 2017, MongoDB a terminé la dernière étape pour devenir public, [fixant son IPO à 24 $](https://www.mongodb.com/press/mongodb-inc-announces-pricing-of-initial-public-offering) et levant 192 millions de dollars dans le processus. Les finances de l'entreprise ont augmenté de manière constante :

MongoDB fournit un logiciel de base de données open source. Cela est très utile pour les startups en phase de démarrage cherchant à se lancer tout en étant contraintes par des budgets serrés. Une revue des tendances de recherche Google pour MongoDB a révélé une augmentation constante de l'intérêt.

![Image](https://cdn-media-1.freecodecamp.org/images/1*76GlEAQiLFt4eGsFaiJIIw.jpeg)
_Google Trends — Terme de recherche : MongoDB_

MongoDB est de plus en plus populaire comme logiciel de base de données. Les bases de données et les systèmes de gestion de bases de données (SGBD) existent depuis plus de cinq décennies. Ils sont apparus au début des années 1960, et le type le plus populaire était le système de base de données relationnelle.

Mais MongoDB se présente comme un système de base de données "non relationnelle", et fait de grandes déclarations sur son approche pour stocker les données. Alors, quel est exactement le grand avantage ici ?

#### MongoDB vs SQL

Pratiquement tous les systèmes de bases de données relationnelles utilisent le langage de requête structuré (SQL) (ou une version modifiée de celui-ci) pour communiquer avec le logiciel de gestion des données. Plusieurs cours universitaires sont entièrement dédiés à la compréhension et à la maîtrise de la syntaxe SQL.

SQL était devenu le langage de facto pour travailler avec tout logiciel de base de données (BD), propriétaire ou open source. Ensuite, MongoDB est arrivé et a décidé de montrer un mépris total pour ce langage ancien de puissance et a introduit une syntaxe de requête qui lui est propre.

> La langue est celle du Mordor que je ne prononcerai pas ici. En langue commune, cela dit : "Un anneau pour les gouverner tous. Un anneau pour les trouver. Un anneau pour les amener tous et dans les ténèbres les lier."

> -Gandalf (_de_ Le Seigneur des Anneaux)

**MongoDB sans schéma vs schéma SQL :** Dans une base de données SQL, il est impossible d'ajouter des données tant que vous n'avez pas défini des tables et des types de champs dans ce qu'on appelle un schéma. Dans une base de données MongoDB, les données peuvent être ajoutées n'importe où, à n'importe quel moment. Il n'est pas nécessaire de spécifier une conception de document ou même une collection à l'avance.

**Documents MongoDB vs tables SQL :** Les bases de données SQL fournissent un stockage de tables de données liées. Chaque ligne est un enregistrement différent. La conception est rigide : vous ne pouvez pas utiliser la même table pour stocker des informations différentes ou insérer une chaîne là où un nombre est attendu.

La base de données MongoDB stocke des documents de paires champ-valeur similaires à JSON. Des documents similaires peuvent être stockés dans une collection, qui est analogue à une table SQL. Cependant, vous pouvez stocker n'importe quelle donnée que vous souhaitez dans n'importe quel document — MongoDB ne se plaindra pas. Les tables SQL créent un modèle de données strict, il est donc difficile de faire des erreurs. MongoDB est plus flexible et indulgent, mais pouvoir stocker n'importe quelle donnée n'importe où peut entraîner des problèmes de cohérence.

Il existe une pléthore de contenu en ligne qui soutient que MongoDB n'est pas un sur-ensemble de SQL. Les applications qui fonctionnent sur SQL ne peuvent pas être portées sur MongoDB. Je vais me risquer à affirmer que, dans le contexte de Django, **MongoDB est un sur-ensemble de SQL**.

Alors, pourquoi la croyance populaire, selon laquelle MongoDB n'est pas un sur-ensemble de SQL, existe-t-elle ?

**MongoDB nécessite la dénormalisation des données :** Dans MongoDB, il n'y a pas de support pour les JOIN. Cela signifie que nous devons dénormaliser nos documents. Les documents dénormalisés entraînent des requêtes plus rapides, mais la mise à jour des informations de champ de document dans plusieurs documents dénormalisés sera significativement plus lente.

**Il n'y a pas de JOIN :** Les requêtes SQL offrent une clause JOIN puissante. Nous pouvons obtenir des données liées dans plusieurs tables en utilisant une seule instruction SQL. Dans les bases de données non relationnelles comme MongoDB, il n'y a pas de JOIN comme il y en aurait dans les bases de données relationnelles. Cela signifie que vous devez effectuer plusieurs requêtes et joindre les données manuellement dans votre code.

**Pas de transactions :** Dans les bases de données SQL, deux ou plusieurs mises à jour peuvent être exécutées dans une transaction — un wrapper tout ou rien qui garantit le succès ou l'échec. Si nous exécutons deux mises à jour individuellement, l'une pourrait réussir et l'autre échouer — laissant ainsi nos chiffres désynchronisés. Placer les mêmes mises à jour dans une transaction garantit que les deux réussissent ou échouent.

**Pas de contraintes de clé étrangère :** La plupart des bases de données SQL vous permettent d'appliquer des règles d'intégrité des données en utilisant des contraintes de clé étrangère. Cela garantit que toutes les lignes ont une clé étrangère valide pour le code qui correspond à une entrée dans la table de jointure, et s'assure qu'un enregistrement de la table de jointure n'est pas supprimé si une ou plusieurs lignes y font encore référence.

Le schéma applique ces règles pour que la base de données les suive. Il est impossible pour les développeurs ou les utilisateurs d'ajouter, de modifier ou de supprimer des enregistrements, ce qui pourrait entraîner des données invalides ou des enregistrements orphelins. Les mêmes options d'intégrité des données ne sont pas disponibles dans MongoDB. Vous pouvez stocker ce que vous voulez, indépendamment de tout autre document. Idéalement, un seul document serait la seule source de toutes les informations sur un élément.

#### Le besoin d'un modèle de base de données

Les objets sont l'abstraction de Python pour les données. Toutes les données dans un programme Python sont représentées par des objets ou par des relations entre objets. Bien que les objets soient un bon moyen de représenter les données, un problème se pose lorsque nous voulons **rendre les données persistantes**. La quantité de données pourrait être énorme, et elle doit être récupérée de la mémoire persistante rapidement et efficacement. Ce logiciel de base de données doit être utilisé pour stocker les objets. Un logiciel de base de données possible est un système relationnel basé sur SQL.

Un mappeur objet-relationnel (ORM) est une bibliothèque de code qui automatise le transfert des données stockées dans les tables de base de données relationnelles vers des objets Python utilisés dans le code Python. Les ORM fournissent une abstraction de haut niveau sur une base de données relationnelle qui permet à un développeur d'écrire du code Python au lieu de la syntaxe SQL pour créer, lire, mettre à jour et supprimer des données et des schémas dans leur base de données. Les développeurs peuvent utiliser le langage de programmation Python avec lequel ils sont à l'aise au lieu d'écrire des instructions SQL ou des procédures stockées.

Un exemple de framework ORM pour Python est SQLAlchemy. L'ORM SQLAlchemy présente une méthode d'association de classes Python définies par l'utilisateur avec des tables de base de données, et des instances de ces classes (objets) avec des lignes dans leurs tables correspondantes. Il inclut un système qui synchronise de manière transparente tous les changements d'état entre les objets et leurs lignes associées. Les frameworks web comme Flask utilisent SQLAlchemy pour stocker les données de manière persistante.

**ORM Django :** Django est livré avec son propre ORM ou modèle en abrégé. Le modèle est la source unique et définitive d'informations sur vos données. Il contient les champs et comportements essentiels des données que vous stockez. Généralement, chaque modèle correspond à une seule table de base de données. Le modèle Django permet également de basculer entre diverses bases de données relationnelles telles que Oracle SQL, MySQL ou MSSQL.

#### Utilisation de l'ORM Django pour ajouter des documents dans MongoDB

Supposons que vous souhaitiez créer une plateforme de blogging en utilisant Django avec MongoDB comme backend.

Dans votre fichier `app/models.py` de Blog, définissez le modèle `BlogContent` :

```
from djongo import models
from djongo.models import forms
```

```
class BlogContent(models.Model):    comment = models.CharField(max_length=100)    author = models.CharField(max_length=100)    class Meta:        abstract = True
```

Pour accéder au modèle en utilisant Django Admin, vous aurez besoin d'une définition de Form pour le modèle ci-dessus. Définissez-le comme indiqué ci-dessous :

```
class BlogContentForm(forms.ModelForm):    class Meta:        model = BlogContent        fields = (            'comment', 'author'        )
```

Maintenant, "intégrez" votre `BlogContent` à l'intérieur d'un `BlogPost` en utilisant le `EmbeddedModelField` comme suit :

```
class BlogPost(models.Model):    h1 = models.CharField(max_length=100)    content = models.EmbeddedModelField(        model_container=BlogContent,        model_form=BlogContentForm    )
```

C'est tout, vous êtes prêt ! Lancez Django Admin sur localhost:8000/admin/ et voici ce que vous obtenez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZkPNUvkWB5VoMn6bEoKxPA.jpeg)

Ensuite, supposons que vous souhaitiez "étendre" le champ auteur pour contenir plus que simplement le nom. Vous avez besoin à la fois d'un nom et d'un email. Rendez simplement le champ auteur un champ "intégré" au lieu d'un champ "char" :

```
class Author(models.Model):    name = models.CharField(max_length=100)    email = models.CharField(max_length=100)    class Meta:        abstract = True

class AuthorForm(forms.ModelForm):    class Meta:        model = Author        fields = (            'name', 'email'        )
```

```
class BlogContent(models.Model):    comment = models.CharField(max_length=100)    author = models.EmbeddedModelField(        model_container=Author,        model_form=AuthorForm    )    class Meta:        abstract = True
```

Si un article de blog a plusieurs contenus de plusieurs auteurs, définissez un nouveau modèle :

```
class MultipleBlogPosts(models.Model):    h1 = models.CharField(max_length=100)    content = models.ArrayModelField(        model_container=BlogContent,        model_form=BlogContentForm    )
```

Lancez Django Admin avec les nouvelles modifications et vous avez :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9ckp5M7dit8F_U9A78FrMA.jpeg)

#### Façons d'intégrer Django et MongoDB.

L'ORM Django se compose de plusieurs couches d'abstraction empilées les unes sur les autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l41TRyQAGHD5lg0LHXzzag.png)
_La pile de l'ORM Django_

En tant que développeur web, vous pouvez relever le défi de connecter Django à MongoDB de deux manières. Jetez un œil à la pile du framework Django ci-dessus pour deviner les points d'entrée possibles.

#### Utiliser un modèle compatible MongoDB

![Image](https://cdn-media-1.freecodecamp.org/images/1*dGgjMqDl6dzrVHJZdiPbfw.png)
_Passer des modèles Django à un ODM_

Vous pouvez complètement éviter d'utiliser les modèles Django "batteries incluses" dans votre projet. Utilisez plutôt un framework tiers comme MongoEngine ou Ming dans vos projets Django.

Choisir un modèle différent signifie que vous passez à côté de :

* 1500+ contributeurs principaux au projet
* [Corrections et résolution de tickets horaires](https://dashboard.djangoproject.com)

Vous réduisez l'expertise des modèles Django existants et augmentez celle du nouveau framework de modèle. Mais peut-être que le plus grand inconvénient est que votre projet ne peut pas utiliser les modèles contrib de Django ! Oubliez l'utilisation de l'Admin, des Sessions, des Utilisateurs, de l'Auth et d'autres modules contrib pour votre projet.

Certains de ces inconvénients sont compensés en créant une nouvelle branche de Django lui-même. Django-nonrel est une branche indépendante de Django qui ajoute le support des bases de données NoSQL à Django. [Django-nonrel](https://github.com/django-nonrel) permet d'écrire des applications Django portables. Cependant, l'interface d'administration ne fonctionne pas complètement. Il n'y a pas de développement actif en cours sur le projet Django-nonrel.

[Django MongoDB Engine](https://django-mongodb-engine.readthedocs.io/en/latest/) est un autre backend MongoDB pour Django qui est un fork de l'ODM MongoEngine.

#### Transpileur Django SQL vers MongoDB — [Djongo](http://nesdis.github.io/djongo/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*QpOq4GaUl_wX4_F6JYkQTA.png)
_Djongo — Le transpileur SQL vers MongoDB_

Une autre approche consiste à traduire la syntaxe des requêtes SQL Django générée par l'ORM Django en commandes pymongo. Djongo est un tel compilateur de requêtes SQL vers MongoDB. Il traduit chaque chaîne de requête SQL en un document de requête MongoDB. En conséquence, tous les modèles Django et les modules associés fonctionnent tels quels. Avec cette approche, vous gagnez :

* **Réutilisation des modèles Django :** Django est un framework stable avec un développement et des améliorations continus. L'ORM Django est assez complet et riche en fonctionnalités. Définir un ORM _tierce partie_ pour travailler avec MongoDB signifie reproduire l'ensemble de l'ORM Django à nouveau. Le nouvel ORM doit constamment s'aligner sur l'ORM Django. Plusieurs fonctionnalités de Django ne seront jamais intégrées dans l'ORM tierce partie. L'idée avec Djongo est de **réutiliser** les fonctionnalités existantes de l'ORM Django en traduisant finalement les requêtes SQL en syntaxe MongoDB.
* **La syntaxe SQL ne changera jamais** quelles que soient les futures additions à Django. En utilisant Djongo, votre projet est maintenant à l'épreuve du futur !

#### Faire fonctionner Django avec MongoDB

**Émuler le schéma dans MongoDB :** Bien qu'il n'y ait pas de support de schéma dans MongoDB, cela peut être émulé. Djongo fournit le support de schéma requis dans Django en utilisant et en définissant une combinaison de règles de validation MongoDB et en créant une collection `__schema__`. La collection `__schema__` stocke des informations pour supporter des fonctionnalités comme la clé AUTOINCREMENT SQL.

**Support des JOIN dans MongoDB :** Dans la version 3.2, MongoDB a introduit l'opérateur `$lookup`. Il effectue une jointure externe gauche vers une collection dans la même base de données pour filtrer les documents de la collection "jointe" pour le traitement. L'étape `$lookup` fait une correspondance d'égalité entre un champ des documents d'entrée et un champ des documents de la collection "jointe".

À chaque document d'entrée, l'étape `$lookup` ajoute un nouveau champ de tableau dont les éléments sont les documents correspondants de la collection "jointe". L'étape `$lookup` transmet ces documents remodelés à l'étape suivante.

Djongo utilise l'opérateur d'agrégation `$lookup` pour effectuer toutes les requêtes JOIN liées à Django. C'est ainsi qu'il fait fonctionner l'admin et d'autres modules contrib tels quels.

**Support des transactions dans MongoDB :** Malgré la puissance des opérations atomiques sur un seul document, il existe des cas qui nécessitent des transactions multi-documents. Lors de l'exécution d'une transaction composée d'opérations séquentielles, certains problèmes surviennent, où si une opération échoue, l'opération précédente au sein de la transaction doit "revenir en arrière" à l'état précédent — c'est-à-dire, "tout ou rien".

Pour les situations qui nécessitent des transactions multi-documents, Djongo implémente le modèle de [validation en deux phases](https://docs.mongodb.com/manual/tutorial/perform-two-phase-commits/) pour fournir un support pour ces types de mises à jour multi-documents. L'utilisation de la validation en deux phases garantit que les données sont cohérentes et, en cas d'erreur, l'état précédent la transaction est récupérable.

Djongo vient avec son propre ensemble de compromis, cependant. Quels sont donc les inconvénients de choisir d'utiliser Djongo pour votre projet Django ?

**Performance :** L'ORM Django fait le gros du travail de conversion des manipulations d'objets complexes en chaînes de requêtes SQL standard. Si votre base de données backend était basée sur SQL, vous pourriez passer cette chaîne de requête directement à celle-ci avec presque aucun post-traitement. Avec Djongo, cependant, la chaîne de requête devra maintenant être convertie en un document de requête MongoDB.

Cela va nécessiter quelques cycles CPU. Mais si les cycles CPU supplémentaires posent vraiment un problème, vous ne devriez probablement pas utiliser Python en premier lieu.

#### Conclusion

Je vous ai présenté plusieurs façons d'intégrer Django avec MongoDB. Vous trouverez une multitude de littérature en ligne décrivant MongoEngine et d'autres variantes pour faire cela.

Je me suis concentré sur [Djongo](http://nesdis.github.io/djongo/) qui est un nouveau connecteur qui rend cela possible d'une manière différente. Il est facile à utiliser et rend le processus de migration d'un backend SQL vers MongoDB très simple, **en ajoutant une seule ligne de code**.