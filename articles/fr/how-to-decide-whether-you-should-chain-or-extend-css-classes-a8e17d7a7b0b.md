---
title: Comment décider si vous devez chaîner ou étendre des classes CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T21:38:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-decide-whether-you-should-chain-or-extend-css-classes-a8e17d7a7b0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F4cl96xj67BOs1-4QVq0Rg.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment décider si vous devez chaîner ou étendre des classes CSS
seo_desc: 'By Sarah Dayan

  If you’re building an app or a website that changes often, modular CSS methods solve
  many issues. Instead of copying your HTML structure in CSS and decorating it, you
  create consumable libraries of components. This makes projects more ...'
---

Par Sarah Dayan

Si vous construisez une application ou un site web qui change souvent, les méthodes CSS modulaires résolvent de nombreux problèmes. Au lieu de copier votre structure HTML en CSS et de la décorer, vous créez des bibliothèques de composants consommables. Cela rend les projets plus évolutifs et maintient la base de code CSS sous contrôle.

La modularité CSS repose sur la composition, ce qui alourdit inévitablement le HTML. Cet effet collatéral peut être un frein significatif pour beaucoup de gens en raison du "bloat" qu'il crée.

Dans cet article, nous comparerons deux techniques : **le chaînage** et **l'extension**. Nous verrons ce qu'elles offrent et quels sont leurs inconvénients afin que vous puissiez faire des choix plus éclairés.

### Chaînage

Le chaînage des classes CSS signifie **composer l'apparence souhaitée en ajoutant des modificateurs granulaires ensemble sur un sélecteur HTML**. Les styles composites créent le résultat visuel final. C'est le comportement par défaut avec la plupart des méthodologies CSS modulaires.

Prenons le code OOCSS suivant pour un bouton :

```
.btn {  display: block;  box-shadow: 0 0 5px 0 rgba(0, 0, 0, .2);}
.btn-default {  border: 3px solid grey;}
.btn-primary {  background: purple; color: white;}
```

Si vous deviez chaîner des modificateurs, votre HTML ressemblerait à ceci :

```
<button class="btn btn-primary">Bouton principal</button>
<button class="btn btn-default">Bouton par défaut</button>
```

Faisons maintenant quelque chose un peu plus complexe, cette fois avec BEM (bloc, élément, modificateur) :

```
<div class="media-object media-object--reverse media-object--outlined">  <div class="media-object__media">    <img class="media-object__img media-object__img--faded img img--square" src="..." alt="...">  </div>  <div class="media-object__body">...</div></div>
```

Ici, nous avons beaucoup plus de classes interactives :

* Le bloc `.media-object` a plusieurs modificateurs (`.media-object--reverse` et `.media-object--outlined`).
* L'élément `.media-object__img` a un modificateur (`.media-object__img--faded`).
* L'élément `.media-object__img` est également un bloc `.img` avec son propre modificateur (`.img--square`).

#### Avantages

Le principal avantage du chaînage des classes est la **responsabilité séparée**. Cela maintient votre base de code CSS propre, légère, confortable à lire et non répétitive. Ce que chaque classe fait est clair, et vous savez immédiatement ce que vous devriez utiliser et ce que vous ne devriez pas.

**Cela empêche également le code mort : puisque vous travaillez avec des blocs de construction, tout est potentiellement utile.** Lorsque vous supprimez un composant, vous n'avez besoin de supprimer que le HTML.

Les modificateurs séparés sont excellents pour représenter l'état. Ainsi, cela facilite la vie des ingénieurs JavaScript. Tout ce qu'ils ont à faire est d'ajouter et de supprimer des classes.

Sur les grands projets, **cette méthode peut vous faire gagner beaucoup de temps**.

#### Inconvénients

L'un des problèmes les plus courants que les gens ont avec le CSS modulaire est qu'il crée une "folie de classes" dans le HTML. Strictement parlant, c'est vrai.

Les modèles de conception qui séparent les responsabilités résultent presque toujours en plus de fichiers et de code verbeux. Le CSS ne fait pas exception : **si vous choisissez une méthode qui est censée rendre votre base de code plus maintenable, le contrepartie est des fichiers HTML longs**.

De nos jours, avoir à taper autant de code devient de moins en moins un problème, car la plupart des éditeurs et IDE offrent une autocomplétion puissante. Mais maintenant, c'est encore plus de code à écrire chaque fois que vous créez une nouvelle page ou composez un nouveau composant. Avec le temps, cela peut induire un sentiment de désordre et de redondance qui rebutera certains développeurs.

