---
title: Comment créer votre propre Heroku avec Dokku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-04T19:01:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-on-heroku-with-dokku
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/dokku.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Docker
  slug: docker
- name: Heroku
  slug: heroku
- name: PaaS
  slug: paas
seo_title: Comment créer votre propre Heroku avec Dokku
seo_desc: 'By Nuno Bispo

  Heroku is a well-known PaaS widely used by developers. And as a fun and useful project,
  you can easily make your own Heroku-like PaaS with Dokku.


  What is Heroku?

  Heroku is a platform as a service (PaaS) company founded in 2007. The pla...'
---

Par Nuno Bispo

Heroku est une PaaS bien connue largement utilisée par les développeurs. Et en tant que projet amusant et utile, vous pouvez facilement créer votre propre PaaS de type Heroku avec Dokku.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/dokku-logo-with-name5-1.png)

## Qu'est-ce que Heroku ?

Heroku est une entreprise de plateforme en tant que service (PaaS) fondée en 2007. La plateforme fonctionne sur AWS, et son système de stockage éphémère s'appelle "Dyno".

Heroku est l'une des PaaS les plus utilisées par les développeurs, et pour une bonne raison – elle est facile à utiliser, bien documentée et supporte plusieurs langages de programmation.

Mais que se passerait-il si vous pouviez déployer votre propre plateforme de type Heroku, incluant un pipeline CI/CD, des connexions de base de données, des connexions HTTPS, et bien plus encore avec une application simple à utiliser ?

Eh bien, c'est ce que Dokku fournit et plus encore. Examinons cela.

## Qu'est-ce qu'une PaaS ?

Platform-as-a-Service (PaaS) est un style d'architecture logicielle qui fournit une couche d'abstraction facile à utiliser pour déployer le code de votre application et le gérer.

Cela vous permet de vous concentrer sur l'écriture de la logique métier plutôt que de vous soucier de la plateforme elle-même.

Les fournisseurs de PaaS fournissent généralement leur propre service de base de données ainsi que d'autres services connexes, ce qui peut grandement simplifier les tâches de développement courantes.

Le grand avantage de la PaaS est que le développeur d'applications n'a pas besoin d'effectuer aucun travail d'administration système. Au lieu de cela, vous pouvez simplement télécharger votre code et vos paramètres de configuration sur une plateforme de serveur central.

Le service se charge ensuite de déployer le code, de le mettre à l'échelle si nécessaire, de sauvegarder les données, de gérer les préoccupations d'hébergement et de disponibilité, et ainsi de suite.

## Qu'est-ce que Dokku ?

Dokku est une plateforme en tant que service hébergée qui permet aux développeurs de déployer leurs applications avec facilité.

De leur site web :

> La plus petite implémentation de PaaS que vous ayez jamais vue

Dokku est basé sur Docker et utilise les build-packs de Heroku pour compiler et packager vos applications.

L'une des meilleures choses à propos de Dokku est qu'il est très léger et peut être installé sur un seul serveur ou une seule machine virtuelle.

Il inclut l'hébergement scalable utilisant des conteneurs Docker, le déploiement continu avec Git, et d'autres outils DevOps populaires.

Dokku offre également une variété de fonctionnalités, telles que le support de plusieurs langages, des domaines personnalisés, des déploiements automatisés, et bien plus encore.

Vous pouvez facilement connecter des bases de données Postgres et même du stockage de fichiers à vos applications.

Vous pouvez consulter plus d'informations sur [https://dokku.com/](https://dokku.com/) ou la documentation sur : [https://dokku.com/docs/getting-started/installation/](https://dokku.com/docs/getting-started/installation/).

Vous pouvez également montrer un peu d'amour pour le [projet open-source GitHub ici](https://github.com/dokku/dokku).

## Comment installer Dokku

Pour installer Dokku, vous aurez besoin d'un VPS Linux et d'un nom de domaine.

Vous pouvez installer et utiliser Dokku sans nom de domaine, mais c'est beaucoup plus simple avec un domaine. Je recommande un VPS cloud car cela facilite l'accès et la configuration.

Lors de la connexion d'un domaine, un domaine unique ou un wildcard peut être associé à l'IP du serveur.

J'utiliserai un VPS hébergé sur [Hetzner](https://hetzner.cloud/) avec Ubuntu 20.04 installé.

Nous commençons par nous assurer que notre système est à jour avec ces commandes :

```bash
# Mettre à jour l'installation Linux
$ sudo apt update
$ sudo apt upgrade -y
```

Ensuite, nous pouvons télécharger et exécuter le script d'installation pour Dokku :

