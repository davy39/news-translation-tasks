---
title: Voici comment optimiser la structure de l'état de votre application React avec
  Redux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T12:19:37.000Z'
originalURL: https://freecodecamp.org/news/optimising-the-state-shape-of-your-react-app-with-redux-3a280e6ef436
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MYp1pEZVIvemp_Af2P34FQ.jpeg
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
seo_title: Voici comment optimiser la structure de l'état de votre application React
  avec Redux
seo_desc: 'By Ivan Pilot

  Using Redux to manage the entire state of you app is one thing. But making sure
  the structure of your state is optimal so that your code is maintainable and efficient
  is an entirely new ball game!


  _Photo by [Unsplash](https://unsplash....'
---

Par Ivan Pilot

Utiliser Redux pour gérer l'état complet de votre application est une chose. Mais s'assurer que la structure de votre état est optimale pour que votre code soit maintenable et efficace est une tout autre paire de manches !

![Image](https://cdn-media-1.freecodecamp.org/images/1*MYp1pEZVIvemp_Af2P34FQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/JuFcQxgCXwA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Samuel Zeller</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Gérer la structure de l'état (state shape) de votre application est absolument fondamental. À mesure que votre application grandit, si la structure de votre état n'est pas bien organisée, sa gestion peut rapidement devenir complexe et même ralentir la réactivité de votre application.

Si vous utilisez React comme framework front-end, il y a de fortes chances que vous utilisiez Redux pour gérer l'état de votre application. Dans ce cas, vous implémenterez un ou plusieurs reducers pour modifier l'état de votre application chaque fois qu'une action est déclenchée en réponse aux actions des utilisateurs. Voyons ci-dessous comment passer d'une structure d'état initiale inefficace à une structure très performante.

### Approche initiale de la structure de l'état

Supposons que nous écrivions une application où les utilisateurs peuvent publier des tweets, et chaque tweet a des commentaires. Supposons également que les tweets puissent être organisés par sujets ou fils de discussion (threads). Une structure d'état basique et inefficace serait la suivante :

Comme vous pouvez le voir ci-dessus, nous avons une structure imbriquée complexe. Cette structure d'état s'avère assez inefficace pour plusieurs raisons :

* Elle est profondément imbriquée, donc modifier l'état pour mettre à jour une propriété d'un tweet oblige le développeur à écrire une quantité importante de code dans le reducer.
* Le tableau `tweets` fait deux choses : il contient les données (c'est-à-dire l'objet `tweet` individuel) et ordonne les tweets puisqu'ils sont à l'intérieur d'un tableau.
* Dans cette situation, les tableaux sont inefficaces. Imaginez que vous ayez 50 000 tweets dans un fil. Trouver le tweet approprié à l'intérieur du tableau prendra du temps. Le temps de recherche à l'intérieur d'un tableau est de O(n) car l'ordinateur doit parcourir toute la liste des éléments jusqu'à ce qu'il trouve le bon.
* Notez que pour les besoins de l'exemple, je n'ai même pas inclus les commentaires liés à chaque `tweet` dans cette structure ci-dessus, car cela aurait été encore plus désordonné.

N'utilisez pas de tableaux pour contenir des objets complexes. Comme nous le verrons plus tard, le seul intérêt d'utiliser des tableaux dans notre état est d'ordonner les éléments. C'est parce que, contrairement aux tableaux, nous ne pouvons pas compter sur les objets pour ordonner les éléments qu'ils contiennent.

### Remplacer les tableaux par des objets

Une première amélioration simple consisterait à utiliser des objets au lieu de tableaux. En reprenant notre exemple précédent et en nous concentrant, pour l'instant, uniquement sur le tableau `tweets`, nous pourrions facilement le modifier comme ceci :

Nous avons modifié le tableau `tweets` précédent et séparé le travail qu'il devait faire en :

1. Créant un objet `byId` dont le rôle est uniquement de contenir les tweets individuels
2. Créant un tableau `allIds` dont le rôle est de trier les tweets — mais ici, nous pouvons simplement mettre l'id de chaque tweet au lieu de l'objet `tweet` complet.

La structure actuelle est déjà beaucoup plus efficace que la première. Pour trouver un tweet, nous allons maintenant le chercher à travers un objet plutôt qu'un tableau. Le temps de recherche à travers un objet est un temps constant, c'est-à-dire O(1), ce qui est une grande amélioration par rapport à O(n). De plus, nous ne nous soucions plus de la position de chaque tweet à l'intérieur de l'objet `byId`. Le tableau `allIds` est là pour trier les tweets, et il est maintenant beaucoup plus simple de travailler avec un tableau de base comme `allIds`.

### Inclure des commentaires pour chaque tweet

Sans rendre notre code plus complexe, nous pouvons maintenant ajouter les commentaires qui appartiendraient à chaque tweet. Une méthode d'implémentation serait la suivante :

Structurer notre état de cette façon s'avère beaucoup plus efficace par rapport au premier exemple que nous avons utilisé. À l'intérieur de chaque objet tweet, nous ne référençons que les commentaires qui lui appartiennent via un tableau d'identifiants de commentaires. Ailleurs, nous avons un objet `comments` à l'intérieur duquel nous pouvons récupérer des informations sur chaque commentaire.

Nous avons maintenant une structure plus "aplatie" sur laquelle nous pouvons travailler efficacement. La mise à jour de cette structure d'état nécessiterait une petite quantité de code à l'intérieur de nos reducers. Notre code est maintenant facilement maintenable, et nous avons réduit les risques de faire des erreurs.

### Récapitulatif

Voyons quel serait le résultat final par rapport à notre approche initiale.

Contrairement à la première approche, où nous mélangions tableaux et objets, rendant l'état difficile et pénible à modifier et à maintenir, cette approche finale est maintenant facile à utiliser. Notre code est facilement maintenable et nos opérations de recherche sont ultra-rapides. C'est clairement une victoire !

Considérons quelques situations pour voir ce qui devrait être fait lors de la modification de certains éléments :

#### Ajouter un tweet

* Créer un nouvel objet `tweet` dans l'objet `byId` de l'objet `tweets`
* Ajouter l'id du nouveau tweet au tableau `allIds` de l'objet `tweets`
* Ajouter l'id du nouveau tweet au tableau `tweets` à l'intérieur de l'objet `thread` approprié

#### Modifier un tweet

* Trouver l'objet `tweet` sélectionné par son id à l'intérieur de l'objet `byId` de l'objet `tweets` et le mettre à jour

#### Supprimer un tweet

* Trouver l'objet `tweet` sélectionné par son id à l'intérieur de l'objet `byId` de l'objet `tweets` et le supprimer
* Supprimer l'id du tweet à l'intérieur du tableau `allIds` de l'objet `tweets`
* Supprimer l'id du tweet à l'intérieur du tableau `tweets` de l'objet `thread` approprié

#### Ajouter un commentaire

* Créer un nouvel objet `comment` dans l'objet `byId` de l'objet `comments`
* Ajouter l'id du nouveau commentaire au tableau `allIds` de l'objet `comments`
* Ajouter l'id du nouveau commentaire au tableau `comments` à l'intérieur de l'objet `tweet` approprié

#### Modifier un commentaire

* Trouver l'objet `comment` sélectionné par son id à l'intérieur de l'objet `byId` de l'objet `comments` et le mettre à jour

### Sélecteurs

Une façon de voir les sélecteurs est de faire un parallèle avec les getters et setters. Dispatch est comme un setter puisqu'il modifie l'état, tandis qu'un sélecteur est comme un getter puisqu'il récupère des données.

Vous utiliserez généralement des sélecteurs au sein de vos composants conteneurs lors du mappage de l'état aux props avec `mapStateToProps`. Supposons (comme indiqué dans notre exemple) que chaque tweet possède une propriété `isEditable` qui est soit `true` soit `false`, et qu'un seul tweet à la fois peut être modifiable. Si vous souhaitez récupérer le tweet modifiable, vous pouvez écrire un sélecteur comme celui ci-dessous :

Je n'ai fourni qu'un seul exemple, mais vous pouvez écrire autant de sélecteurs que nécessaire en fonction des données que vous souhaitez récupérer.

De plus, et comme recommandé par Dan Abramov, il est préférable d'écrire vos sélecteurs dans le même fichier que votre reducer. Cela prend tout son sens, surtout si vous les considérez comme des getters/setters. De plus, vous pouvez également vous référer à la [documentation](https://redux.js.org/docs/recipes/StructuringReducers.html) de Redux qui fournit des informations détaillées.

Amusez-vous bien en implémentant Redux !

Santé !