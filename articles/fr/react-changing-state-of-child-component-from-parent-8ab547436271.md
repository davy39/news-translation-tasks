---
title: Comment changer l'état d'un composant enfant depuis son parent dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T19:12:01.000Z'
originalURL: https://freecodecamp.org/news/react-changing-state-of-child-component-from-parent-8ab547436271
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Zpf89dyMkJnfprjM
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment changer l'état d'un composant enfant depuis son parent dans React
seo_desc: 'By Johny Thomas

  We will be building a simple React app which shows the real name of a superhero
  on a button click.

  Let’s get started.

  First, we will create a Superhero component with a name attribute in state. This
  component will render that name fir...'
---

Par Johny Thomas

Nous allons créer une application React simple qui affiche le vrai nom d'un super-héros lors d'un clic sur un bouton.

Commençons.

Tout d'abord, nous allons créer un composant `Superhero` avec un attribut `name` dans l'état. Ce composant affichera d'abord ce `name`.

![Image](https://cdn-media-1.freecodecamp.org/images/dXk6uX7LQOfLuMWqTAqOZSd7obn-GESaMUkA)

Maintenant, créons une fonction `changeName()` dans le composant `Superhero`. Cette fonction changera le nom dans l'état en le vrai nom du super-héros.

![Image](https://cdn-media-1.freecodecamp.org/images/-3-r39-jq60PNryomLCF7ShV4sHJEOhBBDtl)

Nous avons maintenant le composant `Superhero` qui affiche le nom du super-héros et une fonction qui met à jour le nom en son vrai nom.

Le composant Superhero complet ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yHRO4tad52gX20O9uRC38b-oSgiRe5VK9f6m)

Maintenant, créons le composant `App` qui rendra ce composant `Superhero` et un bouton. Lorsque nous cliquons sur le bouton, il affiche le vrai nom du super-héros.

![Image](https://cdn-media-1.freecodecamp.org/images/vlplStkM5jX8jKzIgUuOZB3ezux7mORUNvMy)

Nous avons ajouté une fonction `handleClick()` qui sera appelée lorsque l'utilisateur clique sur le bouton. Nous devons trouver un moyen de mettre à jour l'état du composant enfant, c'est-à-dire le composant `Superhero`.

Nous avons créé une fonction `changeName()` dans le composant `Superhero`. Cette fonction affichera le vrai nom du super-héros. Si nous pouvons appeler cette fonction depuis le composant `App`, notre travail est terminé. Nous allons donc appeler cette fonction.

C'est là que les **refs** viennent à notre secours.

Créons une ref du composant `Superhero` dans le composant `App`. Voici le code pour faire cela.

![Image](https://cdn-media-1.freecodecamp.org/images/gYY7kDmcNbMT1flktY70lOgXYmqRZAjRErUN)

Ici, nous avons créé une ref en utilisant la méthode `React.createRef()` et attaché la ref au composant `Superhero` en utilisant l'attribut `ref`.

Maintenant, nous pourrons référencer le nœud `Superhero` en utilisant `this.superheroElement.current`. Nous pourrons également appeler la fonction `changeName()` dans le composant `Superhero` en utilisant `this.superheroElement.current.changeName()`.

Mettons à jour notre fonction `handleClick()` dans notre composant `App` pour appeler la fonction `changeName()`.

Notre fonction `handleClick()` ressemblera à ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/Qx7hBSPn7YlzdtGpDSC7Dcr4bP6wR5CKGFOr)

Vous pouvez consulter le code complet dans le sandbox ci-dessous.

[**CodeSandbox**](https://codesandbox.io/embed/4r16r1oxj4)  
[_CodeSandbox est un éditeur en ligne conçu pour les applications web._codesandbox.io](https://codesandbox.io/embed/4r16r1oxj4)

Maintenant, nous avons appris comment mettre à jour l'état d'un composant enfant depuis un composant parent 😊. J'espère que cela a été utile.