---
title: Comment gérer les valeurs monétaires en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T17:00:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-monetary-values-in-javascript-3fef5eeb3eda
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q76Xol7zRdld3s-BbFrB_Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment gérer les valeurs monétaires en JavaScript
seo_desc: 'By Sarah Dayan

  Money is everywhere.

  Banking apps, e-commerce websites, stock exchange platforms — we interact with money
  daily. We also increasingly rely on technology to handle ours.

  Yet, there’s no consensus around how to programmatically handle mo...'
---

Par Sarah Dayan

L'argent est partout.

Les applications bancaires, les sites de commerce électronique, les plateformes boursières — nous interagissons avec l'argent quotidiennement. Nous dépendons également de plus en plus de la technologie pour gérer le nôtre.

Pourtant, il n'y a pas de consensus sur la manière de gérer programmatiquement les valeurs monétaires. C'est un concept prévalent dans les sociétés modernes, mais ce n'est pas un type de données de première classe dans aucun langage grand public, alors que des choses comme la date et l'heure le sont. Par conséquent, **chaque logiciel invente sa propre manière de gérer l'argent, avec tous les pièges qui en découlent**.

#### Piège #1 : L'argent comme un N`ombre`

Votre premier instinct lorsque vous devez représenter de l'argent pourrait être d'utiliser un `Number`.

L'argent n'est rien de plus qu'une valeur numérique, n'est-ce pas ? Faux.

La partie montant d'une valeur monétaire n'est relative qu'à un autre aspect : sa devise. Il n'existe pas de 10 "argent". C'est 10 dollars, 10 euros, 10 bitcoins... Si vous voulez additionner deux valeurs monétaires avec des devises différentes, vous devez d'abord les convertir. Même chose si vous voulez les comparer : si tout ce que vous avez est un montant, vous ne pouvez pas faire une comparaison précise. **Montant et devise ne peuvent pas aller l'un sans l'autre**.

#### Piège #2 : Les mathématiques en virgule flottante

La plupart des devises contemporaines sont soit décimales, soit n'ont pas de sous-unités du tout. Cela signifie que lorsque l'argent a des sous-unités, le nombre de celles-ci dans une unité principale est une puissance de 10. Par exemple, il y a 100 cents dans un dollar, soit 10 à la puissance de 2.

