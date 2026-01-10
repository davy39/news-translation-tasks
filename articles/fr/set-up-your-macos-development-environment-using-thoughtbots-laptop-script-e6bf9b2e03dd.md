---
title: Configurer votre environnement de développement macOS à l'aide du script Laptop
  de Thoughtbot
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2018-02-08T15:12:22.000Z'
originalURL: https://freecodecamp.org/news/set-up-your-macos-development-environment-using-thoughtbots-laptop-script-e6bf9b2e03dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cNXpArTQUERq8nbe9nllqw.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Configurer votre environnement de développement macOS à l'aide du script
  Laptop de Thoughtbot
seo_desc: 'One of the things that may prevent us from changing or even thinking of
  changing our working environment is the necessity to do all the installations and
  the configurations that we have already set up for software development.

  Fortunately, there is a...'
---

L'une des choses qui peut nous empêcher de changer ou même de penser à changer notre environnement de travail est la nécessité de faire toutes les installations et les configurations que nous avons déjà mises en place pour le développement logiciel.

Heureusement, il existe un remède à cette *douleur*. *Laptop* est un script qui prépare votre machine macOS de travail pour le développement web et mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/TYlh5-0uZtwVDI1AstOGORoIqEBT5OIAyYVM align="left")

La configuration du script se compose de :

1. Outils macOS :
   
* [Homebrew](http://brew.sh/) pour gérer les bibliothèques du système d'exploitation.
   

2. Outils Unix :
   
* [Exuberant Ctags](http://ctags.sourceforge.net/) pour indexer les fichiers pour la complétion d'onglets vim
* [Git](https://git-scm.com/) pour le contrôle de version
* [OpenSSL](https://www.openssl.org/) pour la sécurité de la couche transport (TLS)
* [RCM](https://github.com/thoughtbot/rcm) pour gérer les fichiers dotfiles personnels et professionnels
* [The Silver Searcher](https://github.com/ggreer/the_silver_searcher) pour trouver des choses dans les fichiers
* [Tmux](http://tmux.github.io/) pour sauvegarder l'état des projets et basculer entre les projets
* [Watchman](https://facebook.github.io/watchman/) pour surveiller les événements du système de fichiers
* [Zsh](http://www.zsh.org/) comme votre shell

3. Outils Heroku :
   
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) et [Parity](https://github.com/thoughtbot/parity) pour interagir avec l'API Heroku

4. Outils GitHub :
   
* [Hub](http://hub.github.com/) pour interagir avec l'API GitHub

5. Outils d'image :
   
* [ImageMagick](http://www.imagemagick.org/) pour rogner et redimensionner les images

6. Outils de test :
   
* [Qt 5](http://qt-project.org/) pour les tests JavaScript sans tête via [Capybara Webkit](https://github.com/thoughtbot/capybara-webkit)

7. Langages de programmation, gestionnaires de paquets et configuration :
   
* [ASDF](https://github.com/asdf-vm/asdf) pour gérer les versions des langages de programmation
* [Bundler](http://bundler.io/) pour gérer les bibliothèques Ruby
* [Node.js](http://nodejs.org/) et [NPM](https://www.npmjs.org/), pour exécuter des applications et installer des paquets JavaScript
* [Ruby](https://www.ruby-lang.org/en/) stable pour écrire du code général
* [Yarn](https://yarnpkg.com/en/) pour gérer les paquets JavaScript

8. Bases de données :
   
* [Postgres](http://www.postgresql.org/) pour stocker des données relationnelles
* [Redis](http://redis.io/) pour stocker des données clé-valeur

Son installation est assez simple et peut être faite très rapidement.

Tout d'abord, vous devez télécharger le script :

```python
curl --remote-name https://raw.githubusercontent.com/thoughtbot/laptop/master/mac
```

Vous devriez examiner le script avant de l'exécuter :

```python
less mac
```

Ensuite, vous pouvez exécuter le script téléchargé :

```python
sh mac 2>&1 | tee ~/laptop.log
```

Enfin, vous pouvez examiner le journal :

```python
less ~/laptop.log
```

Cela devrait prendre moins de 15 minutes pour s'installer (selon votre machine).

Les versions de macOS qui sont supportées au moment de la rédaction de cet article sont :

* macOS Mavericks (10.9)
   
* macOS Yosemite (10.10)
   
* macOS El Capitan (10.11)
   
* macOS Sierra (10.12)

Selon la [description](https://github.com/thoughtbot/laptop) de Laptop, les versions plus anciennes de macOS peuvent fonctionner mais ne sont pas régulièrement testées.

Laptop est un projet open source, initié et maintenu par [Thoughtbot](https://thoughtbot.com/?utm_source=github). Vous pouvez consulter plus d'informations à ce sujet et sur sa mise en œuvre, et avoir également l'opportunité de contribuer en visitant sa page GitHub [page](https://github.com/thoughtbot/laptop).

*Cet article a été initialement publié sur mon blog,* [*FatosMorina.com*](http://www.fatosmorina.com/set-macos-development-environment-using-thoughtbots-laptop-script/)