```bash
# Installer Dokku avec le script d'installation
$ wget https://raw.githubusercontent.com/dokku/dokku/v0.26.8/bootstrap.sh;
$ sudo DOKKU_TAG=v0.26.8 bash bootstrap.sh

--> Vérification que nous avons les dépendances appropriées
--> Note : L'installation de dokku pour la première fois entraînera la suppression de
    fichiers dans le répertoire 'sites-enabled' de nginx. Veuillez restaurer manuellement
    les fichiers qui peuvent être supprimés après l'installation et
    la configuration web est terminée.

    L'installation se poursuivra dans 10 secondes.
    
    [...........]
    
    --> Exécution de l'installation des dépendances post-installation

 ! Configurez une clé ssh de l'utilisateur pour le déploiement en passant la clé ssh publique comme montré :

     echo 'CONTENU_DU_FICHIER_ID_RSA_PUB' | dokku ssh-keys:add admin
```

Le script d'installation installera Docker et toutes les dépendances nécessaires ainsi que Dokku lui-même, comme vu dans le code ci-dessus.

Après l'installation, nous devons assigner les clés SSH pour l'accès et également configurer notre nom de domaine.

Si vous avez configuré l'accès à votre VPS avec SSH (ce que vous devriez faire), alors vous avez déjà les clés nécessaires – vous devez simplement les ajouter à Dokku :

```
# Assigner la clé SSH à Dokku
$ cat ~/.ssh/authorized_keys | dokku ssh-keys:add admin

SHA256:6O1TLVOUkWV+zmTWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Si vous n'avez pas encore de clé SSH sur le serveur, alors vous devez générer une paire de clés :

```
# Générer une clé SSH
$ ssh-keygen

Génération de la paire de clés rsa publique/privée.
Entrez le fichier dans lequel sauvegarder la clé (/root/.ssh/id_rsa) :
Entrez une phrase de passe (vide pour aucune phrase de passe) :
Entrez à nouveau la même phrase de passe :
Votre identification a été sauvegardée dans /root/.ssh/id_rsa
Votre clé publique a été sauvegardée dans /root/.ssh/id_rsa.pub
L'empreinte de la clé est :
SHA256:7T6BbRCVWjGtcSUXXXXXXXXXXXXXXXXXXXXXXXXXXXXX root@freeDokku
L'image randomart de la clé est :
+---[RSA 3072]----+
[.................]
|     . oS*.o . . |
[.................]
+----[SHA256]-----+

```

Ensuite, vous pouvez l'ajouter à Dokku :

```bash
# Ajouter la clé SSH à Dokku
$ dokku ssh-keys:add admin /root/.ssh/id_rsa.pub

SHA256:7T6BbRCVWjGtcSUXXXXXXXXXXXXXXXXXXXXXXXX

```

Ensuite, et dernière étape, nous devons assigner le domaine pour votre installation Dokku. Nous faisons cela avec la commande :

```bash
# Définir le domaine global de l'installation
$ dokku domains:set-global domain.com

-----> Définir domain.com
```

Assurez-vous de remplacer 'domain.com' par votre propre domaine, et que le DNS de votre nom de domaine pointe vers l'adresse IP du serveur.

Et c'est tout ce que vous devez faire pour installer et configurer Dokku. C'est vraiment aussi simple.

Vous pouvez maintenant commencer à ajouter vos applications.

Voyons un exemple de cela en ajoutant une application Django standard dans la section suivante.

## Comment créer votre application dans Dokku

Pour créer et déployer notre première application, il y a quelques travaux de préparation que nous devons faire sur Dokku.

Pour déployer une application sur Dokku, suivez ces étapes :

* Créez l'application sur Dokku, ce qui signifie lui donner un nom.
* Créez la base de données associée (ou d'autres plugins, si nécessaire). Cela créera et provisionnera une base de données pour une utilisation avec une DATABASE_URL automatique ajoutée à l'application pour faciliter le déploiement.
* Poussez le code nécessaire vers le point de terminaison GitHub interne de l'application Dokku. Cela peut inclure également les étapes de publication nécessaires (comme l'exécution des migrations Django, par exemple).

Après que le code est poussé, Dokku générera tout conteneur Docker nécessaire et exécutera notre application avec toutes les bases de données associées (ou d'autres plugins).

Maintenant que nous avons couvert les étapes nécessaires, passons-les en pratique.

Commençons par créer notre application. Pour ce tutoriel, je vais créer un site web Django très simple qui contient toute la logique nécessaire pour tester Dokku.

Nous créons une application sur Dokku avec cette commande (sur le serveur où nous avons installé Dokku) :

```bash
# Créer notre application sur Dokku
$ dokku apps:create djangotutorial

