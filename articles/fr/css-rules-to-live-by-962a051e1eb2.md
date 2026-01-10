---
title: Règles CSS qui faciliteront votre vie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:08:28.000Z'
originalURL: https://freecodecamp.org/news/css-rules-to-live-by-962a051e1eb2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*KEpWDREymV7FDijB
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Règles CSS qui faciliteront votre vie
seo_desc: 'By Nick Gard

  After years of writing and maintaining a couple of very large web projects and numerous
  smaller ones, I have developed some heuristics for writing maintainable CSS. I have
  used BEM, SMACSS, and CSS Modules for naming, though this article...'
---

Par Nick Gard

Après des années d'écriture et de maintenance de plusieurs projets web très importants et de nombreux autres plus petits, j'ai développé quelques heuristiques pour écrire du CSS maintenable. J'ai utilisé BEM, SMACSS et CSS Modules pour la nomenclature, bien que cet article ne traite pas spécifiquement de la nomenclature. (J'ai tendance à utiliser un mélange de classes atomiques et de noms de type BEM.) Cet article traite davantage des propriétés et des valeurs que j'utilise ou évite.

> Ma configuration StyleLint : [https://github.com/NickGard/css-utils/blob/master/stylelint.config.json](https://github.com/NickGard/css-utils/blob/master/stylelint.config.json)

#### Couleurs

Un de mes points de frustration est la surabondance de valeurs de couleurs dans un projet web. Un grand projet de longue durée sur lequel j'ai travaillé il y a quelques années avait plus de 300 couleurs uniques déclarées dans environ 40 fichiers CSS. Un tiers de celles-ci étaient des nuances de gris. Les couleurs de la marque étaient répétées avec de légères différences de teinte. Beaucoup de ces couleurs différaient par des valeurs littéralement imperceptibles, comme `#3426D1` et `#3426D2`. La solution à cela est d'utiliser soit des classes de couleurs atomiques, soit des variables (en SCSS ou CSS) pour les couleurs de marque acceptées.

Limiter le nombre de couleurs acceptées a l'avantage supplémentaire de rendre simple le respect des directives de contraste des couleurs WCAG2.0 pour les couleurs de premier plan et d'arrière-plan.

Une autre pratique sujette aux bugs est l'utilisation de couleurs avec canal alpha, généralement en déclarant la couleur avec les fonctions `rgba()` ou `hsla()`. Une couleur créée de cette manière avec une valeur de canal alpha différente de `1` est semi-opaque. La couleur perçue change maintenant en fonction de ce qui se trouve en arrière-plan. Habituellement, la couleur souhaitée est celle que cette couleur a sur un fond blanc, donc vous pouvez utiliser une valeur hexadécimale à la place. Certaines fonctions de préprocesseur, comme `lighten()` de SASS, généreront une couleur semi-opaque, donc restez aux valeurs codées en dur ou aux variables.

#### Typographie

Toutes les propriétés qui affectent ou sont affectées par la police doivent être déclarées une seule fois ensemble. Juste après avoir déclaré les règles `@font-face`, j'aime ajouter des classes atomiques pour la police qui changent la `font-size` (via `rem`) et incluent `line-height`, `letter-spacing` et `word-spacing` qui sont appropriés pour cette combinaison de police et de taille. Après cela, aucune propriété `font-*` ou `text-*` (à l'exception de `text-overflow`) ne doit être utilisée dans un ensemble de règles.

