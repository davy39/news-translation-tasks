---
title: Un aperçu rapide des symboles JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-13T08:35:24.000Z'
originalURL: https://freecodecamp.org/news/how-did-i-miss-javascript-symbols-c1f1c0e1874a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3AzH-G1JpbL4UhzH5TXS5w.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un aperçu rapide des symboles JavaScript
seo_desc: 'By Vali Shah

  Symbols

  Symbols are new primitive type introduced in ES6. Symbols are completely unique
  identifiers. Just like their primitive counterparts (Number, String, Boolean), they
  can be created using the factory function Symbol() which returns ...'
---

Par Vali Shah

#### Symboles

Les symboles sont un nouveau type de [**primitive**](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) introduit dans ES6. Les symboles sont des identifiants complètement uniques. Tout comme leurs homologues primitifs (**Number**, **String**, **Boolean**), ils peuvent être créés en utilisant la fonction de fabrication `Symbol()` qui retourne un Symbole.

```js
const symbol = Symbol('description')
```

Chaque fois que vous appelez la fonction de fabrication, un nouveau symbole unique est créé. Le paramètre optionnel de type chaîne est une chaîne descriptive qui est affichée lors de l'impression du symbole.

```js
> symbol
Symbol(description)
```

Chaque symbole retourné par `Symbol()` est unique, donc chaque symbole a sa propre identité :

```js
> Symbol() === Symbol()
false
```

Vous pouvez voir que les symboles sont primitifs si vous appliquez l'opérateur `typeof` à l'un d'eux — il retournera un nouveau résultat spécifique aux symboles :

```js
> typeof symbol
'symbol'
```

#### **Cas d'utilisation : Les symboles comme clés de propriétés non publiques**

Lorsque vous avez des hiérarchies d'héritage en JavaScript, vous avez deux types de propriétés (par exemple, créées via des classes, une approche purement prototypale) :

* Les propriétés **publiques** sont visibles par les clients du code
* Les propriétés **privées** sont utilisées en interne dans les éléments qui composent la hiérarchie d'héritage (par exemple, classes, objets).

Pour des raisons d'utilisabilité, les propriétés publiques ont généralement des clés de type chaîne. Mais pour les propriétés privées avec des clés de type chaîne, des conflits de noms accidentels peuvent devenir un problème. Par conséquent, les symboles sont un bon choix.

Par exemple, dans le code suivant, les symboles sont utilisés pour les propriétés privées `_counter` et `_action` :

```js
const _counter = Symbol('counter');
const _action  = Symbol('action');
class Countdown {
    constructor(counter, action) {
        this[_counter] = counter;
        this[_action] = action;
    }
    dec() {
        let counter = this[_counter];
        if (counter < 1) return;
        counter--;
        this[_counter] = counter;
        if (counter === 0) {
            this[_action]();
        }
    }
}
```

Notez que les symboles vous protègent uniquement des conflits de noms, et non de l'accès non autorisé. Vous pouvez découvrir toutes les clés de propriétés d'un objet — y compris les symboles — via ce qui suit :

```js
const obj = {
  [Symbol('my_key')]  : 1, 
   enum               : 2, 
   nonEnum            : 3
};

Object.defineProperty(obj, 'nonEnum', { enumerable: false }); // Rendre 'nonEnum' non énumérable.

// Ignore les clés de propriétés de type symbole :
> Object.getOwnPropertyNames(obj)
['enum', 'nonEnum']

// Ignore les clés de propriétés de type chaîne :
> Object.getOwnPropertySymbols(obj)
[Symbol(my_key)]

// Prend en compte tous les types de clés :
> Reflect.ownKeys(obj)
[Symbol(my_key),'enum', 'nonEnum']

// Ne considère que les clés de propriétés énumérables qui sont des chaînes :
> Object.keys(obj)
['enum']
```

#### Avons-nous vraiment besoin des symboles ?

Utilisez les symboles lorsque votre besoin est l'un des suivants :

* **Enum** : Pour vous permettre de définir des constantes avec des noms sémantiques et des valeurs uniques.

```js
const directions = {
  UP   : Symbol( 'UP' ),
  DOWN : Symbol( 'DOWN' ),
  LEFT : Symbol( 'LEFT' ),
  RIGHT: Symbol( 'RIGHT' )
};
```

* **Conflits de noms** : lorsque vous souhaitez éviter les collisions avec les clés dans les objets
* **Confidentialité** : lorsque vous ne voulez pas que vos propriétés d'objet soient énumérables
* **Protocoles** : Pour définir comment un objet peut être itéré. Imaginez, par exemple, une bibliothèque comme `dragula` définissant un protocole via `Symbol.for(dragula.moves)`. Vous pouvez ajouter une méthode sur ce `Symbol` à n'importe quel élément DOM. Si un élément DOM suit le protocole, alors `dragula` pourrait appeler la méthode définie par l'utilisateur `el[Symbol.for('dragula.moves')]()` pour vérifier si l'élément peut être déplacé.
* **Symboles bien connus** : En plus des symboles définis par l'utilisateur, JavaScript a certains symboles intégrés. Ceux-ci représentent des comportements internes du langage qui n'étaient pas exposés aux développeurs avant ES5. Plus d'informations [**ici**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#Well-known_symbols).

#### **Conclusion**

Les `Symbols` en JavaScript peuvent fournir un niveau d'accès unique aux objets. Il est utile pour tous les développeurs d'avoir une compréhension de base d'eux et de leurs divers cas d'utilisation.

`code = **co**ffee + **de**veloper`