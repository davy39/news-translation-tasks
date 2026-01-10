---
title: Comment utiliser PostgreSQL dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-22T13:43:52.647Z'
originalURL: https://freecodecamp.org/news/how-to-use-postgresql-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745329406033/4d3cb010-d612-4ca8-8039-2d922e8b0337.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: PostgreSQL
  slug: postgresql
seo_title: Comment utiliser PostgreSQL dans Django
seo_desc: 'If you’re building a Django project and wondering which database to use,
  PostgreSQL is a great choice. It’s reliable, fast, packed with powerful features,
  and works beautifully with Django.

  I’ve used it across multiple projects – from small web apps ...'
---

Si vous construisez un projet Django et que vous vous demandez quelle base de données utiliser, PostgreSQL est un excellent choix. Il est fiable, rapide, rempli de fonctionnalités puissantes et fonctionne parfaitement avec Django.

Je l'ai utilisé dans plusieurs projets - des petites applications web aux plateformes à grande échelle - et il ne m'a jamais déçu.

Dans cet article, je vais vous guider étape par étape pour connecter PostgreSQL avec Django.

Commençons.

### Ce que nous allons couvrir :

1. [Pourquoi utiliser PostgreSQL avec Django ?](#heading-pourquoi-utiliser-postgresql-avec-django)

2. [Ce dont vous aurez besoin](#heading-ce-dont-vous-aurez-besoin)

3. [Comment utiliser PostgreSQL dans Django](#heading-comment-utiliser-postgresql-dans-django)

   * [Étape 1 : Installer PostgreSQL](#heading-etape-1-installer-postgresql)

   * [Étape 2 : Installer l'adaptateur PostgreSQL pour Python](#heading-etape-2-installer-ladaptateur-postgresql-pour-python)

   * [Étape 3 : Créer un projet Django (si ce n'est pas déjà fait)](#heading-etape-3-creer-un-projet-django-si-ce-nest-pas-deja-fait)

   * [Étape 4 : Créer une base de données PostgreSQL](#heading-etape-4-creer-une-base-de-donnees-postgresql)

   * [Étape 5 : Mettre à jour les paramètres Django pour utiliser PostgreSQL](#heading-etape-5-mettre-a-jour-les-parametres-django-pour-utiliser-postgresql)

   * [Étape 6 : Exécuter les migrations](#heading-etape-6-executer-les-migrations)

   * [Étape 7 : Tester la connexion](#heading-etape-7-tester-la-connexion)

4. [Problèmes courants (et solutions)](#heading-problemes-courants-et-solutions)

5. [Optionnel : Utiliser dj-database-url pour de meilleurs paramètres](#heading-optionnel-utiliser-dj-database-url-pour-de-meilleurs-parametres)

6. [Questions fréquemment posées](#heading-questions-frequemment-posees)

   * [PostgreSQL est-il meilleur que SQLite pour Django ?](#heading-postgresql-est-il-meilleur-que-sqlite-pour-django)

   * [Dois-je installer PostgreSQL sur mon serveur de production ?](#heading-dois-je-installer-postgresql-sur-mon-serveur-de-production)

   * [psycopg2-binary est-il sûr à utiliser en production ?](#heading-psycopg2-binary-est-il-sur-a-utiliser-en-production)

   * [Puis-je passer de SQLite à PostgreSQL en cours de projet ?](#heading-puis-je-passer-de-sqlite-a-postgresql-en-cours-de-projet)

7. [Conclusion](#heading-conclusion)

8. [Ressources supplémentaires](#heading-ressources-supplementaires)

## Pourquoi utiliser PostgreSQL avec Django ?

PostgreSQL est une base de données relationnelle open-source populaire, connue pour ses performances, sa flexibilité et ses fonctionnalités puissantes telles que :

* Types de données avancés (JSON, tableaux, etc.)

* Recherche en texte intégral

* Prise en charge des requêtes complexes

* Intégrité et fiabilité des données

Django recommande officiellement PostgreSQL comme le backend de base de données le plus complet qu'il supporte. Si vous prévoyez de construire une application web sérieuse, PostgreSQL est généralement la meilleure base de données à associer avec Django.

## Ce dont vous aurez besoin

Avant de commencer, assurez-vous d'avoir ce qui suit :

* Python installé (3.7 ou supérieur est préférable)

* Django installé (j'utiliserai la version 4.x)

* PostgreSQL installé et en cours d'exécution

* `psycopg2` ou `psycopg2-binary` (c'est l'adaptateur qui permet à Django de communiquer avec PostgreSQL)

## Comment utiliser PostgreSQL dans Django

Voici comment commencer :

### Étape 1 : Installer PostgreSQL

Si vous n'avez pas encore installé PostgreSQL, vous pouvez le télécharger depuis le [site officiel de PostgreSQL](https://www.postgresql.org/download/). Il fonctionne sur Windows, macOS et Linux.

Assurez-vous de vous souvenir du nom d'utilisateur, du mot de passe et du nom de la base de données lorsque vous le configurez - vous en aurez besoin plus tard.

### Étape 2 : Installer l'adaptateur PostgreSQL pour Python

Django a besoin d'un peu d'aide pour se connecter à PostgreSQL. C'est là que `psycopg2` intervient.

Vous pouvez l'installer en utilisant pip :

```bash
pip install psycopg2-binary
```

Astuce : La version `-binary` est plus facile à installer et fonctionne pour la plupart des gens. Si vous rencontrez des problèmes plus tard, vous pouvez passer à `psycopg2` (non-binaire).

### Étape 3 : Créer un projet Django (si ce n'est pas déjà fait)

Si vous n'avez pas encore créé de projet, commencez par :

```bash
django-admin startproject myproject
cd myproject
```

Cela vous donnera la structure de base du projet.

### Étape 4 : Créer une base de données PostgreSQL

Maintenant, ouvrez votre client PostgreSQL (comme `psql` ou pgAdmin), et créez une nouvelle base de données :

```sql
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
```

Cela configure une base de données et un utilisateur avec les bonnes permissions. Remplacez `mydatabase`, `myuser` et `mypassword` par les valeurs que vous préférez.

### Étape 5 : Mettre à jour les paramètres Django pour utiliser PostgreSQL

Maintenant, il est temps de dire à Django d'utiliser votre nouvelle base de données PostgreSQL.

Ouvrez `myproject/settings.py` et cherchez le paramètre `DATABASES`. Remplacez la section `sqlite3` par défaut par ceci :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Cela indique à Django de :

* Utiliser PostgreSQL (`django.db.backends.postgresql`)

* Se connecter à une base de données locale appelée `mydatabase`

* Utiliser l'utilisateur et le mot de passe que vous avez configurés précédemment

### Étape 6 : Exécuter les migrations

Maintenant que tout est connecté, créons les tables de base de données dont Django a besoin :

```bash
python manage.py migrate
```

Si tout fonctionne, vous verrez Django créer des tables dans PostgreSQL. Pas d'erreurs ? Vous êtes prêt à continuer !

### Étape 7 : Tester la connexion

Testons le tout en créant un superutilisateur (compte administrateur) :

```bash
python manage.py createsuperuser
```

Suivez les instructions, puis exécutez :

```bash
python manage.py runserver
```

Ouvrez votre navigateur et allez à `http://127.0.0.1:8000/admin`. Connectez-vous avec votre compte superutilisateur. Vous serez dans le tableau de bord d'administration de Django - et oui, tout cela est maintenant soutenu par PostgreSQL !

## Problèmes courants (et solutions)

Voici quelques problèmes que vous pourriez rencontrer :

* **Erreur :** `psycopg2.errors.UndefinedTable` : Cela signifie généralement que vous avez oublié d'exécuter `migrate`.

* **Impossible de se connecter à la base de données :** Vérifiez bien le nom de la base de données, l'utilisateur et le mot de passe. Assurez-vous que PostgreSQL est en cours d'exécution.

* **Rôle inexistant :** Vous avez peut-être oublié de créer l'utilisateur dans PostgreSQL, ou vous avez utilisé le mauvais nom dans `settings.py`.

## Optionnel : Utiliser `dj-database-url` pour de meilleurs paramètres

Si vous prévoyez de déployer votre application plus tard (surtout sur des services comme Heroku), gérer vos paramètres de base de données via une URL est plus propre.

Installez le package d'aide :

```bash
pip install dj-database-url
```

Puis dans votre `settings.py` :

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgres://myuser:mypassword@localhost:5432/mydatabase')
}
```

Cela vous permet de contrôler votre configuration de base de données à partir d'une variable d'environnement, ce qui est plus sécurisé et flexible.

## Questions fréquemment posées

### **PostgreSQL est-il meilleur que SQLite pour Django ?**

Pour l'apprentissage ou les petits projets, SQLite est bien. Mais pour les applications sérieuses avec beaucoup d'utilisateurs ou des requêtes avancées, PostgreSQL est bien meilleur.

### **Dois-je installer PostgreSQL sur mon serveur de production ?**

Oui - sauf si vous utilisez une solution PostgreSQL hébergée comme [Amazon RDS](https://aws.amazon.com/rds/postgresql/), [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql), ou [Supabase](https://supabase.com/).

### **psycopg2-binary est-il sûr à utiliser en production ?**

Oui, dans la plupart des cas. Mais certains recommandent de passer à la version non-binaire (`psycopg2`) en production pour un meilleur contrôle.

### **Puis-je passer de SQLite à PostgreSQL en cours de projet ?**

Oui, mais vous devrez migrer vos données. Des outils comme [`dumpdata` et `loaddata` de Django](https://docs.djangoproject.com/en/stable/ref/django-admin/#dumpdata) peuvent vous aider.

## Conclusion

Utiliser PostgreSQL dans Django est une excellente étape lorsque vous souhaitez construire des applications réelles, prêtes pour la production.

La configuration est assez simple une fois que vous connaissez les étapes, et les gains de performance en valent la peine.

Venez dire bonjour sur [X.com/_udemezue](http://X.com/_udemezue) et consultez mon [blog](https://Tchelete.com) pendant que vous y êtes !

### Ressources supplémentaires

Si vous souhaitez approfondir, voici quelques liens que je recommande :

* [Documentation des paramètres de base de données Django](https://docs.djangoproject.com/en/stable/ref/settings/#databases)

* [Documentation officielle de PostgreSQL](https://www.postgresql.org/docs/)

* [Utilisation de PostgreSQL avec Django (Real Python)](https://realpython.com/django-setup/#databases)