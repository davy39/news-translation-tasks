---
title: Qu'est-ce que le Document Object Model, et pourquoi vous devriez savoir comment
  l'utiliser.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-07T21:16:41.000Z'
originalURL: https://freecodecamp.org/news/whats-the-document-object-model-and-why-you-should-know-how-to-use-it-1a2d0bc5429d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q8vHD5jcU_xZNqIgs-J-Pg.jpeg
tags:
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Qu'est-ce que le Document Object Model, et pourquoi vous devriez savoir
  comment l'utiliser.
seo_desc: 'By Leonardo Maldonado

  So, you’ve studied HTML, you’ve created your first tags, learned about CSS, made
  beautiful forms, amazing buttons, responsive pages and have started to show everyone
  how amazing all that was.

  But then you decide that you want to...'
---

Par Leonardo Maldonado

Alors, vous avez étudié le HTML, vous avez créé vos premières balises, appris le CSS, fait de beaux formulaires, des boutons incroyables, des pages réactives et avez commencé à montrer à tout le monde à quel point tout cela était génial.

Mais ensuite, vous décidez que vous voulez franchir une nouvelle étape dans votre apprentissage, et vous commencez à vous demander : « Comment puis-je ajouter une animation à ma page ? J'aimerais que ce bouton fasse une animation sur ma page lorsque je clique dessus ! »

Eh bien, c'est là que le DOM intervient pour résoudre votre problème. Vous en avez probablement beaucoup entendu parler, mais vous ne savez peut-être pas encore ce que c'est et quels problèmes il résout. Alors, creusons un peu.

### Alors, qu'est-ce que le DOM ?

Connaissez-vous toutes ces animations cool que vous voyez autour de vous, qui vous font penser : « Wow, j'aimerais pouvoir faire quelque chose comme ça » ? Toutes ces animations sont réalisées en manipulant le DOM. Je vais maintenant vous expliquer comment commencer à le manipuler et à rendre vos sites web plus cool.

Le DOM (Document Object Model) est une interface qui représente comment vos documents HTML et XML sont lus par le navigateur. Il permet à un langage (JavaScript) de manipuler, structurer et styliser votre site web. Après que le navigateur a lu votre document HTML, il crée un arbre représentationnel appelé Document Object Model et définit comment cet arbre peut être accessible.

### Avantages

En manipulant le DOM, vous avez des possibilités infinies. Vous pouvez créer des applications qui mettent à jour les données de la page sans avoir besoin de rafraîchir. De plus, vous pouvez créer des applications personnalisables par l'utilisateur et modifier la mise en page de la page sans rafraîchir. Vous pouvez glisser, déplacer et supprimer des éléments.

Comme je l'ai dit, vous avez des possibilités infinies — il vous suffit d'utiliser votre créativité.

### Représentation par le navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/3n6SPcMH0mmG6cFeB3SJBEA-9Yyfgp3xYZ7u)
_L'arbre représentationnel que le navigateur crée après avoir lu votre document._

Dans l'image ci-dessus, nous pouvons voir l'arbre représentationnel et comment il est créé par le navigateur. Dans cet exemple, nous avons quatre éléments importants que vous allez voir souvent :

1. **Document** : Il traite tous les documents _HTML_.
2. **Elements** : Toutes les balises qui sont à l'intérieur de votre _HTML_ ou _XML_ deviennent un élément DOM.
3. **Text** : Tout le contenu des balises.
4. **Attributes** : Tous les attributs d'un élément _HTML_ spécifique. Dans l'image, l'attribut _class="hero"_ est un attribut de l'élément _<p>_.

### Manipuler le DOM

Maintenant, nous arrivons à la meilleure partie : commencer à manipuler le DOM. D'abord, nous allons créer un élément HTML comme exemple pour voir quelques méthodes et comment les événements fonctionnent.

```
<!DOCTYPE html>  <html lang="pt-br">  <head>      <meta charset="UTF-8">      <meta name="viewport" content="width=device-width, initial-scale=1.0">      <meta http-equiv="X-UA-Compatible" content="ie=edge">      <title>Comprendre le DOM (Document Object Model)</title>  </head>  <body>      <div class="container">          <h1><time>00:00:00</time></h1>          <button id="start">Start</button>          <button id="stop">Stop</button>          <button id="reset">Reset</button>      </div>  </body>  </html>
```

Très simple, n'est-ce pas ? Maintenant, nous allons en apprendre davantage sur les méthodes DOM : comment obtenir nos éléments et commencer à les manipuler.

### Méthodes

