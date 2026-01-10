---
title: Un guide pour débutants sur Docker — comment créer un client/serveur avec docker-compose
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2019-04-19T21:36:23.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QSnA3oNKDD2jCErVkaX-Gg.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un guide pour débutants sur Docker — comment créer un client/serveur avec
  docker-compose
seo_desc: 'You are a developer and you want to discover docker-compose? This article
  is made for you.

  After a short introduction on Docker-Compose, you will be able to create your first
  client/server-side application with Docker.


  This article takes into consid...'
---

#### Vous êtes développeur et vous souhaitez découvrir docker-compose ? Cet article est fait pour vous.

Après une courte introduction sur Docker-Compose, vous serez en mesure de créer votre première application client/serveur avec Docker.

> Cet article suppose que vous connaissez les bases de Docker. Si ce n'est pas le cas, ne paniquez pas ! Je vous suggère de lire mon premier article pour découvrir Docker et apprendre à créer votre première application.



[**Un guide pour débutants sur Docker — comment créer votre première application Docker**  
_Vous êtes développeur et vous souhaitez commencer avec Docker ? Cet article est fait pour vous. Après une courte introduction sur ce qu'est Docker et pourquoi l'utiliser, vous serez en mesure de créer votre première application avec Docker._](https://herewecode.io/blog/a-beginners-guide-to-docker-how-to-create-your-first-docker-application/)

#### Qu'est-ce que Docker-Compose ?

Docker-Compose est un outil fourni par Docker. Pour faire simple, cet outil est implémenté pour résoudre des problèmes architecturaux dans vos projets.

Comme vous avez pu le remarquer dans mon article précédent, nous avons créé un programme simple qui affichait « Docker est magique ! » lorsqu'il était lancé.

Malheureusement, en tant que développeur, vous créez rarement un programme autonome (un programme qui ne nécessite aucun autre service pour fonctionner, comme une base de données).

Cependant, comment savoir si vous avez besoin de Docker-Compose ? C'est très simple — si votre application nécessite plusieurs services pour fonctionner, vous avez besoin de cet outil. Par exemple, si vous créez un site web qui doit se connecter à votre base de données pour authentifier les utilisateurs (ici 2 services, site web et base de données).

Docker-compose vous offre la possibilité de lancer tous ces services en une seule commande.

#### Différence entre Docker et Docker-Compose

Docker est utilisé pour gérer un conteneur individuel (service) pour votre application.

Docker-Compose est utilisé pour gérer plusieurs conteneurs en même temps pour la même application. Cet outil offre les mêmes fonctionnalités que Docker mais permet d'avoir des applications plus complexes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LHq5mhynSjYBIhfgY3czkQ.png)
_Docker (conteneur individuel) VS Docker-Compose (plusieurs conteneurs)_

#### Un cas d'utilisation typique

Cet outil peut devenir très puissant et vous permettre de déployer des applications avec des architectures complexes très rapidement. Je vais vous donner une étude de cas concrète qui prouvera que vous en avez besoin.

Imaginez, vous êtes le fier créateur de votre logiciel web.

Votre solution offre deux sites web. Le premier permet aux magasins de créer leur boutique en ligne en quelques clics. Le second est dédié au support client. Ces deux sites interagissent avec la même base de données.

Vous commencez à avoir du succès et votre serveur n'est plus suffisant. Vous décidez donc de migrer l'ensemble de votre logiciel vers une autre machine.

Malheureusement, vous n'avez pas utilisé docker-compose. Vous allez donc devoir migrer et reconfigurer vos services un après l'autre, en espérant n'avoir rien oublié.

Si vous aviez utilisé un docker-compose, en seulement quelques commandes, vous auriez déployé toute votre architecture sur votre nouveau serveur. Il ne vous reste plus qu'à faire quelques configurations et charger la sauvegarde de votre base de données pour finaliser la migration.

#### Créons maintenant votre première application client/serveur avec Docker-Compose

Maintenant que vous savez à quoi va servir docker-compose, il est temps de créer votre première application client/serveur !

L'objectif de ce tutoriel est de créer un petit site web (serveur) en Python qui contiendra une phrase. Cette phrase doit être récupérée par un programme (client) en Python qui l'affichera.

> Note : Ce tutoriel suppose que vous avez déjà installé Docker sur votre ordinateur et que vous en connaissez les bases. Si ce n'est pas le cas, je vous invite à vous référer à [mon article précédent](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/).

#### 1. Créez votre projet

Pour créer votre première application client/serveur, je vous invite à créer un dossier sur votre ordinateur. Il doit contenir à la racine les fichiers et dossiers suivants :

* Un fichier '_docker-compose.yml_' (fichier docker-compose qui contiendra les instructions nécessaires pour créer les différents services).
* Un dossier '_server_' (ce dossier contiendra les fichiers nécessaires à la configuration du serveur).
* Un dossier '_client_' (ce dossier contiendra les fichiers nécessaires à la configuration du client).

Normalement, vous devriez avoir cette architecture de dossier :

```
.
├── client/
├── docker-compose.yml
└── server/
2 directories, 1 file
```

#### 2. Créez votre serveur

Afin de commencer par des rappels des bases de Docker, nous allons commencer par créer le serveur.

**2a. Créez les fichiers**

Déplacez-vous dans votre dossier '_server_' et créez les fichiers suivants :

* Un fichier '_server.py_' (fichier python qui contiendra le code du serveur).
* Un fichier '_index.html_' (fichier html qui contiendra la phrase à afficher).
* Un fichier '_Dockerfile_' (fichier docker qui contiendra les instructions nécessaires pour créer l'environnement du serveur).

Normalement, vous devriez avoir cette architecture de dossier dans le chemin suivant '_server/_' :

```
.
├── Dockerfile
├── index.html
└── server.py
0 directories, 3 files
```

**2b. Modifiez le fichier Python**

Vous pouvez ajouter le code suivant au fichier '_server.py_' :

```python
#!/usr/bin/env python3

# Import des bibliothèques système de python.
# Ces bibliothèques seront utilisées pour créer le serveur web.
# Vous n'avez pas besoin d'installer quoi que ce soit de spécial, ces bibliothèques sont installées avec Python.
import http.server
import socketserver

# Cette variable va gérer les requêtes de notre client sur le serveur.
handler = http.server.SimpleHTTPRequestHandler

# Ici, nous définissons que nous voulons démarrer le serveur sur le port 1234.
# Essayez de retenir cette information, elle nous sera très utile plus tard avec docker-compose.
with socketserver.TCPServer(("", 1234), handler) as httpd:
    # Cette instruction maintiendra le serveur en cours d'exécution, en attente des requêtes du client.
    httpd.serve_forever()
```

Ce code vous permettra de créer un serveur web simple dans ce dossier. Il récupérera le contenu du fichier index.html pour le partager sur une page web.

**2c. Modifiez le fichier Html**

Vous pouvez ajouter la phrase suivante au fichier '_index.html_' :

```
Docker-Compose est magique !
```

Ce fichier sera partagé par le serveur lorsqu'il sera démarré et cette phrase sera affichée.

**2d. Modifiez le fichier Docker**

Ici, nous allons créer un Dockerfile de base qui sera responsable de l'exécution de notre fichier Python. Nous utiliserons [l'image officielle](https://hub.docker.com/_/python) créée pour exécuter Python.

```python
# Juste un rappel, dockerfile doit toujours commencer par l'import de l'image de base.
# Nous utilisons le mot-clé 'FROM' pour cela.
# Dans notre exemple, nous voulons importer l'image python (de DockerHub).
# Nous écrivons donc 'python' pour le nom de l'image et 'latest' pour la version.
FROM python:latest

# Afin de lancer notre code python, nous devons importer les fichiers 'server.py' et 'index.html'.
# Nous utilisons le mot-clé 'ADD' pour cela.
# Juste un rappel, le premier paramètre 'server.py' est le nom du fichier sur l'hôte.
# Le deuxième paramètre '/server/' est le chemin où mettre le fichier sur l'image.
# Ici, nous mettons les fichiers dans le dossier '/server/' de l'image.
ADD server.py /server/
ADD index.html /server/

# J'aimerais introduire quelque chose de nouveau, la commande 'WORKDIR'.
# Cette commande change le répertoire de base de votre image.
# Ici, nous définissons '/server/' comme répertoire de base (où toutes les commandes seront exécutées).
WORKDIR /server/
```

#### **3. Créez votre client**

Afin de continuer avec des rappels des bases de Docker, nous allons créer le client.

**3a. Créez les fichiers**

Déplacez-vous dans votre dossier '_client_' et créez les fichiers suivants :

* Un fichier '_client.py_' (fichier python qui contiendra le code du client).
* Un fichier '_Dockerfile_' (fichier docker qui contiendra les instructions nécessaires pour créer l'environnement du client).

Normalement, vous devriez avoir cette architecture de dossier dans le chemin suivant '_client/_' :

```
.
├── client.py
└── Dockerfile
0 directories, 2 files
```

**3b. Modifiez le fichier Python**

Vous pouvez ajouter le code suivant au fichier '_client.py_' :

```python
#!/usr/bin/env python3

# Import de la bibliothèque système de python.
# Cette bibliothèque est utilisée pour télécharger le 'index.html' du serveur.
# Vous n'avez pas besoin d'installer quoi que ce soit de spécial, cette bibliothèque est installée avec Python.
import urllib.request

# Cette variable contient la requête sur 'http://localhost:1234/'.
# Vous devez vous demander ce qu'est 'http://localhost:1234' ?
# localhost : Cela signifie que le serveur est local.
# 1234 : Souvenez-vous, nous avons défini 1234 comme port du serveur.
fp = urllib.request.urlopen("http://localhost:1234/")

# 'encodedContent' correspond à la réponse du serveur encodée ('index.html').
# 'decodedContent' correspond à la réponse du serveur décodée (ce que nous voulons afficher).
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Affiche le fichier du serveur : 'index.html'.
print(decodedContent)

# Ferme la connexion au serveur.
fp.close()
```

Ce code vous permettra de récupérer le contenu de la page web du serveur et de l'afficher.

**3c. Modifiez le fichier Docker**

Comme pour le serveur, nous allons créer un Dockerfile de base qui sera responsable de l'exécution de notre fichier Python.

```python
# Même chose que le Dockerfile du 'server'.
FROM python:latest

# Même chose que le Dockerfile du 'server'.
# Nous importons 'client.py' dans le dossier '/client/'.
ADD client.py /client/

# J'aimerais introduire quelque chose de nouveau, la commande 'WORKDIR'.
# Cette commande change le répertoire de base de votre image.
# Ici, nous définissons '/client/' comme répertoire de base.
WORKDIR /client/
```

#### **4. Retour à Docker-Compose**

Comme vous avez pu le remarquer, nous avons créé deux projets différents, le serveur et le client, tous deux avec un Dockerfile.

Jusqu'à présent, rien n'a changé par rapport aux bases que vous connaissez déjà.

Maintenant, nous allons modifier le fichier '_docker-compose.yml_' à la racine du dépôt.

> Note : Docker-Compose étant très complet, cet article vise à vous donner un exemple concret et typique. C'est pourquoi vous ne verrez pas tous les mots-clés.

```python
# Un docker-compose doit toujours commencer par le tag version.
# Nous utilisons "3" car c'est la dernière version à ce jour.
version: "3"

# Vous devez savoir que docker-compose fonctionne avec des services.
# 1 service = 1 conteneur.
# Par exemple, un service peut être un serveur, un client, une base de données...
# Nous utilisons le mot-clé 'services' pour commencer à créer des services.
services:
  # Comme nous l'avons dit au début, nous voulons créer : un serveur et un client.
  # Cela fait deux services.

  # Premier service (conteneur) : le serveur.
  # Ici, vous êtes libre de choisir le mot-clé.
  # Il vous permettra de définir à quoi correspond le service.
  # Nous utilisons le mot-clé 'server' pour le serveur.
  server:
    # Le mot-clé "build" vous permettra de définir
    # le chemin vers le Dockerfile à utiliser pour créer l'image
    # qui vous permettra d'exécuter le service.
    # Ici, 'server/' correspond au chemin vers le dossier serveur
    # qui contient le Dockerfile à utiliser.
    build: server/

    # La commande à exécuter une fois l'image créée.
    # La commande suivante exécutera "python ./server.py".
    command: python ./server.py

    # Souvenez-vous que nous avons défini dans 'server/server.py' le port 1234.
    # Si nous voulons accéder au serveur depuis notre ordinateur (en dehors du conteneur),
    # nous devons partager le port de contenu avec le port de notre ordinateur.
    # Pour cela, le mot-clé 'ports' nous aidera.
    # Sa syntaxe est la suivante : [port que nous voulons sur notre machine]:[port que nous voulons récupérer dans le conteneur]
    # Dans notre cas, nous voulons utiliser le port 1234 sur notre machine et
    # récupérer le port 1234 du conteneur (car c'est sur ce port que
    # nous diffusons le serveur).
    ports:
      - 1234:1234

  # Deuxième service (conteneur) : le client.
  # Nous utilisons le mot-clé 'client' pour le serveur.
  client:
    # Ici, 'client/' correspond au chemin vers le dossier client
    # qui contient le Dockerfile à utiliser.
    build: client/

    # La commande à exécuter une fois l'image créée.
    # La commande suivante exécutera "python ./client.py".
    command: python ./client.py

    # Le mot-clé 'network_mode' est utilisé pour définir le type de réseau.
    # Ici, nous définissons que le conteneur peut accéder au 'localhost' de l'ordinateur.
    network_mode: host

    # Le mot-clé 'depends_on' permet de définir si le service
    # doit attendre que d'autres services soient prêts avant de se lancer.
    # Ici, nous voulons que le service 'client' attende que le service 'server' soit prêt.
    depends_on:
      - server
```

#### **5. Construisez Docker-Compose**

Une fois le docker-compose configuré, votre application client/serveur doit être construite. Cette étape correspond à la commande 'docker build' mais appliquée aux différents services.

```
$ docker-compose build
```

#### 6. Lancez Docker-Compose

Votre docker-compose est construit ! Maintenant, il est temps de démarrer ! Cette étape correspond à la commande 'docker run' mais appliquée aux différents services.

```
$ docker-compose up
```

Voilà, c'est tout. Vous devriez normalement voir « Docker-Compose est magique ! » s'afficher dans votre terminal.

> Note : Comme indiqué dans le tutoriel, votre service 'server' utilise le port 1234 de votre ordinateur pour distribuer son contenu. Si vous ouvrez la page '[http://localhost:1234/](http://localhost:1234/)' sur votre ordinateur, vous devriez voir 'Docker-Compose est magique !'.

### Le code est disponible



Si vous souhaitez récupérer le code complet pour le découvrir plus simplement ou pour l'exécuter, je l'ai mis à votre disposition sur mon GitHub.

**->** [GitHub : Exemple Client Serveur Docker-Compose](https://github.com/gael-thomas/Client-Server-Docker-Compose-example)

### Commandes utiles pour Docker

Comme d'habitude, j'ai préparé une liste de commandes qui peuvent vous être utiles avec docker-compose.

* Arrête les conteneurs et supprime les conteneurs, images... créés par 'docker-compose up'.

```
$ docker-compose down
```

* Affiche la sortie des logs des services (exemple : 'docker-compose logs -f client').

```
$ docker-compose logs -f [nom du service]
```

* Liste les conteneurs.

```
$ docker-compose ps
```

* Exécute une commande dans un conteneur en cours d'exécution (exemple : 'docker-compose exec server ls').

```
$ docker-compose exec [nom du service] [commande]
```

* Liste les images.

```
$ docker-compose images
```

## Conclusion

Vous pouvez vous référer à cet article chaque fois que vous avez besoin d'un exemple simple et concret sur la façon de créer un client/serveur avec docker-compose. Si vous avez des questions ou des commentaires, n'hésitez pas à demander.

Si vous souhaitez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/), où je tweete sur le développement web, l'amélioration personnelle et mon parcours en tant que développeur full stack !

Vous pouvez trouver d'autres articles comme celui-ci sur mon site web : [herewecode.io](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa/herewecode.io).