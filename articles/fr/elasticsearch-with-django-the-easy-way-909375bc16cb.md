---
title: ElasticSearch avec Django de manière simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-13T21:43:09.000Z'
originalURL: https://freecodecamp.org/news/elasticsearch-with-django-the-easy-way-909375bc16cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ojvTsI-Asv1IIjdm61RzKw.jpeg
tags:
- name: Django
  slug: django
- name: elasticsearch
  slug: elasticsearch
- name: NoSQL
  slug: nosql
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: ElasticSearch avec Django de manière simple
seo_desc: 'By Adam Wattis

  A while back I was working on a Django project and wanted to implement fast free
  text search. Instead of using a regular database for this search function — such
  as MySQL or PostgreSQL — I decided to use a NoSQL database. That is when ...'
---

Par Adam Wattis

Il y a quelque temps, je travaillais sur un projet Django et je voulais implémenter une recherche en texte libre rapide. Au lieu d'utiliser une base de données régulière pour cette fonction de recherche — comme MySQL ou PostgreSQL — j'ai décidé d'utiliser une base de données NoSQL. C'est alors que j'ai découvert [ElasticSearch](https://www.elastic.co/).

ElasticSearch indexe des documents pour vos données au lieu d'utiliser des tables de données comme le fait une base de données relationnelle régulière. Cela accélère la recherche et offre de nombreux autres avantages que vous n'obtenez pas avec une base de données régulière. J'ai conservé une base de données relationnelle régulière pour stocker les détails des utilisateurs, les connexions et autres données que ElasticSearch n'avait pas besoin d'indexer.

Après avoir longtemps recherché comment implémenter correctement ElasticSearch avec Django, je n'ai pas vraiment trouvé de réponses satisfaisantes. Certains [guides ou tutoriels](https://qbox.io/blog/how-to-elasticsearch-python-django-part1) étaient compliqués et semblaient prendre des étapes inutiles pour indexer les données dans ElasticSearch. Il y avait beaucoup d'informations sur la façon d'effectuer des recherches, mais pas autant sur la façon dont l'indexation devait être faite. J'ai eu l'impression qu'il devait exister une solution plus simple, alors j'ai décidé d'essayer moi-même.

Je voulais garder cela aussi simple que possible, car les solutions simples tendent à être les meilleures, à mon avis. KISS (Keep It Simple Stupid), Less is More et tout cela résonne beaucoup avec moi, surtout lorsque toutes les autres solutions sont complexes. J'ai décidé d'utiliser l'exemple de Honza Král dans [cette vidéo](https://www.youtube.com/watch?v=1KHM7WvNeL4&t=1141s) pour avoir quelque chose sur quoi baser mon code. Je recommande de la regarder, bien qu'elle soit un peu obsolète à ce stade.

