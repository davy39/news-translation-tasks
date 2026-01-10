---
title: 'Exemples d''objets JSON : Méthodes Stringify et Parse expliquées'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-16T23:05:00.000Z'
originalURL: https://freecodecamp.org/news/json-stringify-method-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c8f740569d1a4ca32e4.jpg
tags:
- name: JavaScript
  slug: javascript
- name: json
  slug: json
- name: toothbrush
  slug: toothbrush
seo_title: 'Exemples d''objets JSON : Méthodes Stringify et Parse expliquées'
seo_desc: 'JSON Stringify

  The JSON.stringify() method converts a JSON-safe JavaScript value to a JSON compliant
  string.

  What are JSON-safe values one may ask! Let’s make a list of all JSON-unsafe values
  and anything that isn’t on the list can be considered JSON...'
---

## **JSON Stringify**

La méthode `JSON.stringify()` convertit une valeur JavaScript _compatible JSON_ en une chaîne conforme JSON.

Quelles sont les valeurs compatibles JSON, pourrait-on demander ! Faisons une liste de toutes les valeurs non compatibles JSON et tout ce qui n'est pas dans cette liste peut être considéré comme compatible JSON.

#### **Valeurs non compatibles JSON :**

* `undefined`
* `function(){}`
* (ES6+) `Symbol`
* Un objet avec des références circulaires

#### **Syntaxe**

```javascript
  JSON.stringify( valeur [, replacer [, espace]])
```

Dans sa forme la plus simple et la plus utilisée :

```javascript
  JSON.stringify( valeur )
```

#### **Paramètres**

`valeur` : La valeur JavaScript à "stringifier".

`replacer` : (Optionnel) Une fonction ou un tableau qui sert de filtre pour les propriétés de l'objet valeur à inclure dans la chaîne JSON.

`espace` : (Optionnel) Une valeur numérique ou chaîne pour fournir une indentation à la chaîne JSON. Si une valeur numérique est fournie, autant d'espaces (jusqu'à 10) servent d'indentation à chaque niveau. Si une valeur chaîne est fournie, cette chaîne (jusqu'aux 10 premiers caractères) sert d'indentation à chaque niveau.

#### **Type de retour**

Le type de retour de la méthode est : `string`.

## **Description**

Les valeurs compatibles JSON sont converties en leur forme de chaîne JSON correspondante. Les valeurs non compatibles JSON, en revanche, retournent :

* `undefined` si elles sont passées en tant que valeurs à la méthode
* `null` si elles sont passées en tant qu'élément de tableau
* rien si passées en tant que propriétés d'un objet
* lève une erreur si c'est un objet avec des références circulaires.

```javascript
  // Valeurs compatibles JSON
  JSON.stringify({});                  // '{}'
  JSON.stringify(true);                // 'true'
  JSON.stringify('foo');               // '"foo"'
  JSON.stringify([1, 'false', false]); // '[1,"false",false]'
  JSON.stringify({ x: 5 });            // '{"x":5}'
  JSON.stringify(new Date(2006, 0, 2, 15, 4, 5))  // '"2006-01-02T15:04:05.000Z"'
  
  // Valeurs non compatibles JSON passées en tant que valeurs à la méthode
  JSON.stringify( undefined );					// undefined
  JSON.stringify( function(){} );					// undefined

  // Valeurs non compatibles JSON passées en tant qu'éléments de tableau
  JSON.stringify({ x: [10, undefined, function(){}, Symbol('')] });  // '{"x":[10,null,null,null]}' 
 
 // Valeurs non compatibles JSON passées en tant que propriétés d'un objet
  JSON.stringify({ x: undefined, y: Object, z: Symbol('') });  // '{}'
  
  // Objet non compatible JSON avec référence circulaire
  var o = { },
    a = {
      b: 42,
      c: o,
      d: function(){}
    };

  // créer une référence circulaire dans `a`
  o.e = a;

  // lèverait une erreur sur la référence circulaire
  // JSON.stringify( a );
```

`JSON.stringify(...)` se comporte différemment si un objet passé contient une méthode `toJSON()` définie. La valeur de retour de la méthode `toJSON()` sera sérialisée au lieu de l'objet lui-même.

Cela s'avère exceptionnellement utile lorsqu'un objet contient une valeur JSON illégale.

```javascript
   // Valeurs non compatibles JSON passées en tant que propriétés d'un objet
   var obj = { x: undefined, y: Object, z: Symbol('') };
   
   // JSON.stringify(obj);  affiche '{}'
   obj.toJSON = function(){
    return {
      x:"undefined",
      y: "Function",
      z:"Symbol"
    }
   }
   JSON.stringify(obj);  //"{"x":"undefined","y":"Function","z":"Symbol"}"
    
  // Objet non compatible JSON avec référence circulaire
  var o = { },
    a = {
      b: 42,
      c: o,
      d: function(){}
    };

  // créer une référence circulaire dans `a`
  o.e = a;

  // lèverait une erreur sur la référence circulaire
  // JSON.stringify( a );
  
  // définir une sérialisation personnalisée des valeurs JSON
  a.toJSON = function() {
    // inclure uniquement la propriété `b` pour la sérialisation
    return { b: this.b };
  };

  JSON.stringify( a ); // "{"b":42}"
```

