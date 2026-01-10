---
title: Comment Dockeriser une Application Flask
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-11-11T16:04:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-dockerize-a-flask-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/flask-docker.png
tags:
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
- name: Flask Framework
  slug: flask
seo_title: Comment Dockeriser une Application Flask
seo_desc: 'By Ondiek Elijah Ochieng

  These days, developers need to develop, ship, and run applications quicker than
  ever. And fortunately, there''s a tool that helps you do that – Docker.

  With Docker, you can now easily ship, test, and deploy your code quickly w...'
---

Par Ondiek Elijah Ochieng

De nos jours, les développeurs doivent développer, livrer et exécuter des applications plus rapidement que jamais. Et heureusement, il existe un outil qui vous aide à faire cela – Docker.

Avec Docker, vous pouvez maintenant facilement livrer, tester et déployer votre code rapidement tout en gardant le contrôle total sur votre infrastructure. Cela réduit considérablement le temps nécessaire pour passer de l'écriture de code à son exécution en production.

Cet article vous montrera comment créer une image Docker de base et l'exécuter en tant que conteneur. Pour la démonstration, nous utiliserons Flask comme framework web et Docker pour la création d'images et la conteneurisation. Vous apprendrez également quelques commandes Docker couramment utilisées.

## Qu'est-ce que Flask ?