-----> Création de djangotutorial...
```

Par défaut, les datastores (ou bases de données) ne sont pas créés lorsqu'une application est créée.

Les datastores sont gérés par une série de plugins. Vous pouvez [vérifier ici pour tous les plugins disponibles](https://dokku.com/docs/community/plugins/#official-plugins-beta).

Pour notre application, nous allons créer un datastore Postgres. Puisque par défaut aucun plugin n'est installé, nous devons d'abord installer le plugin Postgres :

```bash
# installer le plugin postgres
# l'installation du plugin nécessite root, d'où le changement d'utilisateur
sudo dokku plugin:install https://github.com/dokku/dokku-postgres.git
```

Ensuite, nous pouvons créer notre datastore Postgres :

```bash
# Créer un datastore Postgres
$ dokku postgres:create djangotutorial_datastore

       Attente que le conteneur soit prêt
       Création de la base de données du conteneur
       Sécurisation de la connexion à la base de données
=====> Conteneur Postgres créé : djangotutorial_datastore
=====> Informations sur le service postgres djangotutorial_datastore
       Dossier de configuration :          /var/lib/dokku/services/postgres/djangotutorial_datastore/data
       Options de configuration :
       Dossier de données :            /var/lib/dokku/services/postgres/djangotutorial_datastore/data
       Dsn :                 postgres://postgres:ea706cc108c805d5124d134d934024c5@dokku-postgres-djangotutorial-datastore:5432/djangotutorial_datastore
       Ports exposés :       -
       Id :                  782a04fe6bbd25958752c17c304358fd5ec1f3c54d6d53175b6481b3b957d94b
       Ip interne :         172.17.0.5
       Liens :               -
       Racine du service :        /var/lib/dokku/services/postgres/djangotutorial_datastore
       Statut :              en cours d'exécution
       Version :             postgres:14.1

```

Nous pouvons vérifier que notre conteneur Docker pour le datastore est déjà en cours d'exécution avec :

```bash
# Vérifier les conteneurs en cours d'exécution
$ docker ps

ID DU CONTENEUR   IMAGE                      COMMANDE                  CRÉÉ              STATUT              PORTS      NOMS
782a04fe6bbd   postgres:14.1              "docker-entrypoint.s"   Il y a environ une minute   En cours d'exécution depuis environ une minute   5432/tcp   dokku.postgres.djangotutorial_datastore

```

Maintenant que nous avons le datastore en cours d'exécution, nous devons l'associer à notre application :

```bash
# Associer le datastore à l'application
$ dokku postgres:link djangotutorial_datastore djangotutorial

-----> Définition des variables de configuration
       DATABASE_URL:  postgres://postgres:ea706cc108c805d5124d134d934024c5@dokku-postgres-djangotutorial-datastore:5432/djangotutorial_datastore
-----> Redémarrage de l'application djangotutorial
 !     Image de l'application (dokku/djangotutorial:latest) non trouvée

```

Vous pouvez voir qu'une DATABASE_URL est automatiquement créée et associée à l'application.

L'exemple ci-dessus mentionne que notre image d'application n'est pas trouvée car nous n'avons pas encore poussé de code.

Nous pouvons vérifier les variables d'environnement de notre application pour confirmer que notre DATABASE_URL est présente :

```bash
# Vérification des variables d'environnement d'une application
$ dokku config:show djangotutorial

=====> Variables d'environnement de djangotutorial
DATABASE_URL:  postgres://postgres:ea706cc108c805d5124d134d934024c5@dokku-postgres-djangotutorial-datastore:5432/djangotutorial_datastore

```

Nous avons maintenant toutes les configurations nécessaires faites du côté Dokku pour supporter le déploiement de notre application.

Ensuite, nous allons créer le code pour notre application et le déployer sur Dokku pour un pipeline CI/CD automatisé.

## Comment créer le code de notre application sur PyCharm

Avant de pouvoir déployer une application, nous devons avoir son code source à pousser vers Dokku.

Pour ce tutoriel, nous allons créer une application Django très simple qui montre également l'utilisation de la base de données Postgres.

Nous utiliserons PyCharm comme IDE pour créer et gérer notre projet.

Nous créons un nouveau projet dans PyCharm – appelons-le 'DjangoTutorial' :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/PyCharm-NewProject.png)
_Création d'un nouveau projet sur PyCharm - Capture d'écran par l'auteur_

Je préfère personnellement créer de nouveaux projets avec un environnement virtuel déjà en place, ce qui facilite grandement la vie.

Si vous avez créé le projet avec un fichier main.py par défaut (comme je l'ai fait parce que j'oublie toujours de retirer la coche), vous pouvez le supprimer en toute sécurité maintenant. Nous n'allons pas l'utiliser.

La première étape est, bien sûr, d'installer Django afin que nous puissions construire notre application. Nous faisons cette installation en utilisant pip :

```
$ pip install django