Puisque j'utilisais Django — qui est écrit en Python — il était facile d'interagir avec ElasticSearch. Il existe deux bibliothèques clientes pour interagir avec ElasticSearch en Python. Il y a [elasticsearch-py](https://elasticsearch-py.readthedocs.io/en/master/index.html), qui est le client officiel de bas niveau. Et il y a [elasticsearch-dsl](http://elasticsearch-dsl.readthedocs.io/en/latest/index.html), qui est construit sur le premier mais offre une abstraction de plus haut niveau avec un peu moins de fonctionnalités.

Nous allons bientôt entrer dans quelques exemples, mais d'abord, je dois clarifier ce que nous voulons accomplir :

* Installer ElasticSearch sur notre machine locale et s'assurer qu'il fonctionne correctement
* Configurer un nouveau projet Django
* Indexation en masse des données déjà présentes dans la base de données
* Indexation de chaque nouvelle instance qu'un utilisateur sauvegarde dans la base de données
* Un exemple de recherche de base

Très bien, cela semble assez simple. Commençons par installer ElasticSearch sur notre machine. De plus, tout le [code sera disponible sur mon GitHub](https://github.com/adamwattis/elasticsearch-example) afin que vous puissiez facilement suivre les exemples.

#### Installation d'ElasticSearch

Puisqu'ElasticSearch fonctionne avec Java, vous devez vous assurer d'avoir une version mise à jour de JVM. Vérifiez la version que vous avez avec `java -version` dans le terminal. Ensuite, exécutez les commandes suivantes pour créer un nouveau répertoire, télécharger, extraire et démarrer ElasticSearch :

```
mkdir elasticsearch-example
```

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.1.tar.gz
```

```
tar -xzf elasticsearch-5.1.1.tar.gz
```

```
./elasticsearch-5.1.1/bin/elasticsearch
```

Lorsque ElasticSearch démarre, une grande quantité de sortie doit être imprimée dans la fenêtre du terminal. Pour vérifier qu'il est opérationnel, ouvrez une nouvelle fenêtre de terminal et exécutez cette commande `curl` :

```
curl -XGET http://localhost:9200
```

La réponse doit être quelque chose comme ceci :

```
{  "name" : "6xIrzqq",  "cluster_name" : "elasticsearch",  "cluster_uuid" : "eUH9REKyQOy4RKPzkuRI1g",  "version" : {    "number" : "5.1.1",    "build_hash" : "5395e21",    "build_date" : "2016-12-06T12:36:15.409Z",    "build_snapshot" : false,    "lucene_version" : "6.3.0"  },  "tagline" : "You Know, for Search"
```

Super, vous avez maintenant ElasticSearch qui fonctionne sur votre machine locale ! Il est temps de configurer votre projet Django.

#### Configuration d'un projet Django

Tout d'abord, vous créez un environnement virtuel avec `virtualenv venv` et vous y entrez avec `source venv/bin/activate` afin de tout garder contenu. Ensuite, vous installez quelques packages :

```
pip install djangopip install elasticsearch-dsl
```

Pour démarrer un nouveau projet Django, vous exécutez :

```
django-admin startproject elasticsearchprojectcd elasticsearchprojectpython manage.py startapp elasticsearchapp
```

Après avoir créé vos nouveaux projets Django, vous devez créer un modèle que vous allez utiliser. Pour ce guide, j'ai choisi de prendre un bon vieux exemple de blog post. Dans `models.py`, vous placez le code suivant :

```
from django.db import modelsfrom django.utils import timezonefrom django.contrib.auth.models import User# Create your models here.# Blogpost to be indexed into ElasticSearchclass BlogPost(models.Model):   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')   posted_date = models.DateField(default=timezone.now)   title = models.CharField(max_length=200)   text = models.TextField(max_length=1000)
```

Assez simple, jusqu'à présent. N'oubliez pas d'ajouter `elasticsearchapp` à `INSTALLED_APPS` dans `settings.py` et d'enregistrer votre nouveau modèle BlogPost dans `admin.py` comme ceci :

```
from django.contrib import adminfrom .models import BlogPost# Register your models here.# Need to register my BlogPost so it shows up in the adminadmin.site.register(BlogPost)
```

Vous devez également exécuter `python manage.py makemigrations`, `python manage.py migrate` et `python manage.py createsuperuser` pour créer la base de données et un compte administrateur. Maintenant, `python manage.py runserver`, allez sur `[http://localhost:8000/admin/](http://localhost:8000/admin/)` et connectez-vous. Vous devriez maintenant pouvoir voir votre modèle de Blog posts là. Allez-y et créez votre premier article de blog dans l'admin.

Félicitations, vous avez maintenant un projet Django fonctionnel ! Il est enfin temps de passer aux choses amusantes — connecter ElasticSearch.

#### Connexion d'ElasticSearch avec Django

Vous commencez par créer un nouveau fichier appelé `search.py` dans notre répertoire `elasticsearchapp`. C'est là que le code ElasticSearch résidera. La première chose que vous devez faire ici est de créer une connexion de votre application Django à ElasticSearch. Vous faites cela dans votre fichier `search.py` :

```
from elasticsearch_dsl.connections import connectionsconnections.create_connection()
```

Maintenant que vous avez une connexion globale à votre configuration ElasticSearch, vous devez définir ce que vous voulez indexer. Écrivez ce code :

```
from elasticsearch_dsl.connections import connectionsfrom elasticsearch_dsl import DocType, Text, Dateconnections.create_connection()class BlogPostIndex(DocType):    author = Text()    posted_date = Date()    title = Text()    text = Text()    class Meta:        index = 'blogpost-index'
```

Cela ressemble beaucoup à votre modèle, n'est-ce pas ? Le `DocType` fonctionne comme un wrapper pour vous permettre d'écrire un index comme un modèle, et les `Text` et `Date` sont les champs afin qu'ils obtiennent le format correct lorsqu'ils sont indexés.

À l'intérieur de Meta, vous indiquez à ElasticSearch comment vous voulez que l'index soit nommé. Cela sera un point de référence pour ElasticSearch afin qu'il sache quel index il traite lorsqu'il l'initialise dans la base de données et sauvegarde chaque nouvelle instance d'objet créée.

Maintenant, vous devez réellement créer le mappage de votre nouvellement créé `BlogPostIndex` dans ElasticSearch. Vous pouvez faire cela et également créer un moyen de faire l'indexation en masse en même temps — c'est pratique, non ?

#### Indexation en masse des données

La commande `bulk` se trouve dans `elasticsearch.helpers` qui est inclus lorsque vous avez installé `elasticsearch_dsl` puisque c'est construit sur cette bibliothèque. Faites ce qui suit dans `search.py` :

```
...from elasticsearch.helpers import bulkfrom elasticsearch import Elasticsearchfrom . import models...
```

```
...def bulk_indexing():    BlogPostIndex.init()    es = Elasticsearch()    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))
```

« Que se passe-t-il ici ? » pourriez-vous penser. Ce n'est pas si compliqué, en fait.

Puisque vous ne voulez faire l'indexation en masse que lorsque vous changez quelque chose dans notre modèle, vous `init()` le modèle qui le mappe dans ElasticSearch. Ensuite, vous utilisez `bulk` et lui passez une instance de `Elasticsearch()` qui créera une connexion à ElasticSearch. Vous passez ensuite un générateur à `actions=` et itérez sur tous les objets `BlogPost` que vous avez dans votre base de données régulière et appelez la méthode `.indexing()` sur chaque objet. Pourquoi un générateur ? Parce que si vous aviez beaucoup d'objets à itérer, un générateur n'aurait pas à les charger d'abord en mémoire.

Il y a juste un problème avec le code ci-dessus. Vous n'avez pas encore de méthode `.indexing()` sur votre modèle. Corrigons cela :

```
...from .search import BlogPostIndex...
```

```
...# Add indexing method to BlogPostdef indexing(self):   obj = BlogPostIndex(      meta={'id': self.id},      author=self.author.username,      posted_date=self.posted_date,      title=self.title,      text=self.text   )   obj.save()   return obj.to_dict(include_meta=True)
```

Vous ajoutez la méthode d'indexation au modèle `BlogPost`. Elle retourne un `BlogPostIndex` et est sauvegardée dans ElasticSearch.

Essayons cela maintenant et voyons si vous pouvez indexer en masse l'article de blog que vous avez précédemment créé. En exécutant `python manage.py shell`, vous entrez dans le shell Django et importez votre `search.py` avec `from elasticsearchapp.search import *` puis exécutez `bulk_indexing()` pour indexer tous les articles de blog dans votre base de données. Pour voir si cela a fonctionné, exécutez la commande curl suivante :

```
curl -XGET 'localhost:9200/blogpost-index/blog_post_index/1?pretty'
```

Vous devriez obtenir votre premier article de blog dans le terminal.

#### Indexation d'une nouvelle instance sauvegardée

Ensuite, vous devez ajouter un signal qui déclenche `.indexing()` sur chaque nouvelle instance qui est sauvegardée chaque fois qu'un utilisateur sauvegarde un nouvel article de blog. Dans `elasticsearchapp`, créez un nouveau fichier appelé `signals.py` et ajoutez ce code :

```
from .models import BlogPostfrom django.db.models.signals import post_savefrom django.dispatch import receiver@receiver(post_save, sender=BlogPost)def index_post(sender, instance, **kwargs):    instance.indexing()
```

Le signal `post_save` garantira que l'instance sauvegardée sera indexée avec la méthode `.indexing()` après sa sauvegarde.

Pour que cela fonctionne, nous devons également enregistrer Django que nous utilisons des signaux. Nous faisons cela en ouvrant `apps.py` et en ajoutant le code suivant :

```
from django.apps import AppConfigclass ElasticsearchappConfig(AppConfig):    name = 'elasticsearchapp'    def ready(self):        import elasticsearchapp.signals
```

Pour compléter cela, nous devons également indiquer à Django que nous utilisons cette nouvelle configuration. Nous faisons cela à l'intérieur de `__init__.py` dans notre répertoire `elasticsearchapp` en ajoutant :

```
default_app_config = 'elasticsearchapp.apps.ElasticsearchappConfig'
```

Maintenant, le signal `post_save` est enregistré avec Django et est prêt à écouter chaque fois qu'un nouvel article de blog est sauvegardé.

Essayez-le en retournant dans l'admin Django et en sauvegardant un nouvel article de blog. Ensuite, vérifiez avec une commande `curl` s'il a été correctement indexé dans ElasticSearch.

#### Recherche simple

Maintenant, créons une fonction de recherche simple dans `search.py` pour trouver tous les articles filtrés par auteur :

```
...from elasticsearch_dsl import DocType, Text, Date, Search...
```

```
...def search(author):    s = Search().filter('term', author=author)    response = s.execute()    return response
```

Essayons la recherche. Dans le shell : `from elasticsearchapp.search import *` et exécutez `print(search(author="<author name>"))` :

```
>>> print(search(author="home"))<Response: [<Result(blogpost-index/blog_post_index/1): {'text': 'Hello world, this is my first blog post', 'title':...}>]>
```

Vous y êtes ! Vous avez maintenant indexé avec succès toutes vos instances dans ElasticSearch, créé un signal `post_save` qui indexe chaque nouvelle instance sauvegardée, et créé une fonction pour rechercher dans votre base de données ElasticSearch vos données.

#### Conclusion

Cet article était assez long, mais j'espère qu'il est écrit de manière suffisamment simple pour que même les débutants puissent comprendre.

J'ai expliqué comment connecter un modèle Django à ElasticSearch pour l'indexation et la recherche, mais ElasticSearch peut faire bien plus. Je recommande de lire leur site web et d'explorer les autres possibilités existantes, telles que les opérations spatiales et la recherche en texte intégral avec surlignage intelligent. C'est un excellent outil et je m'assurerai de l'utiliser dans de futurs projets !

Si vous avez aimé cet article ou si vous avez un commentaire ou une suggestion, n'hésitez pas à laisser un message ci-dessous. Et restez à l'écoute pour plus de choses intéressantes !