Déclarer ces propriétés une fois en conjonction avec la police garantit que le texte sur le site a toujours l'air correct. Ajuster le `line-height` au lieu du `padding` ou de la `margin` créera des bugs lorsque le texte s'enroule. Ajuster le `font-weight` séparément de la déclaration de la police risque de créer une [fausse police en gras](https://alistapart.com/article/say-no-to-faux-bold/). Changer le `font-style` sur une police qui ne le supporte pas crée une fausse oblique.

Enfin, évitez de définir les tailles de police dans autre chose que des unités `rem`. L'utilisation de `em` pose des problèmes lors de l'imbrication d'éléments car `em` est un multiple scalaire de la `font-size` actuelle. L'utilisation de `px` (ou de toute autre mesure "fixe") risque de créer du texte difficile à lire et [impossible pour l'utilisateur à ajuster](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size#Pixels). Permettez à l'utilisateur (ou au navigateur de l'utilisateur) de définir la `font-size` à ce qui lui convient en ne déclarant pas de `font-size` sur l'élément `body` ou `html` et en utilisant uniquement `rem`.

#### Espacement

Sur un site axé sur le contenu, l'espacement doit compléter le texte. Toute mesure statique, comme `padding: 4px`, semble incorrecte à une certaine taille de police. Une mesure dynamique réactive aux tailles de police, comme `padding: .5em`, semble correcte à chaque taille de police.

Utilisez `em` pour les propriétés d'espacement.

#### Grille

[CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) est très bien supporté (jusqu'à IE10 !) et permet d'organiser le contenu en deux dimensions sans éléments de conteneur supplémentaires comme les éléments de grille `row` ou `col` de Bootstrap. Les designers travaillent souvent avec des grilles à 12 colonnes et les frameworks CSS tendent à suivre cette tendance, mais les grilles, comme tout espacement, doivent compléter le texte, pas le contraindre. Les grilles doivent être écrites ad hoc, pas dans un format prédéterminé sans contexte. Ne gonflez pas votre CSS avec un "framework de grille".

#### Alignement du texte

`text-align` est souvent utilisé pour aligner des éléments autres que du texte. Ce n'est pas l'outil approprié pour cette tâche. Utilisez flexbox pour ce type d'alignement. Utiliser les valeurs `left` et `right` ne fonctionne pas toujours avec les langues qui sont de droite à gauche ou verticales (certains navigateurs mappent ces valeurs aux valeurs relatives au flux `start` et `end`, mais pas tous). Utiliser la valeur `justify` sur du texte peut causer des problèmes dans certaines langues avec des digraphes, et [cela peut causer des problèmes pour les personnes dyslexiques](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align#Accessibility_concerns). Chaque cas d'utilisation de `text-align` est mieux résolu par flexbox, donc utilisez cela à la place. Toujours.

#### Contours

Les contours sur les éléments focus sont la manière native des navigateurs de communiquer quel élément reçoit l'entrée. Les contours par défaut sont généralement suffisamment proéminents pour être utiles à tous les utilisateurs, y compris ceux ayant besoin d'un contraste élevé. Le contour par défaut est généralement écrasé (ou supprimé) car il ne correspond pas au design du site. À moins que vous ne remplaciez le style de contour `outline` focus par un autre indicateur de focus proéminent et accessible, **ne supprimez pas ou ne neutralisez pas la propriété de contour**.

#### Focus & Survol

Comme mentionné ci-dessus, méfiez-vous de changer le style `:focus` car il agit comme un indicateur pour savoir quel élément reçoit actuellement l'entrée. Ajouter des styles à un élément sur `:hover` est souvent une belle touche, mais n'utilisez pas ce pseudo-sélecteur pour afficher du texte supplémentaire à moins de faire de même pour `:focus` (et, bien sûr, si l'élément est focusable). Il est généralement, mais pas toujours, une bonne idée d'utiliser à la fois les pseudo-sélecteurs `:hover` et `:focus` pour le même ensemble de règles. (Ajouter le sélecteur `:focus` aux styles de survol pour un bouton peut faire qu'un bouton pressé semble "bloqué".)

#### Opacité

Définir l'`opacity` d'un élément à `0` ne le cache pas réellement des outils d'accessibilité. L'élément occupe toujours de l'espace dans le flux du document et son texte est toujours lu par les lecteurs d'écran. Les deux seuls cas d'utilisation qui justifient raisonnablement l'utilisation de la propriété `opacity` sont lors de la transition d'un élément dans la vue (transition rapide de `0` à `1`) et lors du style d'un calque de dialogue (pour que le contenu en dessous soit quelque peu visible). Méfiez-vous des calques semi-opaques "empilés". Le niveau d'opacité est multiplicatif, donc le contenu sous deux calques chacun avec `opacity: 50%` est affiché comme s'il était sous un seul élément avec `opacity: 25%`.

#### Sélecteurs

Restez à l'utilisation de sélecteurs de classe et de type classe. L'utilisation d'ID, de type et de sélecteurs universels entraîne des maux de tête. En termes de spécificité CSS, les sélecteurs d'ID l'emporteront toujours sur tout autre sélecteur, mais les [attributs id](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id) [doivent être uniques](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/id) (par page), donc ils ne sont pas utiles pour appliquer des styles réutilisables.

La performance des sélecteurs dans les navigateurs modernes est une préoccupation négligeable, donc malgré ce que vous avez pu entendre sur le sélecteur universel (`*`) n'étant pas performant, ma vraie préoccupation avec son utilisation est qu'il est trop général pour presque tous les cas d'utilisation. Utiliser un sélecteur comme `.my-class > *` finira par nécessiter d'exclure certains enfants, donc vous feriez mieux d'ajouter des classes aux éléments que vous souhaitez styliser et de les cibler directement.

Un argument similaire peut être fait pour ne pas utiliser les sélecteurs de type, comme `div`, `main`. Ils tendent à correspondre à trop d'éléments et nécessitent généralement plus de détails pour être utiles, comme `div.some-class`. Les sélecteurs composés comme celui-ci ont une spécificité plus élevée qu'un sélecteur de classe unique, un problème générateur de bugs abordé ci-dessous.

Restez aux sélecteurs de classe (`.class`), d'attribut (`[attribute]`) et de pseudo-classe (`:focus`). Ils ont tous le même niveau de spécificité.

#### Spécificité

À l'opposé du spectre des sélecteurs trop généraux (comme l'utilisation de `*`) se trouvent les sélecteurs trop spécifiques. Les deux cas causent des problèmes. Un sélecteur trop spécifique engendre des sélecteurs encore plus spécifiques ou les redoutables déclarations `!important`. Chaque sélecteur successif devient un nouvel obstacle à surmonter lors des modifications de style, et suivre ce chemin conduit aux feuilles de style fragiles et toujours croissantes que nous redoutons tous de travailler.

Le CSS a une spécificité naturellement croissante — l'ordre des ensembles de règles. Cela fait partie de [la cascade dans les feuilles de style en cascade](https://medium.com/@ntgard/cascades-in-css-e79f8c0f4df2). Avec cela à l'esprit, nous pouvons écrire des ensembles de règles dans l'ordre croissant d'« importance » sans augmenter le niveau de spécificité du sélecteur. Par exemple :

```
.btn {  color: black;}
.btn--primary {  color: green;}
.btn--primary--light {  color: white;}
```

Dans cet exemple, chaque sélecteur de classe unique est plus spécifique que son prédécesseur, éliminant le besoin de déclarer un ensemble de règles pour `.btn.btn--primary` ou `.btn.btn--primary--light`.

La solution consiste à s'en tenir aux sélecteurs de classe unique autant que possible, écrits dans l'ordre croissant d'« importance », et à éviter d'utiliser les déclarations `!important`.

#### Text-transform

Pour les sites qui supportent des langues autres que l'anglais, l'utilisation de `text-transform` causera probablement des problèmes. [Il existe plusieurs cas où les navigateurs remplacent un caractère par une version incorrecte pour les transformations en majuscules ou minuscules](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform#Browser_compatibility). La solution est de ne jamais utiliser `text-transform` et de s'appuyer plutôt sur une copie correctement capitalisée.

#### Z-index

Si une règle `z-index` est incluse dans une feuille de style, il y aura éventuellement deux autres règles qui déclarent `z-index: 9999;` et `z-index: 99999;`. Tenter d'utiliser des classes atomiques ou des variables pour limiter le nombre de z-index acceptables non seulement échouera à empêcher les développeurs d'utiliser `calc()` et les mathématiques SCSS pour modifier la valeur pour leur cas d'utilisation, mais manquera également complètement la cible en raison du fonctionnement des contextes de superposition.

Il a été de mon expérience que la plupart, sinon toutes, les utilisations de `z-index` peuvent être remplacées en restructurant le HTML pour utiliser le contexte de superposition naturel (les éléments plus bas sur la page sont plus hauts dans le contexte) ou en [ajoutant une propriété à l'élément ou à son parent pour forcer un nouveau contexte de superposition](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context).

Évitez `z-index` à tout prix.

#### Pseudo-éléments

Utiliser les pseudo-éléments `::before` et `::after` est non seulement utile, mais souvent amusant ! De nombreux tours stylistiques reposent sur l'utilisation de ces deux pseudo-éléments et, tant qu'il n'y a pas de texte dedans (via leur propriété `content`), ils sont considérés comme sémantiques. Le problème de mettre du texte dans ces éléments est que leur lecture par les dispositifs d'accessibilité varie selon les navigateurs et les appareils. Il est préférable de ne pas traiter cette disparité en évitant de placer du texte dedans.

Les pseudo-éléments `::first-letter` et `::first-line` ne fonctionnent pas comme vous le pensez probablement. Ils ne ciblent que la première lettre/ligne dans un élément de niveau bloc. Il y a aussi des problèmes avec le sélecteur `::first-line` ciblant incorrectement les caractères double-octet (comme les Kana japonais) et [les digraphes](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-letter#Browser_compatibility).

Manipuler les styles du texte sélectionné ou du texte de remplissage via `::selection` et `::placeholder`, respectivement, conduit souvent à des problèmes. Avec `::placeholder`, la préoccupation est simple : [vous ne devriez pas utiliser de placeholders](https://www.nngroup.com/articles/form-design-placeholders/). Cela est particulièrement vrai pour tout ce qui est important, comme les étiquettes ou les indices d'entrée. En incluant des styles `::placeholder`, vous encouragez les développeurs, les designers et les auteurs à les utiliser, au grand dam de vos utilisateurs.

Modifier les styles de sélection, généralement `color` et `background-color`, conduit à des bugs plus subtils mais insidieux. Bien que [les couleurs de sélection par défaut](https://stackoverflow.com/a/16094931) ne soient pas cohérentes entre les navigateurs ou les appareils et qu'elles ne fournissent pas toujours un contraste acceptable avec la couleur de texte de votre site, les utilisateurs les remplacent parfois pour des raisons d'accessibilité. Changer les couleurs, dans ce cas, pourrait soit ne pas fonctionner (parce que le CSS d'accessibilité de l'utilisateur prime sur le vôtre), soit interférer avec leurs feuilles de style (si vous utilisez `!important`). Utiliser ce pseudo-élément pour essayer de garantir un contraste accessible pourrait finir par perturber l'expérience pour les très personnes que vous souhaitez aider.

(Bien que j'aie oublié beaucoup de détails de ce bug, j'ai rencontré un problème il y a quelques années où le texte traduit automatiquement par Chrome était rendu invisible car il dépendait du style `::selection` que j'avais modifié.)

#### Transitions & Animations

Animer ou transitionner des propriétés autres que `opacity` et `transform` force le navigateur à repeindre ou à reflow la page. Cela peut ne pas sembler être un problème sur une machine de développeur haut de gamme, mais cela causera des saccades sur les ordinateurs portables et les téléphones bas de gamme. Une mauvaise animation est pire que pas d'animation.

#### Prefers Reduced Motion

Écrire des animations qui sont utiles, belles et sûres n'est pas une tâche simple. Avec l'avènement de la requête média `prefers-reduced-motion`, nous pouvons aider à rendre nos pages plus sûres pour les personnes souffrant de troubles vestibulaires, et moins ennuyeuses pour les autres. Bien que l'ajout de cette requête média ne soit pas une solution miracle, cela aide. J'ai écrit la règle imbriquée pour qu'elle soit opt-out, ce qui signifie que **toutes** les animations CSS sont arrêtées sauf si l'auteur inclut la classe `safe-animation` sur l'élément.

```
/* https://github.com/mozdevs/cssremedy/issues/11#issuecomment-462867630 */
@media (prefers-reduced-motion: reduce) {
  *:not(.safe-animation),
  *:not(.safe-animation)::before,
  *:not(.safe-animation)::after {
    animation-duration: 0.01s !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0s !important;
    scroll-behavior: auto !important;
  }
}
```

#### Reset extensions

Mon reset CSS de prédilection est une forme modifiée du [reset de Meyers](https://meyerweb.com/eric/tools/css/reset/). Il y a quelques règles que je retire du reset, cependant. Je n'aime pas supprimer les icônes de liste des éléments `ol` et `ul`. Je trouve que cela encourage les développeurs à utiliser ces éléments de manière non sémantique, comme regrouper des éléments qui sont physiquement proches mais pas ontologiquement proches. Je retire également la règle qui définit le `line-height` sur le `body` à `1`. Définir des attributs qui affectent, ou sont affectés par, la police séparément de la définition de la police est un bug en attente.

Quelques ajouts que je fais au fichier de reset sont ci-dessous. Je n'aime pas inclure une classe atomique `.hidden` dans mon CSS car il existe une meilleure option qui fonctionnera même si le CSS ne se charge pas — l'attribut `hidden`. Le comportement par défaut du navigateur qui définit `display: none` sur les éléments cachés peut être écrasé, même accidentellement, donc j'inclus une règle pour le renforcer.

```
body {
  /* dimensionnement plus intuitif */
  box-sizing: border-box;
}
*, ::before, ::after {
  box-sizing: inherit;
}
i, cite, em, var, dfn, address {
  /* prévenir l'italique faux */
  font-style: normal;
}
b, h1, h2, h3, h4, h5, h6, strong, th {
  /* prévenir le gras faux */
  font-weight: normal;
}[hidden] {
  /* renforcer la sémantique accessible */
  display: none !important;
}
```

> Mon Reset : [https://github.com/NickGard/css-utils/blob/master/reset.css](https://github.com/NickGard/css-utils/blob/master/reset.css)

Un autre utilitaire que je trouve souvent nécessaire est une classe `visually-hidden`. Bien que j'utilise `aria-label` plus souvent pour le texte invisible lisible à l'écran, j'inclus généralement la règle suivante quelque part :

```
/* https://a11yproject.com/posts/how-to-hide-content/ */
.visually-hidden {
  position: absolute !important;
  height: 1px;
  width: 1px;
  overflow: hidden;
  clip: rect(1px, 1px, 1px, 1px);
}
```

#### Nommage de type BEM

Je ne peux pas terminer cet article sans au moins un commentaire sur les conventions de nommage. J'aime le nommage BEM car il se lit bien. `<button class="btn--primary"` /> me dit exactement de quel type de bouton il s'agit. Mon seul écart par rapport à la méthodologie officielle BEM™ est que j'aime utiliser une seule classe sur un élément (avec l'exception possible des classes atomiques). Cela offense mes sensibilités de voir `<button class="btn btn--primary" />` car la deuxième classe me dit déjà que les styles étendent les règles de base du btn. Cela crée également deux raisons pour qu'une ligne change, ce qui est un drapeau rouge.

Dans mon CSS, cela ressemble à ceci :

```
.btn, .btn--primary {
  /* styles de base du bouton */
}
.btn--primary {
  /* remplacements du bouton principal */
  /* a naturellement une spécificité plus élevée */
}
```

En SCSS, vous pouvez obtenir le même effet en utilisant `@extend`.

#### Conclusion

Ce sont mes règles de base depuis plusieurs années maintenant et elles m'ont aidé à maintenir de grandes bases de code avec de nombreux contributeurs. Ce n'est pas parfait et je l'ajuste constamment (`prefers-reduced-motion` est nouveau), mais j'espère qu'en le partageant, cela aidera les autres.