Le DOM a beaucoup de méthodes. Elles sont la connexion entre nos nœuds (éléments) et les événements, quelque chose que nous allons apprendre plus tard. Je vais vous montrer certaines des méthodes les plus importantes et comment elles sont utilisées. Il y a beaucoup plus de méthodes que je ne vais pas vous montrer ici, mais vous pouvez voir toutes ces méthodes [ici](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction).

#### getElementById()

Cette méthode retourne l'élément qui contient le nom _id_ passé. Comme nous le savons, les _id_ doivent être uniques, donc c'est une méthode très utile pour obtenir uniquement l'élément que vous voulez.

```
var myStart = document.getElementsById('start');
```

**myStart** : Notre nom de variable qui ressemble à notre _id_ passé.

**start** : _id_ passé. Et dans le cas où nous n'avons aucun _id_ avec ce nom spécifique, il retourne _null_.

#### getElementsByClassName()

Cette méthode retourne une _HTMLCollection_ de tous ces éléments contenant le nom de _class_ spécifique passé.

```
var myContainer = document.getElementsByClassName('container');
```

**myContainer** : Notre nom de variable qui ressemble à notre _class_ passé.

**.container** : notre _class_ passé. Dans le cas où nous n'avons aucune _class_ avec ce nom spécifique, il retourne _null_.

#### getElementsByTagName()

Cela fonctionne de la même manière que les méthodes ci-dessus : il retourne également une _HTMLCollection_, mais cette fois avec une seule différence : il retourne tous ces _éléments_ avec le nom de balise passé.

```
var buttons = document.getElementsByTagName('button');
```

**buttons** : Notre nom de variable qui ressemble à notre _nom de balise_ passé.

**button** : _nom de balise_ que nous voulons obtenir.

#### querySelector()

Il retourne le premier _élément_ qui a le _sélecteur CSS_ spécifique passé. Rappelez-vous simplement que le _sélecteur_ doit suivre la _syntaxe CSS_. Dans le cas où vous n'avez aucun _sélecteur_, il retourne _null_.

```
var resetButton = document.querySelector('#reset');
```

**resetButton** : Notre nom de variable qui ressemble à notre _sélecteur_ passé.

**#reset** : _sélecteur_ passé, et si vous n'avez aucun _sélecteur_ qui correspond, il retourne _null_.

#### querySelectorAll()

Très similaire à la méthode _querySelector()_, mais avec une seule différence : elle retourne tous les _éléments_ qui correspondent au _sélecteur CSS_ passé. Le _sélecteur_ doit également suivre la _syntaxe CSS_. Dans le cas où vous n'avez aucun _sélecteur_, il retourne _null_.

```
var myButtons = document.querySelector('#buttons');
```

**myButtons** : Notre nom de variable qui ressemble à nos _sélecteurs_ passés.

**#buttons** : _sélecteur_ passé, si vous n'avez aucun _sélecteur_ qui correspond, il retourne _null_.

Ce sont certaines des méthodes DOM les plus utilisées. Il existe plusieurs autres méthodes que vous pouvez utiliser, comme createElement(), qui crée un nouvel élément dans votre page HTML, et setAttribute() qui vous permet de définir de nouveaux attributs pour les éléments HTML. Vous pouvez les explorer par vous-même.