Collecte de django
  Téléchargement de Django-4.0.2-py3-none-any.whl (8.0 MB)
     || 8.0 MB 6.4 MB/s
Collecte de sqlparse>=0.2.2
  Utilisation du cache sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecte de tzdata
  Utilisation du cache tzdata-2021.5-py2.py3-none-any.whl (339 kB)
Collecte de asgiref<4,>=3.4.1
  Téléchargement de asgiref-3.5.0-py3-none-any.whl (22 kB)
Installation des packages collectés : tzdata, sqlparse, asgiref, django
Installation réussie de asgiref-3.5.0 django-4.0.2 sqlparse-0.4.2 tzdata-2021.5
```

Ensuite, nous créons notre projet Django avec :

```
$ django-admin startproject DjangoTutorial .

```

Remarquez le '.' à la fin de la commande. J'aime utiliser cela pour qu'il crée le projet dans le répertoire courant au lieu de créer un sous-répertoire supplémentaire.

Vous devriez maintenant avoir une structure de projet comme celle-ci dans PyCharm :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/PyCharm-Project.png)
_Structure des dossiers PyCharm pour notre application Django - capture d'écran par l'auteur_

Nous pouvons exécuter notre projet avec la commande standard Django :

```
$ python manage.py runserver   

Surveillance des changements de fichiers avec StatReloader
Exécution des vérifications système...

Vérification système n'a identifié aucun problème (0 silencieux).

Vous avez 18 migrations non appliquées. Votre projet peut ne pas fonctionner correctement jusqu'à ce que vous appliquiez les migrations pour les applications : admin, auth, contenttypes, sessions.
Exécutez 'python manage.py migrate' pour les appliquer.
Février 02, 2022 - 16:49:27
Version Django 4.0.2, utilisant les paramètres 'DjangoTutorial.settings'
Démarrage du serveur de développement à http://127.0.0.1:8000/
Quittez le serveur avec CTRL-BREAK.

```

Nous n'avons pas encore appliqué nos migrations, nous allons donc le faire ensuite après avoir discuté de la configuration de la base de données pour l'accès local et Dokku.

En naviguant vers le lien [http://127.0.0.1:8000/](http://127.0.0.1:8000/), nous pouvons maintenant accéder à notre page de bienvenue Django standard :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Django.png)
_Page de bienvenue Django - capture d'écran par l'auteur_

Nous avons notre installation Django en cours d'exécution, nous pouvons donc maintenant commencer à construire le reste du projet.

Comme la plupart des projets, nous aurons besoin de stocker des données dans une base de données (ou une base de données en utilisant la nomenclature Dokku).

Nous voulons également pouvoir déboguer et exécuter notre application localement sur la machine de développement (en utilisant une base de données locale, dans ce cas SQLite) et l'exécuter sur le cloud avec Dokku en utilisant la base de données Postgres.

Cela signifie que nous devons changer certaines configurations dans notre fichier settings.py pour pouvoir supporter les deux cas d'utilisation sans avoir à changer de drapeaux ou de configurations à chaque fois.

Nous commençons par installer le package dj-database-url avec :

```
# Installer les packages pour l'URL de la base de données
$ pip install dj-database-url
$ pip install psycopg2


# Nous installons également ce package pour pouvoir utiliser les variables d'environnement
$ pip install python-decouple
```

Ce package nous permet d'avoir un dictionnaire de connexion de base de données Django, rempli avec toutes les données en spécifiant simplement une URL de base de données.

Avec le package installé, mettons à jour la configuration dans le fichier settings.py :

```python
# Nous devons ajouter cette importation au début pour utiliser les variables d'environnement
import dj_database_url
from decouple import config
from django.conf.global_settings import DATABASES

.....

# Mettons également à jour l'hôte autorisé pour pouvoir l'utiliser plus tard
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

.....

# Nous remplaçons la configuration de base de données par défaut de Django par celle-ci
# Base de données
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# URL DE LA BASE DE DONNÉES
DATABASES['default'] = dj_database_url.parse(config('DATABASE_URL'),conn_max_age=600)
```

Nous devons également créer un fichier '.env' dans le répertoire racine de notre projet :

```
# PARAMÈTRES D'HÔTE
ALLOWED_HOSTS = 127.0.0.1

# PARAMÈTRES DE LA BASE DE DONNÉES
DATABASE_URL='sqlite:///db.sqlite3'
```

Comme vous pouvez le voir, avec ce changement, nous pouvons utiliser l'URL de la base de données à partir du fichier '.env' local sur la machine de développement locale, puis sur Dokku, il utilisera automatiquement la DATABASE_URL déjà définie qui a été créée lorsque nous avons lié le datastore à l'application sur Dokku.

Nous pouvons maintenant créer notre première (et seule) page web de ce tutoriel, un simple compteur qui stocke et lit la valeur de la base de données.

Créons une application séparée pour contenir notre logique :

```bash
$ python manage.py startapp counter

