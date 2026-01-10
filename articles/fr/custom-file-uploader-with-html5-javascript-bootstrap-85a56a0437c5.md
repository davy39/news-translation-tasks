---
title: Comment créer un téléchargeur de fichiers personnalisé avec HTML5, JavaScript
  et Bootstrap
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-07T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/custom-file-uploader-with-html5-javascript-bootstrap-85a56a0437c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B6zah6pnLHvaYJ1Gppp-hQ.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment créer un téléchargeur de fichiers personnalisé avec HTML5, JavaScript
  et Bootstrap
seo_desc: 'By Prashant Yadav

  In this short article, we’ll learn how to create custom file uploader with JQuery,
  ES6, and Bootstrap4.

  We will create a file uploader with a custom design and an option to preview selected
  files and remove them.

  Support me by readi...'
---

Par Prashant Yadav

Dans cet article court, nous allons apprendre comment créer un téléchargeur de fichiers personnalisé avec JQuery, [ES6](https://learnersbucket.com/tutorials/es6/es6-intro), et Bootstrap4.

Nous allons créer un téléchargeur de fichiers avec un design personnalisé et une option pour prévisualiser les fichiers sélectionnés et les supprimer.

_Soutenez-moi en lisant cet article [ici](https://learnersbucket.com/examples/bootstrap4/custom-fileuploader-in-javascript/)._

### Démo

Consultez la démonstration en direct [ici](https://codepen.io/Learnersbucket/pen/drWENz).

### Implémentation

* Nous allons utiliser le téléchargeur de fichiers HTML5 pour télécharger les fichiers.
* Ensuite, avec l'aide de la popover de Bootstrap, nous allons prévisualiser les fichiers sélectionnés.
* Lors de la prévisualisation des fichiers, nous allons fournir une option pour supprimer le fichier sélectionné.
* Comme JQuery est l'une des dépendances pour la popover de Bootstrap, nous allons l'utiliser pour faciliter notre travail.

### Dépendances

### Disposition HTML pour le téléchargeur de fichiers

Explication

* Nous avons créé un conteneur nommé `custom-file-picker`.
* Dans celui-ci, nous avons notre téléchargement de fichiers personnalisé `picture-container` et notre prévisualisateur de popover `popover-container`.
* Chaque sélecteur de fichiers a un identifiant unique `a8755cf0-f4d1-6376-ee21-a6defd1e7c08` et sa popover correspondante fait référence à cet identifiant `data-target="a8755cf0-f4d1-6376-ee21-a6defd1e7c08"` pour prévisualiser les fichiers.

### Stylisation de nos composants

### Gestion de la fonctionnalité

Maintenant que nous avons stylisé nos composants, il est temps de gérer la fonctionnalité. Nous allons utiliser Jquery avec [ES6](https://learnersbucket.com/tutorials/es6/es6-intro) pour simplifier les choses.

### Stockage des fichiers

Nous allons créer une variable globale pour stocker les fichiers.

Nous allons utiliser cette variable pour stocker tous les fichiers du sélecteur de fichiers correspondant à l'aide de son identifiant.

Maintenant, nous allons créer une fonction qui gérera le stockage du fichier et l'affichage du nombre de fichiers. Cette fonction prendra `id` et `tableau de fichiers` en entrée.

`$(`[data-id="${id}"] > .file-total-viewer`).text(files.length); mettra à jour le nombre de fichiers dans le prévisualisateur de popover.

### Gestion de la sélection de fichiers

Nous avons notre fonction prête à mettre à jour le nombre et à stocker les fichiers. Nous allons simplement passer les données à cette fonction une fois que les fichiers sont sélectionnés ou modifiés.

Une fois les fichiers sélectionnés, nous afficherons l'animation complète avec SVG pour notifier les utilisateurs que les fichiers ont été modifiés.

Maintenant, nous avons notre fichier stocké et le nombre visible. Créons le prévisualisateur de fichiers avec une popover Bootstrap.

Bootstrap nous fournit une méthode pour générer dynamiquement le contenu de la popover. Nous attachons donc la popover à `[data-toggle="popover"]`. En savoir plus à ce sujet [ici](https://getbootstrap.com/docs/4.1/components/popovers/).

#### Comment cela fonctionne

* Chaque fois qu'une popup est sur le point de s'afficher, elle utilisera son identifiant `[data-target]` et récupérera tous les fichiers de `fileStorage`.
* S'il y a des fichiers, alors affichez ces fichiers avec le bouton de suppression.
* S'il n'y a pas de fichier, alors affichez un message.

Maintenant, si vous avez plusieurs téléchargeurs de fichiers et que vous souhaitez qu'une seule popover soit ouverte à la fois, ajoutez le code suivant.

Si vous sélectionnez un fichier et cliquez sur `view`, vous devriez pouvoir le visualiser. La dernière chose que nous ferons est de gérer la suppression des fichiers.

### Suppression du fichier

Nous avons fourni l'identifiant du sélecteur de fichiers au bouton de suppression via `data-target` et le nom du fichier via `data-name`. Chaque fois que l'icône de suppression est cliquée, nous utiliserons ces valeurs pour supprimer les fichiers.

Comme nous générons dynamiquement le contenu de la popover et qu'il n'existe pas déjà dans le DOM, nous ne pouvons pas lui assigner un événement. Nous devons donc utiliser une solution de contournement en assignant un événement sur le DOM et en vérifiant si l'icône de suppression est cliquée avec `$(document).on('click', '.popover-content-remove', function (e) {});`.

#### Comment cela fonctionne

* Une fois l'icône de suppression cliquée, nous demanderons une confirmation à l'utilisateur.
* Si l'utilisateur souhaite continuer, nous récupérons l'identifiant et le nom assignés au bouton de suppression via `data-target` et `data-name`.
* Nous supprimons ce fichier particulier en utilisant la méthode filter().
* Une fois le fichier supprimé du tableau, nous mettons à jour son nombre en passant la valeur à notre fonction d'aide `storeFile(id, newArr);`.
* De plus, nous supprimons l'élément de la popover. Si le tableau est vide, alors affichez un message.

Note : Vous devez fournir un identifiant unique à chaque sélecteur de fichiers et à son prévisualisateur de popover.

### Code complet

Si vous avez aimé cet article, donnez-lui 50+ ? et partagez-le ! Si vous avez des questions à ce sujet, n'hésitez pas à me les poser.

_Pour plus d'articles comme celui-ci et des solutions algorithmiques en Javascript, suivez-moi sur_ [**Twitter**](https://twitter.com/LearnersBucket)_._ J'écris sur [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), React, Nodejs, [Structures de données](https://learnersbucket.com/tutorials/topics/data-structures/), et [Algorithmes](https://learnersbucket.com/examples/topics/algorithms/) sur [_learnersbucket.com_](https://learnersbucket.com/)_.