### Extension

Si vous ne voulez pas chaîner les classes, vous pouvez les étendre. Nous avons toujours les mêmes blocs séparés, mais au lieu de les chaîner dans le HTML, **nous héritons des propriétés de la classe de base à ses modificateurs**. De cette façon, nous pouvons les utiliser tous à la fois.

Utilisons la fonction `@extend` dans Sass pour ce faire :

```
.btn {  display: block;  box-shadow: 0 0 5px 0 rgba(0, 0, 0, .2);  &-default {    @extend .btn;    border: 3px solid grey;  }  &-primary {    @extend .btn;    background: purple;    color: white;  }}
```

Cela se transformera en l'extrait CSS suivant :

```
.btn,.btn-default,.btn-primary {  display: block;  box-shadow: 0 0 5px 0 rgba(0, 0, 0, .2);}
.btn-default {  border: 3px solid grey;}
.btn-primary {  background: purple; color: white;}
```

Avec le CSS ci-dessus, notre HTML ressemblerait à ceci :

```
<button class="btn-primary">Bouton principal</button>
<button class="btn-default">Bouton par défaut</button>
```

Au lieu d'avoir une multitude de classes apparemment répétitives, nous n'en avons qu'une. Elle a un nom explicite et maintient le code lisible. Nous pouvons toujours utiliser `.btn` seul, mais si nous avons besoin d'une variation, nous n'avons besoin d'ajouter que la partie modificateur au lieu de chaîner une nouvelle classe.

#### Avantages

**Le point fort de cette méthode est un HTML plus clair, plus lisible et plus léger.** Lorsque vous optez pour le CSS modulaire, vous décidez également de faire plus de HTML et moins de CSS. Le CSS devient une bibliothèque au lieu d'une liste d'instructions. Ainsi, vous passez plus de temps dans le HTML, ce qui explique pourquoi vous pouvez vouloir le garder léger et facile à lire.

#### Inconvénients

Votre CSS peut **sembler** DRY, surtout si vous utilisez un pré-processeur, mais **l'extension de classes résulte en un fichier CSS beaucoup plus lourd**. De plus, vous n'avez pas beaucoup de contrôle sur ce qui se passe : chaque fois que vous utilisez `@extend`, la définition de la classe est déplacée vers le haut et ajoutée à une liste de sélecteurs partageant le même ensemble de règles. Ce processus peut entraîner des remplacements de style étranges et beaucoup plus de code généré.

Il y a aussi le cas où vous voulez utiliser plusieurs modificateurs ensemble. Avec la méthode d'extension, vous ne composez plus dans le HTML. Vous n'avez qu'une solution si vous voulez créer de nouvelles combinaisons : créer encore plus de classes en étendant les modificateurs. **Cela est difficile à maintenir et résulte en plus de code.** Chaque fois que vous devez mélanger des classes, vous devrez modifier le CSS et créer une nouvelle règle potentiellement non réutilisable. Si vous supprimez un jour le HTML qui l'utilise, vous devrez également supprimer la classe CSS.

### Réflexions finales

**Le CSS modulaire a un prix : un HTML plus verbeux**, mais ce n'est pas grand-chose à payer pour tous les avantages qu'il offre. Si vous avez déjà déterminé que vous avez besoin de modularité, ne vous tirez pas une balle dans le pied en utilisant des pratiques incompatibles. Cela entraînera plus de travail pour la moitié des avantages. L'héritage est tentant, mais [la composition a plus d'une fois été reconnue comme une stratégie bien meilleure](https://en.wikipedia.org/wiki/Composition_over_inheritance).

Le "bloat" HTML n'est pas si grave lorsque vous regardez son impact réel. La modularité crée inévitablement plus de code — la méthode que vous choisissez détermine uniquement **où** il va. D'un point de vue performance, [plus de HTML est bien mieux que plus de CSS](https://frontstuff.io/in-defense-of-utility-first-css#it-bloats-the-html).

**Ne vous concentrez pas sur les petites choses qui n'ont pas d'importance.** Au lieu de cela, utilisez des outils qui vous aident à écrire et à naviguer dans le code plus efficacement. Essayez de voir le tableau d'ensemble et faites des choix basés sur des faits, pas sur des préférences personnelles.

_Publié à l'origine sur [frontstuff.io](https://frontstuff.io/should-you-chain-or-extend-css-classes)._