Encore une fois, vous pouvez trouver toutes les méthodes [ici](https://developer.mozilla.org/en-US/docs/Web/API/Element), sur le côté gauche dans _Méthodes_. Je vous recommande vraiment de jeter un coup d'œil à certaines des autres, car vous pourriez en avoir besoin bientôt.

Maintenant, nous allons apprendre les **Événements** — après tout, sans eux, nous ne pouvons pas faire d'animations dans nos pages.

### Événements

Les éléments DOM ont des _méthodes_, comme nous venons de le discuter, mais ils ont aussi des _événements_. Ces événements sont responsables de rendre l'interactivité possible dans notre page. Mais voici une chose que vous ne savez peut-être pas : les _événements_ sont aussi des _méthodes_.

#### click

L'un des événements les plus utilisés est l'événement click. Lorsque l'utilisateur clique sur un élément spécifique, il réalisera une certaine action.

```
myStart.addEventListener('click', function(event) {
```

```
// Faire quelque chose ici.
```

```
}, false);
```

Les paramètres de addEventListener() sont :

1. Le type de l'événement que vous voulez (dans ce cas, 'click').
2. Une fonction de rappel.
3. Le _useCapture_ par défaut est false. Il indique si vous voulez ou non « capturer » l'événement.

#### select

Cet événement est pour lorsque vous voulez _dispatcher_ quelque chose lorsqu'un élément spécifique est sélectionné. Dans ce cas, nous allons _dispatcher_ une simple _alerte_.

```
myStart.addEventListener('select', function(event) {
```

```
alert('Élément sélectionné !');
```

```
}, false);
```

Ce sont certains des événements les plus couramment utilisés. Bien sûr, nous avons beaucoup d'autres événements que vous pouvez utiliser, comme les événements de glisser-déposer — lorsque l'utilisateur commence à glisser un élément, vous pouvez faire une action, et lorsqu'il dépose cet élément, vous pouvez faire une autre action.

Maintenant, nous allons voir comment nous pouvons parcourir le DOM et utiliser certaines propriétés.

### Parcourir le DOM

Vous pouvez parcourir le DOM et utiliser certaines propriétés que nous allons voir maintenant. Avec ces propriétés, vous pouvez retourner des éléments, des commentaires, du texte, etc.

#### .childNodes

Cette propriété retourne une _nodeList_ des nœuds enfants de l'élément donné. Elle retourne du texte, des commentaires, etc. Donc, lorsque vous voulez l'utiliser, vous devez être prudent.

```
var container = document.querySelector('.container');
```

```
var getContainerChilds = container.childNodes;
```

#### .firstChild

Cette propriété retourne le premier enfant de l'élément donné.

```
var container = document.querySelector('.container');
```

```
var getFirstChild = container.firstChild;
```

#### .nodeName

Cette propriété retourne le nom de l'élément donné. Dans ce cas, nous avons passé une _div_, donc elle retournera « div ».

```
var container = document.querySelector('.container');
```

```
var getName = container.nodeName;
```

#### .nodeValue

Cette propriété est spécifique pour les **textes et commentaires**, car elle retourne ou définit la valeur du _nœud_ actuel. Dans ce cas, puisque nous avons passé une div, elle retournera _null_.

```
var container = document.querySelector('.container')
```

```
var getValue = container.nodeValue;
```

#### .nodeType

Cette propriété retourne le **type** de l'élément donné. Dans ce cas, elle retourne « 1 ».

```
var container = document.querySelector('.container')
```

```
var getValue = container.nodeType;
```

Mais, que signifie « 1 » de toute façon ? C'est essentiellement le **nodeType** de l'élément donné. Dans ce cas, il s'agit d'un __ELEMENT_NODE__ et retourne null. Si cela était un attribut, il serait retourné comme « 2 » avec la valeur de l'attribut.

![Image](https://cdn-media-1.freecodecamp.org/images/YOtuBjNlEsuJckztC-v5YHKvTJx2PNQBQQ23)
_Un tableau contenant tous les types de nodeTypes et le nodeName et nodeValue retournés pour chacun d'eux._

Vous pouvez lire plus sur les _nodeTypes_ [ici](https://www.w3schools.com/jsref/prop_node_nodetype.asp).

### Éléments

Ces propriétés, au lieu de celles ci-dessus, nous retournent uniquement des **éléments**. Elles sont plus souvent utilisées et recommandées car elles peuvent causer moins de confusion et sont plus faciles à comprendre.

#### .parentNode

Cette propriété retourne le parent du nœud donné.

```
var container = document.querySelector('.container')
```

```
var getParent = container.parentNode;
```

#### .firstElementChild

Retourne le premier enfant élément de l'élément donné.

```
var container = document.querySelector('.container')
```

```
var getValue = container.firstElementChild;
```

#### .lastElementChild

Retourne le dernier enfant élément de l'élément donné.

```
var container = document.querySelector('.container')
```

```
var getValue = container.lastElementChild;
```

Ce sont certaines des nombreuses propriétés que le DOM possède. Il est très important pour vous de connaître les bases du DOM, comment il fonctionne, et ses méthodes et propriétés, car un jour vous pourriez en avoir besoin.

### Conclusion

Le DOM nous fournit plusieurs API importantes pour créer des applications fantastiques et innovantes. Si vous comprenez les bases, vous pouvez créer des choses incroyables. Si vous voulez en savoir plus sur le DOM, vous pouvez cliquer [ici](https://developer.mozilla.org/en-US/docs/Glossary/DOM) et lire toute la documentation MDN.

? S[**uivez-moi sur Twitter !**](https://twitter.com/leonardomso)   
**✨** S[**uivez-moi sur GitHub !**](https://github.com/leonardomso)

_Je cherche une opportunité à distance, donc si vous en avez, j'adorerais en entendre parler, alors s'il vous plaît contactez-moi !_