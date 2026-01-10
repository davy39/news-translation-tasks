---
title: La méthode addEventListener() – Exemple de code pour l'écouteur d'événements
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T21:53:44.000Z'
originalURL: https://freecodecamp.org/news/javascript-addeventlistener-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/headway-F2KRf_QfCqw-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: La méthode addEventListener() – Exemple de code pour l'écouteur d'événements
  JavaScript
seo_desc: 'By Joe Liang

  The JavaScript addEventListener() method allows you to set up functions to be called
  when a specified event happens, such as when a user clicks a button. This tutorial
  shows you how you can implement addEventListener() in your code.

  ##Un...'
---

Par Joe Liang

La méthode JavaScript addEventListener() vous permet de configurer des fonctions à appeler lorsqu'un événement spécifié se produit, comme lorsqu'un utilisateur clique sur un bouton. Ce tutoriel vous montre comment implémenter addEventListener() dans votre code.

## Comprendre les événements et les gestionnaires d'événements

Les **événements** sont des actions qui se produisent lorsque l'utilisateur ou le navigateur manipule une page. Ils jouent un rôle important car ils peuvent faire changer dynamiquement les éléments d'une page web.

Par exemple, lorsque le navigateur a fini de charger un document, un événement `load` s'est produit. Si un utilisateur clique sur un bouton d'une page, un événement `click` s'est produit.

De nombreux événements peuvent se produire une fois, plusieurs fois ou jamais. Vous ne savez peut-être pas non plus quand un événement se produira, surtout s'il est généré par l'utilisateur.

Dans ces scénarios, vous avez besoin d'un **gestionnaire d'événements** pour détecter quand un événement se produit. Ainsi, vous pouvez configurer du code pour réagir aux événements au fur et à mesure qu'ils se produisent.

JavaScript fournit un gestionnaire d'événements sous la forme de la méthode `addEventListener()`. Ce gestionnaire peut être attaché à un élément HTML spécifique que vous souhaitez surveiller pour les événements, et l'élément peut avoir plus d'un gestionnaire attaché.

## Syntaxe de addEventListener()

Voici la syntaxe :

```js
cible.addEventListener(événement, fonction, useCapture)
```

* **cible** : l'élément HTML auquel vous souhaitez ajouter votre gestionnaire d'événements. Cet élément fait partie du Document Object Model (DOM) et vous pouvez apprendre [comment sélectionner un élément DOM](https://1000mileworld.com/dom-manipulation-using-javascript/#select).
* **événement** : une chaîne de caractères qui spécifie le nom de l'événement. Nous avons déjà mentionné les événements `load` et `click`. Pour les curieux, voici une liste complète des [événements HTML DOM](https://www.w3schools.com/jsref/dom_obj_event.asp).
* **fonction** : spécifie la fonction à exécuter lorsque l'événement est détecté. C'est la magie qui permet à vos pages web de changer dynamiquement.
* **useCapture** : une valeur booléenne facultative (true ou false) qui spécifie si l'événement doit être exécuté dans la [phase de capture ou de propagation](https://javascript.info/bubbling-and-capturing). Dans le cas d'éléments HTML imbriqués (comme une image `img` dans une `div`) avec des gestionnaires d'événements attachés, cette valeur détermine quel événement est exécuté en premier. Par défaut, elle est définie sur false, ce qui signifie que le gestionnaire d'événements HTML le plus interne est exécuté en premier (phase de propagation).

<h2>Exemple de code addEventListener()</h2>

%[https://codepen.io/1000mileworld/pen/JjGVRjw]

Voici un exemple simple que j'ai créé pour vous montrer `addEventListener()` en action.

Lorsque l'utilisateur clique sur le bouton, un message s'affiche. Un autre clic sur le bouton masque le message. Voici le JavaScript pertinent :

```js
let bouton = document.querySelector('#button');
let msg = document.querySelector('#message');

bouton.addEventListener('click', ()=>{
  msg.classList.toggle('reveal');
})
```

En suivant la syntaxe montrée précédemment pour `addEventListener()` :
* **cible** : élément HTML avec `id='button'`
* **fonction** : fonction anonyme (fléchée) qui configure le code nécessaire pour révéler/masquer le message
* **useCapture** : laissé à la valeur par défaut `false`

Ma fonction peut révéler/masquer le message en ajoutant/supprimant une classe CSS appelée "reveal" qui modifie la visibilité de l'élément message.

Bien sûr, dans votre code, n'hésitez pas à personnaliser cette fonction. Vous pouvez également remplacer la fonction anonyme par une fonction nommée de votre choix.

## Passer l'événement en tant que paramètre

Parfois, nous pouvons vouloir plus d'informations sur l'événement, comme quel élément a été cliqué. Dans cette situation, nous devons passer un paramètre d'événement à notre fonction.

Cet exemple montre comment vous pouvez obtenir l'id de l'élément :

```js
bouton.addEventListener('click', (e)=>{
  console.log(e.target.id)
})
```

Ici, le paramètre d'événement est une variable nommée `e`, mais elle peut facilement être appelée autre chose comme "event". Ce paramètre est un objet qui contient diverses informations sur l'événement, comme l'id de la cible.

Vous n'avez rien à faire de spécial et JavaScript sait automatiquement quoi faire lorsque vous passez un paramètre de cette manière à votre fonction.

## Supprimer les gestionnaires d'événements

Si, pour une raison quelconque, vous ne voulez plus qu'un gestionnaire d'événements s'active, voici comment le supprimer :

```js
cible.removeEventListener(événement, fonction, useCapture);
```

Les paramètres sont les mêmes que pour `addEventListener()`.

## C'est en forgeant qu'on devient forgeron

La meilleure façon de s'améliorer avec les gestionnaires d'événements est de pratiquer avec votre propre code.

Voici un [projet d'exemple](https://1000mileworld.com/Portfolio/Flex/flexPanels.html) que j'ai réalisé dans lequel j'ai utilisé des gestionnaires d'événements pour changer la couleur, la taille et la vitesse des bulles qui traversent l'arrière-plan d'une page web (vous devrez cliquer sur le panneau central pour révéler les contrôles).

Amusez-vous et allez créer quelque chose d'extraordinaire !

Pour plus de connaissances en développement web adaptées aux débutants, visitez mon blog à [1000 Mile World](https://1000mileworld.com/) et suivez-moi sur [Twitter](https://twitter.com/1000mileworld).