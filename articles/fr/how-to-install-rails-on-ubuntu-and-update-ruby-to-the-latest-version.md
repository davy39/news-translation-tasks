---
title: Comment installer Rails sur Ubuntu et mettre à jour Ruby vers la dernière version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-rails-on-ubuntu-and-update-ruby-to-the-latest-version
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Slice-3-1-.jpg
tags:
- name: Rails
  slug: rails
- name: Ruby
  slug: ruby
- name: Ubuntu
  slug: ubuntu
seo_title: Comment installer Rails sur Ubuntu et mettre à jour Ruby vers la dernière
  version
seo_desc: 'By Adebola Adeniran

  A couple of months ago, when I learned Ruby-on-Rails for the first time, I had to
  work on a collaborative project with a coding partner. We kept running into issues,
  as he had a different version of Rails and Buby setup for the pr...'
---

Par Adebola Adeniran

Il y a quelques mois, lorsque j'ai appris Ruby-on-Rails pour la première fois, j'ai dû travailler sur un projet collaboratif avec un partenaire de codage. Nous avons rencontré des problèmes, car il avait une version différente de Rails et Ruby configurée pour le projet. Je ne comprenais pas comment installer les versions nécessaires au projet. 

Voici le guide que j'aurais souhaité avoir. Il vous montre également comment changer la version de Ruby ou Rails que vous utilisez, en fonction des projets sur lesquels vous travaillez.

Tout d'abord, installons la dernière version de Ruby. Pour cela, nous devons installer un package appelé **RVM - Ruby version manager.** Ce package nous permet d'installer N'IMPORTE QUELLE version de Ruby sur notre machine Ubuntu et nous permet de basculer entre les versions.

Tout le code ici sera exécuté en utilisant le CLI/terminal d'Ubuntu.

## Installation de RVM

1. Tout d'abord, nous devons installer un prérequis. Ouvrez votre terminal Ubuntu et tapez la commande :

```
sudo apt-get install software-properties-common

```

Ensuite, nous devons ajouter le **PPA (Personal Package Archive)**. Un PPA est un moyen d'obtenir des fichiers distribués par des développeurs qui ne sont pas encore disponibles dans le magasin officiel de packages/applications d'Ubuntu. 

C'est aussi un moyen pour les développeurs de distribuer les dernières versions de leurs logiciels tout en attendant qu'Ubuntu les teste et les publie dans le magasin officiel.

```
sudo apt-add-repository -y ppa:rael-gc/rvm
```

La commande ci-dessus ajoute le PPA à la liste des emplacements depuis lesquels nous pouvons télécharger des packages sur notre machine Ubuntu.

Ensuite, actualisons notre liste de packages en exécutant :

`sudo apt-get update`

Enfin, installons RVM lui-même.

```
sudo apt-get install rvm
```

Redémarrez maintenant votre terminal pour que vos modifications prennent effet. Ensuite, tapez `rvm version` et appuyez sur `enter` pour vérifier que rvm est installé. Vous devriez obtenir une réponse comme celle-ci :

`rvm 1.29.10 (manuel) par Michal Papis, Piotr Kuczynski, Wayne E. Seguin [[https://rvm.io](https://rvm.io)]`

## Installation de Ruby 

Maintenant, nous pouvons installer la dernière version de Ruby, qui est la 2.7.1. Exécutez la commande `rvm install 2.7.1`. Alternativement, vous pouvez exécuter `rvm install ruby` qui installera la dernière version stable (cela installera la v2.7.0).  
  
Pour voir quelles versions de Ruby vous avez installées, exécutez `rvm ls`. Pour basculer entre les versions de Ruby, exécutez `rvm use <version_number>` (par exemple, `rvm use 2.7.1`).

## Installation de Ruby-on-Rails

La dernière version de Rails est la 6.03. Rails est simplement un gem Ruby, et avec Ruby installé, nous pouvons installer Rails ! Exécutez `gem install rails` pour installer la dernière version de Rails.  
  
Enfin, pour vérifier que tout s'est bien passé, exécutez `rails -v`. Vous devriez obtenir `Rails 6.0.3.2` en retour, car c'est la dernière version au moment de la publication de cet article.   
  
Vous pouvez maintenant démarrer votre premier projet Rails en tapant `rails new myapp`.

Hé, vous êtes maintenant sur Rails !