---
title: Flux de travail de développement Docker — un guide avec Flask et Postgres
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-08T11:05:40.000Z'
originalURL: https://freecodecamp.org/news/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NlqpTTAM8DbGl4paBmjE_g.jpeg
tags:
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Flux de travail de développement Docker — un guide avec Flask et Postgres
seo_desc: 'By Timothy Ko

  Docker, one of the latest crazes, is an amazing and powerful tool for packing, shipping,
  and running applications. However, understanding and setting up Docker for your
  specific application can take a bit of time. Since the internet is ...'
---

Par Timothy Ko

Docker, l'une des dernières tendances, est un outil incroyable et puissant pour emballer, livrer et exécuter des applications. Cependant, comprendre et configurer Docker pour votre application spécifique peut prendre un peu de temps. Comme l'internet est rempli de guides conceptuels, je n'irai pas trop en profondeur conceptuellement sur les Conteneurs. Au lieu de cela, j'expliquerai ce que chaque ligne que j'écris signifie et comment vous pouvez l'appliquer à votre application et configuration spécifiques.

![Image](https://cdn-media-1.freecodecamp.org/images/Qv18K6q0lHj07pm6jZk8lWgCkfib7Zg6xQMP)
_Photo par [Unsplash](https://unsplash.com/photos/m_HRfLhgABo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Christopher Gower</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Pourquoi Docker ?

Je fais partie d'une organisation à but non lucratif gérée par des étudiants appelée Hack4Impact à UIUC, où nous développons des projets techniques pour des organisations à but non lucratif afin de les aider à accomplir leurs missions. Chaque semestre, nous avons plusieurs équipes de projet de 5 à 7 développeurs logiciels étudiants, avec une variété de niveaux de compétence, y compris des étudiants qui n'ont terminé que leur premier cours de sciences informatiques de niveau universitaire.

Comme de nombreuses organisations à but non lucratif demandaient souvent des applications web, j'ai créé un Flask Boilerplate pour permettre aux équipes de mettre rapidement en place leurs services d'API REST backend. Les fonctions utilitaires courantes, la structure de l'application, les enveloppes de base de données et les connexions sont toutes fournies avec une documentation pour la configuration, les meilleures pratiques de codage et les étapes pour le déploiement sur Heroku.

#### Problèmes avec l'environnement de développement et les dépendances

Cependant, comme nous intégrons de nouveaux développeurs logiciels étudiants chaque semestre, les équipes passaient beaucoup de temps à configurer et à résoudre les problèmes d'environnement. Nous avions souvent plusieurs membres développant sur différents systèmes d'exploitation et nous sommes heurtés à une myriade de problèmes (Windows, je te regarde). Bien que beaucoup de ces problèmes soient triviaux, comme démarrer la bonne version de la base de données PostgreSQL avec le bon utilisateur/mot de passe, cela gaspillait du temps qui aurait pu être consacré au produit lui-même.

En plus de cela, j'ai seulement écrit de la documentation pour les utilisateurs de MacOS avec uniquement des instructions bash (j'ai un Mac), et j'ai essentiellement laissé les utilisateurs de Windows et Linux dans le flou. J'aurais pu lancer quelques machines virtuelles et documenter la configuration à nouveau pour chaque OS, mais pourquoi le ferais-je si Docker existe ?

#### Entrez Docker

Avec Docker, l'ensemble de l'application peut être isolé dans des conteneurs qui peuvent être portés d'une machine à une autre. Cela permet des environnements et des dépendances cohérents. Ainsi, vous pouvez « construire une fois, exécuter n'importe où », et les développeurs pourront maintenant installer une seule chose — Docker — et exécuter quelques commandes pour faire fonctionner l'application. Les nouveaux venus pourront commencer à développer rapidement sans se soucier de leur environnement. Les organisations à but non lucratif pourront également apporter rapidement des modifications à l'avenir.

Docker offre également de nombreux autres avantages, tels que sa nature portable et économe en ressources (par rapport aux machines virtuelles), et la manière dont vous pouvez configurer sans douleur l'intégration continue et déployer rapidement votre application.

### Un bref aperçu des composants principaux de Docker

Il existe de nombreuses ressources en ligne qui expliquent Docker mieux que je ne pourrais le faire, donc je ne les passerai pas en revue en détail. Voici un [article de blog génial](https://medium.freecodecamp.org/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b) sur ses concepts, et [un autre](https://medium.com/@xenonstack/docker-overview-a-complete-guide-43decd218eca) sur Docker spécifiquement. Je vais cependant passer en revue certains des composants principaux de Docker nécessaires pour comprendre le reste de cet article de blog.

#### Images Docker

Les images Docker sont des modèles en lecture seule qui décrivent un conteneur Docker. Elles incluent des instructions spécifiques écrites dans un Dockerfile qui définit l'application et ses dépendances. Considérez-les comme une capture instantanée de votre application à un moment donné. Vous obtiendrez des images lorsque vous exécuterez `docker build`.

#### Conteneurs Docker

Les conteneurs Docker sont des instances d'images Docker. Ils incluent le système d'exploitation, le code de l'application, l'environnement d'exécution, les outils système, les bibliothèques système, et ainsi de suite. Vous pouvez connecter plusieurs conteneurs Docker ensemble, comme avoir une application Node.js dans un conteneur qui est connectée à un conteneur de base de données Redis. Vous exécuterez un conteneur Docker avec `docker start`.

#### Registres Docker

Un registre Docker est un endroit où vous pouvez stocker et distribuer des images Docker. Nous utiliserons des images Docker comme nos images de base à partir de DockerHub, un registre gratuit hébergé par Docker lui-même.

#### Docker Compose

Docker Compose est un outil qui vous permet de construire et de démarrer plusieurs images Docker en une seule fois. Au lieu d'exécuter les mêmes commandes multiples chaque fois que vous voulez démarrer votre application, vous pouvez tout faire en une seule commande — une fois que vous avez fourni une configuration spécifique.

### Exemple Docker avec Flask et Postgres

Avec tous les composants Docker en tête, passons à la configuration d'un environnement de développement Docker avec une application Flask utilisant Postgres comme stockage de données. Pour le reste de cet article de blog, je ferai référence à [Flask Boilerplate](https://github.com/tko22/flask-boilerplate), le dépôt que j'ai mentionné précédemment pour Hack4Impact.

Dans cette configuration, nous utiliserons Docker pour construire deux images :

* `app` — l'application Flask servie sur le port 5000
* `postgres` — la base de données Postgres servie sur le port 5432

Lorsque vous regardez le répertoire principal, il y a trois fichiers qui définissent cette configuration :

* **Dockerfile** — un script composé d'instructions pour configurer les conteneurs `app`. Chaque commande est automatique et est exécutée successivement. Ce fichier sera situé dans le répertoire où vous exécutez l'application (`python manage.py runserver` ou `python app.py` ou `npm start` en sont quelques exemples). Dans notre cas, il se trouve dans le répertoire principal (où se trouve `manage.py`). Un Dockerfile accepte les [instructions Docker](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#build-cache).
* **.dockerignore** — spécifie les fichiers à ne pas inclure dans le conteneur. C'est comme `.gitignore` mais pour les conteneurs Docker. Ce fichier est associé au Dockerfile.
* **docker-compose.yml** — Fichier de configuration pour Docker Compose. Cela nous permettra de construire les images `app` et `postgres` en une seule fois, de définir des volumes et de déclarer que `app` dépend de `postgres`, et de définir les variables d'environnement requises.

**Note :** Il n'y a qu'un seul Dockerfile pour deux images car nous utiliserons une image Docker Postgres officielle de DockerHub ! Vous pouvez inclure votre propre image Postgres en écrivant votre propre Dockerfile pour celle-ci, mais il n'y a pas d'intérêt.

#### Dockerfile

Pour clarifier à nouveau, ce Dockerfile est pour le conteneur `app`. En tant qu'aperçu, voici l'ensemble du Dockerfile — il obtient essentiellement une image de base, copie l'application, installe les dépendances et définit une variable d'environnement spécifique.

```
FROM python:3.6
```

```
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"
```

```
RUN apt-get update
```

```
RUN mkdir /app
```

```
WORKDIR /app
```

```
COPY . /app
```

```
RUN pip install --no-cache-dir -r requirements.txt
```

```
ENV FLASK_ENV="docker"
```

```
EXPOSE 5000
```

Comme cette application Flask utilise Python 3.6, nous voulons un environnement qui le supporte et l'a déjà installé. Heureusement, [DockerHub](https://hub.docker.com/) a une image officielle qui est installée sur Ubuntu. En une ligne, nous aurons une image de base Ubuntu avec Python 3.6, virtualenv et pip. Il y a des tonnes d'images sur DockerHub, mais si vous souhaitez commencer avec une image Ubuntu fraîche et construire par-dessus, vous pourriez le faire.

```
FROM python:3.6
```

Je note ensuite que je suis le mainteneur.

```
LABEL maintainer "Timothy Ko <tk2@illinois.edu>"
```

Il est maintenant temps d'ajouter l'application Flask à l'image. Pour simplifier, j'ai décidé de copier l'application sous le répertoire `/app` sur notre image Docker.

```
RUN mkdir /app
```

```
COPY . /app
```

```
WORKDIR /app
```

`WORKDIR` est essentiellement un `cd` en bash, et `COPY` copie un certain répertoire vers le répertoire fourni dans une image. `ADD` est une autre commande qui fait la même chose que `COPY`, mais elle vous permet également d'ajouter un dépôt à partir d'une URL. Ainsi, si vous souhaitez cloner votre dépôt git au lieu de le copier depuis votre dépôt local (à des fins de staging et de production), vous pouvez utiliser cela. `COPY`, cependant, devrait être utilisé la plupart du temps sauf si vous avez une URL. Chaque fois que vous utilisez `RUN`, `COPY`, `FROM` ou `CMD`, vous créez une nouvelle couche dans votre image docker, ce qui affecte la manière dont Docker stocke et met en cache les images. Pour plus d'informations sur les meilleures pratiques et la couche, voir [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

Maintenant que nous avons notre dépôt copié dans l'image, nous allons installer toutes nos dépendances, qui sont définies dans `requirements.txt`

```
RUN pip install --no-cache-dir -r requirements.txt
```

Mais disons que vous avez une application Node au lieu de Flask — vous écriviez plutôt `RUN npm install`. L'étape suivante consiste à dire à Flask d'utiliser les configurations Docker que j'ai codées en dur dans `config.py`. Dans cette configuration, Flask se connectera à la base de données correcte que nous configurerons plus tard. Comme j'avais des configurations de production et de développement régulier, j'ai fait en sorte que Flask choisisse la configuration Docker chaque fois que la variable d'environnement `FLASK_ENV` est définie sur `docker`. Donc, nous devons configurer cela dans notre image `app`.

```
ENV FLASK_ENV="docker"
```

Ensuite, exposez le port (5000) sur lequel l'application Flask s'exécute :

```
EXPOSE 5000
```

Et c'est tout ! Donc, peu importe le système d'exploitation que vous utilisez, ou à quel point vous êtes mauvais pour suivre les instructions de documentation, votre image Docker sera la même que celle de vos coéquipiers grâce à ce Dockerfile.

Chaque fois que vous construisez votre image, ces commandes suivantes seront exécutées. Vous pouvez maintenant construire cette image avec `sudo docker build -t app .`. Cependant, lorsque vous l'exécutez avec `sudo docker run app` pour démarrer un conteneur Docker, l'application rencontrera une erreur de connexion à la base de données. Cela est dû au fait que vous n'avez pas encore provisionné de base de données.

#### docker-compose.yml

Docker Compose vous permettra de le faire et de construire votre image `app` en même temps. Le fichier entier ressemble à ceci :

```
version: '2.1'services:  postgres:    restart: always    image: postgres:10    environment:      - POSTGRES_USER=${POSTGRES_USER}      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}      - POSTGRES_DB=${POSTGRES_DB}    volumes:      - ./postgres-data/postgres:/var/lib/postgresql/data    ports:      - "5432:5432"  app:    restart: always    build: .    ports:      - 5000:5000    volumes:      - .:/app
```

Pour ce dépôt spécifique, j'ai décidé d'utiliser la version 2.1 car je suis plus à l'aise avec elle et elle avait quelques guides et tutoriels supplémentaires — oui, c'est ma seule raison de ne pas utiliser la version 3. Avec la version 2, vous devez fournir des « services » ou des images que vous souhaitez inclure. Dans notre cas, il s'agit de `app` et `postgres` (ce ne sont que des noms que vous pouvez utiliser lorsque vous utilisez des commandes docker-compose. Vous pouvez les appeler `database` et `api` ou ce qui vous plaît).

#### Image Postgres

En regardant le service Postgres, je précise qu'il s'agit d'une image `postgres:10`, qui est une autre image DockerHub. Cette image est une image Ubuntu qui a Postgres installé et démarrera automatiquement le serveur Postgres.

```
postgres:  restart: always  image: postgres:10  environment:    - POSTGRES_USER=${USER}    - POSTGRES_PASSWORD=${PASSWORD}    - POSTGRES_DB=${DB}  volumes:    - ./postgres-data/postgres:/var/lib/postgresql/data  ports:    - "5432:5432"
```

Si vous voulez une version différente, changez simplement le « 10 » en autre chose. Pour spécifier l'utilisateur, le mot de passe et la base de données que vous souhaitez dans Postgres, vous devez définir des variables d'environnement au préalable — cela est implémenté dans le Dockerfile de l'image Docker officielle de postgres. Dans ce cas, l'image `postgres` injectera les variables d'environnement `$USER`, `$PASSWORD` et `$DB` et les transformera en variables d'environnement `POSTGRES_USER`, `POSTGRES_PASSWORD` et `POSTGRES_DB` **à l'intérieur** du conteneur postgres. Notez que `$USER` et les autres variables d'environnement injectées sont des variables d'environnement spécifiées sur votre propre ordinateur (plus précisément le processus de ligne de commande que vous utilisez pour exécuter la commande `docker-compose up`. En injectant vos identifiants, cela vous permet de ne pas commettre vos identifiants dans un dépôt public.

Docker-compose injectera également automatiquement des variables d'environnement si vous avez un fichier `.env` dans le même répertoire que votre fichier `docker-compose.yml`. Voici un exemple de fichier .env pour ce scénario :

```
USER=testusrPASSWORD=passwordDB=testdb
```

Ainsi, notre base de données PostgreSQL s'appellera **testdb** avec un utilisateur appelé **testusr** avec le mot de passe **password**.

Notre application Flask se connectera à cette base de données spécifique, car j'ai écrit son URL dans les configurations Docker que j'ai mentionnées précédemment.

Chaque fois qu'un conteneur est arrêté et supprimé, les données sont supprimées. Ainsi, vous devez fournir un stockage de données persistant afin qu'aucune des données de la base de données ne soit supprimée. Il existe deux façons de le faire :

* Volumes Docker
* Montages de répertoires locaux

J'ai choisi de le monter localement vers `./postgres-data/postgres`, mais cela peut être n'importe où. La syntaxe est toujours `[HOST]:[CONTAINER]`. Cela signifie que toute donnée de `/var/lib/postgresql/data` est en réalité stockée dans `./postgres-data`.

```
volumes:- ./postgres-data/postgres:/var/lib/postgresql/data
```

Nous utiliserons la même syntaxe pour les ports :

```
ports:- "5432:5432"
```

#### Image app

Nous allons ensuite définir l'image `app`.

```
app:  restart: always  build: .  ports:    - 5000:5000  volumes:     - .:/app  depends_on:    - postgres  entrypoint: ["python", "manage.py","runserver"]
```

Nous définissons d'abord qu'elle doit avoir `restart: always`. Cela signifie qu'elle redémarrera chaque fois qu'elle échouera. Cela est particulièrement utile lorsque nous construisons et démarrons ces conteneurs. `app` démarrera généralement avant `postgres`, ce qui signifie que `app` essaiera de se connecter à la base de données et échouera, car `postgres` n'est pas encore démarré. Sans cette propriété, `app` s'arrêterait simplement et ce serait la fin.

Nous définissons ensuite que nous voulons que cette construction soit le Dockerfile qui se trouve dans ce répertoire actuel :

```
build: .
```

Cette étape suivante est assez importante pour que le serveur Flask redémarre chaque fois que vous modifiez un code dans votre dépôt local. Cela est très utile afin que vous n'ayez pas à reconstruire votre image encore et encore chaque fois pour voir vos modifications. Pour ce faire, nous faisons la même chose que nous avons faite pour `postgres` : nous déclarons que le répertoire `/app` à l'intérieur du conteneur sera ce qui se trouve dans .(le répertoire actuel). Ainsi, toute modification dans votre dépôt local sera reflétée à l'intérieur du conteneur.

```
volumes:  - .:/app
```

Après cela, nous devons dire à Docker Compose que app dépend du conteneur `postgres`. Notez que si vous changez le nom de l'image en autre chose comme `database`, vous devez remplacer ce `postgres` par ce nom.

```
depends_on:  - postgres
```

Enfin, nous devons fournir la commande qui est appelée pour démarrer notre application. Dans notre cas, c'est `python manage.py runserver`.

```
entrypoint: ["python", "manage.py","runserver"]
```

Un point à noter pour Flask est que vous devez explicitement indiquer quel hôte (port) vous souhaitez utiliser pour l'exécuter, et si vous souhaitez qu'il soit en mode debug lorsque vous l'exécutez. Donc dans `manage.py`, je fais cela avec :

```
def runserver():    app.run(debug=True, host=0.0.0.0', port=5000)
```

Enfin, construisez et démarrez votre application Flask et votre base de données Postgres en utilisant votre ligne de commande :

```
docker-compose builddocker-compose up -ddocker-compose exec app python manage.py recreate_db
```

La dernière commande crée essentiellement le schéma de la base de données défini par mon application Flask dans Postgres.

Et c'est tout ! Vous devriez pouvoir voir l'application Flask s'exécuter sur http://localhost:5000 !

#### Commandes Docker

Se souvenir et trouver des commandes Docker peut être assez frustrant au début, donc [voici](https://medium.com/statuscode/dockercheatsheet-9730ce03630d) une liste d'entre elles ! J'ai également écrit un tas de commandes couramment utilisées dans ma [documentation Flask Boilerplate](https://github.com/tko22/flask-boilerplate) si vous souhaitez vous y référer.

### Conclusion

Docker permet vraiment aux équipes de développer beaucoup plus rapidement avec sa portabilité et ses environnements cohérents sur différentes plateformes. Bien que je n'aie passé en revue que l'utilisation de Docker pour le développement, Docker excelle lorsque vous l'utilisez pour l'intégration continue/les tests et le déploiement.

Je pourrais ajouter quelques lignes de plus et avoir une configuration de production complète avec Nginx et Gunicorn. Si je voulais utiliser Redis pour la mise en cache de session ou comme une file d'attente, je pourrais le faire très rapidement et tout le monde dans mon équipe pourrait avoir le même environnement lorsqu'ils reconstruisent leurs images Docker.

Non seulement cela, je pourrais lancer 20 instances de l'application Flask en quelques secondes si je le voulais. Merci d'avoir lu ! :)

_Si vous avez des pensées et des commentaires, n'hésitez pas à laisser un commentaire ci-dessous ou à m'envoyer un email à tk2@illinois.edu ! De plus, n'hésitez pas à utiliser mon code ou à partager cela avec vos pairs !_