#### **Le `replacer`**

Le `replacer`, comme mentionné précédemment, est un filtre qui indique quelles propriétés doivent être incluses dans la chaîne JSON. Il peut s'agir d'un tableau ou d'une fonction. Lorsqu'il s'agit d'un tableau, le replacer contient les représentations sous forme de chaîne uniquement des propriétés à inclure dans la chaîne JSON.

```javascript
  var foo = {foundation: 'Mozilla', model: 'box', week: 45, transport: 'car', month: 7};
  JSON.stringify(foo, ['week', 'month']);    // '{"week":45,"month":7}', ne conserve que les propriétés "week" et "month"
```

Si `replacer` est une fonction, elle sera appelée une fois pour l'objet lui-même, puis une fois pour chaque propriété de l'objet, et chaque fois, deux arguments lui sont passés, _clé_ et _valeur_. Pour ignorer une _clé_ dans la sérialisation, il faut retourner `undefined`. Sinon, la _valeur_ fournie doit être retournée. Si l'une de ces _valeurs_ est elle-même un objet, la fonction `replacer` les sérialise également de manière récursive.

```javascript
  function replacer(key, value) {
    // Filtrer les propriétés
    if (typeof value === 'string') {
      return undefined;
    }
    return value;
  }

  var foo = {foundation: 'Mozilla', model: 'box', week: 45, transport: 'car', month: 7};
  JSON.stringify(foo, replacer);  // '{"week":45,"month":7}'
```

Si un tableau est passé à `JSON.stringify()` et que `replacer` retourne `undefined` pour l'un de ses éléments, la valeur de l'élément est remplacée par `null`. Les fonctions `replacer` ne peuvent pas supprimer de valeurs d'un tableau.

```javascript
  function replacer(key, value) {
    // Filtrer les propriétés
    if (typeof value === 'string') {
      return undefined;
    }
    return value;
  }

  var foo = ['Mozilla', 'box', 45, 'car', 7];
  JSON.stringify(foo, replacer);  // "[null,null,45,null,7]"
```

#### **L'`espace`**

Le paramètre `espace` utilisé pour l'indentation rend le résultat de `JSON.stringify()` plus lisible.

```javascript
  var a = {
    b: 42,
    c: "42",
    d: [1,2,3]
  };

  JSON.stringify( a, null, 3 );
  // "{
  //    "b": 42,
  //    "c": "42",
  //    "d": [
  //       1,
  //       2,
  //       3
  //    ]
  // }"

  JSON.stringify( a, null, "-----" );
  // "{
  // -----"b": 42,
  // -----"c": "42",
  // -----"d": [
  // ----------1,
  // ----------2,
  // ----------3
  // -----]
  // }"
```

## **JSON Parse**

La méthode `JSON.parse()` analyse une chaîne et construit un nouvel objet décrit par une chaîne.

### Syntaxe :

```javascript
    JSON.parse(texte [, reviver])
```

### Paramètres :

`texte` La chaîne à analyser en tant que JSON

`reviver` (Optionnel) La fonction recevra `clé` et `valeur` en tant qu'arguments. Cette fonction peut être utilisée pour transformer la valeur résultante.

Voici un exemple sur la façon d'utiliser `JSON.parse()` :

```javascript
var data = '{"foo": "bar"}';

console.log(data.foo); // Cela affichera `undefined` puisque `data` est de type chaîne et n'a pas de propriété nommée `foo`

// Vous pouvez utiliser JSON.parse pour créer un nouvel objet JSON à partir de la chaîne donnée
var convertedData = JSON.parse(data);

console.log(convertedData.foo); // Cela affichera `bar`
```

[Démo Repl.it](https://repl.it/MwgK/0)

Voici un exemple avec `reviver` :

```javascript
var data = '{"value": 5}';

var result = JSON.parse(data, function(key, value) {
    if (typeof value === 'number') {
        return value * 10;
    }
    return value;
});

// Données originales
console.log("Données originales :", data); // Cela affichera Données originales : {"value": 5}
// Résultat après analyse
console.log("Résultat analysé : ", result); // Cela affichera Résultat analysé :  { value: 50 }
```

Dans l'exemple ci-dessus, toutes les valeurs numériques sont multipliées par `10` - [Démo Repl.it](https://repl.it/Mwfp/0)

## Plus d'informations sur JSON :

* [Syntaxe JSON](https://guide.freecodecamp.org/javascript/standard-objects/json/json-syntax)
* [Transformez votre site web en une application mobile avec 7 lignes de JSON](https://www.freecodecamp.org/news/how-to-turn-your-website-into-a-mobile-app-with-7-lines-of-json-631c9c9895f5/)