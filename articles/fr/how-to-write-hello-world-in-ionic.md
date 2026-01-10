---
title: Comment écrire "Hello, World!" dans Ionic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T19:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-hello-world-in-ionic
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c84740569d1a4ca32ac.jpg
tags:
- name: Ionic Framework
  slug: ionic
- name: toothbrush
  slug: toothbrush
seo_title: Comment écrire "Hello, World!" dans Ionic
seo_desc: 'This guide will teach you how to write a simple Hello World program in
  Ionic.

  Step 1: installation

  Install ionic, npm ,angular and cordova if not installed. [See first introduction
  for more information.]

  sudo apt-get install nodejs

  sudo apt-get insta...'
---

Ce guide vous apprendra à écrire un programme simple Hello World dans Ionic.

## Étape 1 : installation

Installez ionic, npm, angular et cordova si ce n'est pas déjà fait. [Voir la [première](https://guide.freecodecamp.org/ionic) introduction pour plus d'informations.]

```shell
sudo apt-get install nodejs
sudo apt-get install npm 
sudo npm install -g ionic cordova
```

## Étape 2 : Créer un dossier nommé helloworld

```shell
ionic start helloworld blank
```

Note : Comme il s'agit d'un petit projet, entrez Non ou N lorsque vous y êtes invité pendant l'exécution du programme.

## Étape 3 : Changer de répertoire pour helloworld [ceci est votre répertoire ionic]

```shell
cd helloworld
```

## Étape 4 : Ouvrir le dossier dans votre éditeur de texte.

Vous verrez divers fichiers et sous-dossiers.

Ne paniquez pas – ces fichiers sont générés automatiquement par npm pour vous. Allez simplement dans `src`->`page`->`home`->`home.html`.

### Format de fichier de base

```text
`home.html` est la page html où vous pouvez écrire la syntaxe html.<br/>

`home.scss` est la page css pour écrire la syntaxe css.<br/>

`home.ts` est la page typescript pour écrire le code typescript.
```

## Étape 6 : Supprimer le modèle et ajouter la syntaxe html comme montré ci-dessous

```html
 <ion-header>
  <ion-navbar>
    <ion-title>
      Projet Ionic
    </ion-title>
   </ion-navbar>
  </ion-header>

  <ion-content padding>
   <h2>Bonjour le monde</h2>
  </ion-content>
```

## Étape 7 : Sauvegarder le code et exécuter

```shell
ionic serve
```

Pour voir votre code en cours d'exécution, allez dans le navigateur et ouvrez localhost:8100 dans l'URL. C'est tout !

## Plus d'informations sur Ionic :

* [Cours complet sur Ionic (vidéo)](https://www.freecodecamp.org/news/ionic-full-course/)
* [Créer une application todo CRUD avec Ionic](https://www.freecodecamp.org/news/creating-a-crud-to-do-app-using-ionic-4/)