```

Nous devons maintenant avoir un nouveau dossier appelé 'counter' dans notre projet. Ajoutons un nouveau modèle en ouvrant le fichier 'models.py' :

```python
from django.db import models


class Counter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.count
```

Nous pouvons maintenant ajouter une nouvelle URL pour charger notre page de compteur. Nous faisons cela en ajoutant un nouveau fichier appelé 'urls.py' à notre dossier 'counter' :

```python
from django.urls import path
from . import views

urlpatterns = [
    path('counter/', views.counter, name='counter'),
]
```

Nous avons maintenant à la fois le modèle et l'URL pour charger notre page de test. Tout ce dont nous avons besoin maintenant est la vue et le modèle HTML pour rendre la page.

Créons la vue en éditant le fichier 'views.py' :

```python
from django.shortcuts import render
from .models import Counter


def counter(request):
    counter_value = Counter.objects.last()

    if counter_value is None:
        counter_value = Counter(count=0)
        counter_value.save()

    if request.method == 'POST':
        counter_value.count += 1
        counter_value.save()

    return render(request, 'counter.html', {'counter': counter_value.count})

```

Maintenant, nous pouvons créer notre modèle HTML pour afficher la valeur du compteur sur la page. Nous créons un nouveau fichier appelé 'counter.html' à l'intérieur d'un nouveau dossier 'templates' :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Counter</title>
</head>
<body>
  <form method="post">
      {%csrf_token%}
    <h4>Counter value is: {{ counter }}</h4>
    <input type="submit" name="submit" value="Increase Counter">
  </form>
</body>
</html>
```

La dernière étape consiste à ajouter notre nouvelle application au fichier 'settings.py' afin que Django la reconnaisse :

```
.....

INSTALLED_APPS = [
    'counter',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

.....
```

Et l'URL vers notre fichier principal d'URLs :

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('counter.urls')),
    path('admin/', admin.site.urls),
]
```

Avec tout le code et le HTML nécessaires en place, nous pouvons maintenant créer et exécuter nos migrations pour créer notre nouveau modèle dans la base de données. Nous faisons d'abord cela sur le serveur local en exécutant :

```bash
# Créer et exécuter les migrations
$ python manage.py makemigrations
$ python manage.py migrate

Opérations à effectuer :
  Appliquer toutes les migrations : admin, auth, contenttypes, counter, sessions
Exécution des migrations :
  Application de contenttypes.0001_initial... OK
  Application de auth.0001_initial... OK
  Application de admin.0001_initial... OK
  Application de admin.0002_logentry_remove_auto_add... OK
  Application de auth.0009_alter_user_last_name_max_length... OK
  Application de auth.0010_alter_group_name_max_length... OK
  Application de auth.0011_update_proxy_permissions... OK
  Application de auth.0012_alter_user_first_name_max_length... OK
  Application de counter.0001_initial... OK
  Application de sessions.0001_initial... OK

