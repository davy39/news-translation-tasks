---
title: Comment écrire une bibliothèque similaire à jQuery en 71 lignes de code — Apprendre
  sur le DOM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-11T02:07:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-jquery-like-library-in-71-lines-of-code-learn-about-the-dom-e9fb99dbc8d2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FLAKTYk8B7EpCYlMqtAFkw.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment écrire une bibliothèque similaire à jQuery en 71 lignes de code
  — Apprendre sur le DOM
seo_desc: 'By Kurt

  JavaScript frameworks are all the rage. Chances are that any JavaScript related
  news feed you open will be littered with references to tools like ReactJS, AngularJS,
  Meteor, RiotJS, BackboneJS, jQuery, and beyond.

  Anyone learning to code (and...'
---

Par Kurt

Les frameworks JavaScript sont très populaires. Il est probable que tout flux d'actualités lié à JavaScript que vous ouvrez sera rempli de références à des outils comme ReactJS, AngularJS, Meteor, RiotJS, BackboneJS, jQuery, et bien d'autres.

Toute personne apprenant à coder (et même les développeurs expérimentés) ressentira une énorme pression pour apprendre ces nouveaux outils. Le battage médiatique crée la demande. Si vous n'êtes pas à jour avec ce qui est demandé, il peut sembler que vos services ne sont pas demandés.

J'ai remarqué une tendance où les gens se lancent tête baissée dans l'apprentissage de ces outils sans réellement savoir **_ce qu'ils font,_** et encore moins **_comment ils le font._** Cela rend finalement le débogage et la conceptualisation de l'outil exceptionnellement difficiles. Il existe des milliers de cas de mauvaise utilisation où des projets entiers sont créés simplement pour une liaison de données bidirectionnelle, pour un effet d'animation, ou même juste pour afficher un curseur d'images.

#### Les développeurs négligent l'apprentissage du DOM lui-même

Le DOM, ou [Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model), est le cœur et l'âme de votre navigateur web. Vous le regardez en ce moment même. Pour clarifier, le DOM n'est pas une fonctionnalité de JavaScript — il n'est même pas écrit en JavaScript — c'est une interface de programmation, une API entre le langage et le navigateur. Le langage contrôle les calculs, etc., le navigateur contrôle l'affichage et les événements.

Je vais démontrer ci-dessous comment créer une simple bibliothèque de manipulation du DOM similaire à jQuery. Cela permettra de cibler des éléments en utilisant le célèbre sélecteur $, de créer de nouveaux éléments, d'ajouter du HTML, et de contrôler la liaison d'événements.

### Pour commencer

Nous devons créer notre objet de base. Appelons-le _domElement_. Cet objet servira de wrapper pour les éléments ciblés.

```js
var domElement = function(selector) {
 this.selector = selector || null; //Le sélecteur ciblé
 this.element = null; //L'élément DOM réel
};
```

#### Maintenant, nous pouvons commencer à ajouter des fonctionnalités.

Les méthodes jQuery que nous allons répliquer sont le sélecteur/créateur **$() .on(), .off(), .val(), .append, .prepend()** et **.html()**

Commençons par la liaison d'événements. C'est de loin la méthode la plus compliquée que nous allons créer ainsi que la plus utile. C'est le lien dans un modèle de liaison de données bidirectionnelle. (Le modèle met à jour ses abonnés lorsqu'un événement tel qu'une mise à jour est déclenché, et les abonnés font de même.)

Nous allons utiliser un [modèle de conception Publish/Subscribe](https://addyosmani.com/resources/essentialjsdesignpatterns/book/#observerpatternjavascript).

Lorsque _.on(event, callback)_ est appelé, nous **_nous abonnons_** à l'événement et de même lorsque **_.off(event)_** est appelé, nous nous _désabonnons_ de l'événement.

Le gestionnaire d'événements sera son propre objet.

Commençons par créer un objet de base et étendre le prototype de **_domElement_** avec celui-ci.

```js
domElement.prototype.eventHandler = {
 events: [] //Tableau d'événements et de callbacks auxquels l'élément est abonné.
}
```

Super, maintenant créons notre méthode d'abonnement. Nous l'appellerons **_bindEvent_** puisque elle lie un écouteur d'événement à notre élément DOM.

```js
domElement.prototype.eventHandler = {
 events: [], //Tableau d'événements auxquels l'élément est abonné.
 
bindEvent: function(event, callback, targetElement) {
    //supprimer tout événement dupliqué 
    this.unbindEvent(event,targetElement);
    
    //lier l'écouteur d'événement à l'élément DOM
    targetElement.addEventListener(event, callback, false);
    
    this.events.push({
      type: event,
      event: callback,
      target: targetElement
    }); //ajouter le nouvel événement à notre tableau d'événements.
  }
  
}
```

#### C'est tout ! Décomposons rapidement la fonction

1. Nous supprimons tous les événements existants sur l'élément qui ont le type qui est lié. C'est purement une question de préférence personnelle. Je préfère garder des gestionnaires d'événements uniques, car ils sont plus faciles à gérer et à déboguer. La suppression de la ligne permettra plusieurs gestionnaires du même type. Nous créerons la fonction **_unbindEvent_** un peu plus tard.
2. Nous lions l'événement à l'élément DOM, le rendant actif.
3. Nous ajoutons l'événement et toutes ses informations dans le tableau d'événements afin que l'élément puisse garder une trace de nos écouteurs.

Maintenant, avant de pouvoir supprimer un événement, nous aurons besoin d'une méthode pour le trouver et le retourner à partir du tableau d'événements, s'il existe. Créons une méthode rapide pour trouver et retourner un événement par son type, en utilisant la méthode intégrée [**_array filter_**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter).

```js
domElement.prototype.eventHandler = {
 events: [], //Tableau d'événements auxquels l'élément est abonné.
 
bindEvent: function(event, callback, targetElement) {
    //supprimer tout événement dupliqué 
    this.unbindEvent(event,targetElement);
    
    //lier l'écouteur d'événement à l'élément DOM
    targetElement.addEventListener(event, callback, false);
    
    this.events.push({
      type: event,
      event: callback,
      target: targetElement
    }); //ajouter le nouvel événement à notre tableau d'événements.
  },
    
  findEvent: function(event) {
    return this.events.filter(function(evt) {
      return (evt.type === event); //si le type d'événement correspond, retourner
    }, event)[0];
  }
}
```

#### Maintenant, nous pouvons ajouter notre méthode **_unbindEvent_**.

```js
domElement.prototype.eventHandler = {
 events: [], //Tableau d'événements auxquels l'élément est abonné.
    
bindEvent: function(event, callback, targetElement) {
    //supprimer tout événement dupliqué 
    this.unbindEvent(event,targetElement);
    
    //lier l'écouteur d'événement à l'élément DOM
    targetElement.addEventListener(event, callback, false);
    
this.events.push({
      type: event,
      event: callback,
      target: targetElement
    }); //ajouter le nouvel événement à notre tableau d'événements.
  },
    
findEvent: function(event) {
    return this.events.filter(function(evt) {
      return (evt.type === event); //si le type d'événement correspond, retourner
    }, event)[0];
  },
    
unbindEvent: function(event, targetElement) {
    //rechercher les événements
    var foundEvent = this.findEvent(event);
    
    //supprimer l'écouteur d'événement s'il est trouvé
    if (foundEvent !== undefined) {
      targetElement.removeEventListener(event, foundEvent.event, false);
    }
    
    //mettre à jour le tableau d'événements
    this.events = this.events.filter(function(evt) {
      return (evt.type !== event);
    }, event);
  }
};
```

#### Et voilà notre gestionnaire d'événements ! Essayez-le ci-dessous...

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="domElement Events" src="//codepen.io/kurtr/embed/eJbEWb/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/kurtr/pen/eJbEWb/'>domElement Events</a> by kurt rohlandt
  (<a href='https://codepen.io/kurtr'>@kurtr</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

C'est un utilitaire assez utile, mais vous vous demandez probablement ce que cela a à voir avec jQuery, et pourquoi les méthodes pour le gestionnaire d'événements ne sont pas nommées "on" et "off".

C'est ce que nous allons faire ensuite. Puisque nous avons besoin que le gestionnaire d'événements soit un objet, et que nous ne voulons pas appeler **_$('element').eventHandler.on(..)_**, nos méthodes pointeront simplement vers les fonctions correctes.

Voici le code pour les méthodes **_on_** et **_off_** :

```js
domElement.prototype.on = function(event, callback) {
   this.eventHandler.bindEvent(event, callback, this.element);
}
domElement.prototype.off = function(event) {
   this.eventHandler.unbindEvent(event, this.element);
}
```

Vous voyez comment cela fonctionne ? Maintenant, ajoutons nos autres fonctions utilitaires...

```js
domElement.prototype.val = function(newVal) {
 return (newVal !== undefined ? this.element.value = newVal : this.element.value);
};
domElement.prototype.append = function(html) {
 this.element.innerHTML = this.element.innerHTML + html;
};
domElement.prototype.prepend = function(html) {
 this.element.innerHTML = html + this.element.innerHTML;
};
domElement.prototype.html = function(html) {
 if(html === undefined){
 return this.element.innerHTML;
 }
 this.element.innerHTML = html;
};
```

Celles-ci sont toutes assez simples. La seule à laquelle il faut prêter attention est **_.html()._** Cette méthode peut être invoquée de deux manières : si elle est appelée sans argument, elle retournera le **_innerHTML_** de l'élément, mais si elle est appelée avec un argument, elle définit le **_HTML_** de l'élément. Cela est communément appelé une fonction **_getter / setter_**.

### Initialisation

#### Lors de l'initialisation, nous devons faire l'une des deux choses suivantes...

1. Si le sélecteur commence par une parenthèse ouverte '<', nous allons créer un nouvel élément.
2. Sinon, nous allons utiliser **_document.querySelector_** pour sélectionner un élément _existant_.

Dans un souci de simplicité, je ne fais que le strict minimum en ce qui concerne la validation du HTML dans le cas de la création d'un élément et lorsque je sélectionne un élément, j'utilise **_document.querySelector_**, ce qui signifie qu'il ne retournera qu'un seul élément (la première correspondance) indépendamment du nombre de correspondances.

Cela peut être changé sans trop d'efforts pour sélectionner tous les éléments correspondants en utilisant **_document.querySelectorAll_** et en refactorisant les méthodes pour qu'elles fonctionnent avec un tableau d'éléments.

```js
domElement.prototype.init = function() {
 switch(this.selector[0]){
 case '<' :
 //créer un élément
 var matches = this.selector.match(/<([\w-]*)>/);
 if(matches === null || matches === undefined){
 throw 'Invalid Selector / Node';
 return false;
 }
 var nodeName = matches[0].replace('<','').replace('>','');
 this.element = document.createElement(nodeName);
 break;
 default :
 this.element = document.querySelector(this.selector);
 }
};
```

#### Passons en revue le code ci-dessus.

1. Nous utilisons une instruction **_switch_**, et passons le premier caractère de notre sélecteur comme argument.
2. S'il commence par une parenthèse, nous faisons une correspondance **_Regex_** rapide pour trouver le texte entre les parenthèses ouvertes et fermées. Si cela échoue, nous lançons une erreur indiquant que le sélecteur est invalide.
3. Si une correspondance est trouvée, nous supprimons les parenthèses et passons le texte à **_document.createElement_** pour créer un nouvel élément.
4. Alternativement, nous cherchons une correspondance en utilisant **_document.querySelector_**, cela retourne null si aucune correspondance n'est trouvée.
5. Enfin, nous définissons la propriété de l'élément sur notre **_domElement_** à l'élément correspondant / créé.

### Utilisation de $ pour référencer **_domElement_**

#### Enfin, nous allons assigner le symbole **_$_** pour initialiser un nouveau **_domElement_**. 

```js
$ = function(selector){
 var el = new domElement(selector); // nouveau domElement
 el.init(); // initialiser le domElement
 return el; // retourner le domElement
}
```

Le symbole **_$_** n'est qu'une variable ! C'est notre bibliothèque similaire à jQuery terminée, et tout cela en 71 lignes de code lisibles et bien espacées.

#### Voici un exemple exécutant la bibliothèque complète... utilisez votre console.

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="javascriptDom" src="//codepen.io/kurtr/embed/wMRgJK/?height=265&theme-id=0&default-tab=html,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/kurtr/pen/wMRgJK/'>javascriptDom</a> by kurt rohlandt
  (<a href='https://codepen.io/kurtr'>@kurtr</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Que faire ensuite ?

1. Pourquoi ne pas essayer de répliquer vos fonctions utilitaires préférées ?
2. Plongez dans le [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
3. Utilisez des écouteurs d'événements pour lier des données bidirectionnelles.

### Notes importantes

Un merci spécial à [Quincy Larson](https://www.freecodecamp.org/news/how-to-write-a-jquery-like-library-in-71-lines-of-code-learn-about-the-dom-e9fb99dbc8d2/undefined) pour avoir humanisé cet article en corrigeant mon massacre de la langue anglaise, les ajustements visuels et la grande image d'en-tête.

Ce code a été écrit comme un exemple simple pour illustrer comment les bibliothèques JavaScript interagissent avec — et modifient — le DOM. Il doit être traité comme tel.

J'ai utilisé des instructions simples et claires pour aider les lecteurs à comprendre et à suivre les exemples, et j'ai légèrement contourné — ou complètement ignoré — les points de défaillance et de validation.

L'élément retourné n'aura que les méthodes créées liées au wrapper. Vous pouvez accéder à l'élément DOM réel et à ses méthodes en appelant **_$('selector').element._** Cela permet d'éviter d'étendre le DOM, ce qui est un sujet sensible nécessitant son propre article.

Si vous avez suivi les étapes correctement, vous devriez avoir un fichier complet comme ci-dessous :

```js
var domElement = function(selector) {
 this.selector = selector || null;
 this.element = null;
};
domElement.prototype.init = function() {
 switch (this.selector[0]) {
 case '<':
 var matches = this.selector.match(/<([\w-]*)>/);
 if (matches === null || matches === undefined) {
 throw 'Invalid Selector / Node';
 return false;
 }
 var nodeName = matches[0].replace('<', '').replace('>', '');
 this.element = document.createElement(nodeName);
 break;
 default:
 this.element = document.querySelector(this.selector);
 }
};
domElement.prototype.on = function(event, callback) {
 var evt = this.eventHandler.bindEvent(event, callback, this.element);
}
domElement.prototype.off = function(event) {
 var evt = this.eventHandler.unbindEvent(event, this.element);
}
domElement.prototype.val = function(newVal) {
 return (newVal !== undefined ? this.element.value = newVal : this.element.value);
};
domElement.prototype.append = function(html) {
 this.element.innerHTML = this.element.innerHTML + html;
};
domElement.prototype.prepend = function(html) {
 this.element.innerHTML = html + this.element.innerHTML;
};
domElement.prototype.html = function(html) {
 if (html === undefined) {
 return this.element.innerHTML;
 }
 this.element.innerHTML = html;
};
domElement.prototype.eventHandler = {
 events: [],
 bindEvent: function(event, callback, targetElement) {
 this.unbindEvent(event, targetElement);
 targetElement.addEventListener(event, callback, false);
 this.events.push({
 type: event,
 event: callback,
 target: targetElement
 });
 },
 findEvent: function(event) {
 return this.events.filter(function(evt) {
 return (evt.type === event);
 }, event)[0];
 },
 unbindEvent: function(event, targetElement) {
 var foundEvent = this.findEvent(event);
 if (foundEvent !== undefined) {
 targetElement.removeEventListener(event, foundEvent.event, false);
 }
 this.events = this.events.filter(function(evt) {
 return (evt.type !== event);
 }, event);
 }
};
$ = function(selector) {
 var el = new domElement(selector);
 el.init();
 return el;
}
```

Si vous avez aimé cet article, jetez un coup d'œil à d'autres choses que j'ai écrites.

[**Programmation préventive — comment corriger les bugs avant qu'ils ne se produisent**](https://medium.com/p/9df82cf215c5)  
[_...et pourquoi Sherlock Holmes aurait été un programmeur brillant_](https://medium.com/p/9df82cf215c5)

[**5 choses à retenir lorsque vous apprenez à programmer**](https://medium.com/p/1ed8e734b04f)  
[_Apprendre à programmer est un défi. En plus de choisir un langage ou de configurer un environnement de développement que vous..._](https://medium.com/p/1ed8e734b04f)

[**Comment je suis devenu programmeur. Et quand j'ai commencé à m'appeler un**](https://medium.com/p/54a0533c4335)  
[_J'ai voulu commencer à bloguer sur la programmation depuis des mois maintenant et comme tant d'autres avant moi, je me suis lancé plein de..._](https://medium.com/p/54a0533c4335)

[**Faire pleuvoir du code — Style Matrix**](https://medium.com/p/ec6e1386084e)  
[_Une introduction aux animations HTML 5 canvas_](https://medium.com/p/ec6e1386084e)

[**Transformer le code en cash — Comment gagner de l'argent en tant que développeur Web et vivre pour en parler.**](https://medium.com/p/f5eedc557b3e)  
[_Alors vous venez d'apprendre à coder. Vous êtes enthousiaste et quiconque ne peut pas coder pense que vous êtes un génie, la nouvelle se répand et tout le monde..._medium.com](https://medium.com/p/f5eedc557b3e)