[**Flask**](https://flask.palletsprojects.com/en/2.0.x/) est un framework web micro Python populaire qui vous aide à développer rapidement et facilement des applications web et des API légères.

En tant que framework web, il offre une plus grande flexibilité, personnalisation et évolutivité pour les applications web simples tout en restant hautement compatible avec les technologies de pointe.

## Qu'est-ce que Docker ?

Docker est un outil qui facilite la création, le déploiement et l'exécution d'applications à l'aide de conteneurs.

Un **conteneur Docker** est une collection de dépendances et de code organisées en logiciel qui permet aux applications de s'exécuter rapidement et efficacement dans une gamme d'environnements informatiques.

Une **image Docker**, en revanche, est un plan qui spécifie comment exécuter une application. Afin que Docker puisse construire des images automatiquement, un ensemble d'instructions doit être stocké dans un fichier spécial connu sous le nom de **Dockerfile**.

Les instructions de ce fichier sont exécutées par l'utilisateur sur l'interface de ligne de commande afin de créer une image. (Source : [docker.com](https://www.docker.com/resources/what-container))

![Image](https://www.freecodecamp.org/news/content/images/2021/11/docker-illustration-2.png)

## Comment Configurer le Projet

### Structure de répertoire de base

Après avoir terminé les étapes suivantes, la structure de notre répertoire d'application ressemblera à ceci :

**flask-docker**  
├── app.py   
├── Dockerfile   
├── requirements.txt   
└── **venv**

Dans cette section, nous allons passer en revue comment créer une application avec une structure similaire à celle montrée ci-dessus. Vous pouvez trouver un guide détaillé sur la façon de créer ou d'installer ce projet [ici](https://github.com/Dev-Elie/Flask-Docker-App/blob/main/README.md#create-a-new-application-from-scratch).

En supposant que vous avez suivi correctement les instructions d'installation et que vous avez un environnement virtuel actif avec Flask installé, nous allons maintenant modifier les deux fichiers créés dans le README GitHub comme suit.

### Comment modifier app.py

Ajoutons les lignes de code suivantes à notre **app.py** :

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)
```

Maintenant, si nous exécutons **python app.py** sur la ligne de commande pour tester notre application Flask, nous devrions obtenir des résultats similaires à ceux montrés ci-dessous :

```bash
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 316-584-348


```

### Comment modifier le Dockerfile

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

Avant de construire une image pour l'application que nous venons de créer, comprenons d'abord ce que signifient les lignes de code dans le fichier Docker ci-dessus et quel rôle elles jouent.

Le code ci-dessous doit être la première ligne de chaque Dockerfile – il indique au constructeur Docker quelle syntaxe utiliser lors de l'analyse du Dockerfile et l'emplacement du fichier de syntaxe Docker. ([Source](https://docs.docker.com/engine/reference/builder/#syntax))

```dockerfile
# syntax=docker/dockerfile:1
```

Bien qu'il soit possible de créer nos propres images de base, il n'est pas nécessaire d'aller aussi loin car Docker nous permet d'hériter d'images existantes. La ligne suivante indique à Docker quelle image de base utiliser — dans ce cas, une image Python.

```
FROM python:3.8-slim-buster
```

Pour garder les choses organisées, nous indiquons également à Docker quel dossier utiliser pour le reste des opérations, nous utilisons donc un chemin relatif comme indiqué ci-dessous.

Dans ce cas, nous disons à Docker d'utiliser le même répertoire et le même nom pour le reste de ses opérations — c'est un répertoire contenu dans notre image de conteneur.

```
WORKDIR /python-docker

```

Dans les quatrième et cinquième lignes, nous disons à Docker de copier le contenu de notre fichier requirements.txt dans le fichier requirements.txt de l'image du conteneur. Ensuite, exécutez pip install pour installer toutes les dépendances dans le même fichier à utiliser par l'image.

```
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
```

En continuant avec la copie, nous copions maintenant le reste des fichiers de notre répertoire de travail local vers le répertoire dans l'image docker.

```
COPY . .
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/docker-illustration.png)

Notre image contient jusqu'à présent tous les fichiers qui sont similaires à ceux de notre répertoire de travail local. Notre prochaine tâche consiste à aider Docker à comprendre comment exécuter cette image à l'intérieur d'un conteneur.

Cette ligne indique spécifiquement à Docker d'exécuter notre application Flask en tant que module, comme l'indique le tag "-m". Ensuite, elle indique à Docker de rendre le conteneur disponible externement, par exemple depuis notre navigateur, plutôt que simplement depuis l'intérieur du conteneur. Nous passons le port hôte :

```
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

Puisque nous avions,

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Parce que nous avions l'instruction "if" dans notre fichier d'application, cela sera vrai si nous exécutons ce module en tant que programme autonome. Par conséquent, il peut fonctionner comme un module importé par un autre programme ou comme un programme autonome, mais il n'exécutera le code dans l'instruction if que s'il est exécuté en tant que programme. ([Source](https://stackoverflow.com/a/1973391/12943692))

## Comment Construire une Image Docker

Après cela, il ne reste plus qu'à construire notre image. En utilisant **`docker build`**, nous pouvons maintenant solliciter l'aide de Docker pour construire l'image. Vous pouvez combiner la commande de construction avec d'autres tags, tels que le flag "--tag", pour spécifier le nom de l'image.

```
docker build --tag python-docker .
```

### Comment exécuter une image en tant que conteneur

Exécuter une image à l'intérieur d'un conteneur est aussi simple que d'en construire une. Mais avant de le faire, nous aimerions voir quelles autres images sont disponibles dans notre environnement. Pour afficher les images depuis la ligne de commande, exécutez ce qui suit :

```
docker images
```

Si la commande ci-dessus trouve des images, la sortie devrait ressembler à ceci :

```bash
REPOSITORY      TAG       IMAGE ID       CREATED             SIZE
python-docker   latest    cd52b70b361a   About an hour ago   912MB
headless-cms    latest    e8b253e230ee   43 hours ago        937MB
scrappy         latest    3e7ac0d44890   7 weeks ago         904MB
python          3.9.2     587b1bc803b3   7 months ago        885MB

```

Maintenant, nous pouvons choisir quelle image exécuter. En utilisant la commande **`docker run`**, nous pouvons exécuter une image en passant le nom de l'image en tant que paramètre.

```docker
docker run
```

Lors de l'exécution de la commande ci-dessus, vous remarquerez que sur la ligne de commande, il indique que l'application est en cours d'exécution. Mais lorsque vous entrez [`http://localhost:5000/`](http://localhost:5000/) dans le navigateur, le message de salutation sera :

> Ce site est inaccessible, localhost a refusé la connexion.

Indépendamment du fait que le conteneur est en cours d'exécution, il fonctionne en mode isolation et ne peut pas se connecter à localhost:5000.

La meilleure solution est d'exécuter l'image en mode détaché. Parce que nous devons voir cette application dans le navigateur plutôt que dans le conteneur, nous allons modifier notre commande docker run et ajouter deux tags supplémentaires : "-d" pour l'exécuter en mode détaché et "-p" pour spécifier le port à exposer.

La commande docker run sera maintenant formatée comme suit :

```
docker run -d -p 5000:5000 python-docker
```

Cette fois, nous verrons la sortie suivante si nous l'exécutons en mode détaché et visitons localhost au port 5000 :

![Image](https://www.freecodecamp.org/news/content/images/2021/11/d.png)

Nous pouvons utiliser la commande suivante pour voir quels conteneurs sont actuellement en cours d'exécution :

```
docker ps
```

La sortie est la suivante :

```
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                    NAMES
a173935297cd   python-docker   "python3 -m flask ru…"   5 minutes ago   Up 5 minutes   0.0.0.0:5000->5000/tcp   happy_wescoff

```

Pour arrêter le conteneur actuellement en cours d'exécution, nous exécutons cette commande :

```
docker stop <container-name>
```

Une autre commande utile à avoir lors de l'utilisation de Docker est celle-ci :

```
docker container prune
```

Elle supprime les ressources inutilisées, libérant de l'espace et gardant votre système propre.

Et c'est tout !

Merci d'avoir pris le temps de lire cet article. Veuillez partager, me remercier dans un tweet et n'oubliez pas de me suivre sur Twitter [@dev_elie](https://twitter.com/dev_elie).

Vous pouvez trouver plus d'informations sur Docker et Python dans la [documentation officielle](https://docs.docker.com/language/python/). Je vous retrouverai la prochaine fois.