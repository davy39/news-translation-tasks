---
title: Guide du débutant sur Docker — comment créer votre première application Docker
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2019-04-02T17:17:11.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5ErAAkV5REH3bE6-xAzzFg.png
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
seo_title: Guide du débutant sur Docker — comment créer votre première application
  Docker
seo_desc: 'You are a developer and you want to start with Docker? This article is
  made for you.

  After a short introduction on what Docker is and why to use it, you will be able
  to create your first application with Docker.

  What is Docker?

  Docker is a free softw...'
---

#### Vous êtes développeur et vous souhaitez commencer avec Docker ? Cet article est fait pour vous.

Après une courte introduction sur ce qu'est Docker et pourquoi l'utiliser, vous serez en mesure de créer votre première application avec Docker.

#### **Qu'est-ce que Docker ?**

[Docker](https://www.docker.com/) est un logiciel libre développé par Docker Inc. Il a été présenté au grand public le 13 mars 2013 et est devenu depuis ce jour un incontournable dans le monde du développement informatique.

Il permet aux utilisateurs de créer des environnements indépendants et isolés pour lancer et déployer leurs applications. Ces environnements sont alors appelés conteneurs.

Cela permettra au développeur d'exécuter un conteneur sur n'importe quelle machine.

Comme vous pouvez le voir, avec Docker, il n'y a plus de problèmes de dépendances ou de compilation. Il vous suffit de lancer votre conteneur et votre application se lancera immédiatement.

#### **Mais, Docker est-il une machine virtuelle ?**

Voici l'une des questions les plus posées sur Docker. La réponse est : en réalité, pas tout à fait.

Cela peut ressembler à une machine virtuelle au premier abord, mais la fonctionnalité n'est pas la même.

Contrairement à Docker, une machine virtuelle inclura un système d'exploitation complet. Elle fonctionnera de manière indépendante et agira comme un ordinateur.

Docker ne partagera que les ressources de la machine hôte afin d'exécuter ses environnements.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Blog.-Are-containers-..VM-Image-1-1024x435.png)
_Docker VS Machines virtuelles (Copyright à [Docker blog](https://blog.docker.com/2018/08/containers-replacing-virtual-machines/" rel="noopener))_

#### **Pourquoi utiliser Docker en tant que développeur ?**

Cet outil peut vraiment changer le quotidien d'un développeur. Afin de répondre au mieux à cette question, j'ai écrit une liste non exhaustive des avantages que vous trouverez :

* Docker est rapide. Contrairement à une machine virtuelle, votre application peut démarrer en quelques secondes et s'arrêter tout aussi rapidement.
* Docker est multiplateforme. Vous pouvez lancer votre conteneur sur n'importe quel système.
* Les conteneurs peuvent être construits et détruits plus rapidement qu'une machine virtuelle.
* Plus de difficultés à configurer votre environnement de travail. Une fois votre Docker configuré, vous n'aurez plus jamais à réinstaller vos dépendances manuellement. Si vous changez d'ordinateur ou si un employé rejoint votre entreprise, vous n'aurez qu'à lui donner votre configuration.
* Vous gardez votre espace de travail propre, car chacun de vos environnements sera isolé et vous pourrez les supprimer à tout moment sans impacter le reste.
* Il sera plus facile de déployer votre projet sur votre serveur afin de le mettre en ligne.

### Maintenant, créons votre première application

Maintenant que vous savez ce qu'est Docker, il est temps de créer votre première application !

Le but de ce court tutoriel est de créer un programme Python qui affiche une phrase. Ce programme devra être lancé via un Dockerfile.

Vous verrez, ce n'est pas très compliqué une fois que vous avez compris le processus.

> Note : Vous n'aurez pas besoin d'installer Python sur votre ordinateur. Ce sera à l'environnement Docker de contenir Python afin d'exécuter votre code.

#### 1. Installer Docker sur votre machine

_Pour Ubuntu :_

Tout d'abord, mettez à jour vos paquets :

```
$ sudo apt update
```

Ensuite, installez Docker avec apt-get :

```
$ sudo apt install docker.io
```

Enfin, vérifiez que Docker est installé correctement :

```
$ sudo docker run hello-world
```

* _Pour MacOSX :_ vous pouvez suivre [ce lien](https://docs.docker.com/docker-for-mac/install/).
* _Pour Windows :_ vous pouvez suivre [ce lien](https://docs.docker.com/docker-for-windows/install/).

#### 2. Créer votre projet

Afin de créer votre première application Docker, je vous invite à créer un dossier sur votre ordinateur. Il doit contenir les deux fichiers suivants :

* Un fichier _main.py_ (fichier Python qui contiendra le code à exécuter).
* Un fichier _Dockerfile_ (fichier Docker qui contiendra les instructions nécessaires pour créer l'environnement).

Normalement, vous devriez avoir cette architecture de dossier :

```
.
├── Dockerfile
└── main.py
0 directories, 2 files
```

#### 3. Modifier le fichier Python

Vous pouvez ajouter le code suivant au fichier _main.py_ :

```python
#!/usr/bin/env python3

print("Docker est magique !")
```

Rien d'exceptionnel, mais une fois que vous verrez _Docker est magique !_ s'afficher dans votre terminal, vous saurez que votre Docker fonctionne.

#### 4. Modifier le fichier Docker

Un peu de théorie : la première chose à faire lorsque vous souhaitez créer votre Dockerfile est de vous demander ce que vous voulez faire. Notre objectif ici est de lancer du code Python.

Pour ce faire, notre Docker doit contenir toutes les dépendances nécessaires pour lancer Python. Un Linux (Ubuntu) avec Python installé dessus devrait suffire.

La première étape à suivre lorsque vous créez un fichier Docker est d'accéder au site [DockerHub](https://hub.docker.com/). Ce site contient de nombreuses images préconçues pour vous faire gagner du temps (par exemple : toutes les images pour Linux ou les langages de code).

Dans notre cas, nous taperons Python dans la barre de recherche. Le premier résultat est [l'image officielle](https://hub.docker.com/_/python) créée pour exécuter Python. Parfait, nous allons l'utiliser !

```python
# Un dockerfile doit toujours commencer par importer l'image de base.
# Nous utilisons le mot-clé 'FROM' pour cela.
# Dans notre exemple, nous voulons importer l'image python.
# Nous écrivons donc 'python' pour le nom de l'image et 'latest' pour la version.
FROM python:latest

# Afin de lancer notre code python, nous devons l'importer dans notre image.
# Nous utilisons le mot-clé 'COPY' pour cela.
# Le premier paramètre 'main.py' est le nom du fichier sur l'hôte.
# Le deuxième paramètre '/' est le chemin où mettre le fichier sur l'image.
# Ici, nous mettons le fichier à la racine de l'image.
COPY main.py /

# Nous devons définir la commande à lancer lorsque nous allons exécuter l'image.
# Nous utilisons le mot-clé 'CMD' pour cela.
# La commande suivante exécutera "python ./main.py".
CMD [ "python", "./main.py" ]
```

#### 5. Créer l'image Docker

Une fois votre code prêt et le Dockerfile écrit, il ne vous reste plus qu'à créer votre image pour contenir votre application.

```
$ docker build -t python-test . 
```

L'option _-t_ vous permet de définir le nom de votre image. Dans notre cas, nous avons choisi _python-test_, mais vous pouvez mettre ce que vous voulez.

#### 6. Exécuter l'image Docker

Une fois l'image créée, votre code est prêt à être lancé.

```
$ docker run python-test
```

Vous devez mettre le nom de votre image après _docker run_.

Voilà, c'est tout. Vous devriez normalement voir Docker est magique ! s'afficher dans votre terminal.

### Le code est disponible

Si vous souhaitez récupérer le code complet pour le découvrir facilement ou pour l'exécuter, je l'ai mis à votre disposition sur mon GitHub.

**->** [GitHub : Exemple de première application Docker](https://github.com/gael-thomas/Docker-First-Application-example)

### Commandes utiles pour Docker

Avant de vous laisser, j'ai préparé une liste de commandes qui pourraient vous être utiles sur Docker.

* Lister vos images.

```
$ docker image ls
```

* Supprimer une image spécifique.

```
$ docker image rm [nom de l'image]
```

* Supprimer toutes les images existantes.

```
$ docker image rm $(docker images -a -q)
```

* Lister tous les conteneurs existants (en cours d'exécution et non en cours d'exécution).

```
$ docker ps -a
```

* Arrêter un conteneur spécifique.

```
$ docker stop [nom du conteneur]
```

* Arrêter tous les conteneurs en cours d'exécution.

```
$ docker stop $(docker ps -a -q)
```

* Supprimer un conteneur spécifique (uniquement s'il est arrêté).

```
$ docker rm [nom du conteneur]
```

* Supprimer tous les conteneurs (uniquement s'ils sont arrêtés).

```
$ docker rm $(docker ps -a -q)
```

* Afficher les logs d'un conteneur.

```
$ docker logs [nom du conteneur]
```

#### Qu'est-ce qui suit ?

Après tous vos retours, j'ai décidé d'écrire la suite de ce guide pour débutants. Dans cet article, vous découvrirez comment utiliser docker-compose pour créer votre première application client/serveur avec Docker.

-> [Guide du débutant sur Docker — comment créer une application client/serveur avec docker-compose](https://herewecode.io/blog/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose/)

## Conclusion

Vous pouvez vous référer à cet article chaque fois que vous avez besoin d'un exemple simple et concret sur la façon de créer votre première application Docker. Si vous avez des questions ou des commentaires, n'hésitez pas à demander.

Si vous souhaitez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/), où je tweete sur le développement web, l'amélioration personnelle et mon parcours en tant que développeur full stack !

Vous pouvez trouver d'autres articles comme celui-ci sur mon site web : [herewecode.io](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/herewecode.io).