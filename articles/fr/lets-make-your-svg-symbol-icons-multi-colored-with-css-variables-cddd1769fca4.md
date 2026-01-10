---
title: Créons des icônes multicolores avec des symboles SVG et des variables CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-31T13:25:33.000Z'
originalURL: https://freecodecamp.org/news/lets-make-your-svg-symbol-icons-multi-colored-with-css-variables-cddd1769fca4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WO5mgu0bcFNdt7R6JH6mhQ.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Créons des icônes multicolores avec des symboles SVG et des variables CSS
seo_desc: 'By Sarah Dayan

  Long gone are the days of using images and CSS sprites to make icons for the web.
  With the explosion of web fonts, icon fonts have become the number one solution
  for displaying icons in your web projects.

  Fonts are vectors, so you don’...'
---

Par Sarah Dayan

Les jours où l'on utilisait des images et des sprites CSS pour créer des icônes pour le web sont révolus. Avec l'explosion des polices web, les polices d'icônes sont devenues la solution numéro un pour afficher des icônes dans vos projets web.

Les polices sont des vecteurs, donc vous n'avez pas à vous soucier de la résolution. Elles bénéficient des mêmes propriétés CSS que le texte. Par conséquent, vous avez un contrôle total sur la taille, la couleur et le style. Vous pouvez ajouter des transformations, des effets et des décorations tels que des rotations, des soulignements ou des ombres.

