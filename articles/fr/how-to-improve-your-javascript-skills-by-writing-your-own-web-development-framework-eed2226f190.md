---
title: Comment améliorer vos compétences en JavaScript en écrivant votre propre Framework
  de développement Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T15:10:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KR8iGkB0dfLoeHz9kq5t4g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment améliorer vos compétences en JavaScript en écrivant votre propre
  Framework de développement Web
seo_desc: 'By Jérémy Bardon

  Have you ever asked yourself how a framework works?

  When I discovered AngularJS after learning jQuery many years ago, AngularJS seemed
  like dark magic to me.

  Then Vue.js came out, and upon analyzing how it works under the hood, I was...'
---

Par Jérémy Bardon

Vous êtes-vous déjà demandé comment fonctionne un framework ?

Lorsque j'ai découvert [AngularJS](https://angularjs.org/) après avoir appris [jQuery](https://jquery.com/) il y a de nombreuses années, AngularJS me semblait être de la magie noire.

Ensuite, Vue.js est arrivé, et en analysant son fonctionnement sous le capot, j'ai été encouragé à essayer d'écrire mon propre [système de liaison bidirectionnelle](https://en.wikipedia.org/wiki/Data_binding).

Dans cet article, je vais vous montrer comment écrire un framework JavaScript moderne avec des attributs d'éléments HTML personnalisés, de la réactivité et une liaison double.

### Comment fonctionne la réactivité ?

Il serait bon de commencer par comprendre comment fonctionne la réactivité. La bonne nouvelle est que c'est simple. En fait, lorsque vous déclarez un nouveau composant dans Vue.js, le framework va [proxifier chaque propriété](https://vuejs.org/v2/guide/reactivity.html#How-Changes-Are-Tracked) (getters et setters) en utilisant le [modèle de conception proxy](https://en.wikipedia.org/wiki/Proxy_pattern).

Ainsi, il sera capable de détecter les changements de valeur des propriétés à la fois depuis le code et les entrées utilisateur.

### À quoi ressemble le modèle de conception proxy ?

L'idée derrière le modèle proxy est simplement de surcharger l'accès à un objet. Une analogie dans la vie réelle pourrait être l'accès à votre compte bancaire.

Par exemple, vous ne pouvez pas accéder directement au solde de votre compte bancaire et changer la valeur selon vos besoins. Il est nécessaire pour vous de demander à quelqu'un qui a cette permission, dans ce cas, votre banque.

```js
var account = {
	balance: 5000
}

// Une banque agit comme un proxy entre votre compte bancaire et vous
var bank = new Proxy(account, {
    get: function (target, prop) {
    	return 9000000;
    }
});

console.log(account.balance); // 5,000 (votre solde réel)
console.log(bank.balance);    // 9,000,000 (la banque ment)
console.log(bank.currency);   // 9,000,000 (la banque fait n'importe quoi)
```

Dans l'exemple ci-dessus, lorsque vous utilisez l'objet `bank` pour accéder au solde du `account`, la fonction getter est surchargée, et elle retourne toujours `9,000,000` au lieu de la valeur de la propriété, même si la propriété n'existe pas.

```js
// Surcharger la fonction setter par défaut
var bank = new Proxy(account, {
    set: function (target, prop, value) {
        // Toujours définir la valeur de la propriété à 0
        return Reflect.set(target, prop, 0); 
    }
});

account.balance = 5800;
console.log(account.balance); // 5,800

bank.balance = 5400;
console.log(account.balance); // 0 (la banque fait n'importe quoi)
```

En surchargeant la fonction `set`, il est possible de manipuler son comportement. Vous pouvez changer la valeur à définir, mettre à jour une autre propriété à la place, ou même ne rien faire du tout.

### Exemple de réactivité

Maintenant que vous êtes confiant sur le fonctionnement du modèle de conception proxy, commençons à écrire notre framework JavaScript.

Pour garder les choses simples, nous allons imiter la syntaxe AngularJS. Déclarer un contrôleur et lier les éléments de modèle aux propriétés du contrôleur est assez simple.

```js
<div ng-controller="InputController">
    <!-- "Hello World!" -->
    <input ng-bind="message"/>   
    <input ng-bind="message"/>
</div>

<script type="javascript">
  function InputController () {
      this.message = 'Hello World!';
  }
  angular.controller('InputController', InputController);
</script>
```

Tout d'abord, définissez un contrôleur avec des propriétés. Ensuite, utilisez ce contrôleur dans un modèle. Enfin, utilisez l'attribut `ng-bind` pour activer la liaison double avec la valeur de l'élément.

### Analyser le modèle et instancier le contrôleur

Pour avoir des propriétés à lier, nous avons besoin d'un endroit (aka contrôleur) pour déclarer ces propriétés. Ainsi, il est nécessaire de définir un contrôleur et de l'introduire dans notre framework.

Lors de la déclaration du contrôleur, le framework recherchera les éléments qui ont des attributs `ng-controller`.

S'il correspond à l'un des contrôleurs déclarés, il créera une nouvelle instance de ce contrôleur. Cette instance de contrôleur est uniquement responsable de cette partie particulière du modèle.

```js
var controllers = {};
var addController = function (name, constructor) {
    // Stocker le constructeur du contrôleur
    controllers[name] = {
        factory: constructor,
        instances: []
    };
    
    // Rechercher les éléments utilisant le contrôleur
    var element = document.querySelector('[ng-controller=' + name + ']');
    if (!element){
       return; // Aucun élément n'utilise ce contrôleur
    }
    
    // Créer une nouvelle instance et la sauvegarder
    var ctrl = new controllers[name].factory;
    controllers[name].instances.push(ctrl);
    
    // Rechercher les liaisons.....
};

addController('InputController', InputController);
```

Voici à quoi ressemble la déclaration de la variable `controllers` faite à la main. L'objet `controllers` contient tous les contrôleurs déclarés dans le framework en appelant `addController`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*li6MNxPJEvE6BdgNwAQgwg.png)
_Définition des contrôleurs faits à la main_

Pour chaque contrôleur, une fonction `factory` est sauvegardée pour instancier un nouveau contrôleur lorsque cela est nécessaire. Le framework stocke également chacune des nouvelles instances du même contrôleur utilisé dans le modèle.

### Recherche de liaisons

À ce stade, nous avons une instance du contrôleur et une partie du modèle utilisant cette instance.

L'étape suivante consiste à rechercher les éléments avec des liaisons qui utilisent les propriétés du contrôleur.

```js
var bindings = {};

// Note : element est l'élément dom utilisant le contrôleur
Array.prototype.slice.call(element.querySelectorAll('[ng-bind]'))
    .map(function (element) {
        var boundValue = element.getAttribute('ng-bind');

        if(!bindings[boundValue]) {
            bindings[boundValue] = {
                boundValue: boundValue,
                elements: []
            }
        }

        bindings[boundValue].elements.push(element);
    });
```

Assez simple, il stocke toutes les liaisons d'un objet (utilisé comme une [table de hachage](https://en.wikipedia.org/wiki/Hash_table)). Cette variable contient toutes les propriétés à lier avec la valeur actuelle et tous les éléments DOM qui lient cette propriété.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4-mQb0bbJwzdZQZsgOqb-g.png)
_Déclaration des liaisons faites à la main_

### Lier les propriétés du contrôleur en double

Après le travail préliminaire effectué par le framework, voici la partie intéressante : **la liaison double**.

Cela implique de lier la propriété du contrôleur aux éléments DOM pour mettre à jour le DOM chaque fois que le code met à jour la valeur de la propriété.

N'oubliez pas non plus de lier les éléments DOM à la propriété du contrôleur. Ainsi, lorsque l'utilisateur change la valeur de l'entrée, cela mettra à jour la propriété du contrôleur. Ensuite, cela mettra également à jour tous les autres éléments liés à cette propriété.

#### Détecter les mises à jour depuis le code avec un proxy

Comme expliqué ci-dessus, Vue enveloppe les composants dans un proxy pour réagir aux changements de propriétés. Faisons de même en proxifiant le setter uniquement pour les propriétés liées du contrôleur.

```js
// Note : ctrl est l'instance du contrôleur
var proxy = new Proxy(ctrl, {
    set: function (target, prop, value) {
        var bind = bindings[prop];
        if(bind) {
            // Mettre à jour chaque élément DOM lié à la propriété  
            bind.elements.forEach(function (element) {
                element.value = value;
                element.setAttribute('value', value);
            });
        }
        return Reflect.set(target, prop, value);
    }
});
```

Chaque fois qu'une propriété liée est définie, le proxy vérifiera tous les éléments liés à cette propriété. Ensuite, il les mettra à jour avec la nouvelle valeur.

Dans cet exemple, nous supportons uniquement la liaison des éléments **input**, car seul l'attribut `value` est défini.

#### Réagir aux événements des éléments

La dernière chose à faire est de réagir aux interactions de l'utilisateur. Les éléments DOM déclenchent des événements lorsqu'ils détectent un changement de valeur.

Écoutez ces événements et mettez à jour la propriété liée avec la nouvelle valeur de l'événement. Tous les autres éléments liés à la même propriété seront mis à jour automatiquement grâce au proxy.

```js
Object.keys(bindings).forEach(function (boundValue) {
  var bind = bindings[boundValue];
  
  // Écouter les événements des éléments et mettre à jour la propriété proxy   
  bind.elements.forEach(function (element) {
    element.addEventListener('input', function (event) {
      proxy[bind.boundValue] = event.target.value; // Déclenche également le setter du proxy
    });
  })  
});
```

Une fois que vous avez tout assemblé, vous obtenez des entrées à double liaison faites à la main. Voici une démonstration fonctionnelle incluant tout le code.

%[https://codepen.io/jbardon/pen/eVjPVR]

Merci d'avoir lu. J'espère que cela vous a aidé à démystifier le fonctionnement des frameworks JavaScript.

Félicitations ! Vous avez développé des fonctionnalités populaires telles que des attributs d'éléments HTML personnalisés, de la réactivité et une liaison double !

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien !** ?

**N'oubliez pas de me suivre pour être informé de mes prochains articles** ?

### Consultez mes autres articles

[https://www.freecodecamp.org/news/author/jbardon/](https://www.freecodecamp.org/news/author/jbardon/)

#### ➡ React pour débutants

* [Un guide rapide pour apprendre React et comment son Virtual DOM fonctionne](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44)
* [Comment apporter de la réactivité dans React avec les états](https://medium.freecodecamp.org/how-to-bring-reactivity-into-react-with-states-exclude-redux-solution-4827d293dfc4)

#### ➡ JavaScript

* [Erreurs courantes à éviter lors de l'utilisation de Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)
* [Arrêtez le débogage douloureux de JavaScript et adoptez Intellij avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [Comment réduire les bundles JavaScript énormes sans effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)