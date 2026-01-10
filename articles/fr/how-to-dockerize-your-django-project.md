---
title: Comment Dockeriser Votre Projet Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-18T16:37:57.106Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-your-django-project
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744994272728/248cef70-5f8e-46fd-a640-66852ffda7d2.png
tags:
- name: Python
  slug: python
- name: Docker
  slug: docker
seo_title: Comment Dockeriser Votre Projet Django
seo_desc: 'If you''re working on a Django project and you want to make your life easier
  – especially when it comes to running your app across different environments – Docker
  is your new best friend.

  Docker makes it possible to package your Django app, along with...'
---

Si vous travaillez sur un projet Django et que vous souhaitez vous simplifier la vie, surtout lorsqu'il s'agit d'exécuter votre application dans différents environnements, Docker est votre nouveau meilleur ami.

Docker permet d'empaqueter votre application Django, ainsi que toutes ses dépendances, dans ce qu'on appelle un "conteneur".

Ainsi, elle s'exécute de la même manière sur votre ordinateur, celui de votre collègue, un serveur de test, ou même en production.

Lorsque j'ai commencé à utiliser Docker, cela m'a semblé un peu écrasant. Mais après l'avoir configuré pour quelques applications Django, tout est devenu clair.

La bonne nouvelle ? Je vais vous guider étape par étape, de manière facile à suivre, même si vous êtes nouveau dans Docker.

## Table des Matières

