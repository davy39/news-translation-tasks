---
title: Comment coller des images directement dans un article dans Draft.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T18:50:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-paste-images-directly-into-an-article-in-draft-js-e23ed3e0c834
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4SnkY7WxnP785isausYzEg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment coller des images directement dans un article dans Draft.js
seo_desc: 'By Andrey Semin

  The problem

  For some of you this may be a surprise, but Draft.js doesn’t support images out
  of the box. To be able to display images in the Editor, you need to install and
  configure [draft-js-image-plugin](https://www.draft-js-plugins...'
---

Par Andrey Semin

### Le problème

Pour certains d'entre vous, cela peut être une surprise, mais Draft.js ne supporte pas les images directement. Pour pouvoir afficher des images dans l'éditeur, vous devez installer et configurer `[draft-js-image-plugin](https://www.draft-js-plugins.com/plugin/image)` (nous n'aborderons pas ce sujet ici, car sa documentation est assez complète). Cela signifie également qu'il n'y a pas de support pour une fonctionnalité aussi courante que le collage d'images (ou de tout autre fichier) dans l'éditeur. Le but de cet article est de montrer comment vous pouvez ajouter un support de base pour coller des fichiers (nous nous concentrerons sur les images).

### Solution

Commençons par lire la [documentation de Draft.js](https://draftjs.org/docs/getting-started). Il s'avère qu'il existe une propriété appelée `[handlePastedFiles](https://draftjs.org/docs/api-reference-editor#handlepastedfiles)` dans l'éditeur. Elle reçoit un tableau de fichiers et est censée vous offrir la possibilité de manipuler les fichiers lors d'une action de collage. Cependant, les choses ne fonctionnent pas exactement de cette manière.

> _Il y a un problème : lorsque vous essayez de coller plusieurs fichiers dans l'éditeur, vous recevrez un tableau ne contenant qu'un seul d'entre eux. C'est un problème connu et une [issue](https://github.com/facebook/draft-js/issues/1955) a été ouverte dans le [dépôt Draft.js](https://github.com/facebook/draft-js) le 11 décembre 2018. Ce qui signifie qu'elle est assez récente mais toujours ennuyeuse._

Maintenant, nous devons définir quels types de fichiers nous allons gérer. Pour les images, ce sont `image/png`, `image/jpeg` et `image/gif`.

Maintenant que nous savons que nous allons travailler uniquement avec des images, il est temps de lire les données du fichier. Pour cela, nous allons implémenter une fonction appelée `readImageAsDataUrl` et utiliser l'API `[FileReader](https://developer.mozilla.org/en-US/docs/Web/API/FileReader)` et la méthode `[readAsDataUrl](https://developer.mozilla.org/en-US/docs/Web/API/FileReader/readAsDataURL)` en particulier. Cette combinaison d'étapes nous permet de lire le fichier et son contenu en encodage base64, qui peut ensuite être utilisé comme valeur de l'attribut `src` de l'élément `img`.

Maintenant que nous avons notre image encodée en base64, tout ce que nous avons à faire est de créer une entité Draft.js et de mettre à jour l'état de l'éditeur pour contenir cette entité.

Nous pouvons commencer par utiliser la méthode `[create](https://draftjs.org/docs/api-reference-entity#create)` du module `Entity` qui fait partie de Draft.js. (Gardez à l'esprit, cependant, que la documentation indique que `Entity.create` est obsolète et que les développeurs devraient utiliser `contentState.createEntity`. Cette dernière ne fonctionnait pas au moment où cet article a été écrit. Nous allons donc continuer avec l'utilisation de `Entity` mais nous suivrons cette évolution).

Nous devons fournir 3 arguments ici :

* le premier est le type d'entité que nous allons créer (`image` dans notre cas)
* le second est la mutabilité de l'entité (`IMMUTABLE` signifie que nous ne pouvons pas éditer le contenu du texte contenant cette entité. Si nous essayons de supprimer quelque chose, toute la plage de texte serait supprimée)
* et le troisième est un objet optionnel contenant toutes les données que vous souhaitez stocker avec une entité (dans notre cas, il s'agit de `src` qui est requis par `draft-js-image-plugin`).

En retour, nous obtenons une clé avec laquelle nous pouvons adresser cette entité dans l'état de l'éditeur. Maintenant, nous devons utiliser cette clé pour insérer un bloc dans l'éditeur et attacher cette entité exacte à ce bloc. Nous utiliserons la fonction `insertAtomicBlock` du module `AtomicBlockUtils` de Draft.js. Nous devons passer l'état actuel de l'éditeur, la clé de l'entité et un caractère (qui ne doit pas être une chaîne vide, c'est pourquoi nous utilisons un espace unique) et nous obtiendrons un nouvel état de l'éditeur !

Maintenant que tout est prêt, combinons tout cela et jetons un coup d'œil à notre fonction `handlePastedFiles` :

Voilà ! Maintenant nous pouvons coller l'image dans l'éditeur Draft.js en appuyant simplement sur CTRL+V. Vous pouvez étendre cette fonctionnalité de la manière que vous souhaitez ! Par exemple, nous pouvons permettre à nos utilisateurs de changer la taille des images avec une interface utilisateur élégante.

Si vous avez lu cet article jusqu'au bout, vous pourriez également vouloir consulter [mon précédent article](https://hackernoon.com/draft-js-how-to-remove-formatting-of-the-text-cd191866d9ad) sur l'enchantement de Draft.js. Vous pourriez vouloir l'appliquer à votre projet également.