```

Comme vous pouvez le voir, nous avons non seulement appliqué les migrations pour notre nouvelle application, mais nous avons également exécuté les migrations initiales pour les autres applications Django puisque c'était la première fois que nous exécutions les migrations.

Nous pouvons à nouveau exécuter notre serveur localement et nous devrions pouvoir accéder à l'URL [http://127.0.0.1:8000/counter/](http://127.0.0.1:8000/counter/) et incrémenter le compteur :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/CounterPage_Local.gif)
_Exécution de notre application de compteur - GIF par l'auteur_

Comme vous pouvez le voir, le rechargement de la page conserve notre valeur de compteur, ce qui signifie que la valeur est stockée dans la base de données avec notre modèle.

## Comment déployer notre application sur Dokku

Nous avons maintenant une application très simple en cours d'exécution avec une intégration de base de données pour stocker notre valeur de compteur.

Nous sommes prêts à la déployer dans le cloud afin de pouvoir la tester là-bas et nous assurer que notre base de données fonctionne également dans le cloud.

Avant de faire le push Git pour déployer le code sur Dokku, nous devons faire quelques préparations :

* Installer notre serveur web (gunicorn)
* Créer notre fichier de requirements (pour nos packages)
* Créer notre Procfile (pour nos commandes de déploiement)

Commençons par installer notre serveur web à utiliser dans le cloud :

```bash
# Installer notre serveur web
$ pip install gunicorn
```

Avec nos packages en place, nous pouvons maintenant créer notre fichier de requirements avec :

```bash
# Créer le fichier de requirements
$ pip freeze > requirements.txt
```

Maintenant, nous devons créer le 'Procfile'. Ce fichier est utilisé par Dokku pour déterminer quelles commandes exécuter lors du déploiement et après le déploiement.

Créons donc un nouveau fichier appelé 'Procfile' dans le répertoire racine avec le contenu :

```
web: gunicorn DjangoTutorial.wsgi
release: python manage.py migrate
```

Nous avons créé deux commandes pour que Dokku les exécute :

* release – cette commande est exécutée lors du déploiement de notre application dans Dokku. Nous l'utilisons pour migrer notre base de données.
* web – cette commande permet à Dokku de savoir quel serveur web exécuter pour permettre l'accès à l'application.

Enfin, pour nous assurer que nous pouvons collecter les fichiers statiques lorsque notre code est déployé sur Dokku, nous devons créer un nouveau répertoire appelé 'static' dans le répertoire racine. À l'intérieur, nous créons un fichier vide appelé '.gitkeep' (cela nous permettra d'ajouter le répertoire au dépôt Git plus tard).

Nous devons également ajouter ce chemin pour les fichiers statiques à notre fichier 'settings.py' :

```python
# Fichiers statiques (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"
```

Maintenant, tous les fichiers et la logique sont en place et nous pouvons déployer sur Dokku avec un push Git standard. Vérifions notre structure de fichiers actuelle :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/PyCharm-FolderStrcuture-1.png)
_Structure des dossiers PyCharm - capture d'écran par l'auteur_

Pour pouvoir pousser notre code vers Dokku, nous devons ajouter notre projet à un dépôt Git.

Puisque nous ne voulons pas pousser tous les fichiers de notre structure de dossiers vers le dépôt git de Dokku, nous créons un '.gitignore' pour exclure certains fichiers et répertoires. J'utilise le contenu de ce Gist excellent pour remplir le fichier :

%[https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a]

Nous pouvons maintenant initialiser et commiter notre code dans un dépôt Git localement :

```bash
# Initialiser le dépôt
$ git init -b main

# Ajouter et commiter nos fichiers
$ git add . && git commit -m "initial commit"

[main (root-commit) e77a16a] initial commit
 20 fichiers modifiés, 438 insertions(+)       
 mode de création 100644 .gitignore
 mode de création 100644 DjangoTutorial/__init__.py
 mode de création 100644 counter/tests.py
 mode de création 100644 counter/urls.py
 mode de création 100644 counter/views.py
 mode de création 100644 db.sqlite3
 mode de création 100644 manage.py
 mode de création 100644 requirements.txt

```

Avec notre dépôt commité, nous pouvons maintenant le pousser vers un dépôt distant, c'est-à-dire le dépôt Git de Dokku pour notre application :

```bash
# Ajout de notre dépôt distant (remplacez domain.com par votre nom de domaine)
$ git remote add dokku dokku@domain.com:djangotutorial

# Il est temps de pousser notre code vers le dépôt distant
$ git push dokku main

Énumération des objets : 34, terminé.
Comptage des objets : 100% (34/34), terminé.
Compression delta utilisant jusqu'à 8 threads
Compression des objets : 100% (31/31), terminé.
Écriture des objets : 100% (34/34), 11.41 KiB | 402.00 KiB/s, terminé.
Total 34 (delta 7), réutilisé 0 (delta 0)
-----> Définir main sur DOKKU_DEPLOY_BRANCH.
-----> Nettoyage...
-----> Construction de djangotutorial à partir de herokuish
-----> Ajout de BUILD_ENV à l'environnement de construction...
       BUILD_ENV ajouté avec succès
-----> Application Python détectée
-----> Aucune version de Python n'a été spécifiée. Utilisation de la version par défaut du buildpack : python-3.9.9
       Pour utiliser une version différente, voir : https://devcenter.heroku.com/articles/python-runtimes
