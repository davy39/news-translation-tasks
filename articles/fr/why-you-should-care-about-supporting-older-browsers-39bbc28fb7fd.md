---
title: Pourquoi vous devriez vous soucier de supporter les anciens navigateurs
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-01-11T17:08:34.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-care-about-supporting-older-browsers-39bbc28fb7fd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U_gLONEItc8d9fmZuGb8Fw.png
tags:
- name: Browsers
  slug: browsers
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
seo_title: Pourquoi vous devriez vous soucier de supporter les anciens navigateurs
seo_desc: 'Supporting older browsers

  You don’t have to worry much about supporting older browsers today. They’ve been
  decent ever since Internet Explorer 8 died.

  But the question remains: How should you go about supporting Internet Explorer 9
  and other browsers...'
---

### **Supporter les anciens navigateurs**

Vous n'avez pas à vous soucier beaucoup de supporter les anciens navigateurs aujourd'hui. Ils ont été décents depuis la disparition d'Internet Explorer 8.

Mais la question reste : Comment devriez-vous procéder pour supporter Internet Explorer 9 et d'autres navigateurs ? En premier lieu, devriez-vous même penser à supporter Internet Explorer 9 ?

Nous allons examiner quelques points que vous voudrez considérer.

#### Pensez aux fonctionnalités, pas aux navigateurs

Supposons que le monde ne contient que deux fonctionnalités et deux navigateurs.

1. Le navigateur A supporte la fonctionnalité A mais pas la fonctionnalité B.
2. Le navigateur B supporte la fonctionnalité B mais pas la fonctionnalité A.

Il est possible de détecter ce que les navigateurs supportent comme fonctionnalités et d'agir en conséquence.

```
// Ceci est du JavaScript
```

```
if (Browser A) {  // Code pour A}
```

```
if (Browser B) {  // code pour B}
```

Mais que se passe-t-il s'il y a plus de navigateurs ? Que se passe-t-il si le monde contient les navigateurs C, D et E ? Il devient difficile de supporter les fonctionnalités dont vous avez besoin si vous pensez en termes de navigateurs.

Il y a une meilleure façon : Vous pouvez vérifier si une fonctionnalité existe. Si elle existe, utilisez-la. Sinon, fournissez un code de repli.

Le bloc de code suivant fonctionne du navigateur A au navigateur Z.

```
// Ceci est du JavaScript
```

```
if (feature A) {  // Code si le navigateur contient la fonctionnalité A} else {  // Code si le navigateur ne contient pas la fonctionnalité A}
```

Et maintenant, vous n'avez plus à vous soucier des navigateurs.

#### Décider d'utiliser une fonctionnalité

Beaucoup de gens décident d'utiliser une fonctionnalité en fonction du nombre de navigateurs qui la supportent. Mais, comme je l'ai argumenté ci-dessus, **les navigateurs n'ont pas d'importance.**

Ce qui compte, c'est : Pouvez-vous coder facilement le repli pour la fonctionnalité ? **Si vous pouvez coder facilement le repli, allez-y et utilisez la fonctionnalité.** Si vous ne pouvez pas coder facilement le repli, n'utilisez pas la fonctionnalité.

#### Décider quels navigateurs supporter

Vous avez toujours besoin d'une limite.

Quels navigateurs allez-vous supporter ?

Quels navigateurs ne allez-vous PAS supporter ? Si vous ne voulez pas supporter le navigateur, alors il n'a pas de sens pour vous d'écrire du code de repli pour celui-ci.

Ma meilleure réponse est : Observez qui utilise votre site. Quels navigateurs utilisent-ils ? Suivez en conséquence.

Oui, il peut y avoir des exceptions qui essaient de visiter votre site web sur Internet Explorer 6. Mais avez-vous le temps et l'énergie d'écrire du code supplémentaire pour un navigateur que presque personne n'utilise ?

Votre énergie ne serait-elle pas mieux dépensée ailleurs ?

#### Le niveau de support