![Image](https://cdn-media-1.freecodecamp.org/images/jPs5hZEkOo7Q7SPfh2fuoQEcU2LGDgFCffM6)
_Pas étonnant que des projets comme Font Awesome aient été téléchargés [plus de 15 millions de fois sur npm seul](http://npm-stats.com/~packages/font-awesome" rel="noopener" target="_blank" title=") à ce jour._

**Les polices d'icônes ne sont pas parfaites cependant**, c'est pourquoi un nombre croissant de personnes préfèrent utiliser des images SVG en ligne. CSS Tricks a écrit une [liste des domaines où les polices d'icônes sont inférieures aux éléments SVG natifs](https://css-tricks.com/icon-fonts-vs-svg) : netteté, positionnement, ou même des échecs en raison du chargement cross-domaine, des bugs spécifiques aux navigateurs et des bloqueurs de publicités. Maintenant, vous pouvez contourner la plupart de ces problèmes, faisant généralement des polices d'icônes un choix sûr.

Pourtant, il y a une chose qui reste absolument impossible avec les polices d'icônes : **le support multicolore**. Seul le SVG peut le faire.

**_TL;DR_**_: cet article approfondit le comment et le pourquoi. Si vous voulez comprendre tout le processus de réflexion, continuez à lire. Sinon, vous pouvez regarder le code final sur [CodePen](https://codepen.io/sarahdayan/pen/GOzaEQ)._

### Installation des icônes de symboles SVG

Le problème avec les SVG en ligne est leur verbosité. Vous ne voulez pas copier/coller toutes ces coordonnées chaque fois que vous avez besoin d'utiliser la même icône. Cela serait répétitif, difficile à lire et un casse-tête à maintenir.

Avec les icônes de symboles SVG, vous avez une copie de chaque élément SVG, et vous les instanciez n'importe où avec une référence.

Vous commencez par inclure le SVG en ligne, le masquer, l'envelopper dans un `<symbol>` et l'identifier avec un attribut id.

```
<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path d="..." />  </symbol></svg>
```

_Le balisage SVG complet est inclus une fois et masqué dans le HTML._

Ensuite, tout ce que vous avez à faire est d'instancier l'icône avec un élément `<use>`.

```
<svg>  <use xlink:href="#my-first-icon" /></svg>
```

_Cela affichera une copie exacte de votre icône SVG originale._

![Image](https://cdn-media-1.freecodecamp.org/images/h50v1hbWZfisticSZPXcpnw8B27gYBQS-bpK)

**C'est tout !** Plutôt bien, non ?

Vous avez probablement remarqué l'attribut étrange `xlink:href` : c'est le lien entre votre instance et le SVG original.

Il est important de mentionner que `xlink:href` est un attribut SVG obsolète. Même si la plupart des navigateurs le supportent encore, **vous devriez utiliser `href` à la place**. Maintenant, le problème est que certains navigateurs comme Safari ne supportent pas les références de ressources SVG via l'attribut `href`, donc vous devez encore fournir `xlink:href`.

Pour être sûr, fournissez les deux attributs.

### Ajouter de la couleur

Contrairement aux polices, `color` n'a aucun effet sur les icônes SVG : vous devez utiliser les attributs `fill` pour définir une couleur. Cela signifie qu'elles n'héritent pas de la couleur du texte parent comme le font les polices d'icônes, mais vous pouvez toujours les styliser en CSS.

```
// HTML<svg class="icon">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon {  width: 100px;  height: 100px;  fill: red;}
```

À partir de là, vous pouvez créer d'autres instances de la même icône avec une couleur de remplissage différente.

```
// HTML<svg class="icon icon-red">  <use xlink:href="#my-first-icon" /></svg>
```

```
<svg class="icon icon-blue">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon {  width: 100px;  height: 100px;}.icon-red {  fill: red;}.icon-blue {  fill: blue;}
```

Cela fonctionne, mais ce n'est pas **exactement** ce que nous voulons. Jusqu'à présent, tout ce que nous avons fait peut être réalisé avec une police d'icônes régulière. Ce que nous voulons, c'est avoir une **différente** couleur pour chaque **partie** de l'icône. Nous voulons remplir chaque **chemin** avec une couleur différente, sans altérer les autres instances, et nous voulons pouvoir la remplacer si nécessaire.

Au début, vous pourriez être tenté de vous appuyer sur la spécificité.

```
// HTML<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path class="path1" d="..." />    <path class="path2" d="..." />    <path class="path3" d="..." />  </symbol></svg>
```

```
<svg class="icon icon-colors">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon-colors .path1 {  fill: red;}.icon-colors .path2 {  fill: green;}.icon-colors .path3 {  fill: blue;}
```

**Cela ne fonctionnera pas.**

Nous essayons de styliser `.path1`, `.path2` et `.path3` comme s'ils étaient imbriqués dans `.icon-colors`, mais techniquement parlant **ils ne le sont pas**. L'élément `<use>` n'est **pas un espace réservé** qui est remplacé par votre définition SVG. **C'est une référence** qui clone le contenu auquel il pointe dans [le DOM de l'ombre](https://developer.mozilla.org/fr/docs/Web/Web_Components/Shadow_DOM).

**Que pouvons-nous faire alors ?** Comment pouvons-nous affecter le contenu des enfants de manière limitée lorsque lesdits enfants ne sont pas dans le DOM ?

### Les variables CSS à la rescousse

En CSS, [certaines propriétés](https://developer.mozilla.org/fr/docs/Web/CSS/héritage) sont héritées des ancêtres aux enfants. Si vous attribuez une couleur de texte au `body`, tout le texte de la page héritera de cette couleur jusqu'à ce qu'elle soit remplacée. L'ancêtre n'est pas conscient des enfants, mais les styles **héritables** sont toujours propagés.

Dans notre exemple précédent, nous avons hérité de la propriété `fill`. Regardez à nouveau, et vous verrez que la classe dans laquelle nous avons déclaré une couleur `fill` est ajoutée sur les **instances**, pas sur les définitions. C'est ainsi que nous avons pu obtenir différentes couleurs pour chaque instance d'une seule définition.

Maintenant, voici le problème : nous voulons passer des couleurs **différentes** à des **chemins** **différents** du SVG original, mais il n'y a qu'un seul attribut `fill` dont nous pouvons hériter.

Rencontrez les **variables CSS**.

Les variables CSS sont déclarées dans les règles comme n'importe quelle autre propriété. Vous pouvez les nommer comme vous le souhaitez et leur attribuer n'importe quelle valeur CSS valide. Ensuite, vous les déclarez comme **valeur** pour elles-mêmes, ou pour n'importe quelle propriété enfant, et **elles seront héritées**.

```
.parent {  --custom-property: red;  color: var(--custom-property);}
```

_Tous les enfants de `.parent` auront du texte rouge._

```
.parent {  --custom-property: red;}.child {  color: var(--custom-property);}
```

_Tous les `.child` imbriqués dans les éléments `.parent` auront du texte rouge._

Maintenant, appliquons ce concept à notre symbole SVG. Nous utiliserons l'attribut `fill` sur chaque chemin de la définition SVG, et nous les définirons avec différentes variables CSS. Ensuite, nous leur attribuerons différentes couleurs.

```
// HTML<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path fill="var(--color-1)" d="..." />    <path fill="var(--color-2)" d="..." />    <path fill="var(--color-3)" d="..." />  </symbol></svg>
```

```
<svg class="icon icon-colors">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon-colors {  --color-1: #c13127;  --color-2: #ef5b49;  --color-3: #cacaea;}
```

Et... **ça marche** ! ✨

![Image](https://cdn-media-1.freecodecamp.org/images/YsRaKkdEcVKJNcnPE1ezPjuEt1eVAOmOvNq6)

Désormais, tout ce que nous avons à faire pour créer une instance avec un schéma de couleurs différent est de créer une nouvelle classe.

```
// HTML<svg class="icon icon-colors-alt">  <use xlink:href="#my-first-icon" /></svg>
```

```
// CSS.icon-colors-alt {  --color-1: brown;  --color-2: yellow;  --color-3: pink;}
```

Si vous souhaitez toujours avoir des icônes monochromes, **vous n'avez pas à répéter la même couleur sur chaque variable CSS**. Au lieu de cela, vous pouvez déclarer une seule règle `fill` : parce que les variables CSS ne sont pas définies, elle reviendra à votre déclaration `fill`.

```
.icon-monochrome {  fill: grey;}
```

_Votre déclaration `fill` fonctionnera parce que les attributs `fill` sur le SVG original sont définis avec des valeurs de variables CSS non définies._

### Comment nommer mes variables CSS ?

Il y a généralement deux routes que vous pouvez prendre lorsque vous nommez des choses en CSS : **descriptif** ou **sémantique**. Descriptif signifie appeler une couleur **ce qu'elle est** : si vous stockez `#ff0000`, vous l'appellerez `--red`. Sémantique signifie appeler la couleur par **comment elle est appliquée** : si vous utilisez `#ff0000` pour l'anse d'une tasse de café, vous l'appellerez `--cup-handle-color`.

Les noms descriptifs peuvent être votre premier instinct. Cela semble plus DRY puisque `#ff0000` peut être utilisé pour autre chose que l'anse de la tasse de café. Une variable CSS `--red` est réutilisable pour d'autres chemins d'icônes qui doivent être rouges. Après tout, c'est ainsi que fonctionne le CSS utilitaire et [c'est un système correct](https://frontstuff.io/in-defense-of-utility-first-css).

Le problème est que, dans notre cas, **nous ne pouvons pas appliquer des classes granulaires aux éléments que nous voulons styliser**. Les principes utilitaires ne peuvent pas s'appliquer, car nous avons une seule référence pour chaque icône, et nous devons la styliser par le biais de variations de classe.

L'utilisation de noms de classes sémantiques, comme `--cup-handle-color` par exemple, a plus de sens pour ce cas d'utilisation. Lorsque vous voulez changer la couleur d'une partie d'une icône, vous savez instantanément ce que c'est et ce qu'il faut remplacer. Le nom de la classe restera pertinent quelle que soit la couleur que vous attribuez.

### Par défaut ou non

Il est tentant de faire de la version multicolore de vos icônes leur état par défaut. De cette façon, vous pourriez les utiliser sans avoir besoin de style supplémentaire, et vous ajouteriez vos propres classes uniquement lorsque nécessaire.

Il existe deux façons d'y parvenir : **:root** et **var() default**.

### :root

Vous pouvez définir toutes vos variables CSS sur le sélecteur `:root`. Cela les conserve toutes au même endroit et vous permet de "partager" des couleurs similaires. `:root` a la priorité la plus faible, il reste donc facile à remplacer.

```
:root {  --color-1: red;  --color-2: green;  --color-3: blue;  --color-4: var(--color-1);}
```

```
.icon-colors-alt {  --color-1: brown;  --color-2: yellow;  --color-3: pink;  --color-4: orange;}
```

Cependant, **il y a des inconvénients majeurs à cette méthode**. Tout d'abord, garder les définitions de couleurs séparées de leurs icônes respectives peut être déroutant. Lorsque vous décidez de les remplacer, vous devez aller et venir entre la classe et le sélecteur `:root`. Mais plus important encore, **cela ne vous permet pas de limiter la portée de vos variables CSS**, vous empêchant ainsi de réutiliser les mêmes noms.

La plupart du temps, lorsqu'une icône n'utilise qu'une seule couleur, j'utilise le nom `--fill-color`. C'est simple, compréhensible, et cela a du sens d'utiliser le même nom pour toutes les icônes qui n'ont besoin que d'une couleur de remplissage. Si je dois déclarer toutes les variables dans la déclaration `:root`, je ne peux pas avoir plusieurs `--fill-color`. Je serai obligé de définir `--fill-color-1`, `--fill-color-2`, ou d'utiliser des espaces de noms comme `--star-fill-color`, `--cup-fill-color`.

### var() default

La fonction `var()`, que vous utilisez pour attribuer une variable CSS à une propriété, peut prendre une valeur par défaut comme deuxième argument.

```
<svg xmlns="http://www.w3.org/2000/svg" style="display: none">  <symbol id="my-first-icon" viewBox="0 0 20 20">    <title>my-first-icon</title>    <path fill="var(--color-1, red)" d="..." />    <path fill="var(--color-2, blue)" d="..." />    <path fill="var(--color-3, green)" d="..." />  </symbol></svg>
```

Jusqu'à ce que vous définissiez `--color-1`, `--color-2` et `--color-3`, l'icône utilisera les valeurs par défaut que vous avez définies pour chaque `<path>`. Cela résout le problème de portée globale que nous avons lorsque nous utilisons `:root`, mais soyez prudent : vous avez maintenant une valeur par défaut et elle fait son travail. Par conséquent, vous ne pouvez plus utiliser une déclaration `fill` unique pour définir des icônes monochromes. Vous devrez attribuer la couleur à chaque variable CSS utilisée sur l'icône, une par une.

Définir des valeurs par défaut peut être utile, mais c'est un compromis. Je vous suggère de ne pas en faire une habitude et de le faire uniquement lorsque cela a du sens pour un projet donné.

### À quel point tout cela est-il compatible avec les navigateurs ?

[Les variables CSS sont compatibles avec la plupart des navigateurs modernes](https://caniuse.com/#feat=css-variables), mais comme vous vous en doutez probablement, Internet Explorer ne les supporte **pas du tout**. Pas même IE11, et puisque le développement a été abandonné au profit de Edge, il n'y a aucune chance qu'il se mette un jour à jour.

Maintenant, simplement parce qu'une fonctionnalité n'est pas supportée par un navigateur auquel vous devez vous adapter, cela ne signifie pas que vous devez l'exclure complètement. Dans de tels cas, optez pour une **dégradation élégante** : offrez des icônes multicolores aux navigateurs modernes et fournissez une couleur de remplissage de secours pour les plus anciens.

Ce que vous voulez faire, c'est définir une déclaration qui ne fonctionnera que si les variables CSS ne sont pas supportées. Cela peut être réalisé en définissant la propriété `fill` avec la couleur de secours : si les variables CSS sont supportées, elle ne sera même pas prise en compte. Si elles ne le sont pas, votre déclaration `fill` s'appliquera.

Si vous utilisez Sass, cela peut être abstrait dans un `@mixin`.

```
@mixin icon-colors($fallback: black) {  fill: $fallback;  @content;}
```

Nous pouvons maintenant définir des schémas de couleurs sans nous soucier de la compatibilité des navigateurs.

```
.cup {  @include icon-colors() {    --cup-color: red;    --smoke-color: grey;  };}
```

```
.cup-alt {  @include icon-colors(green) {    --cup-color: green;    --smoke-color: grey;  };}
```

_Passer les variables CSS dans le mixin via `@content` est facultatif. Si vous le faites à l'extérieur, le CSS compilé sera le même. Mais cela peut être utile de tout regrouper en un seul endroit : vous pouvez plier des extraits dans votre éditeur et identifier visuellement les déclarations qui vont ensemble._

Consultez [ce stylo](https://codepen.io/sarahdayan/pen/GOzaEQ/) sur différents navigateurs. Sur les versions à jour de Firefox, Chrome et Safari, les deux dernières tasses seront respectivement rouges avec de la fumée grise et bleues avec de la fumée grise. Sur Internet Explorer et Edge avant la version 15, la troisième tasse sera toute rouge et la quatrième sera toute bleue ! ✨

Si vous voulez en savoir plus sur les icônes de symboles SVG (et le SVG en général), je vous **recommande vivement** de lire [tout ce qui est écrit par Sara Soueidan](https://www.sarasoueidan.com/blog). Et si vous avez des questions sur les icônes de symboles CSS, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/frontstuff_io) !

_Initialement publié sur [frontstuff.io](https://frontstuff.io/multi-colored-svg-symbol-icons-with-css-variables)._