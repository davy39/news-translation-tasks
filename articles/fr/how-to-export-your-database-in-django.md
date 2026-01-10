---
title: Comment exporter votre base de données dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-21T15:23:46.740Z'
originalURL: https://freecodecamp.org/news/how-to-export-your-database-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745248996492/6d3f5665-3329-4894-9f99-3ba257867e0d.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: Comment exporter votre base de données dans Django
seo_desc: 'When you''re working on a Django project – whether it''s a small side project
  or a growing web app – there comes a point where you need to export your database.

  Maybe you’re switching hosting providers. Maybe you''re backing things up or sharing
  data wi...'
---

Lorsque vous travaillez sur un projet Django  qu'il s'agisse d'un petit projet secondaire ou d'une application web en croissance  il arrive un moment où vous devez exporter votre base de données.

Peut-être changez-vous de fournisseur d'hébergement. Peut-être faites-vous une sauvegarde ou partagez-vous des données avec quelqu'un. Ou peut-être souhaitez-vous simplement consulter vos données dans un format différent.

Exporter une base de données semble technique (et oui, ça l'est un peu), mais cela n'a pas à être difficile. Django vous offre des outils intégrés qui rendent le processus beaucoup plus facile que ce que la plupart des gens attendent.

Je travaille avec Django depuis un certain temps maintenant, et j'ai aidé des développeurs, des débutants aux professionnels, à gérer les exportations de bases de données.

Dans ce tutoriel, je vais vous guider à travers toutes les méthodes pour exporter votre base de données dans Django.

### Voici ce que nous allons couvrir :

* [Pourquoi voudriez-vous exporter votre base de données ?](#heading-pourquoi-voudriez-vous-exporter-votre-base-de-donnees)
  
* [D'abord, connaissez votre base de données](#heading-d'abord-connaissez-votre-base-de-donnees)
  
  * [Méthode 1 : Utiliser la commande dumpdata de Django](#heading-methode-1-utiliser-la-commande-dumpdata-de-django)
      
  * [Un conseil rapide sur les fixtures](#heading-un-conseil-rapide-sur-les-fixtures)
      
  * [Méthode 2 : Utiliser les outils de votre base de données](#heading-methode-2-utiliser-les-outils-de-votre-base-de-donnees)
      
  * [Méthode 3 : Exporter vers CSV pour Excel ou Google Sheets](#heading-methode-3-exporter-vers-csv-pour-excel-ou-google-sheets)
      
  * [Méthode 4 : Utiliser les actions de l'admin Django](#heading-methode-4-utiliser-les-actions-de-ladmin-django)
      
* [FAQ](#heading-faq)
  
  * [Puis-je exporter des données au format XML au lieu de JSON ?](#heading-puis-je-exporter-des-donnees-au-format-xml-au-lieu-de-json)
      
  * [Quel est le meilleur format pour les sauvegardes ?](#heading-quel-est-le-meilleur-format-pour-les-sauvegardes)
      
  * [Puis-je automatiser les sauvegardes ?](#heading-puis-je-automatiser-les-sauvegardes)
      
* [Pour aller plus loin](#heading-pour-aller-plus-loin)
  
* [Conclusion](#heading-conclusion)
  

## Pourquoi voudriez-vous exporter votre base de données ?

Il y a plusieurs raisons pour lesquelles vous pourriez vouloir exporter votre base de données Django :

* **Sauvegarde** : Avant d'apporter des modifications importantes, il est judicieux de sauvegarder une copie.
  
* **Migration** : Passage à un autre serveur ou changement de SQLite à PostgreSQL.
  
* **Partage de données** : Donner un instantané des données à des collègues ou à des analystes.
  
* **Test** : Peupler un environnement de test ou de préproduction avec des données réelles.
  
* **Conformité** : Raisons légales ou politiques pour stocker des données en dehors de votre application.
  

La bonne nouvelle ? Django dispose d'outils solides pour vous aider à faire tout cela rapidement et proprement.

## D'abord, connaissez votre base de données

Django prend en charge plusieurs types de bases de données : SQLite (par défaut), PostgreSQL, MySQL, et plus encore. Selon ce que vous utilisez, votre processus d'exportation peut sembler un peu différent.

Mais pour la plupart des cas courants, surtout si vous utilisez SQLite ou PostgreSQL, les méthodes que je vais vous montrer fonctionneront très bien.

### Méthode 1 : Utiliser la commande `dumpdata` de Django

C'est la manière la plus facile et la plus courante d'exporter vos données.

#### Étapes :

1. Ouvrez votre terminal.
  
2. Accédez à votre dossier de projet Django.
  
3. Exécutez la commande suivante :
  

```bash
python manage.py dumpdata > db.json
```

C'est tout. Vous venez d'exporter toutes vos données dans un fichier JSON appelé `db.json`.

#### Que se passe-t-il ici ?

* `dumpdata` est une commande de gestion Django qui parcourt votre base de données et exporte les données de tous les modèles.
  
* Le symbole `>` signifie "envoyer la sortie dans un fichier" au lieu de l'afficher à l'écran.
  
#### Vous voulez exporter une seule application ?

Vous pouvez être plus spécifique :

```bash
python manage.py dumpdata myapp > myapp_data.json
```

Ou même un seul modèle :

```bash
python manage.py dumpdata myapp.MyModel > model_data.json
```

Cela est utile si votre base de données est volumineuse et que vous n'avez besoin que d'une partie.

#### Un conseil rapide sur les fixtures

Le fichier que vous venez de créer (`db.json`) est appelé une *fixture* dans Django. Vous pouvez l'utiliser pour charger des données dans un autre projet en utilisant :

```bash
python manage.py loaddata db.json
```

Donc oui, `dumpdata` + `loaddata` est une combinaison super pratique pour déplacer des données.

### Méthode 2 : Utiliser les outils de votre base de données

Selon la base de données que vous utilisez, vous pouvez également utiliser des outils qui fonctionnent en dehors de Django.

#### Pour SQLite (par défaut dans Django)

Votre base de données est simplement un fichier, généralement nommé `db.sqlite3`.

Vous pouvez le copier comme n'importe quel autre fichier :

```bash
cp db.sqlite3 db_backup.sqlite3
```

Si vous souhaitez exporter les données sous forme d'instructions SQL, vous pouvez utiliser l'outil de ligne de commande `sqlite3` :

```bash
sqlite3 db.sqlite3 .dump > db_dump.sql
```

Cela crée un fichier avec toutes les commandes SQL nécessaires pour recréer votre base de données. Très pratique pour les sauvegardes.

#### Pour PostgreSQL

Vous aurez besoin d'accéder à `pg_dump`, qui est l'outil d'exportation intégré de PostgreSQL.

Voici un exemple :

```bash
pg_dump -U your_username your_database > backup.sql
```

Vous devrez peut-être entrer votre mot de passe, selon la configuration de votre base de données.

Vous pouvez [trouver plus d'informations sur `pg_dump` ici](https://www.postgresql.org/docs/current/app-pgdump.html).

### Méthode 3 : Exporter vers CSV pour Excel ou Google Sheets

Si vous souhaitez vos données dans une feuille de calcul, vous pouvez les exporter au format CSV.

Django n'a pas de commande intégrée pour cela, mais vous pouvez écrire un script simple.

Voici un exemple qui exporte toutes les entrées d'un modèle :

#### Exemple :

Supposons que vous avez un modèle comme ceci :

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
```

Pour l'exporter vers CSV :

```python
# export_books.py
import csv
from myapp.models import Book

with open('books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author'])

    for book in Book.objects.all():
        writer.writerow([book.title, book.author])
```

Exécutez ce script avec le shell de Django :

```bash
python manage.py shell < export_books.py
```

Vous avez maintenant un fichier `books.csv` que vous pouvez ouvrir dans Excel ou Google Sheets.

### Méthode 4 : Utiliser les actions de l'admin Django

Si votre modèle est enregistré dans l'admin Django, vous pouvez créer une action admin personnalisée qui vous permet d'exporter des données directement depuis l'interface.

Voici un exemple rapide :

```python
# admin.py
import csv
from django.http import HttpResponse
from .models import Book

@admin.action(description='Exporter les livres sélectionnés vers CSV')
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=books.csv'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Author'])

    for book in queryset:
        writer.writerow([book.title, book.author])
    
    return response

class BookAdmin(admin.ModelAdmin):
    actions = [export_to_csv]

admin.site.register(Book, BookAdmin)
```

Maintenant, vous pouvez sélectionner des lignes dans l'admin Django et les exporter. Simple et convivial.

## FAQ

### **Puis-je exporter des données au format XML au lieu de JSON ?**

Oui ! Il suffit d'ajouter l'option `--format` :

```bash
python manage.py dumpdata --format=xml > db.xml
```

### **Quel est le meilleur format pour les sauvegardes ?**

JSON est idéal pour les transferts entre projets Django. SQL (en utilisant `pg_dump` ou `sqlite3 .dump`) est meilleur pour les sauvegardes complètes de bases de données.

### **Puis-je automatiser les sauvegardes ?**

Absolument. Configurez une tâche cron ou un script Python simple qui exécute `dumpdata` selon un calendrier et sauvegarde le fichier dans le stockage cloud.

## Conclusion

Exporter votre base de données dans Django n'a pas à être une tâche ardue. Avec des commandes intégrées comme `dumpdata`, ou même des scripts personnalisés pour les exportations CSV, vous pouvez gérer les données en toute sécurité et avec confiance. Et une fois que vous aurez pris le coup de main, vous utiliserez probablement ces outils tout le temps.

### Pour aller plus loin

* [Documentation Django dumpdata](https://docs.djangoproject.com/en/stable/ref/django-admin/#dumpdata)
  
* [PostgreSQL pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)
  
* [Sauvegarde des bases de données SQLite](https://www.sqlite.org/backup.html)
  
* [Commande Django loaddata](https://docs.djangoproject.com/en/stable/ref/django-admin/#loaddata)