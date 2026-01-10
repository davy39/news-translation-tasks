---
title: Comment configurer le déploiement continu dans votre projet personnel facilement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T22:49:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-continuous-deployment-in-your-home-project-the-easy-way-41b84a467eed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pnP8tnza1D2UAqBJXsnpug.jpeg
tags:
- name: continuous deployment
  slug: continuous-deployment
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment configurer le déploiement continu dans votre projet personnel facilement
seo_desc: 'By Julius

  Continuous Deployment is a beautiful thing. Committing your project and seeing it
  being built and deployed without having to do anything is mesmerizing.

  And in this article, I want to show you how to get it done in your home project
  with ea...'
---

Par Julius

Le déploiement continu est une chose magnifique. Commiter votre projet et le voir se construire et se déployer sans avoir à faire quoi que ce soit est fascinant.

Et dans cet article, je veux vous montrer comment le faire dans votre projet personnel avec facilité.

Pour clarifier, voici un organigramme montrant les différences entre la livraison continue et le déploiement continu.

![Image](https://cdn-media-1.freecodecamp.org/images/xEnnOKXV4Pipmzu6EXGwIrNllSB6L9Nk98xi)
_Livraison continue vs. Déploiement continu_

Puisque la plupart du temps, personne d'autre que vous ne dépend de votre projet personnel, nous allons opter pour un workflow avec déploiement continu afin que vous puissiez voir vos changements déployés immédiatement. Si ce n'est pas le cas, vous pouvez changer le workflow plus tard.

Vous allez apprendre les points suivants :

* Comment créer un Dockerfile
* Comment pousser votre projet sur GitHub
* Construire automatiquement l'image docker sur Docker Hub
* Télécharger et exécuter automatiquement l'image avec [Watchtower](https://github.com/v2tec/watchtower)

Prérequis :

* Quelques connaissances sur Docker et le Dockerfile, bien que j'en expliquerai une partie en cours de route
* Avoir [git](https://git-scm.com/) installé
* Un compte [Docker Hub](https://hub.docker.com/)
* Un serveur (Linux) (physique ou virtuel) exécutant Docker

Pour référence, [ceci](https://github.com/juligreen/easy_CD_tutorial) est le dépôt GitHub exemple, et [ceci](https://hub.docker.com/r/juligreen/easy_cd_tutorial) est le dépôt Docker Hub exemple que je vais utiliser.

Ainsi, ce tutoriel ne sera utile que si vous prévoyez d'exécuter votre logiciel avec Docker (ce que je recommande car Docker est fantastique).

#### Pourquoi utiliser Docker ?

Docker vous permet d'avoir le même environnement pour le développement et la production, ce qui élimine les [Heisenbugs](https://en.wikipedia.org/wiki/Heisenbug) et le problème "ça marche sur ma machine". De plus, les conteneurs sont isolés, ce qui nous offre des avantages en termes de sécurité.  
Il y a plus à dire, mais ces deux avantages me font toujours livrer mon logiciel dans des conteneurs Docker.

#### Configuration de votre Dockerfile

Tout d'abord, nous allons créer un Dockerfile pour le projet. Ce fichier spécial s'appelle toujours "Dockerfile" sans extension et se trouve dans le répertoire racine de votre projet.

Un Dockerfile commence par l'instruction `FROM` qui indique à Docker quelle image de base vous souhaitez utiliser. Vous pouvez imaginer cela comme utiliser une toile avec l'arrière-plan déjà dessiné et seule la partie centrale (votre programme) manquante.  
La plupart du temps, l'image que vous souhaitez tirer est l'image de base de votre langage de programmation, que vous pouvez trouver sur le [Docker Hub](https://hub.docker.com/) mentionné précédemment.

Ensuite, nous copions nos fichiers de projet dans le conteneur docker avec la commande `COPY..`. Que fait cela ?

Il prend les fichiers du premier répertoire (le point fait référence au répertoire actuel du fichier, qui inclut tous vos fichiers de projet) et les place dans le répertoire actuel de votre conteneur Docker (rappelez-vous que votre conteneur Docker est son propre système d'exploitation). Vos fichiers sont maintenant à la racine, ce que vous pouvez vouloir changer.

Ensuite, nous devons installer les dépendances, pour lesquelles j'utiliserai `python pip`, mais tout système de gestion de paquets équivalent en fonction de votre langage de choix fera l'affaire. La chose cruciale à apprendre ici est comment exécuter des commandes dans le conteneur avec RUN.

```
From python:3.7COPY . .RUN pip install -r requirements.txt
```

Facile, n'est-ce pas ? Maintenant, nous devons démarrer notre programme dans le conteneur.

```
CMD ["python", "./my_script.py"]
```

L'instruction CMD est unique. Chaque Dockerfile doit l'avoir comme dernière ligne car elle démarre le processus principal dans le conteneur.

Vous avez terminé votre Dockerfile ! Vous pouvez maintenant construire manuellement votre image et votre conteneur, mais nous allons sauter cette étape pour l'instant.

Maintenant, nous allons créer notre dépôt sur GitHub, mais n'oubliez pas de laisser "Initialize this repository with a README" décoché.

![Image](https://cdn-media-1.freecodecamp.org/images/p2vOXrhxde9j6cgaJr9xVaUzmeUPFRy2gn4v)

Ensuite, vous devez copier l'URL distante.

![Image](https://cdn-media-1.freecodecamp.org/images/-eXorLpmcko2fgM90tBcb9tMftguLhpf1UbV)

Ouvrez un cmd/shell dans le répertoire racine de votre projet.

Vous devez initialiser votre dépôt git, ajouter vos fichiers, configurer le distant, commiter les fichiers et pousser votre projet sur GitHub.

```
git initgit add *git remote add origin https://github.com/<user>/<repository>.gitgit commit -a -m "Préparer Dockerfile pour CD"git push -u origin master
```

Maintenant, votre dépôt GitHub devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/k8CCf3yng-7yKMFCUyKwxs1NVJGmQQ8xPuyB)

Félicitations, vous êtes à moitié terminé !

L'étape suivante consiste à connecter GitHub à Docker Hub. Pour cela, vous allez dans les paramètres du compte.

![Image](https://cdn-media-1.freecodecamp.org/images/7kSYmYk8hcF0-lzHuP1bYGf2U-Q6QTWVKtM8)

Faites défiler vers le bas et connectez votre hôte git.

![Image](https://cdn-media-1.freecodecamp.org/images/SBZCVplxQiaLApLklpqfCruODRyHLpWC1pXa)

Créez votre dépôt sur Docker Hub maintenant.

![Image](https://cdn-media-1.freecodecamp.org/images/FRgXa6dDUumrTAOHHiwjF1VrvOsHP8EPe5r3)

Donnez un nom au dépôt et cliquez sur l'icône GitHub (ou Bitbucket, si c'est votre choix). Choisissez maintenant votre organisation (généralement votre nom d'utilisateur) et le nom de votre projet. Si vous souhaitez utiliser votre image master pour la construction et toujours pousser vers latest, vous pouvez maintenant cliquer sur "Create & Build" et regarder votre image être construite pour vous. Sinon, vous devez modifier les paramètres de construction.

![Image](https://cdn-media-1.freecodecamp.org/images/ZG12hUUr3GBIgVV7RjsivzjbTd4Pm2ycpcy9)

Dernières étapes ! Maintenant, vous avez besoin de [Watchtower](https://github.com/v2tec/watchtower) sur votre machine cible.  
Watchtower est un programme qui tire vos images docker en cours d'exécution et vérifie les mises à jour. S'il y a des mises à jour, il arrête gracieusement le conteneur original et crée un conteneur à partir de la nouvelle image avec les mêmes paramètres.

Le meilleur, c'est que nous pouvons aussi installer Watchtower avec Docker !

Entrez ce qui suit dans votre terminal :

```
docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock v2tec/watchtower
```

Ensuite, vous devez exécuter le conteneur Docker pour votre projet !

```
docker run -d --name <mon-projet> <username>/<mon-projet>
```

L'option "-d" fait fonctionner votre programme en arrière-plan, donc le programme ne s'arrête pas si vous fermez le terminal.

Donc, pour résumer, si vous poussez un commit vers votre dépôt GitHub, Docker Hub construira automatiquement une image Docker pour vous. Cette image est ensuite tirée par WatchTower et exécutée avec toutes les options originales.

Si vous avez besoin d'aide à un moment donné, n'hésitez pas à demander, je suis heureux de vous aider.  
Si c'est un problème technique, une issue sur le [projet GitHub](https://github.com/juligreen/easy_CD_tutorial/issues) serait génial !

#### Mais qu'en est-il des tests ?

Bonne question !  
Vous pouvez utiliser Travis CI pour exécuter vos tests en même temps.  
Vous pouvez lire à ce sujet [ici](https://docs.travis-ci.com/user/tutorial/), mais l'essentiel est que vous ajoutez un autre fichier à votre dépôt qui contient des instructions pour un serveur externe afin d'exécuter des tests unitaires ou toute autre instruction.

> Mais que se passe-t-il si je ne veux que mon image docker soit construite si les tests passent ?

Cela rompt un peu notre workflow.  
Nous ne pouvons plus compter sur Docker Hub pour construire nos images. Au lieu de cela, ce sera aussi Travis CI qui produira l'image et la poussera ensuite vers votre dépôt Docker Hub. Lisez à ce sujet [ici](https://docs.travis-ci.com/user/docker/).