-----> Aucun changement dans les requirements détecté, installation à partir du cache
-----> Installation de python-3.9.9
-----> Installation de pip 21.3.1, setuptools 57.5.0 et wheel 0.37.0
-----> Installation de SQLite3
-----> Installation des requirements avec pip
       Collecte de asgiref==3.5.0
       Téléchargement de asgiref-3.5.0-py3-none-any.whl (22 kB)
       Collecte de dj-database-url==0.5.0
       Téléchargement de dj_database_url-0.5.0-py2.py3-none-any.whl (5.5 kB)
       Collecte de Django==4.0.2
       Téléchargement de Django-4.0.2-py3-none-any.whl (8.0 MB)
       Collecte de gunicorn==20.1.0
       Téléchargement de gunicorn-20.1.0-py3-none-any.whl (79 kB)
       Collecte de psycopg2==2.9.3
       Téléchargement de psycopg2-2.9.3.tar.gz (380 kB)
       Préparation des métadonnées (setup.py) : démarré
       Préparation des métadonnées (setup.py) : terminé avec le statut 'done'
       Collecte de python-decouple==3.5
       Téléchargement de python_decouple-3.5-py3-none-any.whl (9.6 kB)
       Collecte de sqlparse==0.4.2
       Téléchargement de sqlparse-0.4.2-py3-none-any.whl (42 kB)
       Collecte de tzdata==2021.5
       Téléchargement de tzdata-2021.5-py2.py3-none-any.whl (339 kB)
       Construction des roues pour les packages collectés : psycopg2
       Construction de la roue pour psycopg2 (setup.py) : démarré
       Construction de la roue pour psycopg2 (setup.py) : terminé avec le statut 'done'
       Roue créée pour psycopg2 : filename=psycopg2-2.9.3-cp39-cp39-linux_x86_64.whl size=579484 sha256=9d6a2810a5d766738526d6f411e5e9ce514cce882b6c80a47a13c02dc7529e02
       Stocké dans le répertoire : /tmp/pip-ephem-wheel-cache-8k0chg5g/wheels/b3/a1/6e/5a0e26314b15eb96a36263b80529ce0d64382540ac7b9544a9
       Construction réussie de psycopg2
       Installation des packages collectés : sqlparse, asgiref, tzdata, python-decouple, psycopg2, gunicorn, Django, dj-database-url
       Installation réussie de Django-4.0.2 asgiref-3.5.0 dj-database-url-0.5.0 gunicorn-20.1.0 psycopg2-2.9.3 python-decouple-3.5 sqlparse-0.4.2 tzdata-2021.5
-----> $ python manage.py collectstatic --noinput
       128 fichiers statiques copiés vers '/tmp/build/static'.

-----> Découverte des types de processus
       Procfile déclare les types -> release, web
-----> Publication de djangotutorial...
-----> Vérification de la tâche de pré-déploiement
       Aucune tâche de pré-déploiement trouvée, saut
-----> Vérification de la tâche de release
-----> Exécution de la tâche de release depuis le Procfile : python manage.py migrate
=====> Début de la tâche de release djangotutorial (a602cab30) output
       Opérations à effectuer :
         Appliquer toutes les migrations : admin, auth, contenttypes, counter, sessions
       Exécution des migrations :
         Application de contenttypes.0001_initial... OK
         Application de auth.0001_initial... OK
         Application de admin.0001_initial... OK
         Application de admin.0002_logentry_remove_auto_add... OK
         Application de admin.0003_logentry_add_action_flag_choices... OK
         Application de contenttypes.0002_remove_content_type_name... OK
         Application de auth.0002_alter_permission_name_max_length... OK
         Application de auth.0003_alter_user_email_max_length... OK
         Application de auth.0004_alter_user_username_opts... OK
         Application de auth.0005_alter_user_last_login_null... OK
         Application de auth.0006_require_contenttypes_0002... OK
         Application de auth.0007_alter_validators_add_error_messages... OK
         Application de auth.0008_alter_user_username_max_length... OK
         Application de auth.0009_alter_user_last_name_max_length... OK
         Application de auth.0010_alter_group_name_max_length... OK
         Application de auth.0011_update_proxy_permissions... OK
         Application de auth.0012_alter_user_first_name_max_length... OK
         Application de counter.0001_initial... OK
         Application de sessions.0001_initial... OK
=====> Fin de la tâche de release djangotutorial (a602cab30) output
-----> Fichier Procfile de l'application trouvé
=====> Traitement des vérifications de déploiement
       Aucun fichier CHECKS trouvé. Des vérifications de conteneur simples seront effectuées.
       Pour des déploiements sans temps d'arrêt plus efficaces, créez un fichier CHECKS. Voir https://dokku.com/docs/deployment/zero-downtime-deploys/ pour des exemples
-----> Déploiement de djangotutorial via le planificateur docker-local...
-----> Déploiement web (count=1)
       Tentative de vérifications pré-vol (web.1)
       Attente de 10 secondes (web.1)
       Vérification du conteneur par défaut réussie (web.1)
-----> Déploiement release (count=0)
-----> Exécution post-déploiement
-----> Création du nouveau fichier d'hôte virtuel de l'application...
-----> Configuration de djangotutorial.domain.com...(en utilisant le modèle intégré)
-----> Création de http nginx.conf
       Rechargement de nginx
-----> Renommage des conteneurs
       Renommage du conteneur djangotutorial.web.1.upcoming-7101 (f8d229ebd8bc) en djangotutorial.web.1
