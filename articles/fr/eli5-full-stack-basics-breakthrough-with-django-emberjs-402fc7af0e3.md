---
title: 'ELI5 Full Stack Basics : percée avec Django & EmberJS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T23:04:23.000Z'
originalURL: https://freecodecamp.org/news/eli5-full-stack-basics-breakthrough-with-django-emberjs-402fc7af0e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-YXdpMxaFFkY2QKdxgIsFQ.png
tags:
- name: Django
  slug: django
- name: ember
  slug: ember
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'ELI5 Full Stack Basics : percée avec Django & EmberJS'
seo_desc: 'By Michael Xavier

  Welcome to ELI5 Full Stack: Breakthrough with Django & EmberJS. This is an introduction
  to full stack development for everyone, especially beginners. We’ll go step-by-step
  through the development of a basic web application. A librar...'
---

Par Michael Xavier

Bienvenue dans **_ELI5 Full Stack : Percée avec Django & EmberJS_**. Il s'agit d'une introduction au développement full stack pour tous, en particulier pour les **débutants**. Nous allons passer étape par étape par le développement d'une application web basique. Une sorte de bibliothèque. Ensemble, nous allons construire un back-end pour stocker des données et une API RESTful pour les gérer. Ensuite, nous allons construire une interface utilisateur front-end pour que les utilisateurs puissent visualiser, ajouter, modifier et supprimer les données.

Ceci n'est pas censé être une plongée profonde dans **Django** ou **EmberJS**. Je ne veux pas que nous soyons submergés par trop de complexité. **Plutôt, son but est de montrer les éléments critiques du développement full stack de base**. Comment assembler le back-end et le front-end en une application fonctionnelle. Je vais entrer dans les détails sur les logiciels, les frameworks et les outils utilisés dans le processus. Chaque commande de terminal exécutée et chaque ligne de code dans l'application finale est présente dans ce tutoriel.

J'ai gardé chaque section courte et directe afin que personne n'ait l'impression que sa tête explose. Il y a aussi des indicateurs pour marquer les points de réflexion afin que vous puissiez revenir en arrière et regarder ce que nous avons fait et sauvegarder l'état. Si vous ne savez pas ce que signifie quelque chose, cliquez sur les articles liés qui expliqueront en détail. N'oubliez pas, ceci est une introduction pour tout le monde, y compris les **débutants**. Si vous n'avez pas besoin d'être guidé, passez aux sections pertinentes pour vous.

Si vous êtes un débutant, je suggère que vous écriviez chaque ligne de code et exécutiez chaque commande de terminal vous-même. Ne copiez pas et ne collez pas. Cela ne s'imprégnera pas. Prenez votre temps et réfléchissez à ce que vous faites. C'est une caractéristique critique d'un programmeur efficace et autonome. Vous allez développer cela avec le temps si vous écrivez votre propre code et réfléchissez à ce que vous écrivez. Si vous faites une erreur (regardez mon historique de commits, j'en ai définitivement fait), ne vous en faites pas. Revenez en arrière. Ce n'est pas une course. Vous allez bien si vous prenez votre temps.

