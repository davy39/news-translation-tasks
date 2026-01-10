---
title: Comment générérer toutes vos classes utilitaires avec les Maps Sass
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-01T17:14:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-all-your-utility-classes-with-sass-maps-8921ab3b4508
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HJAnPhGEMFf-pqxuuW8yyw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment générérer toutes vos classes utilitaires avec les Maps Sass
seo_desc: 'By Sarah Dayan

  One of the powers of utility classes lies in giving you access to every small concept
  of your design system in a slew of contexts. If your main color is royal blue, you
  can apply it as a text color on anything with a .text-royal-blue c...'
---

Par Sarah Dayan

L'un des pouvoirs des classes utilitaires réside dans le fait de vous donner accès à chaque petit concept de votre système de design dans une multitude de contextes. Si votre couleur principale est le bleu royal, vous pouvez l'appliquer comme couleur de texte sur n'importe quoi avec une classe `.text-royal-blue`, comme couleur de fond avec une classe `.bg-royal-blue`, et ainsi de suite.

Mais comment les écrire de manière efficace, cohérente et évolutive ?

**_TL;DR_** : cet article approfondit les aspects pratiques. Si vous voulez comprendre tout le processus de réflexion, continuez à lire. Sinon, vous pouvez récupérer le code sur [GitHub](https://gist.github.com/sarahdayan/4d2cc04a636e8039f10a889a0e29fbd9) ou le tester sur [SassMeister](https://www.sassmeister.com/gist/4d2cc04a636e8039f10a889a0e29fbd9).

```
$royal-blue: #0007ff;
```

```
.text-royal-blue {  color: $royal-blue;}
```

```
.bg-royal-blue {  background: $royal-blue;}
```

```
...
```

C'est répétitif. Non seulement vous tapez à la main le nom et la valeur de la couleur à chaque fois, mais vous créez également un système difficile à maintenir. Que se passe-t-il lorsque vous avez dix utilitaires de couleur comme ceux-ci, et que vous devez ajouter une couleur supplémentaire au schéma ?

Vous ne devriez pas passer de temps sur des tâches fastidieuses et répétitives. **C'est pour cela que les langages de script existent**. Si vous utilisez déjà Sass, vous devez exploiter sa puissance et le laisser vous aider.

### Qu'est-ce que les Maps Sass ?

Les [Maps](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#Maps) sont un type de données Sass qui représentent **une association entre des clés et des valeurs**. Si vous êtes familier avec d'autres langages de script, vous pourriez les voir comme un [tableau associatif](https://en.wikipedia.org/wiki/Associative_array). Cela vous permet de stocker des données et d'avoir un nom pour référencer chaque élément.

Les [Listes](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#Lists) et les maps sont un peu similaires, en ce sens qu'elles stockent toutes deux une collection de données et qu'elles sont toutes deux itérables dans une boucle `@each`. Mais contrairement aux listes, les maps permettent de référencer facilement n'importe quel élément en l'appelant par son nom. Cela les rend idéales pour regrouper des informations logiquement liées.

```
$colors: (  mako-grey: #404145,  fuel-yellow: #ecaf2d,  pastel-green: #5ad864);
```

### Ajoutons un peu de logique

Maintenant que nos couleurs sont soigneusement stockées dans une map, nous devons l'itérer pour générer nos classes utilitaires. Pour cela, nous allons utiliser la directive `@each` à l'intérieur d'un `@mixin` que nous inclurons plus tard dans notre classe de base utilitaire.

```
@mixin color-modifiers {  // faire des choses}
```

Utilisons maintenant la directive `@each` pour parcourir `$colors` et récupérer les bonnes données.

```
@mixin color-modifiers {  @each $name, $hex in $colors {    // faire des choses  }}
```

Nous parcourons `$colors` et à chaque boucle, la clé actuelle sera référencée dans `$name` et le code hexadécimal de la couleur sera dans `$hex`. Nous pouvons commencer à construire notre règleset.

```
@mixin color-modifiers {  @each $name, $hex in $colors {    &-#{$name} {      color: $hex;    }  }}
```

Maintenant, pour chaque paire dans la map, `@each` générera un règleset qui référence le sélecteur parent avec le caractère `&`, ajoute un tiret et le nom de la couleur, et définit l'attribut `color` à la valeur hexadécimale actuelle.

En d'autres termes, faire ceci :

```
.text {  @include color-modifiers;}
```

Générera ceci :

```
.text-mako-grey {  color: #404145;}.text-fuel-yellow {  color: #ecaf2d;}.text-pastel-green {  color: #5ad864;}
```

Plutôt bien, n'est-ce pas ? En fait, nous n'avons fait qu'effleurer la surface. Pour l'instant, notre mixin ne peut générer que des règles avec l'attribut `color`. Que faire si nous voulons créer des classes utilitaires pour les couleurs de fond ?

Heureusement, Sass nous permet de passer des arguments aux mixins.

```
@mixin color-modifiers($attribute: 'color') {  @each $name, $hex in $colors {    &-#{$name} {      #{$attribute}: $hex;    }  }}
```

Maintenant, nous pouvons spécifier exactement quel attribut nous voulons.

Améliorons un peu plus notre mixin : actuellement, le préfixe du modificateur est un tiret codé en dur. Cela signifie que vos classes seront toujours sous la forme `.base-modifier`. Que faire si vous avez besoin de le changer ? Que faire si vous voulez également générer des modificateurs de style BEM (avec deux tirets) ? Encore une fois, c'est quelque chose que nous pouvons réaliser en utilisant des arguments.

```
@mixin color-modifiers($attribute: 'color', $prefix: '-') {  @each $name, $hex in $colors {    &#{$prefix}#{$name} {      #{$attribute}: $hex;    }  }}
```

Maintenant, nous pouvons générer des classes de modificateurs avec n'importe quel type de préfixe que nous voulons. Donc, faire ceci :

```
.text {  @include color-modifiers($prefix: '--');}
```

Générera ceci :

```
.text--mako-grey {  color: #404145;}.text--fuel-yellow {  color: #ecaf2d;}.text--pastel-green {  color: #5ad864;}
```

**Astuce pro** : dans Sass, vous pouvez nommer explicitement les arguments lorsque vous appelez un mixin ou une fonction (comme dans l'exemple ci-dessus). Cela évite d'avoir à les fournir dans l'ordre.

### Maps dans les maps

J'aime utiliser un système de couleurs légèrement différent afin de pouvoir gérer les variations tonales. En imbriquant des maps dans des maps, j'ai un moyen propre et lisible de garder les nuances regroupées.

```
$colors: (  grey: (    base: #404145,    light: #c7c7cd  ),  yellow: (    base: #ecaf2d  ),  green: (    base: #5ad864  ));
```

Si nous voulons travailler avec un tel système de couleurs, nous devons adapter notre mixin pour qu'il itère un niveau plus profond.

```
@mixin color-modifiers($attribute: 'color', $prefix: '-', $separator: '-') {  @each $name, $color in $colors {    &#{$prefix}#{$name} {      @each $tone, $hex in $color {        &#{$separator}#{$tone} {          #{$attribute}: $hex;        }      }    }  }}
```

Nous avons ajouté un nouvel argument, `$separator`, pour lier le nom de la couleur et le ton. Nous aurions pu utiliser le `$prefix` mais il n'a pas le même but. Utiliser une variable dédiée avec une valeur par défaut est un meilleur choix, car cela nous donne une liberté totale lorsque nous utilisons le mixin.

Maintenant, faire ceci :

```
.text {  @include color-modifiers;}
```

Générera ceci :

```
.text-grey-base {  color: #404145;}.text-grey-light {  color: #c7c7cd;}.text-yellow-base {  color: #ecaf2d;}.text-green-base {  color: #5ad864;}
```

Super ! Nous avons maintenant des helpers composés d'une classe de base, d'une couleur et d'un ton. Une chose que nous devons améliorer, cependant, est la façon dont les modificateurs de couleur de base sont générés. En fait, nous n'avons pas besoin de ce suffixe `-base` — la classe de base et la couleur suffisent.

Ce que nous devons faire, c'est vérifier le ton dans la boucle `@each` imbriquée, et ne l'afficher que lorsque ce n'est pas « base ». Heureusement pour nous, Sass a déjà tout ce dont nous avons besoin.

### @if, @else, if()

Notre premier instinct pourrait être d'utiliser les directives `@if/@else`. Le problème est que cela nous forcerait à répéter du code et entraînerait un code compliqué. Au lieu de cela, nous allons utiliser l'une des armes secrètes de Sass : `if()`.

`if()` est l'opérateur conditionnel (ternaire) de Sass. Il prend trois arguments : une condition et deux instructions de retour. Si la condition est remplie, `if()` retournera la première instruction. Sinon, il retournera la seconde. Vous pouvez le voir comme un raccourci pour `@if/@else`.

```
@mixin color-modifiers($attribute: 'color', $prefix: '-', $separator: '-', $base: 'base') {  @each $name, $color in $colors {    &#{$prefix}#{$name} {      @each $tone, $hex in $color {        &#{if($tone != $base, #{$separator}#{$tone}, '')} {          #{$attribute}: $hex;        }      }    }  }}
```

Chaque fois que la boucle `@each` imbriquée analysera un `$tone` différent de « base », elle retournera le `$separator` et le `$tone` comme suffixe de classe. Sinon, elle ne retournera rien, laissant la classe telle quelle.

```
.text-grey {  color: #404145;}.text-grey-light {  color: #c7c7cd;}.text-yellow {  color: #ecaf2d;}.text-green {  color: #5ad864;}
```

### Tout assécher (DRY)

Dans un projet réel, il est probable que vous souhaitiez utiliser diverses structures de maps. Par exemple, vous pourriez avoir des maps à un niveau de profondeur pour les tailles de police et des maps à deux niveaux de profondeur pour les couleurs. **Vous n'allez pas écrire un mixin différent pour chaque niveau de profondeur**. Cela serait répétitif et difficile à maintenir. Vous devez pouvoir compter sur un seul mixin pour gérer cela.

Nous voulons un mixin générique pour générer tous les modificateurs, et un qui soit capable de gérer des maps multidimensionnelles. Si vous comparez les deux mixins que nous avons conçus dans ce tutoriel, vous remarquerez qu'ils se ressemblent beaucoup. La seule différence est que l'un effectue une boucle supplémentaire avant d'imprimer la déclaration CSS calculée. C'est un travail typique pour un **mixin récursif**.

Il commencera par une directive `@each` où nous pouvons commencer à construire notre sélecteur. C'est là que nous vérifierons si la `$key` actuelle est égale à « base » afin de décider de l'afficher ou non. Ensuite, nous vérifierons si la `$value` actuelle est elle-même une map : si oui, nous devons exécuter à nouveau le mixin à partir de là où nous sommes et lui passer la map imbriquée. Sinon, nous pouvons imprimer la déclaration CSS.

```
@mixin modifiers($map, $attribute, $prefix: '-', $separator: '-', $base: 'base') {  @each $key, $value in $map {    &#{if($key != $base, #{$prefix}#{$key}, '')} {      @if type-of($value) == 'map' {        @include modifiers($value, $attribute, $separator);      }      @else {        #{$attribute}: $value;      }    }  }}
```

Et _voilà_ ! Ce mixin fonctionnera avec des maps de n'importe quelle profondeur. N'hésitez pas à l'utiliser dans vos propres projets ! Si vous l'aimez, vous pouvez montrer votre soutien en [l'étoilant sur GitHub](https://gist.github.com/sarahdayan/4d2cc04a636e8039f10a889a0e29fbd9). De plus, si vous souhaitez l'améliorer, veuillez laisser un commentaire sur le gist afin que je puisse le mettre à jour ?

_Originalement publié sur [frontstuff.io](https://frontstuff.io/generate-all-your-utility-classes-with-sass-maps).