Je dirais qu'il y a quatre niveaux de support :

1. tout doit avoir la même apparence et fonctionner de la même manière dans tous les navigateurs
2. le site doit avoir la même apparence, mais la fonctionnalité peut être différente selon les navigateurs
3. la fonctionnalité doit être la même, mais l'apparence peut être différente selon les navigateurs
4. l'apparence et la fonctionnalité peuvent toutes deux différer selon les navigateurs

Quel type de support fournissez-vous aux anciens navigateurs ? Pourquoi ?

#### Conclusion

Réfléchissez à ceci :

1. pourquoi essayez-vous de supporter l'ancien navigateur que vous essayez de supporter ?
2. quel niveau de support donnez-vous ?
3. cela vaut-il les ressources que vous avez allouées ?

### Supporter les anciens navigateurs — CSS

Il existe deux façons de fournir des replis pour les fonctionnalités CSS :

1. replis de propriétés
2. requêtes de fonctionnalités

#### Replis de propriétés

**Si un navigateur ne reconnaît pas une propriété ou sa valeur correspondante, le navigateur ignorera complètement la propriété.**

Lorsque cela se produit, le navigateur utilise — ou revient — à la valeur précédente qu'il trouve.

C'est la manière la plus simple de fournir un repli.

Voici un exemple :

```
.layout {  display: block;   display: grid; }
```

Dans cet exemple, les navigateurs qui supportent CSS Grid utiliseront `display: grid`. Un navigateur qui ne supporte pas CSS Grid reviendra à `display: block`.

#### Omettre les valeurs par défaut

Si l'élément que vous utilisez a par défaut `display: block`, vous pouvez omettre la déclaration `display: block`. Cela signifie que vous pouvez supporter CSS Grid avec une seule ligne de code :

```
.layout {  display: grid; }
```

Les navigateurs qui supportent CSS Grid seront capables de lire d'autres propriétés CSS comme `grid-template-columns`. Les navigateurs qui ne supportent pas CSS Grid ne le pourront pas.

Cela signifie que vous pouvez écrire des propriétés CSS Grid supplémentaires sans vous soucier des valeurs de repli.

```
.layout {  display: grid;   grid-template-columns: 1fr 1fr 1fr 1fr;  grid-gap: 1em; }
```

Les requêtes de fonctionnalités, ou `@supports`, vous indiquent si une propriété CSS ou sa valeur correspondante est supportée par le navigateur.

**Vous pouvez penser aux requêtes de fonctionnalités CSS comme des instructions `if/else` en JavaScript.** Elles ressemblent à ceci :

```
@supports (property: value) {  /* Code lorsque la propriété ou la valeur est supportée*/}
```

```
@supports not (property: value) {  /* Code lorsque la propriété ou la valeur n'est pas supportée */}
```

`@supports` est utile si vous voulez que les navigateurs lisent le CSS **uniquement** s'ils supportent une propriété spécifique.

Pour l'exemple CSS Grid que nous avions ci-dessus, vous pouvez faire ceci :

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

Dans cet exemple, `padding-left` et `padding-right` ne seront lus que par les navigateurs qui supportent à la fois `@supports` **et** CSS Grid.

Jen Simmons a un meilleur exemple de `@supports` en action. Elle utilise des requêtes de fonctionnalités pour détecter si les navigateurs supportent une propriété comme `-webkit-initial-letter`.

```
@supports (initial-letter: 4) or (-webkit-initial-letter: 4) {  p::first-letter {     -webkit-initial-letter: 4;     initial-letter: 4;     color: #FE742F;     font-weight: bold;     margin-right: 0.5em;  }}
```