Utiliser un système décimal a des avantages, mais soulève un problème majeur en matière de programmation. Les ordinateurs utilisent un système binaire, donc [ils ne peuvent pas représenter nativement les nombres décimaux](http://0.30000000000000004.com/). Certains langages ont trouvé leurs propres solutions comme le type `[BigDecimal](https://docs.oracle.com/javase/7/docs/api/java/math/BigDecimal.html)` en Java ou le type `[decimal](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/decimal)` en C#. JavaScript n'a que le type `Number`, qui peut être utilisé comme un entier ou un [double précision float](https://en.wikipedia.org/wiki/IEEE_754). Parce que c'est une représentation binaire d'un système en base 10, **vous obtenez des résultats inexacts lorsque vous essayez de faire des mathématiques**.

```
0.1 + 0.2 // retourne 0.30000000000000004 ? 
```

**Utiliser des floats pour stocker des valeurs monétaires est une mauvaise idée**.

Au fur et à mesure que vous calculez plus de valeurs, les erreurs de précision imperceptibles conduisent à des écarts plus grands. Cela finit inévitablement par causer des problèmes d'arrondi.

#### Piège #3 : Pourcentage vs. allocation

Parfois, vous devez diviser de l'argent, mais **les pourcentages ne peuvent pas le faire sans ajouter ou perdre des centimes**.

Imaginez que vous devez facturer 999,99 $ avec un acompte de 50 %. Cela peut être fait avec un peu de mathématiques simples. La moitié est 499,995 $, mais vous ne pouvez pas diviser un centime, donc vous arrondirez probablement le résultat à 500 $. Le problème est que, lorsque vous facturez la deuxième moitié, vous obtenez le même résultat et facturez un centime en plus.

Vous ne pouvez pas vous fier uniquement aux pourcentages ou aux divisions pour diviser de l'argent parce que **il n'est pas divisible à l'infini**. Le prix de l'essence peut montrer plus de deux chiffres fractionnaires, mais ce n'est que symbolique : vous finissez toujours par payer un prix arrondi.

#### L'ingénierie à la rescousse

Comme vous pouvez le voir, il y a beaucoup plus à l'argent que ce qui apparaît à première vue, et c'est plus que ce que les simples types de données `Number` peuvent gérer.

Heureusement, **l'ingénieur logiciel [Martin Fowler](https://martinfowler.com/) a trouvé une solution**. Dans [_Patterns of Enterprise Application Architecture_](https://martinfowler.com/books/eaa.html), il décrit [un modèle pour les valeurs monétaires](https://martinfowler.com/eaaCatalog/money.html) :

#### Propriétés

Méthodes

* Math : add, subtract, multiply, allocate
* Comparaison : equals to, greater than, greater than or equal, lesser than, lesser than or equal.

**À partir de cela, vous pouvez créer des objets de valeur qui répondent à la plupart de vos besoins monétaires**.

#### L'argent comme structure de données

L'argent se comporte différemment d'un simple nombre et doit donc être traité différemment. La première et la plus importante chose est qu'**il doit toujours être composé d'un montant et d'une devise**.

Vous pouvez tout faire à partir d'un montant et d'une devise. Vous pouvez additionner des montants monétaires, vérifier s'ils sont égaux ou non, et les formater selon vos besoins. Cela peut être fait via les méthodes d'un objet. **En JavaScript, n'importe quel type de fonction qui retourne un objet fera l'affaire**.

#### Montants en centimes

Il existe plusieurs façons de résoudre le problème des nombres à virgule flottante en JavaScript.

Vous pouvez utiliser des bibliothèques comme [Decimal.js](https://mikemcl.github.io/decimal.js) qui géreront vos floats comme des chaînes. Ce n'est pas une mauvaise solution, et cela s'avère même utile lorsque vous devez gérer des [grands nombres](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Number/MAX_SAFE_INTEGER). **Pourtant, cela se fait au détriment de l'ajout d'une dépendance (lourde), ce qui entraîne des performances plus lentes**.

Vous pouvez multiplier les floats en entiers avant de calculer, puis les diviser à nouveau.

```
(0.2 * 100 + 0.01 * 100) / 100 // retourne 0.21 ? 
```

C'est une solution acceptable, mais elle nécessite des calculs supplémentaires soit lors de la construction de l'objet, soit lors de chaque manipulation. Cela n'est pas nécessairement épuisant pour les performances, mais c'est tout de même plus de travail que nécessaire.

Une troisième alternative est de stocker directement les valeurs en centimes, par rapport à l'unité. Si vous devez stocker 10 centimes, vous ne stockerez pas `0.1`, mais `10`. Cela vous permet de travailler uniquement avec des entiers, ce qui signifie des calculs sûrs (jusqu'à ce que vous atteigniez des [grands nombres](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Number/MAX_SAFE_INTEGER)) et de grandes performances.

#### Dinero.js, une bibliothèque immutable pour créer, calculer et formater des valeurs monétaires

À partir de ces observations, j'ai créé une bibliothèque JavaScript : [**Dinero.js**](https://github.com/sarahdayan/dinero.js).

![Image](https://cdn-media-1.freecodecamp.org/images/4BaMJ7Ega3Xo2M3Iv5h3EiqqfsaLy7vA3HZB)

Dinero.js suit le modèle de Fowler et plus encore. Il vous permet de créer, calculer et formater des valeurs monétaires en JavaScript. Vous pouvez faire des mathématiques, analyser et formater vos objets, leur poser des questions et faciliter votre processus de développement.

La bibliothèque a été conçue pour être immutable et chainable. Elle supporte les paramètres globaux, dispose d'options de formatage étendues et fournit un support natif pour l'internationalisation.

#### Pourquoi immutable ?

Une bibliothèque immutable est plus sûre et plus prévisible. Les opérations mutables et les copies de référence sont la source de nombreux bugs. Opter pour l'immuabilité les évite complètement.

Avec Dinero.js, vous pouvez effectuer des calculs sans vous soucier de modifier les instances originales. Dans l'exemple Vue.js suivant, `price` ne sera pas altéré lorsque `priceWithTax` est appelé. Si l'instance était mutable, ce serait le cas.

```
const vm = new Vue({  data: {    price: Dinero({ amount: 500 })  },  computed: {    priceWithTax() {      return this.price.add(this.price.percentage(10))    }  }})
```

#### Chainabilité

Les bons développeurs s'efforcent de rendre leur code plus concis et plus facile à lire. Lorsque vous voulez effectuer plusieurs opérations successivement sur un seul objet, le chaînage fournit une notation élégante et une syntaxe concise.

```
Dinero({ amount: 500 })  .add(Dinero({ amount: 200 }))  .multiply(4)  .setLocale('fr-FR')  .toFormat() // retourne "28,00 US$"
```

#### Paramètres globaux

Lorsque vous gérez de nombreuses valeurs monétaires, il est probable que vous souhaitiez que certaines d'entre elles partagent des attributs. Si vous faites un site web en allemand, vous voudrez probablement afficher les montants avec le format de devise allemand.

C'est là que les paramètres globaux deviennent utiles. Au lieu de les passer à chaque instance, vous pouvez déclarer des options qui s'appliqueront à tous les nouveaux objets.

```
Dinero.globalLocale = 'de-DE'Dinero({ amount: 500 }).toFormat() // retourne "5,00 $"
```

#### Support natif de l'internationalisation

Traditionnellement, les bibliothèques utilisent des fichiers de locale pour l'internationalisation. Si vous êtes exhaustif, ils tendent à rendre les bibliothèques beaucoup plus lourdes.

![Image](https://cdn-media-1.freecodecamp.org/images/4l3nTXKehx5SpPmPpl18QQXnfS2d4WE-MpAY)
_Moment.js est quatre fois plus lourd avec les fichiers de locale._

Les fichiers de locale sont également difficiles à maintenir. L'API d'internationalisation est native et [bien supportée](https://caniuse.com/#feat=internationalization). À moins que vous deviez travailler avec des navigateurs obsolètes et/ou marginaux, `toFormat` est sûr à utiliser.

#### Formatage

Un objet est idéal pour stocker des données, mais pas très utile lorsqu'il s'agit de les afficher. Dinero.js vient avec diverses méthodes de formatage, y compris `toFormat`. Il fournit un sucre syntaxique intuitif et concis sur `Number.prototype.toLocaleString`. Associez-le à `setLocale` et vous pourrez afficher n'importe quel objet Dinero dans le format approprié, dans n'importe quelle langue. Cela est particulièrement utile pour les sites de commerce électronique multilingues.

#### Qu'est-ce qui suit ?

Le modèle d'argent de Fowler est largement reconnu comme une excellente solution. Il a inspiré de nombreuses implémentations dans de nombreux langages. Si vous êtes adepte du DIY, je le recommande ainsi que les observations de cet article comme point de départ. Ou vous pouvez choisir [Dinero.js](https://github.com/sarahdayan/dinero.js) : une solution moderne, fiable et entièrement testée qui fonctionne déjà.

Amusez-vous bien !

_Des questions sur Dinero.js ? Ou sur la façon de créer votre propre structure de données monétaires ? Parlons-en sur [Twitter](https://twitter.com/frontstuff_io) !_

_Originalement publié sur [frontstuff.io](https://frontstuff.io/how-to-handle-monetary-values-in-javascript)._