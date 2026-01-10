---
title: Exemple Angular NgClass – Comment ajouter des classes CSS conditionnelles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-07T15:01:26.000Z'
originalURL: https://freecodecamp.org/news/angular-ngclass-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/angular-ngclass-article.jpg
tags:
- name: Angular
  slug: angular
- name: CSS
  slug: css
seo_title: Exemple Angular NgClass – Comment ajouter des classes CSS conditionnelles
seo_desc: 'By Xing Liu

  ngClass is a directive in Angular that adds and removes CSS classes on an HTML element.
  In this article, we are talking about ngClass in Angular only, not ng-class in angular.js.

  Prerequisites – What is Property Binding?

  Two things we hav...'
---

Par Xing Liu

`ngClass` est une [directive dans Angular](https://angular.io/api/common/NgClass) qui ajoute et supprime des classes CSS sur un élément HTML. Dans cet article, nous parlons uniquement de `ngClass` dans Angular, et non de `ng-class` dans angular.js.

## Prérequis – Qu'est-ce que le Property Binding ?

Deux choses que nous devons comprendre d'abord sont le [property binding](https://angular.io/guide/property-binding) et l'[interpolation](https://angular.io/guide/interpolation) dans Angular. Prenons l'attribut `placeholder` de `input` comme exemple.

Considérons le code suivant :

```html
<!-- HTML Normal -->
<input placeholder="du texte">

<!-- Interpolation -->
<input placeholder="{{ variable }}">
<!-- Property Binding -->
<input [placeholder]="variable">
```

Étant donné que nous avons `variable = 'du texte'` défini dans le composant, alors tout le code ci-dessus fera **exactement la même chose**.

Je considérerais l'interpolation (`{{ }}`) comme un `eval`. Et le property binding est simplement une manière moins verbeuse d'atteindre le même objectif. Personnellement, j'utilise le property binding autant que possible.

## Qu'est-ce que ngClass dans Angular ? Les bases

En ce qui concerne `ngClass`, il supporte trois types de valeurs de retour d'expression : `String`, `Array` et `Object`. Voici un exemple de la [documentation officielle](https://angular.io/api/common/NgClass#description) :

```html
<div [ngClass]="'first second'">
<div [ngClass]="['first', 'second']">
<div [ngClass]="{first: true, second: true, third: true}">
<div [ngClass]="{'first second': true}">
```

Tous les éléments `div` ci-dessus ont deux classes : `first` et `second`. Notez que dans la documentation officielle, il y a une paire de guillemets simples dans chacune des clés d'objet dans le troisième exemple. Mais ni `first` ni `second` n'a de trait d'union ou d'espace. Nous pouvons donc supprimer les guillemets en toute sécurité.

Dans le quatrième exemple, cependant, puisque la clé est `first second` (qui a un espace entre les deux), nous devons ajouter les guillemets simples.

Juste un petit rappel – la valeur de `ngClass` n'a pas besoin d'être un littéral, comme montré ci-dessus. Gardez à l'esprit que le property binding évalue son expression. Donc tant que l'expression peut être interprétée comme `String/Array/Object`, nous sommes bons.

## Comment utiliser ngClass dans Angular

Alors, qu'est-ce qu'une expression ? Normalement, une `expression` est quelque chose qui représente une valeur, et une `instruction` ferait quelque chose sans valeur de retour. Vous connaissez probablement les instructions `if`, qui sont responsables du flux de contrôle. Notez que les instructions `if` n'ont pas de valeur de retour.

D'un autre côté, disons que `num + 10` est une expression (étant donné que `num` a une valeur comme `1`) et qu'elle a une "valeur de retour" de `11`.

Dans ECMAScript, l'assignation est également considérée comme une `expression` et elle a une "valeur de retour". Mais nous ne pouvons pas mettre une expression d'assignation dans le property binding dans Angular, ce qui générera une erreur disant que "Les bindings ne peuvent pas contenir d'assignations".

Cela dit, tous les `[ngClass]` suivants sont valides :

```html
<!-- Étant donné que val="foo", la classe de la div suivante serait "foofoo" -->
<div [ngClass]="val + val">

<!-- Étant donné que val="foo", la classe de la div suivante serait "foo" -->
<div [ngClass]="[val]">

<!-- Étant donné que func est une fonction qui retourne "foo", la classe de la div suivante serait "foo" -->
<div [ngClass]="func()">
```

## Comment utiliser Angular ngClass avec une condition simple

Nous ne pouvons pas écrire une instruction `if` dans `ngClass`, en raison du fait que c'est une instruction. Mais nous pouvons utiliser un opérateur ternaire puisque c'est une expression.

Par exemple, si nous voulons que le texte dans une cellule de tableau ait une classe `red` lorsque sa valeur est supérieure à `10`, et si ce n'est pas le cas, il devrait avoir une classe `green`, voici le code :

```html
<td [ngClass]="val > 10 ? 'red' : 'green'">{{ val }}</td>
```

Et si nous voulons basculer une classe en fonction d'une condition, nous pourrions faire en sorte que l'une des expressions soit une chaîne vide.

Par exemple, si nous voulons ajouter une classe `error` dans un formulaire lorsqu'il est invalide, et supprimer la classe `error` lorsqu'il est valide, nous pourrions faire ceci :

```html
<input type="text" [ngClass]="control.isInvalid ? 'error' : ''" />
```

Mais il y a une manière moins verbeuse. Rappelez-vous que `ngClass` supporte également un objet comme valeur :

```
<input type="text" [ngClass]="{ error: control.isInvalid }" />
```

Une autre manière d'atteindre le même objectif est d'utiliser le [class binding](https://angular.io/guide/attribute-binding#binding-to-a-single-css-class). Cela est idéal pour une seule classe :

```html
<input type="text" [class.error]="control.isInvalid" />
```

## Comment travailler avec des littéraux d'objet et ngClass

Lorsque nous utilisons des littéraux d'objet, la `clé` représente la `classe` que nous allons configurer pour l'élément, tandis que la `valeur` représente si la classe doit être appliquée à l'élément.

Notez que la `clé` sera appliquée uniquement lorsque la `valeur` est `[truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)`. Dans l'exemple ci-dessus, si `coltrol.isInvalid` est l'un de `false`, `undefined`, `''`, etc., alors la classe `error` ne **s'appliquera pas** à l'élément.

Une autre chose à noter est que la syntaxe [computed property name](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names) n'est pas encore supportée. Mais il y a un [problème ouvert](https://github.com/angular/angular/issues/13855) dans le dépôt officiel GitHub d'Angular.

## Angular ngClass et conditions complexes

Que faire si la condition est plus que simplement `true/false` ? Supposons que nous ayons besoin de différents noms de classe lorsque `val` est `0-5`, `6-10` et `>= 11`, ce que vous pouvez facilement représenter avec une instruction `if/else` :

```typescript
if (val >= 0 && val <= 5) {
  return 'low';
} else if (val >= 6 && val <= 10) {
  return 'medium';
} else {
  return 'high'
}
```

Comme mentionné ci-dessus, nous ne pouvons pas utiliser une instruction `if/else` dans `ngClass`. Mais attendez, `function` est une expression valide avec une valeur de retour, et nous pouvons utiliser une instruction `if/else` dans une `function` :

```typescript
class MyComponent {
  getClassOf(val) {
    if (val >= 0 && val <= 5) {
      return 'low';
    } else if (val > 5 && val <= 10) {
      return 'medium';
    } else {
      return 'high'
    }
  }
}
```

```html
<td [ngClass]="getClassOf(val)">{{ val }}</td>
```

Jusqu'à présent, tout va bien. Mais je tiens à souligner que cela n'est en réalité pas idéal. En bref, en raison du fonctionnement de `ChangeDetection` dans Angular, la fonction `getClassOf` ci-dessus pourrait s'exécuter plusieurs fois, même lorsque _nous_ la considérons comme inutile.

Cela dépasse largement le sujet de cet article, mais vous pouvez consulter [cet article](https://medium.com/showpad-engineering/why-you-should-never-use-function-calls-in-angular-template-expressions-e1a50f9c0496) si vous souhaitez en savoir plus.

Nous pouvons toujours obtenir le même résultat sans utiliser de `function`. Avec un littéral d'objet, cela ressemble à ceci :

```html
<td [ngClass]="{ low: val >= 0 && val <=5, medium: val > 5 && val <= 10, high: val > 10}">
  {{ val }}
</td>
```

Cela semble un peu verbeux. Considérons qu'il n'y aura qu'une seule classe appliquée à l'élément, donc si nous pouvons transformer notre `val` d'abord, c'est idéal :

```typescript
type ClassName = 'low' | 'medium' | 'high';

class MyComponent {
  className: ClassName = 'low';
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes.val) {
      className = mapValToClass(changes.val.currentValue);
    }
  }
  
  private mapValToClass(val: number): ClassName {
    if (val >= 0 && val <= 5) {
      return 'low';
    } else if (val > 5 && val <= 10) {
      return 'medium';
    } else {
      return 'high'
    }
  }
}
```

Et tout ce que nous devons faire dans le template est :

```html
<td [ngClass]="className"></td>
```

Il y a des cas où nous pouvons utiliser un tableau. Considérons la relation de mappage suivante :

```
{
  1: 'first-element',
  2: 'second-element',
  3: 'third-element',
}
```

Cela signifie que pour une `val` qui est `1`, la classe de l'élément sera `first-element`. Lorsque nous voyons des nombres consécutifs comme `1`, `2` et `3`, alors nous pouvons envisager d'utiliser un tableau. Cela est dû au fait qu'en soustrayant `1` de chaque valeur, nous obtenons `0`, `1` et `2`, qui sont simplement les indices d'un tableau :

```typescript
type Val = 1 | 2 | 3;

class MyComponent {
  classArr = ['first-element', 'second-element', 'third-element'];
  val: Val = 1;
}
```

```html
<td [ngClass]="classArr[val - 1]"></td>
```

Un fait amusant est que dans ECMAScript, un tableau est simplement un objet avec quelques propriétés et méthodes supplémentaires. Vous pouvez donc faire ce qui précède avec un objet également :

```typescript
type Val = 1 | 2 | 3;

class MyComponent {
  classMap = {
    1: 'first-element',
    2: 'second-element',
    3: 'third-element',
  }
  val: Val = 1;
}
```

```html
<td [ngClass]="classMap[val]"></td>
```

Notez que vous pouvez également atteindre ce qui précède avec des opérateurs ternaires imbriqués, ce que j'essaie toujours d'éviter.

## [ngClass] vs [class] dans Angular

Avant de conclure, une chose qui vaut la peine d'être mentionnée est la notation `[class]`. Cela est disponible à partir de [Ivy](https://angular.io/guide/ivy), qui a été introduit dans Angular 9 comme compilateur et runtime par défaut.

Le `[class]` est presque rétrocompatible avec `[ngClass]`, avec quelques divergences :

1. `[ngClass]="{'a b': true}"` fonctionne, mais `[class]="{'a b': true}"` ne fonctionnera pas. Voir [ce problème ouvert](https://github.com/angular/angular/issues/40623).
2. La valeur de `[class]` n'est pas "deepwatched". Voir [ici](https://hackmd.io/jzDc7hIDTdWtQblv2TbL9A).

## Conclusion

Merci d'avoir lu ! Espérons que vous savez maintenant comment fonctionne `ngClass` et que vous pouvez l'utiliser en toute confiance.