![Image](https://cdn-media-1.freecodecamp.org/images/p8pNpSgs7lVe7s8qunRS66fvJSPEaEBaxsHo)

L'exemple de Jen nous amène à une question : Les sites doivent-ils avoir la même apparence sur tous les navigateurs ? Nous examinerons cela plus tard. Mais d'abord, plus d'informations sur les requêtes de fonctionnalités.

#### Support des requêtes de fonctionnalités

Les requêtes de fonctionnalités ont gagné un [grand support](https://caniuse.com/#search=feature%20queries). Tous les principaux navigateurs actuels supportent les requêtes de fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/qZWyleUprSdhJB7VGUL0KCSG547I7d6nduaP)

#### Que se passe-t-il si une fonctionnalité est supportée, mais pas les requêtes de fonctionnalités ?

C'était autrefois la partie délicate. Jen Simmons et d'autres experts nous ont mis en garde contre cette possibilité. Vous pouvez lire comment la gérer [dans cet article](https://hacks.mozilla.org/2016/08/using-feature-queries-in-css/).

Voici mon avis : Je ne supporte plus IE 11, donc j'utilise les requêtes de fonctionnalités de la manière que j'ai mentionnée ci-dessus.

#### Utiliser les replis de propriétés et les requêtes de fonctionnalités en même temps

Regardez le code suivant. Quelles valeurs de padding les navigateurs appliqueront-ils ?

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

```
.layout {    padding-left: 2em;   padding-right: 2em; }
```

La réponse est : Tous les navigateurs appliqueront `2em` de padding gauche et droit.

Pourquoi ?

Cela se produit parce que `padding-left: 2em` et `padding-right: 2em` ont été déclarés plus tard dans le fichier CSS. Les propriétés déclarées plus tard remplacent les propriétés déclarées plus tôt.

Si vous voulez que `padding-left: 2em` et `padding-right: 2em` **s'appliquent uniquement** aux navigateurs qui **ne supportent pas** CSS Grid, vous pouvez inverser l'ordre des propriétés.

```
.layout {    padding-left: 2em;   padding-right: 2em; }
```

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

**Note** : Il est toujours bon de déclarer le code de repli en premier en CSS en raison de sa nature en cascade.

Cela signifie également que si vous utilisez à la fois `@supports` **et** `@supports not`, vous devriez déclarer `@supports not` en premier. Cela rend votre code cohérent.

```
/* Toujours écrire "@supports not" en premier si vous l'utilisez */@supports not (display: grid) {  .layout {      padding-left: 2em;     padding-right: 2em;   }}
```

```
@supports (display: grid) {  .layout {    display: grid;     grid-template-columns: 1fr 1fr 1fr 1fr;    grid-gap: 1em;     padding-left: 1em;    padding-right: 1em;  }}
```

Maintenant, parlons de savoir si les sites doivent avoir la même apparence sur tous les navigateurs.

#### Les sites doivent-ils avoir la même apparence sur tous les navigateurs ?

Certaines personnes pensent que les sites doivent avoir la même apparence sur tous les navigateurs. Ils pensent que la marque est importante et soulignent que les sites doivent avoir une apparence cohérente pour préserver la marque.

D'autres disent non. Ils pensent qu'ils devraient embrasser l'esprit de l'amélioration progressive. Ils peuvent donner plus d'amour aux utilisateurs avec de meilleurs navigateurs.

Les deux points de vue sont corrects, mais ils viennent d'angles différents.

**Le point de vue le plus important vient des utilisateurs.** Votre site est-il capable de fournir aux utilisateurs ce qu'ils sont venus chercher ?

Si oui, vous n'avez pas à être trop strict sur la cohérence. Allez-y et donnez aux utilisateurs avec de meilleurs navigateurs des expériences encore meilleures !

#### Conclusion

Pour fournir un support pour les fonctionnalités CSS, vous pouvez utiliser :

1. Replis de propriétés
2. Requêtes de fonctionnalités

Lorsque vous écrivez du CSS, assurez-vous de déclarer le code de repli en premier avant l'autre ensemble de code pour les navigateurs avec un meilleur support.

### Supporter les anciens navigateurs — JavaScript

Il est facile de fournir un support JavaScript pour les anciens navigateurs. La plupart du temps, vous avez juste besoin d'utiliser un polyfill.

Mais il y a plus de choses que vous pouvez faire.

#### Qu'est-ce qu'un polyfill ?

Un polyfill est un morceau de code qui indique aux navigateurs comment implémenter une fonctionnalité JavaScript. Une fois que vous avez ajouté un polyfill, vous n'avez plus à vous soucier du support. Cela fonctionnera.

Voici comment fonctionne un polyfill :

1. il vérifie si la fonctionnalité est supportée
2. si ce n'est pas le cas, il ajoute du code pour supporter la fonctionnalité

Voici un exemple de polyfill en action. Il vérifie si le navigateur supporte `Array.prototype.find`. Si le navigateur ne supporte pas `Array.prototype.find`, il indique au navigateur comment le supporter.

Vous pouvez trouver ce code sur [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find).

```
if (!Array.prototype.find) {  Object.defineProperty(Array.prototype, 'find', {    value: function(predicate) {     // 1. Let O be ? ToObject(this value).      if (this == null) {        throw new TypeError('"this" is null or not defined');      }
```

```
var o = Object(this);
```

```
// 2. Let len be ? ToLength(? Get(O, "length")).      var len = o.length >>> 0;
```

```
// 3. If IsCallable(predicate) is false, throw a TypeError exception.      if (typeof predicate !== 'function') {        throw new TypeError('predicate must be a function');      }
```

```
// 4. If thisArg was supplied, let T be thisArg; else let T be undefined.      var thisArg = arguments[1];
```

```
// 5. Let k be 0.      var k = 0;
```

```
// 6. Repeat, while k < len      while (k < len) {        // a. Let Pk be ! ToString(k).        // b. Let kValue be ? Get(O, Pk).        // c. Let testResult be ToBoolean(? Call(predicate, T,  kValue, k, O )).        // d. If testResult is true, return kValue.        var kValue = o[k];        if (predicate.call(thisArg, kValue, k, o)) {          return kValue;        }        // e. Increase k by 1.        k++;      }
```

```
// 7. Return undefined.      return undefined;    },    configurable: true,    writable: true  });}
```

**Note** : Un polyfill est un sous-ensemble d'un shim. Un shim est une bibliothèque qui apporte une nouvelle API à un environnement plus ancien.

#### Utiliser des polyfills

Il existe deux façons d'utiliser des polyfills :

1. polyfill manuellement, comme dans l'exemple ci-dessus
2. ajouter de nombreux polyfills à la fois via une bibliothèque

#### Polyfiller manuellement

Tout d'abord, vous devez **rechercher le polyfill** dont vous avez besoin. Vous devriez pouvoir en trouver un en cherchant sur Google. Des développeurs intelligents ont créé des polyfills pour presque tout ce dont vous aurez jamais besoin.

Une fois que vous avez trouvé le polyfill, **utilisez le processus ci-dessus** pour créer un support pour les anciens navigateurs.

#### Ajouter de nombreux polyfills à la fois

**Certaines bibliothèques contiennent de nombreux polyfills.** [ES6-shim](https://github.com/paulmillr/es6-shim) est un exemple d'une telle bibliothèque. Il fournit un support pour toutes les fonctionnalités ES6 sur les anciens navigateurs.

#### Utiliser des fonctionnalités JavaScript de pointe

Si vous voulez utiliser des fonctionnalités JavaScript de pointe, envisagez d'ajouter [Babel](https://babeljs.io) à votre processus de construction.

Babel est un outil qui compile JavaScript. Pendant ce processus de compilation, il peut :

1. ajouter tout shim/polyfill dont vous avez besoin
2. compiler des préprocesseurs en JavaScript

Plus sur le deuxième point :

Babel fonctionne hors ligne dans votre processus de construction. Il peut lire les fichiers que vous lui passez, puis convertir ces fichiers en JavaScript que le navigateur peut lire.

Cela signifie que vous pouvez utiliser des fonctionnalités de pointe comme Flow, TypeScript et d'autres technologies cool dont vous avez entendu parler. Elles fonctionneront toutes dans les navigateurs, à condition de les passer d'abord par Babel !

#### Que faire si les polyfills ne suffisent pas ?

Si les polyfills ne suffisent pas pour supporter la fonctionnalité, vous pourriez vouloir reconsidérer le niveau de support que vous fournissez pour le navigateur en question.

Devez-vous fournir la même fonctionnalité sur différents navigateurs ? Peut-être devriez-vous envisager l'amélioration progressive à la place.

Peut-être pouvez-vous coder de manière à ne pas utiliser la fonctionnalité ?

Beaucoup de peut-être, mais vous voyez l'idée.

#### Comment savoir si un navigateur supporte la fonctionnalité ?

Tout d'abord, je vérifie [caniuse.com](https://caniuse.com/). Écrivez le nom de la fonctionnalité JavaScript que vous voulez, et vous pourrez voir les niveaux de support des navigateurs.

Voici un exemple avec [Abort Controller](https://caniuse.com/#search=Abort)

![Image](https://cdn-media-1.freecodecamp.org/images/UYLLYIDxtE5PLD6AnfiGsl71ynSKewV3fBFQ)

Si [caniuse.com](https://caniuse.com/) ne me donne aucune information, je vérifie MDN. Vous trouverez le support des navigateurs en bas de la plupart des articles.

Voici à nouveau l'exemple avec [Abort Controller](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) :

![Image](https://cdn-media-1.freecodecamp.org/images/1S4zvx6y-EhvCev6kXUdR2LTVjNpUTirlgQr)

#### Attention au coût de JavaScript

Lorsque vous utilisez des polyfills, vous ajoutez plus de code JavaScript.

Le problème avec l'ajout de plus de JavaScript est, eh bien, qu'il y a plus de JavaScript. Et avec plus de JavaScript viennent plus de problèmes :

1. les anciens navigateurs vivent généralement dans des anciens ordinateurs. Ils peuvent ne pas avoir assez de puissance de traitement.
2. les bundles JavaScript peuvent retarder le chargement du site. Plus d'informations à ce sujet dans « [The cost of JavaScript](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4) » par Addy Osmani

#### Conclusion

Il est facile d'ajouter un support pour les fonctionnalités JavaScript. La plupart du temps, vous ajoutez un polyfill et c'est tout. Mais soyez conscient du coût de JavaScript lorsque vous le faites !

Parfois, il peut être bon d'abandonner complètement la fonctionnalité.

### Pourquoi supporter les anciens navigateurs ?

Pourquoi devez-vous vous soucier des anciens navigateurs ?

Qui utilise les anciens navigateurs ? Probablement des utilisateurs avec de vieux ordinateurs ?

S'ils utilisent de vieux ordinateurs, peut-être qu'ils n'ont pas d'argent pour en acheter un nouveau.

S'ils n'ont pas d'argent pour acheter un nouvel ordinateur, ils n'achèteront probablement rien de vous non plus.

S'ils n'achèteront rien de vous, pourquoi devez-vous vous soucier de supporter leurs navigateurs ?

Pour une personne d'affaires, c'est une pensée parfaitement raisonnable. Mais pourquoi nous, les développeurs, insistons-nous encore pour supporter les anciens navigateurs ?

**Décortiquons cela**

Il y a tant de couches d'hypothèses dans le processus de pensée original.

> « Qui utilise les anciens navigateurs ? Probablement des utilisateurs avec de vieux ordinateurs ? S'ils utilisent de vieux ordinateurs, peut-être qu'ils n'ont pas d'argent pour en acheter un nouveau. »

Bien qu'il soit vrai que les gens utilisent des anciens navigateurs parce qu'ils utilisent de vieux ordinateurs, nous ne pouvons pas supposer que les gens ne peuvent pas se permettre d'en acheter de nouveaux.

* Peut-être que leur entreprise ne veut pas leur en acheter un.
* Peut-être qu'ils sont heureux avec leur ordinateur et ne veulent pas le mettre à niveau.
* Peut-être qu'ils n'ont pas les connaissances pour mettre à niveau leurs ordinateurs.
* Peut-être qu'ils n'ont pas accès à de nouveaux ordinateurs.
* Peut-être qu'ils sont liés à des téléphones mobiles qui n'ont pas de bons navigateurs.

**Ne supposez pas.**

> S'ils n'ont pas d'argent pour acheter un nouvel ordinateur, ils n'achèteront probablement rien de vous non plus. S'ils n'achèteront rien de vous, pourquoi devez-vous vous soucier de supporter leurs navigateurs ?

Nous devons zoomer sur d'autres domaines pour parler de ce point.

#### Accessibilité en fauteuil roulant

Si vous êtes allé à Singapour, vous remarquerez qu'il y a une rampe ou un ascenseur à côté de presque chaque escalier.

Mais pourquoi ? Pourquoi le gouvernement et les entreprises privées dépensent-ils de l'argent pour des ascenseurs et des rampes ? Pourquoi les construire alors que les escaliers suffisent à amener les gens d'un niveau inférieur à un niveau supérieur ?

Il s'avère que certaines personnes ne peuvent pas utiliser les escaliers. Elles ne peuvent pas marcher avec leurs pieds. Elles doivent s'asseoir dans des fauteuils roulants et ne peuvent pas se hisser elles-mêmes sur un escalier. Les ascenseurs et les rampes servent ces personnes.

Et il s'avère que plus de personnes bénéficient des ascenseurs et des rampes.

1. Les personnes qui ont des genoux plus faibles.
2. Les personnes qui ont un vélo ou une trottinette avec elles.
3. Les parents qui poussent une poussette pour bébé.

Si vous vous retrouvez à pousser quelque chose avec des roues, vous utiliserez la rampe ou l'ascenseur sans réfléchir à deux fois. Vous en bénéficiez aussi.

Mais le problème est : Personne ne gagne un seul centime en exploitant les rampes ou les ascenseurs ? Alors pourquoi les construire ?

Parce que cela en vaut la peine.

Et la valeur ne signifie pas toujours de l'argent.

#### Considérez le réchauffement climatique

Vous vivez sur Terre. Que pensez-vous du réchauffement climatique ?

Certaines personnes ne s'en soucient pas. Ce n'est pas grave si les forêts brûlent. Ce n'est pas grave si les entreprises polluent les rivières et rejettent des tonnes de dioxyde de carbone dans l'air. Cela ne les affecte pas.

Mais il y a un groupe de personnes qui s'en soucient. Ils aiment la planète sur laquelle nous vivons. Ils veulent donner à leurs enfants un meilleur endroit où vivre. Il y a beaucoup de raisons pour lesquelles ils s'en soucient. Et ils veulent probablement économiser autant de ressources que possible.

Où vous situez-vous ?

Donneriez-vous de l'argent à une entreprise qui détruit la terre tout en opérant ?

Peut-être que oui. Peut-être que non. Peut-être que vous ne vous en souciez pas. Les trois options sont valides.

Et une fois de plus, vous voyez, ce n'est pas toujours une question d'argent.

#### Le web est pour tout le monde

> Le rêve derrière le Web est celui d'un espace d'information commun dans lequel nous communiquons en partageant des informations.

> — Tim Berners-Lee

Nous, les développeurs frontend, sommes les gardiens du web. La façon dont le web évolue dépend de nous. Nous ne pouvons pas forcer tout le monde à construire des rampes et des ascenseurs, mais nous pouvons nous assurer de les construire nous-mêmes.

Le choix vous appartient, vraiment.

Vous n'avez pas à vous en soucier si vous ne le voulez pas.

La plupart des bons développeurs frontend que je connais ? Ils s'en soucient. Ils choisissent d'être inclusifs. C'est ce qui fait de nous des développeurs frontend.

Nous nous soucions.

Mais parfois, nous avons aussi des contraintes et des limites. Et nous travaillons avec ces limites.

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/).

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.