1. [Ce Dont Vous Avez Besoin](#heading-ce-dont-vous-avez-besoin)
    
2. [Comment Dockeriser Votre Projet Django](#comment-dockeriser-votre-projet-django)
    
    * [Étape 1 : Démarrer un Projet Django](#heading-etape-1-demarrer-un-projet-django)
        
    * [Étape 2 : Créer un Dockerfile](#heading-etape-2-creer-un-dockerfile)
        
    * [Étape 3 : Ajouter un requirements.txt](#heading-etape-3-ajouter-un-requirementstxt)
        
    * [Étape 4 : Créer docker-compose.yml](#heading-etape-4-creer-docker-composeyml)
        
    * [Étape 5 : Exécuter !](#heading-etape-5-executer)
        
3. [Problèmes Courants](#heading-problemes-courants)
    
    * [Port Déjà Utilisé ?](#heading-port-deja-utilise)
        
    * [Base de Données Ne Fonctionne Pas ?](#heading-base-de-donnees-ne-fonctionne-pas)
        
4. [FAQ](#heading-faq)
    
    * [Ai-je besoin de Docker pour le développement ?](#heading-ai-je-besoin-de-docker-pour-le-developpement)
        
    * [Puis-je exécuter des migrations à l'intérieur de Docker ?](#heading-puis-je-executer-des-migrations-a-linterieur-de-docker)
        
    * [Comment tout arrêter ?](#heading-comment-tout-arreter)
        
5. [Conseil Supplémentaire : Utiliser .dockerignore](#heading-conseil-supplementaire-utiliser-dockerignore)
    
6. [Ce Que Vous Avez Construit](#heading-ce-que-vous-avez-construit)
    
7. [Voulez-vous Approfondir ?](#heading-voulez-vous-approfondir)
    
8. [Lectures Complémentaires](#heading-lectures-complementaires)
    

## Ce Dont Vous Avez Besoin

Avant de commencer, assurez-vous d'avoir installé quelques éléments :

* **Python 3** (n'importe quelle version supportée par Django)
    
* **Django** (bien sûr)
    
* **Docker et Docker Compose**  
    👉 [Installer Docker](https://docs.docker.com/engine/install/)  
    👉 [Installer Docker Compose](https://docs.docker.com/compose/install/linux/)
    

Vous n'avez pas besoin d'être un expert en Docker. Je vais expliquer chaque partie au fur et à mesure que nous le construirons ensemble.

## Comment Dockeriser Votre Projet Django

### Étape 1 : Démarrer un Projet Django

Si vous avez déjà un projet Django, vous pouvez sauter cette partie.

Sinon, ouvrez votre terminal et exécutez :

```bash
django-admin startproject monprojet
cd monprojet
```

Cela créera un nouveau projet Django appelé `monprojet`. Vous verrez une structure comme celle-ci :

```markdown
monprojet/
├── manage.py
└── monprojet/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Disons que c'est votre application que vous souhaitez exécuter dans Docker.

### Étape 2 : Créer un Dockerfile

À la racine de votre projet (dans le même dossier que `manage.py`), créez un fichier appelé `Dockerfile`. Pas d'extension de fichier, juste `Dockerfile`.

Voici ce qui va à l'intérieur :

```dockerfile
# Utilise l'image officielle Python
FROM python:3.10-slim

# Définit les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Installe les dépendances
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie le reste du code
COPY . /app/
```

Laissez-moi décomposer cela :

* `FROM python:3.10-slim` : Cela indique à Docker d'utiliser une version légère de Python 3.10.
    
* `ENV` : Ces lignes aident à avoir des logs plus propres et de meilleures performances.
    
* `WORKDIR /app` : Cela définit le répertoire de travail par défaut à l'intérieur du conteneur.
    
* `COPY` et `RUN` : Ces lignes copient votre code dans le conteneur et installent vos packages Python.
    

### Étape 3 : Ajouter un `requirements.txt`

Vous aurez besoin d'un fichier listant vos packages Python.

Créez un fichier appelé `requirements.txt` dans le dossier racine et ajoutez :

```plaintext
Django>=4.0,<5.0
```

Vous pouvez en ajouter plus tard si votre projet grandit. Pour l'instant, cela suffit.

Pour générer une liste complète des dépendances à partir de votre environnement virtuel local, exécutez :

```bash
pip freeze > requirements.txt
```

### Étape 4 : Créer `docker-compose.yml`

Maintenant, créons le fichier qui indique à Docker comment exécuter tout ensemble.

Dans votre dossier racine, créez `docker-compose.yml` :

```yaml
version: '3.9'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
```

Passons en revue ligne par ligne :

* `build: .` : Cela indique à Docker d'utiliser le `Dockerfile` dans le dossier courant.
    
* `command` : Cela exécute le serveur de développement de Django à l'intérieur du conteneur.
    
* `volumes` : Cela monte votre code dans le conteneur afin que les modifications soient reflétées en direct.
    
* `ports` : Cela mappe le port 8000 à l'intérieur de Docker au port 8000 sur votre machine.
    

Ainsi, si vous allez sur `http://localhost:8000`, vous verrez votre application.

### Étape 5 : Exécuter !

Maintenant, la partie amusante. Depuis votre terminal, exécutez :

```bash
docker-compose up --build
```

Cela indique à Docker de :

* Construire le conteneur
    
* Installer les dépendances
    
* Exécuter le serveur Django
    

Si tout se passe bien, vous verrez les logs du serveur Django, et vous pourrez ouvrir votre navigateur et aller sur `http://localhost:8000`.

Vous devriez voir l'écran de bienvenue de Django.

## Problèmes Courants

### Port Déjà Utilisé ?

Si le port 8000 est occupé, changez cette ligne dans `docker-compose.yml` :

```yaml
ports:
  - "8001:8000"
```

Puis allez sur `http://localhost:8001`.

### Base de Données Ne Fonctionne Pas ?

Si vous avez besoin d'une base de données (comme PostgreSQL), vous pouvez ajouter un autre service à `docker-compose.yml`. Voici un exemple avec PostgreSQL :

```yaml
services:
  db:
    image: postgres
    environment:
      POSTGRES_DB: mabasededonnees
      POSTGRES_USER: utilisateur
      POSTGRES_PASSWORD: motdepasse
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
```

Ensuite, mettez à jour votre `settings.py` dans Django pour utiliser cette base de données.

## FAQ

### **Ai-je besoin de Docker pour le développement ?**

Non, mais cela aide à garder votre environnement propre et cohérent. Si cela fonctionne dans Docker, cela fonctionnera partout.

### **Puis-je exécuter des migrations à l'intérieur de Docker ?**

Oui ! Il suffit d'exécuter :

```bash
docker-compose run web python manage.py migrate
```

### **Comment tout arrêter ?**

Appuyez sur `Ctrl+C` pour arrêter le serveur en cours d'exécution, et si vous voulez supprimer les conteneurs :

```bash
docker-compose down
```

## Conseil Supplémentaire : Utiliser `.dockerignore`

Tout comme `.gitignore`, vous pouvez créer un fichier `.dockerignore` pour éviter de copier des fichiers inutiles dans le conteneur Docker. En voici un simple :

```nginx
__pycache__
*.pyc
*.pyo
*.pyd
.env
.git
```

## Ce Que Vous Avez Construit

À ce stade, vous avez :

* Créé un projet Django
    
* Construit un conteneur Docker pour celui-ci
    
* Configuré `docker-compose` pour exécuter le tout
    
* Appris à tout gérer facilement
    

Une fois que vous êtes à l'aise, vous pouvez étendre cette configuration avec des fichiers statiques, NGINX, Gunicorn, ou même des builds Docker prêts pour la production.

## Voulez-vous Approfondir ?

Si cela semble beaucoup, c'est normal. Cela prend un peu de pratique, mais une fois que vous l'avez fait quelques fois, Docker devient une seconde nature.

Vous passerez moins de temps à déboguer les problèmes de configuration et plus de temps à coder votre application.

### Lectures Complémentaires

* [Documentation Docker](https://docs.docker.com/)
    
* [Documentation Officielle de Django](https://docs.djangoproject.com/)
    
* [Référence du Fichier Compose](https://docs.docker.com/reference/compose-file/)