![Image](https://cdn-media-1.freecodecamp.org/images/A4ayt-UmztcellrLe6SvphBGHrsHz1u1IXMk)
_Parfois, j'ai un coup de fouet_

**Note** : J'ai développé ce tutoriel sur un MacBook Pro exécutant [macOS High Sierra (10.3.6)](https://www.macrumors.com/roundup/macos-10-13/). J'utilise [iTerm2](https://www.iterm2.com/) pour le terminal et [Sublime Text 3](https://www.sublimetext.com/3) comme éditeur de texte. Tous les tests utilisent le navigateur [Chrome](https://www.google.com/chrome/) et ses outils intégrés. Le code réel ne devrait pas avoir de différences. Vous pouvez [**télécharger les fichiers du projet final depuis le dépôt Github**](https://github.com/lookininward/my_library).

### Table des matières

#### **Section 1 : Les Quoi, Comment et Pourquoi**

1.1 Pourquoi j'ai écrit ce tutoriel  
1.2 Back End, Front End. Quelle est la différence ?  
1.3 Le Concept : Une Application de Bibliothèque Basique  
1.4 Structure du Répertoire du Projet  
1.5 Configuration du Répertoire du Projet  
1.6 Conclusion

#### Section 2 : Plongeons dans le Back End

2.1 Installer le Logiciel Requis  
2.2 Démarrer un Projet Django : server  
2.3 Démarrer une Application Django : books  
2.4 Décrire le modèle Book  
2.5 Enregistrer le modèle Book avec l'admin  
2.6 Conclusion

#### Section 3 : Construire un Serveur, puis REST

3.1 Django REST Framework  
3.2 Créer le dossier api books  
3.3 Créer un sérialiseur de livre  
3.4 Créer une vue pour obtenir et poster les données des livres  
3.5 Créer des URLs pour accéder aux données des livres  
3.6 Conclusion

#### Section 4 : Poser les Fondations du Front-end

4.1 Installer le Logiciel Requis  
4.2 Démarrer un Projet Ember : client  
4.3 Affichage des données des livres   
4.4 La route des livres  
4.5 Affichage des données réelles dans la route des livres  
4.6 Conclusion

#### **Section 5 : Formats de données corrects, gestion des enregistrements individuels**

5.1 Installer le Django REST Framework JSON API  
5.2 Travailler avec des enregistrements de livres individuels  
5.3 La route du livre  
5.4 Conclusion

#### Section 6 : Front-end Fonctionnel

6.1 Ajouter un nouveau livre à la base de données  
 6.2 Supprimer un livre de la base de données  
6.3 Modifier un livre dans la base de données  
6.4 Conclusion

#### Section 7 : Passer à autre chose

7.1 Qu'est-ce qui suit ?  
7.2 Lectures Complémentaires

### Section 1 : Les Quoi, Comment et Pourquoi

### 1.1 Pourquoi j'ai écrit ce tutoriel

Imaginez que vous venez de rejoindre une nouvelle entreprise. Ils sont en activité depuis un certain temps, et leurs principaux produits sont déjà en production. Imaginez l'application que vous voyez aujourd'hui comme un gâteau. Le processus de choix des ingrédients, de la recette et de l'assemblage de tout cela... eh bien, c'est terminé depuis longtemps. Vous allez travailler sur des morceaux de ce gâteau fini.

Les développeurs au début d'un projet ont établi certaines configurations. Celles-ci changent et les conventions se développent également avec le temps à mesure que les développeurs viennent et partent. Au moment où vous arrivez, il peut être difficile de comprendre comment nous en sommes arrivés là. C'était ma situation. J'ai senti que plonger dans toute la pile serait le seul moyen pour moi de me sentir à l'aise. Cela m'aiderait à comprendre d'où nous venons et comment avancer avec le logiciel que nous construisons.

Ce tutoriel est le résultat de mes expériences en tant que développeur logiciel junior. J'ai beaucoup appris pendant mon temps avec [Closing Folders](http://we%27re%20hiring%20now%20so%20feel%20free%20to%20get%20in%20touch%21/). Il représente un changement dans ma façon de penser alors que je fais des pas vers un développement full stack plus complexe. Il sert également de point d'entrée pour les développeurs au stade où ils se demandent comment le gâteau est cuit. J'espère que ce tutoriel sera aussi utile pour vous qu'il a été instructif pour moi de le créer.

![Image](https://cdn-media-1.freecodecamp.org/images/ReFm2Fb6XzpWqD5x8fDDWipgkDicy7WfarFg)
_Cette sensation de bien-être_

**Note** : Dans un flux de travail typique, un développeur commencerait par le back-end pour configurer la base de données et créer une API REST. Ensuite, il travaillerait sur le front-end et construirait l'interface utilisateur. Les choses ne sont pas si simples, cependant. Nous faisons des erreurs et devons souvent revenir en arrière pour les résoudre. Le fait de sauter d'avant en arrière aidera à établir plus de connexions dans votre esprit et vous aidera à mieux comprendre comment toutes les pièces s'emboîtent. Acceptez vos erreurs. Vous allez en faire beaucoup !

**Note2** : Attention Senior Devs, Junior Devs et Designers ! [Closing Folders](http://We're hiring now so feel free to get in touch!) recrute maintenant, alors n'hésitez pas à nous contacter.

### 1.2 Back End, Front End. Quelle est la différence ?

Développement back-end. Développement front-end. Développement full-stack. Tant de développement... Quelle est la différence, de toute façon ?

Pensez au développement front-end comme à la partie de l'application que vous voyez et avec laquelle vous interagissez. Par exemple, l'interface utilisateur fait partie du front-end. C'est là que l'utilisateur visualise les données et interagit avec elles.

Le développement back-end est tout ce qui stocke et sert les données. Pensez à ce qui se passe lorsque vous vous connectez à Medium. Aucune de vos données de profil utilisateur ou de vos histoires n'existe sur le front-end. Elles sont stockées et servies depuis le back-end.

Le front-end et le back-end travaillent ensemble pour former l'application. Le back-end contient les instructions sur la façon de stocker et de servir les données. Le front-end contient les instructions pour capturer les données et comment les afficher.

![Image](https://cdn-media-1.freecodecamp.org/images/qD5LLIeEVVXSlKjIuqV2OJspW-Sxlu-YSNX4)
_Communication basique entre le front-end et le back-end._

Découvrez-en plus sur les différences dans [cet article](http://blog.teamtreehouse.com/i-dont-speak-your-language-frontend-vs-backend).

![Image](https://cdn-media-1.freecodecamp.org/images/kysaEsRUJ593f1PnOYBlVm1W2UOjl9UX4CnJ)
_MFW J'ai réalisé que le développement ne se termine jamais réellement_

### 1.3 Le Concept : Une Application de Bibliothèque Basique

Avant de commencer à construire quoi que ce soit, définissons nos plans et ce que nous essayons d'accomplir. Nous voulons construire une [application web](https://stackoverflow.com/a/8694944/5513243) appelée **my_library** qui s'exécute dans le navigateur. L'application est exactement ce à quoi elle ressemble, une bibliothèque numérique de livres. Nous ne traiterons pas avec le contenu réel des livres, cependant. Les livres n'auront que des informations sur le titre, l'auteur et la description. Gardons cela simple.

L'application aura les fonctionnalités suivantes :

* Voir tous les livres sous forme de liste unique sur la page d'accueil, ordonnés par titre
* Voir chaque livre en détail, affichant son titre, son auteur et sa description
* Ajouter un nouveau livre avec les champs titre, auteur et description
* Modifier les champs titre, auteur et description d'un livre existant
* Supprimer un livre existant

#### 1.3.1 Design final et fonctionnalités de my_library

Jetez un œil aux captures d'écran ci-dessous. Elles représentent l'apparence finale et les fonctionnalités de l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/OfA6C6cfPUhNSjp6GhZy3N2gXD6UyRhOm5GZ)
_Voir tous les livres dans notre base de données sous forme de liste unique ordonnée par titre._

![Image](https://cdn-media-1.freecodecamp.org/images/E0AxS4kV57E1jZegwU599JK3Mre18RUt2C0Z)
_Cliquez sur un livre pour voir une vue détaillée avec les informations sur l'auteur et la description._

![Image](https://cdn-media-1.freecodecamp.org/images/ris6Kqmw0lMqDzocS3T72WpXJpBxovfoV0Jy)
_Ajoutez un nouveau livre à la base de données avec les champs titre, auteur et description._

![Image](https://cdn-media-1.freecodecamp.org/images/8Vx8NrPBH7ae-u0LG8tzT8QZGSHmmaU8MN0R)
_Modifiez les champs titre, auteur et description d'un livre existant._

![Image](https://cdn-media-1.freecodecamp.org/images/XOuou7IuqqxrlNSU5DdADIxx-gISjjnyn42l)
_Confirmez la suppression d'un livre existant._

### 1.4 Structure du Répertoire du Projet

Il existe d'innombrables façons de structurer un projet donné. Je vais tout garder sous un dossier `my_library` pour des raisons de simplicité comme suit :

```
my_library
  - server
    - server
    - books
      - api
    - db.sqlite3
    - manage.py
  - client
    - app
      - adapters
      - controllers
      - models
      - routes
      - templates
      - styles
      router.js
```

Ce ne sont pas tous les dossiers et fichiers que le projet contiendra, bien qu'ils soient les principaux. Vous remarquerez quelques fichiers autogénérés que vous pouvez ignorer. Bien qu'il serait utile pour vous de lire la documentation qui explique leur but.

Le répertoire `my_library` contient des dossiers pour les sous-projets back-end et front-end. `server` fait référence au back-end Django, et `client` fait référence au front-end EmberJS.

#### 1.4.1 Back End

* `server` contient un autre dossier appelé `server`. À l'intérieur se trouvent les configurations et paramètres de haut niveau pour le back-end.
* Le dossier `books` contiendra tous les modèles, vues et autres configurations pour les données des livres.
* À l'intérieur du dossier `books/api`, nous créerons les sérialiseurs, URLs et vues qui composent notre API REST.

#### 1.4.2 Front End

* `client` est notre front-end EmberJS. Il contient des routes, templates, modèles, contrôleurs, adaptateurs et styles. `router.js` décrit toutes les routes de l'application.

Allons-y et configurons le répertoire principal du projet `my_library`.

### 1.5 Configuration du Répertoire du Projet

#### 1.5.1 Créer le dossier principal du projet : my_library

Maintenant que nous savons ce que nous allons construire, prenons quelques minutes pour configurer le répertoire principal du projet `my_library` :

```
# cd dans le bureau et créer le dossier principal du projet
  cd ~/desktop && mkdir my_library
```

Créez un fichier `README.md` basique à l'intérieur du dossier avec le contenu suivant :

```
# my_library
Ceci est une application de bibliothèque full stack basique construite. Consultez le tutoriel : 'ELI5 Full Stack : Percée avec Django & EmberJS'.
```

Maintenant, engageons ce projet dans un nouveau dépôt Git comme point de départ du projet.

#### 1.5.2 Installer Git pour le contrôle de version

Git est un logiciel de contrôle de version. Nous l'utiliserons pour suivre notre projet et sauvegarder notre état étape par étape afin de pouvoir toujours revenir en arrière si nous faisons des erreurs critiques. Je suis sûr que la plupart d'entre vous sont déjà familiers avec lui.

Pour les non-initiés, vous pouvez en savoir plus [ici](https://git-scm.com/about). Si vous n'avez pas Git installé, vous pouvez le télécharger [ici](https://git-scm.com/download/mac).

Vérifiez qu'il est installé avec :

```
$ git --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/KApRH2jTbtKv40ejPFGjr54s8hGPoH9YefFD)

#### 1.5.3 Créer un nouveau dépôt de projet

J'ai un compte avec [Github](https://github.com/). C'est populaire et ça fonctionne bien, donc c'est ce que j'utiliserai. N'hésitez pas à utiliser d'autres solutions si elles vous conviennent mieux.

Créez un nouveau dépôt et obtenez l'URL distante qui devrait ressembler à ceci :

```
git@github.com:username/repo_name.git
```

![Image](https://cdn-media-1.freecodecamp.org/images/qbjGYbQ9czlLwNvoMw5JwaOmU9jRFD3dDyn7)

#### 1.5.4 Valider et pousser vos modifications vers le dépôt du projet

À l'intérieur du dossier `my_library`, initialisez le dépôt vide :

```
git init
```

Maintenant, [ajoutez l'URL distante](https://help.github.com/articles/adding-a-remote/) afin que Git sache où nous poussons nos fichiers :

```
git remote add origin git@github.com:username/repo_name.git
# vérifiez qu'il est défini, devrait afficher l'origine
  git remote -v
```

Il est temps de pousser notre code vers Github :

```
# vérifiez le statut de notre dépôt
# devrait montrer le nouveau fichier README.md, aucun commit précédent
  git status
# ajoutez toutes les modifications
  git add .
# créez un commit avec un message
  git commit -m "[BASE] Début du projet"
# poussez les modifications vers la branche master du dépôt
  git push origin master
```

Le dépôt Git distant se met à jour avec les modifications que nous avons poussées :

![Image](https://cdn-media-1.freecodecamp.org/images/jNsMz7ixvdfL8iXHX-g5D8Q7Ov0OptROPTVW)

Maintenant que nous avons un répertoire principal de projet et un dépôt, nous pouvons enfin commencer à travailler sur notre back-end !

**NOTE** : À partir de ce point, je n'entrerai plus dans les détails des commits. L'**indicateur de révision et de commit ci-dessous** vous indiquera quand il est bon de le faire :

![Image](https://cdn-media-1.freecodecamp.org/images/o4SwOn9IR02bwppfcmoKRBV2iujutkGXN8e4)

### 1.6 Conclusion

Nous sommes arrivés à la fin de la **Section 1** avec les étapes suivantes complétées :

* Nous avons une idée de ce que nous construisons et de son fonctionnement
* Créé le répertoire principal du projet `my_library`
* Installé `git` et créé un dépôt de projet distant sur Github
* Initialisé le dépôt local et défini l'URL distante
* Créé un fichier `README.md`, puis validé et poussé toutes les modifications

![Image](https://cdn-media-1.freecodecamp.org/images/oMqTTVH075JVrjgb8mj56cKWDPBEfogE5Pea)
_Le chiot est fier de vous_

### Section 2 : Plongeons dans le Back End

Cette section est entièrement consacrée au développement back-end avec Django. Nous commencerons par l'installation du logiciel requis.

Ensuite, nous passerons à la création d'un nouveau projet Django appelé `server` et créerons une nouvelle application appelée `books`. Dans l'application `books`, nous décrivons le modèle `Book` et enregistrons le modèle avec l'admin.

Une fois que nous avons créé un compte `Superuser`, nous pouvons nous connecter au site d'administration Django. Nous utiliserons le site d'administration Django pour administrer la base de données et commencer à la remplir avec des données de livres.

### 2.1 Installer le Logiciel Requis

Avant de commencer notre projet back-end, nous devons installer certains logiciels :

* [Python](https://www.python.org/doc/essays/blurb/)
* [pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py)
* [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Django](https://docs.djangoproject.com/en/1.11/topics/install/)

#### 2.1.1 Python

Si votre MacOS est à jour, il a probablement déjà `Python 2.7` installé. N'hésitez pas à utiliser soit `2.7` soit `3.x`. Ils sont les mêmes pour les besoins de ce tutoriel.

L'installation est simple. [Téléchargez l'installateur](https://www.python.org/downloads/) et installez-le comme vous le feriez pour une application MacOS typique. Ouvrez le terminal et vérifiez qu'il est installé :

```
python --version 
```

![Image](https://cdn-media-1.freecodecamp.org/images/KN6ZDc46wNzVcEH1yPRUr3ty4fL8wuh6loJV)

#### 2.1.2 pip

En termes simples, pip (Pip Installs Packages) est un système de gestion de paquets. Il est utilisé pour installer et gérer des paquets logiciels écrits en Python. Dans le terminal :

```
# cd dans le bureau
  cd ~/desktop
 
# téléchargez le script Python pip
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 
# exécutez le script
  python get-pip.py
# une fois l'installation terminée, vérifiez qu'il est installé
  pip --version
```

La documentation complète de l'installation est disponible [ici](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py).

#### 2.1.3 virtualenv

virtualenv est un _outil pour créer des environnements Python isolés_. Ces environnements ont leurs propres répertoires d'installation. Ils ne partagent pas de bibliothèques avec d'autres. De tels silos protègent les bibliothèques installées globalement contre les modifications non désirées.

Avec lui, nous pouvons jouer avec les bibliothèques Python sans perturber l'environnement global. Par exemple, vous installez `exampleSoftware 1.0` sur votre ordinateur. Avec un environnement virtuel activé, vous pouvez passer à `exampleSoftware 1.2` et l'utiliser. Cela n'affectera pas du tout l'installation globale de `exampleSoftware 1.0`.

Pour le développement d'une application particulière, vous pouvez vouloir utiliser `1.2` et pour d'autres contextes, `1.0` sera approprié. Les environnements virtuels nous donnent la capacité de séparer ces contextes. La documentation complète de l'installation est disponible [ici](https://virtualenv.pypa.io/en/stable/installation/).

Maintenant, ouvrez le terminal pour installer virtualenv :

```
# utilisez pip pour installer virtualenv
  pip install virtualenv
# vérifiez qu'il est installé
  virtualenv --version
```

Créons un répertoire pour héberger nos environnements virtuels :

```
# cd dans le répertoire racine
  cd ~/
# créez un dossier caché appelé .envs pour les environnements virtuels
  mkdir .envs
# cd dans le répertoire des environnements virtuels
  cd .envs
```

Nous pouvons maintenant créer un environnement virtuel pour notre projet :

```
# créez un dossier d'environnement virtuel : my_library
  virtualenv my_library
# activez l'environnement virtuel depuis n'importe où en utilisant
  source ~/.envs/my_library/bin/activate
```

Maintenant que nous avons créé un environnement virtuel appelé `my_library`, il y a quelques règles à garder à l'esprit. **Assurez-vous que l'environnement est toujours activé avant d'installer ou de mettre à jour des paquets.**

Enfin, prenez un moment pour mettre à niveau pip à l'intérieur de cet environnement virtuel :

```
pip install -U pip
```

#### 2.1.4 Django 1.11 (LTS)

Django est un framework web qui _encourage le développement rapide et une conception propre et pragmatique_

Il nous fournit un ensemble de composants communs afin que nous n'ayons pas à tout réinventer à partir de zéro.

Les exemples incluent :

* un panneau de gestion
* un moyen de gérer l'authentification des utilisateurs

Consultez [cet article de DjangoGirls](https://tutorial.djangogirls.org/en/django/) pour en savoir plus sur Django et pourquoi il est utilisé.

![Image](https://cdn-media-1.freecodecamp.org/images/xTQRhumtGS8zEEkoz6pjawMTmfHTJBYDzmJd)

Dans ce projet, nous allons utiliser Django pour gérer le back-end. Avec ses modules complémentaires, Django fournit les outils de base pour développer une API REST.

```
# à l'intérieur de my_library avec virtualenv activé
  pip install Django==1.11
# vérifiez qu'il est installé, ouvrez la console Python
  python
# accédez à la bibliothèque django et obtenez la version (devrait être 1.11)
  import django
  print(django.get_version())
# quittez en utilisant le raccourci clavier ctrl+D ou :
  exit()
```

La documentation complète de l'installation est disponible [ici](https://docs.djangoproject.com/en/1.11/topics/install/).

### 2.2 Démarrer un Projet Django : server

Utilisons [django-admin](https://docs.djangoproject.com/en/2.1/ref/django-admin/) pour générer un nouveau projet Django. Il s'agit de l'_utilitaire en ligne de commande de Django pour les tâches administratives_ :

```
# cd dans le dossier du projet
  cd ~/desktop/my_library
# initialiser l'environnement virtuel
  source ~/.envs/my_library/bin/activate
# utiliser Django pour créer un projet : server
  django-admin startproject server
# cd dans le nouveau projet Django
  cd server
# synchroniser la base de données
  python manage.py migrate
# exécuter le serveur Django
  python manage.py runserver
```

Maintenant, visitez `http://localhost:8000` dans votre navigateur et confirmez que le projet Django fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/7i6tTqE67PlSVFaTr9cp64isfajFSzMzFehh)
_Serveur en cours d'exécution. Succès !_

Vous pouvez arrêter le serveur avec `cmd+ctrl`.

#### 2.2.1 Créer le compte Superuser

Nous devons créer un [superuser](https://docs.djangoproject.com/en/1.11/ref/django-admin/#createsuperuser) pour nous connecter au site d'administration et gérer les données de la base de données. À l'intérieur de `my_library/server`, nous exécutons :

```
# créer un superuser
  python manage.py createsuperuser
```

Remplissez les champs `Nom d'utilisateur`, `Adresse e-mail` (facultatif) et `Mot de passe`. Vous devriez recevoir un message de succès.

Maintenant, exécutez le serveur avec `python manage.py runserver` et allez sur `localhost:8000/admin` pour voir la page de connexion de l'admin. Entrez les détails de votre compte superuser pour vous connecter.

![Image](https://cdn-media-1.freecodecamp.org/images/o1Gki-a2KqtXWP15qNmcEomH8Zo8lpMzxkk-)
_Connecté au site d'administration Django_

Super ! Nous avons accès au site d'administration Django. Une fois que nous avons créé le modèle `books` et fait la configuration appropriée, nous pourrons ajouter, modifier, supprimer et visualiser les données des livres.

Déconnectez-vous et arrêtez le serveur avec `cmd+ctrl`.

#### 2.2.2 Protéger Nos Secrets

Avant de continuer, nous allons vouloir mettre à jour le fichier settings.py. Il contient des informations d'authentification que nous ne voulons pas exposer au public. Nous allons vouloir garder ces informations d'authentification hors de notre dépôt distant. Il existe de nombreuses [façons de nous protéger](https://medium.freecodecamp.org/how-to-securely-store-api-keys-4ff3ea19ebda). Voici mon approche :

```
# créer un fichier config.json pour contenir nos valeurs de configuration
  my_library/server/server/config.json
```

À l'intérieur, nous allons stocker notre valeur `SECRET_KEY` de `settings.py` sous `API_KEY` :

```
{
  "API_KEY" : "abcdefghijklmopqrstuvwxyz123456789"
}
```

Dans `settings.py`, importez la bibliothèque `json` et chargez les variables de configuration :

```py
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(BASE_DIR + '/server/config.json', 'r') as config:
    obj = json.load(config)
SECRET_KEY = obj["API_KEY"]
...
```

Pour que `config.json` (avec la clé secrète) ne soit pas poussé vers le dépôt, créez un fichier `.gitignore` dans `my_library`. Cela l'ignore (ainsi que certains autres fichiers autogénérés et la base de données) :

```
### Django ###
config.json
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
media
```

![Image](https://cdn-media-1.freecodecamp.org/images/gdH03DpyBNSsAOwSThZDMwnkkM8LFI0DIoyQ)

Maintenant, lorsque vous validez les modifications, les fichiers et dossiers listés ci-dessus ne sont pas ajoutés. Nos secrets sont en sécurité et notre dépôt ne contiendra pas de fichiers supplémentaires inutiles !

![Image](https://cdn-media-1.freecodecamp.org/images/unF2nV9ydWZI5ueW1dOY5nrSbkGBObGUe48x)

### 2.3 Démarrer une Application Django : books

Pensez aux applications Django comme à des modules qui se connectent à votre projet. Nous allons créer une application appelée `books` contenant les modèles, les vues et d'autres paramètres. C'est ainsi que nous interagissons avec les données des livres dans la base de données.

Quelles sont les différences entre les projets et les applications dans Django ? Consultez [ce fil de discussion](https://stackoverflow.com/questions/19350785/what-s-the-difference-between-a-project-and-an-app-in-django-world).

```
# créer une nouvelle application : books
  python manage.py startapp books
# crée le répertoire : my_library/server/books
```

Maintenant, nous allons installer l'application `books` dans le projet `server`. Ouvrez le fichier de paramètres : `my_library/server/server/settings.py`.

Faites défiler jusqu'au tableau `INSTALLED_APPS`. Django a installé ses propres applications principales par défaut. Installez l'application `books` à la fin du tableau :

```
INSTALLED_APPS = [
  ...
  'books'
]
```

### 2.4 Décrire le modèle Book

Ensuite, nous décrivons le modèle `Book` dans l'application books. Ouvrez le fichier models `my_library/server/books/models.py`.

Décrivez un modèle `Book` qui indique à Django que chaque livre dans la base de données aura :

* un champ `title` d'une longueur maximale de 500 caractères
* un champ `author` d'une longueur maximale de 100 caractères
* un champ `description` avec un nombre ouvert de caractères

```py
from django.db import models

class Book(models.Model):
  title       = models.CharField(max_length=500)
  author      = models.CharField(max_length=100)
  description = models.TextField()
```

### 2.5 Enregistrer le modèle Book avec l'admin

Maintenant, nous enregistrons le modèle `Book` avec l'admin pour notre application `books`. Cela nous permet de le visualiser dans le site d'administration et de manipuler les données des livres à partir de là. Ouvrez le fichier admin `my_library/server/books/admin.py` et ajoutez :

```py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'description']
```

Avec un nouveau modèle créé, nous devons faire et exécuter des [migrations](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-makemigrations) afin que la base de données se synchronise :

```
python manage.py makemigrations
python manage.py migrate
```

Exécutez le serveur et allez sur `localhost:8000/admin` pour vous connecter. Remarquez que le modèle Book enregistré avec l'admin s'affiche :

![Image](https://cdn-media-1.freecodecamp.org/images/BByc9ryhPWVpc6U4SWpaz3E6JTrOeFcQcwFB)
_Avec le modèle 'Book' enregistré avec l'admin_

En cliquant sur 'Books', une liste vide s'affiche car il n'y a pas de livres dans la base de données. Cliquez sur 'Add' pour commencer à créer un nouveau livre à ajouter à la base de données. Allez-y et créez quelques livres.

![Image](https://cdn-media-1.freecodecamp.org/images/g24EmlIIvatYfhwIRgzXi3yakh8MzCJnnxfo)
_Ajoutez un nouveau livre à la base de données_

Enregistrez et retournez à la liste pour visualiser les nouvelles données. Maintenant, il affiche les champs titre, auteur et description (`list_display array`).

![Image](https://cdn-media-1.freecodecamp.org/images/jnqaPh1DSeqpT2wrzeA9bppZRhWcVM3Z4O21)
_Liste de tous les livres que nous avons ajoutés à la base de données_

C'est génial. Nous pouvons maintenant visualiser nos livres de la base de données dans le site d'administration. Les fonctions de création, d'édition et de suppression sont également disponibles.

**Note** : Pour des raisons de simplicité, nous utiliserons la [base de données SQLite](https://www.sqlite.org/about.html). Elle est préinstallée avec la création de chaque projet Django. Pas besoin de faire un travail supplémentaire avec les bases de données pour les besoins de ce tutoriel.

![Image](https://cdn-media-1.freecodecamp.org/images/vMyJyhv4xHSQNKh3IkRdoJvFKtO5Olet5iQz)

### 2.6 Conclusion

Félicitations, nous sommes arrivés à la fin de la **Section 2** ! Voici ce que nous avons fait jusqu'à présent :

* Installé `python`
* Utilisé `python` pour installer le gestionnaire de paquets `pip`
* Utilisé `pip` pour installer `virtualenv` afin de créer des environnements virtuels
* Créé un environnement virtuel dans `~/.envs` appelé `my_library`
* Activé l'environnement `my_library` et mis à niveau `pip`
* Installé `Django 1.11 LTS` dans l'environnement `my_library`
* Créé notre répertoire de projet `my_library`
* Créé le projet Django `server`
* Créé un compte `Superuser` pour accéder au site d'administration Django
* Protégé nos secrets en déplaçant notre `SECRET_KEY` dans `config.json`
* Ignoré les fichiers autogénérés et/ou sensibles avec `.gitignore`
* Créé une nouvelle application appelée `books`
* Décrire le modèle `Book`
* Enregistré le modèle `Book` avec l'admin
* Ajouté des données de livres dans la base de données

![Image](https://cdn-media-1.freecodecamp.org/images/-CPsLneURbcGROamQjKRjILkxEgEv5-DNq3o)
_Ce qui maintient l'internet ensemble_

### Section 3 : Construire un Serveur, puis REST

Dans cette section, nous utilisons le Django REST Framework pour construire notre API `books`. Elle possède des sérialiseurs, des vues et des URLs qui interrogent, structurent et livrent les données des livres. Les données et les méthodes sont accessibles via des points de terminaison de l'API.

Ces points de terminaison sont une extrémité d'un canal de communication. Points de contact de la communication entre l'API et un autre système. L'autre système dans ce contexte est notre client front-end Ember. Le client Ember interagira avec la base de données via les points de terminaison de l'API. Nous créons ces points de terminaison avec Django et le Django REST Framework.

Nous avons utilisé Django pour configurer le modèle `book` et le site d'administration qui nous permet d'interagir avec la base de données. Django REST Framework nous aidera à construire l'API REST que le front-end utilisera pour interagir avec le back-end.

![Image](https://cdn-media-1.freecodecamp.org/images/DRBFIYTjAoZWDNDv9VOK1bWvOIIJej8x5xOP)
_Couches d'application empilées une par une._

### 3.1 Django REST Framework

[Django REST Framework](http://www.django-rest-framework.org/) (DRF) se construit sur Django. Il simplifie la création d'[API Web RESTful](http://rest.elkstein.org/). Il vient avec des outils pour rendre le processus simple.

Les développeurs de DRF ont identifié des motifs communs pour les sérialiseurs et les vues. Puisque nos données et ce que les utilisateurs peuvent en faire sont simples, nous utiliserons les sérialiseurs et les vues intégrés. N'oubliez pas, nos données de livres n'ont que trois champs : `title`, `author` et `description`. Les utilisateurs peuvent créer de nouveaux enregistrements de livres, les modifier et supprimer des enregistrements existants. Cette fonctionnalité est bien dans la plage des motifs communs de base. Ils sont bien supportés par les sérialiseurs et les vues intégrés. Nous n'aurons pas à les construire à partir de zéro.

Pour des projets plus complexes, vous voudrez peut-être écraser les valeurs par défaut ou créer les vôtres. Encore une fois, pour des raisons de simplicité, nous utiliserons ce qui sort de la boîte sans modification indue.

![Image](https://cdn-media-1.freecodecamp.org/images/e6SmOCOMO13g05h-y06mLtBMqtAn2is3WxwX)

#### 3.1.1 Installer Django REST Framework

Entrez dans le répertoire `my_library` et activez l'environnement virtuel. Pour commencer à travailler avec DRF, installez-le avec `pip` :

```
# entrer dans my_library
  cd ~/desktop/my_library

# activer l'environnement virtuel
  source ~/.envs/my_library/bin/activate

# installer Django REST Framework
  pip install djangorestframework
# installer le support Markdown pour l'API navigable
  pip install markdown
```

Maintenant, ouvrez `my_library/server/server/settings.py`. Installez DRF juste au-dessus de l'application `books` dans le tableau `INSTALLED_APPS` :

```
INSTALLED_APPS = [
  ...
  'rest_framework',
  'books'
]
```

Ajoutez les paramètres par défaut en bas du fichier sous forme d'objet appelé `REST_FRAMEWORK` :

```
REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': [      
   'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
  ]
}
```

L'objet des paramètres contient une clé `DEFAULT_PERMISSION_CLASSES` avec un tableau. Le seul élément dans le tableau est une classe de permission. Celle-ci _permet aux utilisateurs non authentifiés d'avoir un accès en lecture seule à l'API_. En savoir plus sur les permissions [ici](http://www.django-rest-framework.org/api-guide/permissions/#permissions).

### 3.2 Créer le dossier api books

Avec DRF installé, commençons à construire l'API `books`. Créez un nouveau dossier appelé `api` à l'intérieur de l'application `books`. Ensuite, créez un fichier `__init__.py` vide à l'intérieur : `my_library/server/books/api/__init__.py`.

Le fichier vide indique à Python que ce dossier est un module Python. Le dossier `api` contiendra les sérialiseurs, les vues et les URLs pour nos données de livres. Je vais expliquer la signification de ces termes dans leurs sections respectives ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/teuNGFUsjk6LLyFuKtD-pcN1IwvWwP8o0oh6)

### 3.3 Créer un sérialiseur de livre

En termes simples, les [sérialiseurs](http://www.django-rest-framework.org/api-guide/serializers/) prennent les données de la base de données et les restructurent. Cette structure est un plan pour que les données alternent entre les couches de l'application. Cela permet au front-end et au back-end de se parler dans une langue commune.

Par exemple, le front-end que nous allons créer attend que la réponse retournée par une requête soit au format JSON. La sérialisation des données pour qu'elles soient en JSON garantit que le front-end pourra les lire et les écrire.

```py
from rest_framework import serializers
from books.models import Book
class bookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = (
      'id',
      'title',
      'author',
      'description',
    )
```

Ce sérialiseur prend les données et les transforme au format JSON. Cela garantit qu'elles sont compréhensibles par le front-end.

#### **Imports**

Nous importons les `serializers` intégrés de DRF, et le modèle `Book` de notre application `books`.

```
from rest_framework import serializers
from books.models import Book
```

#### **La classe bookSerializer**

Pour ce projet, nous voulons une classe `Serializer` qui _correspond aux champs du modèle_. Le sérialiseur doit mapper les champs du modèle `title`, `author` et `description`. Nous pouvons faire cela avec le `[ModelSerializer](http://www.django-rest-framework.org/api-guide/serializers/#modelserializer)`. Selon la documentation :

La classe `ModelSerializer` est la même qu'une classe `Serializer` régulière, sauf que :

* Elle générera un ensemble de champs pour vous, basé sur le modèle.
* Elle générera des validateurs pour le sérialiseur, tels que les validateurs unique_together.
* Elle inclut des implémentations par défaut simples de `.create()` et `.update()`.

Les outils intégrés sont plus que capables de gérer nos besoins de base.

```py
class bookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = (
      'id',
      'title',
      'author',
      'description',
    )
```

### 3.4 Créer une vue pour obtenir et poster les données des livres

Les fonctions de vue prennent une requête web et retournent des réponses web. Une requête web à `localhost:8000/api/books`, par exemple, suscite une réponse du serveur.

Cette réponse peut être _le contenu HTML d'une page Web, ou une redirection, ou une erreur 404, ou un document XML, ou une image . . . ou n'importe quoi_ Dans notre cas, nous nous attendons à obtenir les données des livres structurées au format JSON.

Créez le fichier des vues dans `my_library/server/books/api/views.py` :

```py
from rest_framework import generics, mixins
from books.models import Book
from .serializers import  bookSerializer
class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'books'
  serializer_class = bookSerializer
  def get_queryset(self):
    return Book.objects.all()
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
```

#### **Imports**

Tout d'abord, nous importons `[generics](http://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)` et `[mixins](http://www.django-rest-framework.org/api-guide/generic-views/#mixins)` de DRF. Ensuite, le modèle `Book` de notre application `books` et le `bookSerializer` que nous avons créé.

`generics` fait référence aux vues d'API qui _mappent à vos modèles de base de données_. Ce sont des _vues pré-construites qui fournissent des motifs communs_. `mixins` sont des classes qui _fournissent les actions qui étaient utilisées pour fournir le comportement de base de la vue_. Notre modèle de livre est simpliste. Il n'a que les attributs `title`, `author` et `description`, donc ceux-ci nous fournissent les bases dont nous avons besoin.

```py
from rest_framework import generics, mixins
from books.models import Book
from .serializers import  bookSerializer
```

#### **La vue bookAPI**

Nous créons ensuite une `bookAPIView` qui prend en charge le `[CreateModelMixin](http://www.django-rest-framework.org/api-guide/generic-views/#createmodelmixin)` et le `[ListAPIView](http://www.django-rest-framework.org/api-guide/generic-views/#listapiview)`.

`CreateModelMixin` fournit une méthode `.create(request, *args, **kwargs)`. Cela implémente la création et la persistance d'une nouvelle instance de modèle. En cas de succès, il retourne une réponse `201 Create`. Cela inclut une représentation sérialisée de l'objet qu'il a créé.

Par exemple, nous ferions une requête POST pour créer un nouvel enregistrement de livre pour le livre Steve Jobs de Walter Isaacson. En cas de succès, nous obtenons une réponse avec le code `201`. La représentation sérialisée de l'enregistrement du livre comme suit :

```py
{
  "data": {
    "type": "books",
    "id":"10",
    "attributes": {
      "title": "Steve Jobs",
      "author": "Walter Isaacson",
      "description": "Basé sur plus de quarante interviews avec Jobs menées sur deux ans...
    }
  }
}
```

En cas d'échec, nous obtiendrons une réponse `400 Bad Request` avec les détails des erreurs. Par exemple, si nous essayons de créer un nouvel enregistrement de livre mais ne fournissons aucune information de `title` :

```json
{
  "errors":[
    {
      "status": "400",
      "source": {
        "pointer": "/data/attributes/title"
      },
      "detail": "Ce champ ne peut pas être vide."
    }
  ]
}
```

`ListAPIView` sert nos points de terminaison en lecture seule (GET). Il représente _une collection d'instances de modèle_. Nous l'utilisons lorsque nous voulons obtenir tous ou plusieurs livres.

`bookAPIView` prend également le `bookSerializer` récemment créé pour sa `serializer_class`.

Nous définissons le `resource_name` sur books pour _spécifier la clé de type dans la sortie json_. La couche de stockage de données du client front-end aura un modèle `book` qui est sensible à la casse. Nous ne voulons pas que le modèle `book` dans Ember et le modèle `Book` dans Django entrent en conflit. La définition du `resource_name` ici résout ce problème.

```py
class bookAPIView(mixins.CreateModelMixin, generics.ListAPIView):
  resource_name = 'books'
  serializer_class = bookSerializer
```

#### **Fonctions**

La fonction `get_queryset` retourne tous les objets livre dans la base de données. `post` prend la requête et les arguments et crée un nouvel enregistrement de livre dans la base de données si la requête est valide.

```py
def get_queryset(self):
    return Book.objects.all()
def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
```

### 3.5 Créer des URLs pour accéder aux données des livres

Les motifs d'URL mappent une URL à des vues. Par exemple, visiter `localhost:8000/api/books` devrait mapper à un motif d'URL. Celui-ci retourne ensuite les résultats d'une requête à cette vue.

Créez le fichier des URLs dans `my_library/server/books/api/urls.py` :

```py
from .views import bookAPIView
from django.conf.urls import url
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]
```

#### **Imports**

Nous importons notre vue `bookAPIView` et `url`. Nous utiliserons `url` pour créer une liste d'instances d'url.

```py
from .views import bookAPIView
from django.conf.urls import url
```

#### **Motifs d'URL de l'API books**

Dans le tableau `urlpatterns`, nous créons un motif d'URL avec la structure suivante :

* le motif `r'^$'`
* le chemin Python vers la vue `bookAPIView.as_view()`
* le nom `name='book-create'`

Le motif `r^$` est une expression régulière qui _correspond à une ligne/chaîne vide_. Cela signifie qu'il correspond à `localhost:8000`. Il correspond à tout ce qui vient après l'URL de base.

Nous appelons `[.as_view()](https://docs.djangoproject.com/en/1.11/ref/class-based-views/base/#django.views.generic.base.View.as_view)` sur `bookAPIView` car pour connecter la vue à l'url. Il _est la fonction (méthode de classe) qui connectera [la] classe avec son url_. Visitez une URL particulière et le serveur tente de la faire correspondre au motif d'URL. Ce motif retournera ensuite les résultats de la vue `bookAPI` que nous lui avons dit de répondre.

L'attribut `name=book-create` nous fournit un attribut `name`. Nous l'utilisons pour faire référence à notre URL dans tout le projet. Supposons que vous souhaitiez changer l'URL ou la vue à laquelle elle fait référence. Changez-la ici. Sans `name`, nous devrions parcourir tout le projet pour mettre à jour chaque référence. Consultez [ce fil de discussion](https://stackoverflow.com/a/11241936/5513243) pour en savoir plus.

```
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
]
```

#### **Motifs d'URL du serveur**

Maintenant, ouvrons le fichier des URLs de `server` `my_library/server/server/urls.py` :

```py
from django.conf.urls import url, include
from django.contrib import admin
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^api/books', include('books.api.urls', 
                              namespace='api-books'))
]
```

Ici, nous importons `include` et créons le motif `r^api/books` qui prend en charge toutes les URLs que nous avons créées dans le dossier `api`. Maintenant, l'URL de base pour nos URLs de l'API `books` devient `localhost:8000/api/books`. Visiter cette URL correspondra à notre motif `r^/api/books`. Cela correspond au motif `r^$` que nous avons construit dans l'API `books`.

Nous utilisons `namespace=api-books` afin que les URLs ne se heurtent pas les unes aux autres. Cela se produirait si elles étaient nommées de la même manière dans une autre application que nous créons. En savoir plus sur pourquoi nous utilisons `namespaces` dans [ce fil de discussion](https://stackoverflow.com/a/19171674/5513243).

#### 3.5.1 Démonstration : Parcourir l'API des livres

Maintenant que nous avons la configuration de base du framework REST, vérifions les données que le back-end retourne. Avec le serveur en cours d'exécution, visitez `localhost:8000/api/books`. L'[API navigable](http://www.django-rest-framework.org/topics/browsable-api/) devrait retourner quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vRQH7EEhJl7Dt0M8tqtXezjE48ESk1PF4Urv)
_Django REST Framework retournant les données des livres de la base de données_

![Image](https://cdn-media-1.freecodecamp.org/images/nhkde41r7VxTDjRtIB0qc-ry3jugObDiqfWE)

### 3.6 Conclusion

Super, nous commençons à avancer maintenant. À la fin de la **Section 3**, nous avons complété les étapes suivantes :

* Installé Django REST Framework dans notre projet
* Commencé à construire l'API `books`
* Créé un `serializer` pour les livres
* Créé une `view` pour les livres
* Créé des `URLs` pour les livres
* Parcouru l'API des livres qui retourne les données des livres depuis le back-end

![Image](https://cdn-media-1.freecodecamp.org/images/QeaabxrQLyzXfW30akDR1qeTrjxVyXUZ4dez)
_Cadeau des dieux_

### Section 4 : Poser les Fondations du Front-end

Dans cette section, nous changeons notre attention vers le front-end et commençons à travailler avec le framework Ember. Nous allons installer le logiciel requis, configurer un DOM de base, des styles, créer le modèle `book`, et la route `books`. Nous allons également charger des données de livres fictives à des fins de démonstration avant de passer à l'accès aux données réelles du back-end.

### 4.1 Installer le Logiciel Requis

Pour commencer le développement front-end, nous devons installer certains logiciels :

* [Node.js, NPM](https://nodejs.org/en/)
* [Ember CLI](https://ember-cli.com/)

#### 4.1.1 NodeJS et NPM

NodeJS est un environnement serveur open source. Nous n'avons pas besoin d'entrer dans les détails pour l'instant. NPM est un gestionnaire de paquets pour les paquets Node.js. Nous l'utilisons pour installer des paquets comme Ember CLI.

Installez NodeJS et NPM en utilisant [le fichier d'installation du site officiel](http://nodejs.org/en/download/).

Une fois l'installation terminée, vérifiez que tout est installé :

```
node --version
npm --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/hEqfcvp-GnAp2OUfgwCUCBON6UN0fDoovaJu)

#### 4.1.2 Ember CLI

Utilisons NPM pour installer Ember CLI. C'est l'_utilitaire officiel en ligne de commande utilisé pour créer, construire, servir et tester les applications et addons [Ember.js](https://emberjs.com/). Ember CLI vient avec tous les outils dont nous avons besoin pour construire le front-end de notre application.

```
# installer Ember CLI
  npm install -g ember-cli
# vérifier qu'il est installé
  ember --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/6hklopSfXA8qI9ssI6yPxWmES2K2oF40a-Xm)

### 4.2 Démarrer un Projet Ember : client

Créons un client front-end appelé `client` en utilisant Ember CLI :

```
# cd dans le dossier principal du projet
  cd ~/desktop/my_library
# créer une nouvelle application : client
  ember new client
# cd dans le répertoire
  cd client
# exécuter le serveur
  ember s
```

Rendez-vous sur `http://localhost:4200` et vous devriez voir cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/9CdYwMxZs608uCFDtckD2hupL4IKrcfI1Ehz)
_En cours d'exécution_

Le projet client Ember de base s'exécute comme prévu. Vous pouvez arrêter le serveur avec `ctrl+C`.

#### 4.2.1 Mettre à jour .gitignore avec les exclusions Ember

Avant de faire de nouveaux commits, mettons à jour le fichier `.gitignore`. Nous voulons exclure les fichiers indésirables du dépôt. Ajoutez au fichier ci-dessous la section Django :

```
...
### Ember ###
/client/dist
/client/tmp
# dépendances
/client/node_modules
/client/bower_components
# divers
/client/.sass-cache
/client/connect.lock
/client/coverage/*
/client/libpeerconnection.log
/client/npm-debug.log
/client/testem.log
# ember-try
/client/.node_modules.ember-try/
/client/bower.json.ember-try
/client/package.json.ember-try
```

### 4.3 Affichage des données des livres

#### 4.3.1 Configuration du DOM

Maintenant que nous avons généré un projet de base, configurons un DOM et des styles de base. Je ne fais rien de fantaisiste ici. C'est le minimum nécessaire pour que nos données s'affichent dans un format lisible.

Localisez le fichier `client/app/templates/application.hbs`. Supprimez `{{welcome-page}}` et les commentaires.

Ensuite, créez une `div` avec la classe `.nav`. Utilisez l'aide intégrée `[{{#link-to}}](https://guides.emberjs.com/release/templates/links/)` d'Ember pour créer un lien vers la route `books` (nous la créerons plus tard) :

```html
<div class="nav">
  {{#link-to 'books' class="nav-item"}}Home{{/link-to}}
</div>
```

Enveloppez tout, y compris le `[{{outlet}}](https://guides.emberjs.com/release/routing/rendering-a-template/)`, dans une `div` avec la classe `.container`. Chaque modèle de route se rendra à l'intérieur de `{{outlet}}` :

```html
<div class="container">
  <div class="nav">
    {{#link-to 'books' class="nav-item"}}Home{{/link-to}}
  </div>
{{outlet}}
</div>
```

C'est le modèle pour la route de niveau parent `application`. Toutes les sous-routes comme `books` se rendront à l'intérieur de `{{outlet}}`. Cela signifie que le `nav` sera toujours visible à l'écran.

#### 4.3.2 Créer des styles

Je ne vais pas entrer dans les détails du CSS. C'est assez simple à comprendre. Localisez le fichier `client/app/styles/app.css` et ajoutez les styles suivants :

**Variables et Utilitaires**

```css
:root {
  --color-white:  #fff;
  --color-black:  #000;
  --color-grey:   #d2d2d2;
  --color-purple: #6e6a85;
  --color-red:    #ff0000;
  --font-size-st: 16px;
  --font-size-lg: 24px;
  --box-shadow: 0 10px 20px -12px rgba(0, 0, 0, 0.42),
                0 3px  20px  0px  rgba(0, 0, 0, 0.12),
                0 8px  10px -5px  rgba(0, 0, 0, 0.2);
}
.u-justify-space-between {
  justify-content: space-between !important;
}
.u-text-danger {
  color: var(--color-red) !important;
}
```

**Général**

```css
body {
  margin: 0;
  padding: 0;
  font-family: Arial;
}
.container {
  display: grid;
  grid-template-rows: 40px calc(100vh - 80px) 40px;
  height: 100vh;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/5XDkBqqpQcV7KXyA9HFpXOMED7ISf-wTnlhR)

**Navigation**

```css
.nav {
  display: flex;
  padding: 0 10px;
  background-color: var(--color-purple);
  box-shadow: var(--box-shadow);
  z-index: 10;
}
.nav-item {
  padding: 10px;
  font-size: var(--font-size-st);
  color: var(--color-white);
  text-decoration: none;
}
.nav-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/vNzYqMngN91hTgUYcAqWpW01vkaJDBGTWGJ7)

**En-têtes**

```css
.header {
  padding: 10px 0;
  font-size: var(--font-size-lg);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/UKbiWepf0IEUTAjL-9JuR8MUa6zO3HxkCpvU)

**Liste des Livres**

```css
.book-list {
  padding: 10px;
  overflow-y: scroll;
}
.book {
  display: flex;
  justify-content: space-between;
  padding: 15px 10px;
  font-size: var(--font-size-st);
  color: var(--color-black);
  text-decoration: none;
  cursor: pointer;
}
.book:hover {
  background: var(--color-grey);
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/rcfJhkZZS1D0wxCyxIC9X9jc6BkLnsVAMlWJ)

**Boutons**

```
button {
  cursor: pointer;
}
```

**Détail du Livre**

```css
.book.book--detail {
  flex-direction: column;
  justify-content: flex-start;
  max-width: 500px;
  background: var(--color-white);
  cursor: default;
}
.book-title {
  font-size: var(--font-size-lg);
}
.book-title,
.book-author,
.book-description {
  padding: 10px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/-8Ss5ml2SZVM6ZLhROuRXIFeMeMVOxER164L)

**Formulaire d'ajout/modification de livre**

```css
.form {
  display: flex;
  flex-direction: column;
  padding: 10px 20px;
  background: var(--color-white);
}
input[type='text'],
textarea {
  margin: 10px 0;
  padding: 10px;
  max-width: 500px;
  font-size: var(--font-size-st);
  border: none;
  border-bottom: 1px solid var(--color-grey);
  outline: 0;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/pdj99DtnkIaB4-7xbtKk1AIbxBUiWt2LOSr-)

**Actions**

```css
.actions {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding: 10px 20px;
  background-color: var(--color-white);;
  box-shadow: var(--box-shadow)
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/KpvfySOayj7YVPKjEmFUV5uZIOTC1Z3YUTmO)

### 4.4 La route des livres

#### **4.4.1 Créer la route des livres**

Maintenant que nous avons nos styles et notre DOM de conteneur en place, générons une nouvelle route qui affichera tous les livres de notre base de données :

```
ember g route books
```

Le fichier du routeur `client/app/router.js` se met à jour avec :

```js
import EmberRouter from '@ember/routing/router';
import config from './config/environment';
const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});
Router.map(function() {
  this.route('books');
});
export default Router;
```

#### **4.4.2 Charger des données fictives dans le hook du modèle**

Modifions la route des livres `client/app/routes/books.js` pour charger tous les livres de la base de données.

```js
import Route from '@ember/routing/route';
export default Route.extend({
  model() {
    return [
      {title: 'Monkey Adventure'},
      {title: 'Island Strife'},
      {title: 'The Ball'},
      {title: 'Simple Pleasures of the South'},
      {title: 'Big City Monkey'}
    ]
  }
});
```

Le hook du modèle retourne un tableau d'objets. Ce sont des données fictives à des fins de démonstration. Nous reviendrons ici plus tard et chargerons les données réelles de la base de données en utilisant Ember Data lorsque nous serons prêts.

#### **4.4.3 Mettre à jour le modèle de la route des livres**

Modifions le modèle de la route des livres `client/app/templates/books.hbs`. Nous voulons afficher les livres retournés dans le modèle.

```html
<div class="book-list">
  {{#each model as |book|}}
    <div class="book">
      {{book.title}}
    </div>
  {{/each}}
</div>
```

Ember utilise la [Bibliothèque de Modèles Handlebars](https://guides.emberjs.com/release/templates/handlebars-basics/). Ici, nous utilisons l'aide `each` pour itérer à travers notre tableau de données de livres dans `model`. Nous enveloppons chacun des éléments du tableau dans une `div` avec la classe `.book`. Accédez et affichez ses informations de titre avec `{{book.title}}`.

#### 4.4.4 Démonstration : route des livres chargeant et affichant des données fictives

Maintenant que nous avons le DOM, le modèle `book` et la route `books` configurés avec quelques données fictives, nous pouvons voir cela fonctionner dans le navigateur. Jetez un œil à `localhost:4200/books` :

![Image](https://cdn-media-1.freecodecamp.org/images/Q9NHnr2xZN1Sv556vGJrBaaH-zmpHo8-qFpn)
_Survoler un titre de livre pour le mettre en évidence_

#### 4.4.5 Créer une route d'application pour la redirection

C'est un peu ennuyeux de devoir ajouter un `/books` pour visiter la route `books`. Générons la route `application`. Nous pouvons utiliser le hook `redirect` pour rediriger vers la route `books` lorsque nous entrons dans la route de base `/`.

```
ember g route application
```

Si vous êtes invité à écraser le modèle `application.hbs`, dites non. Nous ne voulons pas écraser le modèle que nous avons déjà configuré.

Dans `client/app/routes/application.js`, créez le hook `redirect` :

```js
import Route from '@ember/routing/route';
export default Route.extend({
  redirect() {
    this.transitionTo('books');
  }
});
```

Maintenant, si vous visitez `localhost:4200`, il redirigera vers `localhost:4200/books`.

![Image](https://cdn-media-1.freecodecamp.org/images/Tkc46qrVylMjB6TuKWMePLOGYLaYPB7TUKc2)

### 4.5 Affichage des données réelles dans la route des livres

#### 4.5.1 Créer un adaptateur d'application

Nous ne voulons pas utiliser des données fictives pour toujours. Connectons-nous au back-end en utilisant un [adaptateur](https://www.emberjs.com/api/ember-data/release/classes/DS.Adapter) et commençons à extraire les données des livres dans le client. Pensez à l'adaptateur comme un _objet qui reçoit des requêtes d'un magasin_. Il _les traduit en l'action appropriée à prendre contre votre couche de persistance_

Générez un nouvel adaptateur d'application :

```
ember g adapter application
```

Localisez le fichier `client/app/adapters/application.js` et mettez-le à jour :

```js
import DS from 'ember-data';
import { computed } from '@ember/object';
export default DS.JSONAPIAdapter.extend({
  host: computed(function(){
    return 'http://localhost:8000';
  }),
  namespace: 'api'
});
```

Le JSONAPIAdapter est le _adaptateur par défaut utilisé par Ember Data_. Il transforme les requêtes du magasin en requêtes HTTP qui suivent le format [JSON API](http://jsonapi.org/format/). Il se connecte à la bibliothèque de gestion des données appelée [Ember Data](https://github.com/emberjs/data). Nous utilisons Ember Data pour interfacer avec le back-end de manière plus efficace. Il peut stocker et gérer les données dans le front-end et faire des requêtes au back-end lorsque cela est nécessaire. Cela signifie que les mises à jour mineures des pages n'ont pas besoin de requêtes constantes au back-end. Cela aide l'expérience utilisateur à se sentir plus fluide avec des temps de chargement généralement plus rapides.

Nous utiliserons son service `store` pour accéder aux données `server` sans écrire de requêtes `ajax` plus complexes. Celles-ci sont encore nécessaires pour des cas d'utilisation plus complexes.

Ici, l'adaptateur indique à Ember Data que son `host` est à `localhost:8000`, avec un espace de noms `api`. Cela signifie que toute requête au serveur commence par `http://localhost:8000/api/`.

![Image](https://cdn-media-1.freecodecamp.org/images/4lhfnmvPDvGNC0229Z2VqfVVNyn4W5hd4YVs)
_La pile complète_

#### 4.5.2 Créer le modèle de livre

Ember Data a des exigences particulières pour mapper ses données à ce qui provient du back-end. Nous allons générer un modèle `book` afin qu'il comprenne à quoi les données provenant du back-end doivent correspondre :

```
ember g model book
```

Localisez le fichier dans `client/models/book.js` et définissez le modèle `book` :

```js
import DS from 'ember-data';
export default DS.Model.extend({
  title: DS.attr(),
  author: DS.attr(),
  description: DS.attr()
});
```

Les attributs sont les mêmes que ceux que nous avons définis dans le back-end. Nous les définissons à nouveau afin qu'Ember Data sache à quoi s'attendre des données structurées.

#### 4.5.3 Mettre à jour la route `books`

Mettons à jour la route des livres en important le service `store` et en l'utilisant pour demander des données.

```js
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
export default Route.extend({
  store: service(),
  model() {
    const store = this.get('store');
    return store.findAll('book');
  }
});
```

#### 4.5.4 Démonstration : books a un problème CORS

Jusqu'à présent, nous avons créé un adaptateur d'application et mis à jour la route `books` pour interroger tous les livres de la base de données. Voyons ce que nous obtenons en retour.

Exécutez les serveurs Django et Ember. Ensuite, visitez `localhost:4200/books` et vous devriez voir ceci dans la console :

![Image](https://cdn-media-1.freecodecamp.org/images/YofsmuPXJQOamQVnPvs-0dJnGEvCl8LfWure)

Il semble y avoir un problème avec CORS.

#### 4.5.5 Résoudre le problème de partage de ressources cross-origines (CORS)

CORS définit une manière dont le navigateur et le serveur interagissent pour déterminer s'il est sûr d'autoriser une requête. Nous faisons une requête cross-origin de `localhost:4200` à `localhost:8000/api/books`. Du client au serveur dans le but d'accéder à nos données de livres.

Actuellement, le front-end n'est pas une origine autorisée à demander des données à partir de nos points de terminaison back-end. Ce blocage cause notre erreur. Nous pouvons résoudre ce problème en permettant aux requêtes de passer.

Commencez par installer une application qui ajoute des en-têtes CORS aux réponses :

```
pip install django-cors-headers
```

Installez-la dans le fichier `settings.py` de `server` sous le tableau `INSTALLED_APPS` :

```
INSTALLED_APPS = [
...
    'books',
    'corsheaders'
]
```

Ajoutez-la en haut du tableau `MIDDLEWARE` :

```
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
...
]
```

Enfin, autorisez toutes les requêtes à passer pendant le développement :

```
CORS_ORIGIN_ALLOW_ALL = DEBUG
```

#### 4.5.6 Démonstration : problème CORS résolu, format de données incompatible

Visitez `localhost:4200` et vous devriez voir ceci dans la console :

![Image](https://cdn-media-1.freecodecamp.org/images/0klx5kEzDhADK2vxluljOK1uArhWk4PuuPF9)

Il semble que nous ayons résolu le problème CORS et que nous recevions une réponse de `server` avec les données que nous attendons :

```json
[
    {
        "id": 1,
        "title": "Conquistador",
        "author": "Buddy Levy",
        "description": "C'était un moment unique dans ..."
    },
    {
        "id": 2,
        "title": "East of Eden",
        "author": "John Steinbeck",
        "description": "Dans son journal, le lauréat du prix Nobel ..."
    }
]
```

Bien que nous obtenions un tableau d'objets au format JSON, il n'est toujours pas au format que nous souhaitons. Voici ce qu'Ember Data attend :

```json
{
  data: [
    {
      id: "1",
      type: "book",
      attributes: {
        title: "Conquistador",
        author: "Buddy Levy",
        description: "C'était un moment unique dans ..."
      }
    },
    {
      id: "2",
      type: "book",
      attributes: {
        title: "East of Eden",
        author: "John Steinbeck",
        description: "Dans son journal, le lauréat du prix Nobel ..."
      }
    }
  ]
}
```

Presque, mais pas tout à fait là.

![Image](https://cdn-media-1.freecodecamp.org/images/pBr8ZzZtGrBW-ubnBWvlfwv-7tEkxpIxlrV3)

### 4.6 Conclusion

Nous avons complété les étapes suivantes dans la **Section 4** :

* Installé NodeJS et NPM
* Installé Ember CLI et créé un nouveau projet client
* Configuration de base du DOM
* Créé une route `books` et un modèle pour charger et afficher les livres
* Démontré l'application en cours d'exécution avec des données fictives
* Créé un adaptateur d'application pour se connecter au back-end et recevoir des données
* Créé un modèle `book` et mis à jour la route `books` pour capturer les données du back-end
* Démontré que les données du back-end ne sont pas structurées de la manière dont Ember Data les attend

![Image](https://cdn-media-1.freecodecamp.org/images/zRshD6WOw8j2R4PwhMmm4eBJ650PkDGWI9lP)
_Celui-ci est à moi_

### Section 5 : Formats de données corrects, gestion des enregistrements individuels

Dans cette section, nous allons utiliser le Django REST Framework JSON API pour structurer les données de manière à ce qu'Ember Data puisse les utiliser. Nous allons également mettre à jour l'API `books` pour retourner une seule instance d'un enregistrement de livre. Nous allons également ajouter la fonctionnalité pour ajouter, modifier et créer des livres. Ensuite, nous aurons terminé notre application !

### 5.1 Installer le Django REST Framework JSON API

Tout d'abord, nous utilisons pip pour installer le [Django REST Framework JSON API](https://github.com/django-json-api/django-rest-framework-json-api) (DRF). Il transformera les réponses DRF régulières en un modèle `identity` au [format JSON API](http://jsonapi.org/format/#document-resource-object-identification).

Avec l'environnement virtuel activé :

```
# installer le Django REST Framework JSON API
  pip install djangorestframework-jsonapi
```

Ensuite, mettez à jour les paramètres DRF dans `server/server/settings.py` :

```
REST_FRAMEWORK = {
  'PAGE_SIZE': 100,
  
  'EXCEPTION_HANDLER': 
    'rest_framework_json_api.exceptions.exception_handler',
  
  'DEFAULT_PAGINATION_CLASS':    'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
'DEFAULT_PARSER_CLASSES': (
    'rest_framework_json_api.parsers.JSONParser',
    'rest_framework.parsers.FormParser',
    'rest_framework.parsers.MultiPartParser'
  ),
'DEFAULT_RENDERER_CLASSES': (
    'rest_framework_json_api.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
   ),
'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
'DEFAULT_FILTER_BACKENDS': (
     'rest_framework.filters.OrderingFilter',
    ),
'ORDERING_PARAM': 'sort',
   
   'TEST_REQUEST_RENDERER_CLASSES': (
     'rest_framework_json_api.renderers.JSONRenderer',
    ),
   
   'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}
```

Celles-ci remplacent les paramètres par défaut de DRF par les paramètres par défaut de JSON API. J'ai augmenté la `PAGE_SIZE` pour que nous puissions obtenir jusqu'à 100 livres en réponse.

### 5.2 Travailler avec des enregistrements de livres individuels

#### 5.2.1 Créer une vue

Mettons également à jour notre API `books` afin que nous puissions récupérer des instances individuelles d'un enregistrement de livre.

Créez une nouvelle vue appelée `bookRudView` dans `server/books/api/views.py` :

```py
class bookRudView(generics.RetrieveUpdateDestroyAPIView):
  resource_name       = 'books'
  lookup_field        = 'id'
  serializer_class    = bookSerializer
  def get_queryset(self):
    return Book.objects.all()
```

Cette vue utilise le champ de recherche `id` pour récupérer un enregistrement de livre individuel. Le [RetrieveUpdateDestroyAPIView](http://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview) fournit des gestionnaires de méthodes `GET`, `PUT`, `PATCH` et `DELETE` de base. Comme vous pouvez l'imaginer, ceux-ci nous permettent de créer, mettre à jour et supprimer des données de livre individuelles.

#### 5.2.2 Mettre à jour les URLs de l'API des livres

Nous devons créer un nouveau motif d'URL qui livre des données via `bookRudView`.

```py
from .views import bookAPIView, bookRudView
from django.conf.urls import url
urlpatterns = [
  url(r'^$', bookAPIView.as_view(), name='book-create'),
  url(r'^(?P<id>\d+)', bookRudView.as_view(), name='book-rud')
]
```

Importez `bookRudView`, faites-le correspondre au motif `r'^(?P<id>`;\d+)', et donnez-lui le nom `book-rud`.

#### 5.2.3 Mettre à jour les URLs du serveur

Enfin, mettez à jour le motif d'URL de l'API `books` dans `server/server/urls.py`. Nous voulons faire correspondre les motifs qui commencent après `books/` :

```
...
urlpatterns = [
  ...
  url(r'^api/books/?', include('books.api.urls', namespace='api-books')),
]
```

#### 5.2.4 Démonstration : Accéder à un seul enregistrement de livre

Maintenant, si vous visitez `localhost:8000/api/books/1`, il devrait afficher un seul enregistrement de livre qui correspond à l'`id` d'un livre :

![Image](https://cdn-media-1.freecodecamp.org/images/CUK0sNAqhaAp-aYXHTN0o-gCCToOtM4gUg3z)

Remarquez que nous avons accès aux méthodes `DELETE`, `PUT`, `PATCH` et autres. Celles-ci proviennent de `RetrieveUpdateDestroyAPIView`.

#### 5.2.5 Démonstration : Capturer et afficher les données du back-end dans le bon format

Avec `JSONAPI` installé, le back-end devrait envoyer des réponses que Ember peut utiliser. Exécutez les deux serveurs et visitez `localhost:4200/books`. Nous devrions obtenir des données réelles du back-end et avoir la route les afficher. Succès !

![Image](https://cdn-media-1.freecodecamp.org/images/9RQ7BOzrDZuruIw65IraJFmkz9DlN0WJ0bw5)
_Capturer et afficher les données du back-end_

Jetez un œil à la réponse qui arrive. Elle est au format `JSONAPI` valide avec lequel Ember Data fonctionne.

![Image](https://cdn-media-1.freecodecamp.org/images/Hz-SsH8c5UYq6InAy1jeCxwgNlHnMQ4AJ58L)

![Image](https://cdn-media-1.freecodecamp.org/images/PIGhJY1TrhBHlHDRfzeKcev5qvR1XX9aP62C)

### 5.3 La Route du Livre

Nous pouvons maintenant voir la liste des livres de notre base de données dans la route `books`. Ensuite, créons une nouvelle route dans le front-end `client`. Elle affichera les livres individuels en détail avec les données `title`, `author` et `description`.

#### 5.3.1 Créer la route `book`

Générez une nouvelle route pour la page du livre individuel :

```
ember g route book
```

Dans `router.js`, mettez à jour la nouvelle route avec le chemin `books/:book_id`. Cela remplace le chemin par défaut et prend un paramètre `book_id`.

```
...
Router.map(function() {
  this.route('books');
  this.route('book', { path: 'books/:book_id' });
});
...
```

Ensuite, mettez à jour la route `book` `client/app/routes/book.js` pour récupérer un seul enregistrement de livre de la base de données :

```
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
export default Route.extend({
  store: service(),
model(book) {
    return this.get('store').peekRecord('book', book.book_id);
  }
});
```

Comme indiqué dans `router.js`, la route `book` prend le paramètre `book_id`. Le paramètre va dans le hook `model` de la route et nous l'utilisons pour récupérer le livre avec le `store` Ember Data.

#### 5.3.2 Mettre à jour le modèle `book`

Notre modèle `client/app/templates/book.hbs` devrait afficher les données du livre que nous obtenons du `store`. Supprimez `{{outlet}}` et mettez-le à jour :

```html
<div class="book book--detail">
  <div class="book-title">
    {{model.title}}
  </div>
  <div class="book-author">
    {{model.author}}
  </div>
  <div class="book-description">
    {{model.description}}
  </div>
</div>
```

Comme dans le modèle `books`, nous accédons aux attributs du `model` en utilisant la [notation par points](https://codeburst.io/javascript-quickie-dot-notation-vs-bracket-notation-333641c0f781).

#### 5.3.3 Mettre à jour le modèle `books`

Enfin, mettons à jour le modèle `books`. Nous voulons lier chaque page de livre individuelle telle qu'affichée dans la route `book` que nous avons créée :

```html
<div class="book-list">
  {{#each model as |book|}}
    {{#link-to 'book' book.id class="book"}}
      {{book.title}}
    {{/link-to}}
  {{/each}}
</div>
```

Enveloppez le `book.title` avec l'aide `link-to`. Il fonctionne comme ceci :

* crée un lien vers la route `book`
* prend le `book.id` comme paramètre
* prend une `class` pour styliser la balise `<`;a> générée dans le DOM.

#### 5.3.4 Démonstration : Sélectionner un livre pour voir des informations détaillées

Maintenant, vérifiez `localhost:4200/books`. Nous pouvons cliquer sur nos livres pour obtenir une vue détaillée. Super !

![Image](https://cdn-media-1.freecodecamp.org/images/hyC6r85lGgPWSydWXWcCppI10y0v0yo4-1sC)

![Image](https://cdn-media-1.freecodecamp.org/images/kfuloJ1VtO6CV09r3CsY-2Gcl9Dd3ts8kt3G)

### 5.4 Conclusion

Nous sommes arrivés à la fin de la **Section 5** avec les étapes suivantes complétées :

* Identifié le problème avec les données provenant de Django
* Installé le Django REST Framework JSON API
* Mis à jour le modèle de la route `books`
* Créé la route `book` et le modèle

![Image](https://cdn-media-1.freecodecamp.org/images/MLAvJIJz8ChUSLcFJi4DFuVyMVcnlnzoMU87)
_Entrer dans les détails maintenant_

### Section 6 : Front-end Fonctionnel

Dans cette section, nous allons ajouter les fonctionnalités suivantes à l'expérience front-end :

* Ajouter un nouveau livre avec les champs titre, auteur et description
* Modifier les champs titre, auteur et description d'un livre existant
* Supprimer un livre existant

C'est tout ce que nous avons à faire pour compléter le reste de notre application. Nous avons parcouru un long chemin. Poursuivons jusqu'à la fin !

### 6.1 Ajouter un nouveau livre à la base de données

Nous pouvons maintenant voir tous les livres de la base de données et voir les enregistrements de livres individuels en détail. Il est temps de construire la fonctionnalité pour ajouter un nouveau livre à la base de données. Voici les étapes que nous allons suivre pour que cela se produise :

* La route `create-book` gère le processus de création d'un nouveau livre et de son ajout à la base de données
* Le modèle `create-book` aura un formulaire avec deux entrées et une zone de texte pour saisir un `title`, un `author` et une `description`
* Le contrôleur `create-book` gère les données saisies dans le formulaire

#### 6.1.1 Créer la route et le contrôleur create-book

Générez la route `create-book` pour gérer la création de nouveaux livres :

```
ember g route create-book
```

Créez un contrôleur du même nom pour contenir les données du formulaire :

```
ember g controller create-book
```

#### 6.1.2 Configurer le contrôleur `create-book`

Dans `client/app/controllers/create-book.js`, créez une propriété calculée appelée `form`. Elle retournera un objet avec nos attributs de données de livre. C'est ici que nous capturons les nouvelles données de livre saisies par l'utilisateur. Elle est vide par défaut.

```js
import Controller from '@ember/controller';
import { computed } from '@ember/object';
export default Controller.extend({
  form: computed(function() {
    return {
      title: '',
      author: '',
      description: ''
    }
  })
});
```

#### 6.1.3 Configurer la route `create-book`

Dans `client/app/routes/create-book.js`, nous faisons ce qui suit :

* créer des actions pour confirmer la création d'un nouveau livre
* annuler le processus de création
* utiliser un hook de route pour effacer les données du formulaire lors de l'entrée dans la route :

```js
import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';
export default Route.extend({
  store: service(),
  setupController(controller, model) {
    this._super(controller, model);
    this.controller.set('form.title', '');
    this.controller.set('form.author', '');
    this.controller.set('form.description', '');
  },
  actions: {
    create() {
      const form = this.controller.get('form');
      const store = this.get('store');
      const newBook = store.createRecord('book', {
        title: form.title,
        author: form.author,
        description: form.description
      });
      newBook.save()
        .then(() => {
          this.transitionTo('books');
        });
     },
     cancel() {
       this.transitionTo('books');
     }
  }
});
```

Le hook `setupController` nous permet de réinitialiser les valeurs du formulaire. Cela est fait pour qu'elles ne persistent pas lorsque nous allons et venons à travers les pages. Nous ne voulons pas cliquer sur une autre page sans avoir terminé le processus de création de livre. Si nous le faisons, nous reviendrons pour voir les données inutilisées encore présentes dans notre formulaire.

L'action `create()` prendra les données du formulaire et créera un nouvel enregistrement avec le `store` Ember Data. Elle le persiste ensuite dans le back-end Django. Une fois terminé, elle redirigera l'utilisateur vers la route `books`.

Le bouton `cancel` redirige l'utilisateur vers la route `books`.

#### 6.1.4 Configurer le modèle `create-book`

Ensuite, dans `client/app/template/create-book.hbs`, nous construisons le formulaire :

```html
<form class="form">
  <div class="header">
    Ajouter un nouveau livre
  </div>
  {{input
    value=form.title
    name="title"
    placeholder="Titre"
    autocomplete='off'
  }}
  {{input
    value=form.author
    name="author"
    placeholder="Auteur"
    autocomplete='off'
  }}
  {{textarea
    value=form.description
    name="description"
    placeholder="Description"
    rows=10
  }}
</form>
<div class="actions">
  <div>
    <button {{action 'create'}}>
      Créer
    </button>
    <button {{action 'cancel'}}>
      Annuler
    </button>
  </div>
</div>
```

Le `form` utilise les aides intégrées `{{input}}` pour :

* prendre des valeurs
* afficher des placeholders
* désactiver l'autocomplétion.

L'aide `{{text}}` fonctionne de manière similaire, avec l'ajout du nombre de lignes.

La div des actions contient les deux boutons pour créer et annuler. Chaque bouton est lié à son action homonyme en utilisant l'aide `{{action}}`.

#### 6.1.5 Mettre à jour le modèle de la route `books`

La dernière pièce du puzzle de création de livre est d'ajouter un bouton dans la route `books`. Il nous permettra d'accéder à la route `create-book` et de commencer à créer un nouveau livre.

Ajoutez en bas de `client/app/templates/books.hbs` :

```
...
{{#link-to 'create-book' class='btn btn-addBook'}}
  Ajouter un livre
{{/link-to}}
```

#### 6.1.6 Démonstration : Peut ajouter un nouveau livre

Maintenant, si nous revenons et essayons de créer un nouveau livre à nouveau, nous trouverons le succès. Cliquez sur le livre pour voir une vue plus détaillée :

![Image](https://cdn-media-1.freecodecamp.org/images/8ktkFGXqUnl-f3OtzVczYW5Oa4JlfrhEv7Ev)
_Ajout d'un nouveau livre à la bibliothèque_

![Image](https://cdn-media-1.freecodecamp.org/images/7JlRVM4oznuSb0K7FKRdCInNKKVeGOFcy0VS)
_Nouveau livre créé et affiché_

![Image](https://cdn-media-1.freecodecamp.org/images/BUdQmE0HUaMn9xhRvWXR7GI0jU-NlXu8SmzW)

### 6.2 Supprimer un livre de la base de données

Maintenant que nous pouvons ajouter des livres à la base de données, nous devrions également pouvoir les supprimer.

#### 6.2.1 Mettre à jour le modèle de la route `book`

Tout d'abord, mettez à jour le modèle de la route `book`. Ajoutez sous `book book--detail` :

```html
...
<div class="actions {{if confirmingDelete
                         'u-justify-space-between'}}">
  {{#if confirmingDelete}}
    <div class="u-text-danger">
      Êtes-vous sûr de vouloir supprimer ce livre ?
    </div>
    <div>
      <button {{action 'delete' model}}>Supprimer</button>
      <button {{action (mut confirmingDelete)false}}>
        Annuler
      </button>
    </div>
  {{else}}
    <div>
      <button {{action (mut confirmingDelete) true}}>Supprimer</button>
    </div>
  {{/if}}
</div>
```

La div `actions` contient les boutons et le texte pour le processus de suppression du livre.

Nous avons un `bool` appelé `confirmingDelete` qui sera défini sur le `controller` de la route. `confirmingDelete` ajoute la classe utilitaire `.u-justify-space-between` sur `actions` lorsqu'il est `true`.

Lorsque c'est vrai, il affiche également une invite avec la classe utilitaire `.u-text-danger`. Cela invite l'utilisateur à confirmer la suppression du livre. Deux boutons apparaissent. L'un pour exécuter l'action `delete` dans notre route. L'autre utilise l'aide `mut` pour basculer `confirmingDelete` sur `false`.

Lorsque `confirmingDelete` est `false` (l'état par défaut), un seul bouton `delete` s'affiche. Cliquer dessus bascule `confirmingDelete` sur `true`. Cela affiche alors l'invite et les deux autres boutons.

#### 6.2.2 Mettre à jour la route `book`

Ensuite, mettez à jour la route `book`. Sous le hook `model`, ajoutez :

```
setupController(controller, model) {
  this._super(controller, model);
  this.controller.set('confirmingDelete', false);
},
```

Dans `setupController`, nous appelons `this._super()`. C'est pour que le contrôleur passe par ses mouvements habituels avant que nous fassions nos affaires. Ensuite, nous définissons `confirmingDelete` sur `false`.

Pourquoi faisons-nous cela ? Supposons que nous commençons à supprimer un livre, mais que nous quittons la page sans annuler l'action ou supprimer le livre. Lorsque nous allons sur n'importe quelle page de livre, `confirmingDelete` serait défini sur `true` comme un reste.

Ensuite, créons un objet `actions` qui contiendra nos actions de route :

```
actions: {
  delete(book) {
    book.deleteRecord();
    book.save().then(() => {
      this.transitionTo('books');
    });
  }
}
```

L'action `delete` telle que référencée dans notre modèle prend un `book`. Nous exécutons `deleteRecord` sur le `book` puis `save` pour persister le changement. Une fois que cette promesse est terminée, `transitionTo` passe à la route `books` (notre vue de liste).

#### 6.2.3 Démonstration : Peut supprimer un livre existant

Regardons cela en action. Exécutez les serveurs et sélectionnez un livre que vous souhaitez supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/X3g8JcJt5Gh7OfgE4G3JPvszzlEE902n8BJK)
_Bouton Supprimer visible lorsque confirmingDelete est faux_

![Image](https://cdn-media-1.freecodecamp.org/images/VsfnqMVBFAce2azSvhDa1kIkBKYSzZ68RhIk)
_Invite à confirmer la suppression du livre lorsque confirmingDelete est vrai_

Lorsque vous supprimez le livre, il redirige vers la route `books`.

![Image](https://cdn-media-1.freecodecamp.org/images/9OqjwQPyAxDXv9JCgoYGYpF8ARv6WZd-DK4h)

### 6.3 Modifier un livre dans la base de données

Enfin, nous allons ajouter la fonctionnalité pour modifier les informations d'un livre existant.

#### 6.3.1 Mettre à jour le modèle de la route `book`

Ouvrez le modèle `book` et ajoutez un formulaire pour mettre à jour les données du livre :

```html
{{#if isEditing}}
  <form class="form">
    <div class="header">Modifier</div>
    {{input
      value=form.title
      placeholder="Titre"
      autocomplete='off'
    }}
    {{input
      value=form.author
      placeholder="Auteur"
      autocomplete='off'
    }}
    {{textarea
      value=form.description
      placeholder="Description"
      rows=10
    }}
  </form>
  <div class="actions">
    <div>
      <button {{action 'update' model}}>Mettre à jour</button>
      <button {{action (mut isEditing) false}}>Annuler</button>
    </div>
  </div>
{{else}}
  ...
  <div>
    <button {{action (mut isEditing) true}}>Modifier</button>
    <button {{action (mut confirmingDelete) true}}>Supprimer</button>
  </div>
  ...
{{/if}}
```

Tout d'abord, enveloppons tout le modèle dans une instruction `if`. Cela correspond à la propriété `isEditing` qui par défaut sera `false`.

Remarquez que le formulaire est presque identique à notre formulaire de création de livre. La seule vraie différence est que les actions `update` exécutent l'action `update` dans la route `book`. Le bouton `cancel` bascule également la propriété `isEditing` sur `false`.

Tout ce que nous avions avant est imbriqué à l'intérieur du `else`. Nous ajoutons le bouton `Edit` pour basculer `isEditing` sur true et afficher le formulaire.

#### 6.3.2 Créer un contrôleur `book` pour gérer les valeurs du formulaire

Vous vous souvenez du contrôleur `create-book` ? Nous l'avons utilisé pour contenir les valeurs qui sont ensuite envoyées au serveur pour créer un nouvel enregistrement de livre.

Nous utiliserons une méthode similaire pour obtenir et afficher les données du livre dans notre formulaire `isEditing`. Il pré-remplira le formulaire avec les données actuelles du `book`.

Générez un contrôleur de livre :

```
ember g controller book
```

Ouvrez `client/app/controllers/book.js` et créez une propriété calculée `form` comme avant. Contrairement à avant, nous utiliserons le `model` pour pré-remplir notre formulaire avec les données actuelles du `book` :

```js
import Controller from '@ember/controller';
import { computed } from '@ember/object';
export default Controller.extend({
  form: computed(function() {
    const model = this.get('model');
    return {
      title: model.get('title'),
      author: model.get('author'),
      description: model.get('description')
    }
  })
});
```

#### 6.3.3 Mettre à jour la route `book`

Nous devons mettre à jour notre route à nouveau :

```js
setupController(controller, model) {
  ...
  this.controller.set('isEditing', false);
  this.controller.set('form.title', model.get('title'));
  this.controller.set('form.author', model.get('author'));
  this.controller.set('form.description', model.get('description'));
},
```

Ajoutons au hook `setupController`. Définissons `isEditing` sur `false` et réinitialisons toutes les valeurs du formulaire à leurs valeurs par défaut.

Ensuite, créons l'action `update` :

```js
actions: {
  ...
  update(book) {
    const form = this.controller.get('form');
    book.set('title', form.title);
    book.set('author', form.author);
    book.set('description', form.description);
    book.save().then(() => {
      this.controller.set('isEditing', false);
    });
  }
}
```

C'est assez simple. Nous obtenons les valeurs du formulaire, définissons ces valeurs sur le `book` et persistons avec `save`. Une fois réussi, nous basculons `isEditing` à `false`.

#### 6.3.4 Démonstration : Peut modifier les informations d'un livre existant

![Image](https://cdn-media-1.freecodecamp.org/images/xMgtmxnN122AZPurNoIFRX3QyQ6WVR909YOc)
_Bouton Modifier pour basculer la propriété du contrôleur isEditing_

![Image](https://cdn-media-1.freecodecamp.org/images/XBlE7hYhZIyRzAhbtDVBPMUFy3ZNJseyVU6p)
_Formulaire pré-rempli avec les informations actuelles du livre_

![Image](https://cdn-media-1.freecodecamp.org/images/r5A-y2Xi4sDOwQrza0ClHizr5VNmXbloXM58)
_Livre mis à jour avec de nouvelles informations_

![Image](https://cdn-media-1.freecodecamp.org/images/jHXRFAZRrJLz3vqbqdsmxPCYsYVOrxu2qogA)

### 6.4 Conclusion

Nous avons complété les étapes suivantes à la fin de la **Section 6** :

* Identifié le problème avec les données provenant de Django
* Installé JSON API dans Django
* Mis à jour le modèle de la route Books
* Créé la route de détail du livre et le modèle
* Peut visualiser, ajouter, modifier et supprimer des enregistrements de la base de données depuis le client EmberJS

**C'est tout. Nous l'avons fait ! Nous avons construit une application full stack très basique en utilisant Django et Ember.**

Prenons du recul et réfléchissons à ce que nous avons construit pendant une minute. Nous avons une application appelée `my_library` qui :

* liste les livres d'une base de données
* permet aux utilisateurs de voir chaque livre en plus de détails
* ajouter un nouveau livre
* modifier un livre existant
* supprimer un livre

Alors que nous avons construit l'application, nous avons appris à connaître Django et comment il est utilisé pour administrer la base de données. Nous avons créé des modèles, des sérialiseurs, des vues et des motifs d'URL pour travailler avec les données. Nous avons utilisé Ember pour créer une interface utilisateur pour accéder et modifier les données via les points de terminaison de l'API.

![Image](https://cdn-media-1.freecodecamp.org/images/KTyH3U0QWUOf8LUEIgKEXovuO8gabreUhKHN)
_Ouf_

### Section 7 : Passer à autre chose

### 7.1 Qu'est-ce qui suit ?

Si vous êtes arrivé jusqu'ici, vous avez terminé le tutoriel ! L'application fonctionne avec toutes les fonctionnalités prévues. C'est beaucoup à être fier. Le développement logiciel, compliqué ? C'est un euphémisme. Cela peut sembler carrément inaccessible même avec toutes les ressources disponibles. J'ai ce sentiment tout le temps.

Ce qui fonctionne pour moi, c'est de prendre des pauses fréquentes. Se lever et s'éloigner de ce que vous faites. Faire autre chose. Puis revenir et décomposer vos problèmes étape par étape en les plus petites unités. Corriger et refactoriser jusqu'à ce que vous arriviez là où vous voulez être. Il n'y a pas de raccourcis pour construire vos connaissances.

En tout cas, nous avons peut-être fait beaucoup ici pour une introduction, mais nous ne faisons qu'effleurer la surface. Il y a beaucoup plus à apprendre sur le développement full stack. Voici quelques exemples à considérer :

* comptes utilisateurs avec authentification
* test de la fonctionnalité de l'application
* déploiement de l'application sur le web
* écriture de l'API REST à partir de zéro

Quand j'aurai le temps, je regarderai pour écrire plus sur ces sujets moi-même.

J'espère que vous avez trouvé ce tutoriel utile. Il est destiné à servir de point de départ pour vous afin d'en apprendre davantage sur Django, Ember et le développement full stack. Cela a définitivement été une expérience d'apprentissage pour moi. **Un grand merci à mon équipe [Closing Folders](http://closingfolders.com/) pour le soutien et les encouragements. Nous recrutons maintenant, alors n'hésitez pas à nous contacter !**

Si vous souhaitez me contacter, vous pouvez le faire via les canaux suivants :

* [email](mailto:michael.xavier@closingfolders.com)
* [linkedIn](https://www.linkedin.com/in/vinothmichaelxavier/)
* [medium](https://medium.com/@sunskyearthwind)
* [site web personnel](https://lookininward.github.io/)

### 7.2 Lectures Complémentaires

L'écriture de ce tutoriel m'a forcé à affronter les limites de mes connaissances. Voici les ressources qui m'ont aidé à comprendre les sujets abordés :

[Qu'est-ce qu'un programmeur full stack ?](http://qr.ae/TUIx4x)  
[Qu'est-ce qu'une application web ?](https://stackoverflow.com/a/8694944/5513243)  
[Qu'est-ce que Django ?](https://tutorial.djangogirls.org/en/django/)  
[Qu'est-ce qu'EmberJS ?](https://hacks.mozilla.org/2014/02/ember-js-what-it-is-and-why-we-need-to-care-about-it/)  
[Qu'est-ce que le contrôle de version ?](https://www.atlassian.com/git/tutorials/what-is-version-control)  
[Qu'est-ce que Git ?](https://medium.com/swlh/git-as-the-newbies-learning-steroid-963a2146220b)  
[Comment utiliser Git avec Github ?](http://rogerdudler.github.io/git-guide/)  
[Comment créer un dépôt Git ?](https://help.github.com/articles/create-a-repo/)  
[Comment ajouter un dépôt distant Git ?](https://help.github.com/articles/adding-a-remote/)  
[Qu'est-ce qu'un modèle ?](https://docs.djangoproject.com/en/1.11/topics/db/models/)  
[Qu'est-ce qu'une vue ?](https://docs.djangoproject.com/en/1.11/topics/http/views/)  
[Qu'est-ce qu'un superutilisateur ?](https://docs.djangoproject.com/en/1.11/ref/django-admin/#createsuperuser)  
[Qu'est-ce qu'une migration ?](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-makemigrations)  
[Qu'est-ce qu'une migration ?](https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-migrate)  
[Qu'est-ce que SQLite ?](https://www.sqlite.org/about.html)  
[Analyse JSON Python : Un Guide Simple](https://www.makeuseof.com/tag/json-python-parsing-simple-guide/)  
[Comment sécuriser les clés API](https://medium.freecodecamp.org/how-to-securely-store-api-keys-4ff3ea19ebda)  
[Qu'est-ce que Python ?](https://www.python.org/doc/essays/blurb/)  
[Qu'est-ce que pip ?](https://en.wikipedia.org/wiki/Pip_(package_manager))  
[Qu'est-ce que virtualenv ?](https://virtualenv.pypa.io/en/stable/)  
[Meilleures pratiques pour virtualenv et git repo](http://libzx.so/main/learning/2016/03/13/best-practice-for-virtualenv-and-git-repos.html)  
[Qu'est-ce qu'une API ?](https://medium.freecodecamp.org/what-is-an-api-in-english-please-b880a3214a82)  
[Quels sont les points de terminaison de l'API ?](https://smartbear.com/learn/performance-monitoring/api-endpoints/)  
[Qu'est-ce que le Django REST Framework ?](http://www.django-rest-framework.org/)  
[Qu'est-ce que __init__.py ?](https://stackoverflow.com/a/448279/5513243)  
[Qu'est-ce qu'un sérialiseur ?](http://www.django-rest-framework.org/api-guide/serializers/)  
[Quelles sont les vues ?](https://docs.djangoproject.com/en/1.11/topics/http/views/)  
[Quelles sont les URLS ?](https://tutorial.djangogirls.org/en/django_urls/)  
[Qu'est-ce que JSON ?](https://www.w3schools.com/js/js_json_intro.asp)  
[Quelles sont les expressions régulières ?](https://www.tutorialspoint.com/python/python_reg_expressions.htm)  
[Que fait __init__.py ?](https://stackoverflow.com/questions/448271/what-is-init-py-for/448279#448279)  
[Qu'est-ce que REST ?](http://rest.elkstein.org/)  
[Qu'est-ce que Node.js ?](https://www.w3schools.com/nodejs/nodejs_intro.asp)  
[Qu'est-ce que NPM ?](https://www.w3schools.com/nodejs/nodejs_npm.asp)  
[Qu'est-ce qu'EmberJS ?](https://hacks.mozilla.org/2014/02/ember-js-what-it-is-and-why-we-need-to-care-about-it/)  
[Qu'est-ce qu'Ember CLI ?](https://ember-cli.com/)  
[Qu'est-ce qu'Ember-Data ?](https://github.com/emberjs/data)  
[Qu'est-ce qu'un modèle ?](https://guides.emberjs.com/release/models/)  
[Qu'est-ce qu'une route ?](https://guides.emberjs.com/release/routing/)  
[Qu'est-ce qu'un routeur ?](https://guides.emberjs.com/release/routing/defining-your-routes/)  
[Qu'est-ce qu'un modèle ?](https://guides.emberjs.com/release/templates/handlebars-basics/)  
[Qu'est-ce qu'un adaptateur ?](https://www.emberjs.com/api/ember-data/release/classes/DS.Adapter)  
[Qu'est-ce que le Django REST Framework JSON API ?](https://github.com/django-json-api/django-rest-framework-json-api)  
[Qu'est-ce que le format JSON API ?](http://jsonapi.org/format/#document-resource-object-identification)  
[Qu'est-ce que la notation par points ?](https://codeburst.io/javascript-quickie-dot-notation-vs-bracket-notation-333641c0f781)