-----> Vérification de la tâche postdeploy
       Aucune tâche postdeploy trouvée, saut
-----> Fichier de planification mis à jour
=====> Application déployée :
       http://djangotutorial.domain.com

Vers domain.com:djangotutorial
 * [nouvelle branche]      main -> main

```

Nous venons de déployer notre application sur Dokku.

Que vient-il de se passer ? Eh bien, Dokku a fait beaucoup de travail pour nous :

* Installé Python
* Installé les requirements
* Collecté les fichiers statiques
* Effectué les migrations
* Et enfin démarré un serveur gunicorn pour déployer notre application

Si vous avez eu une erreur de permission, alors votre clé privée doit être enregistrée dans votre environnement de développement local. Si vous obtenez une erreur `permission denied` lors du push, vous pouvez enregistrer votre clé privée comme suit : `ssh-add -k ~/<votre clé privée>`.

Vous pouvez également voir une erreur concernant les ALLOWED_HOSTS lors de l'accès à l'application. Dans ce cas, tout ce que vous avez à faire est d'exécuter la commande suivante sur le serveur Dokku pour définir la variable d'environnement à la valeur correcte :

```
# Définir la variable d'environnement ALLOWED_HOSTS (assurez-vous d'utiliser votre nom de domaine)
$ dokku config:set djangotutorial ALLOWED_HOSTS=djangotutorial.domain.com
```

Nous pouvons maintenant accéder et tester notre application à l'URL ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/PageCounter_Server.gif)
_Exécution de notre application de compteur sur Dokku - GIF par l'auteur_

Félicitations, vous venez de déployer votre application sur Dokku.

## Comment ajouter SSL avec Let's Encrypt

Une dernière configuration que nous pouvons faire est d'ajouter une sécurité SSL à notre application en installant un certificat SSL Let's Encrypt.

Nous pouvons le faire très facilement sur Dokku avec le plugin Let's Encrypt :

```bash
# Installer le plugin Let's Encrypt
sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git

# Configurer le plugin (assurez-vous de remplacer par votre email)
dokku config:set --global DOKKU_LETSENCRYPT_EMAIL=email@domain.com

# définir un domaine personnalisé que vous possédez pour votre application
dokku domains:set djangotutorial djangotutorial.your.domain.com

# Activer Let's Encrypt
dokku letsencrypt:enable djangotutorial

# Activer le renouvellement automatique de Let's Encrypt
dokku letsencrypt:cron-job --add
```

Maintenant, nous avons une application plus sécurisée. Après tout, notre compteur est très important.

## Conclusion

L'utilisation d'une PaaS facilite la vie des développeurs lors de la création d'applications web.

Vous pouvez utiliser des PaaS hébergées comme Heroku et il en existe beaucoup d'autres, donc le choix est là.

Mais il y a quelques inconvénients principaux :

* Prix – les solutions hébergées peuvent avoir des limites en termes de stockage de base de données ou de stockage de fichiers, entre autres
* Vous ne contrôlez pas l'hébergement où la PaaS est déployée. Des exemples récents d'AWS montrent que même le plus grand hébergement n'est pas à l'abri des problèmes.

Vous pouvez contourner ces problèmes en auto-hébergeant votre PaaS.

Cela permet un meilleur contrôle en termes de prix. Vous pouvez utiliser des fournisseurs d'hébergement comme [Digital Ocean](https://www.digitalocean.com/), [Hetzner](https://hetzner.cloud/), et d'autres qui ont des VPS assez bon marché qui fonctionnent parfaitement avec Dokku.

Il n'y a pas de limites de base de données. Les seules limites que vous pourriez avoir sont la mémoire et l'espace disque, mais vous pouvez toujours mettre à niveau votre VPS pour un prix inférieur à celui d'une nouvelle base de données chez Heroku.

Dokku est facile à installer et comme nous l'avons vu. La création et le déploiement d'une application est un processus en 3 étapes :

* Créer une application sur Dokku
* Créer un datastore sur Dokku (si nécessaire, comme Postgres) et le lier à l'application
* Déployer votre code sur Dokku avec Git

De plus, vous pourriez avoir besoin de configurer certaines variables d'environnement et certificats SSL, mais c'est tout.

Dokku est vraiment la plus petite implémentation de PaaS.

Le code source complet pour l'application Django est disponible sur :

%[https://github.com/nunombispo/DjangoTutorial]

Suivez-moi sur Twitter : [https://twitter.com/DevAsService](https://twitter.com/DevAsService)

Consultez mon site web à l'adresse : [https://developer-service.io/](https://developer-service.io/)

Ou consultez mon blog à l'adresse : [https://blog.developer-service.io/](https://blog.developer-service.io/)