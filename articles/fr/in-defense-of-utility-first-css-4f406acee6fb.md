---
title: En défense du CSS Utility-First
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-27T01:13:30.000Z'
originalURL: https://freecodecamp.org/news/in-defense-of-utility-first-css-4f406acee6fb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nHfoojHD3eS-ggpdB6zNJw.jpeg
tags:
- name: atomic css
  slug: atomic-css
- name: bem
  slug: bem
- name: CSS
  slug: css
- name: Sass
  slug: sass
- name: Utility First
  slug: utility-first
seo_title: En défense du CSS Utility-First
seo_desc: 'By Sarah Dayan

  “Favor composition over inheritance”.

  This piece of wisdom from Design Patterns, one of the most influential software
  engineering books, is the foundation of utility-first CSS. It also shares many principles
  with functional programming...'
---

Par Sarah Dayan

**_« Privilégiez la composition plutôt que l'héritage »_**.

Ce conseil de [_Design Patterns_](https://en.wikipedia.org/wiki/Design_Patterns), l'un des livres les plus influents en ingénierie logicielle, est le fondement du **CSS utility-first**. Il partage également de nombreux principes avec la **programmation fonctionnelle** : immutabilité, composabilité, prévisibilité et évitement des effets secondaires. Le but derrière tous ces termes techniques est d'écrire du code qui est **plus facile à maintenir et à faire évoluer**.

Malgré sa popularité croissante, le CSS utility-first n'a pas encore convaincu tout le monde. Alors que certains [le louent](http://jon.gold/2015/07/functional-css), d'autres ont été [vivement critiques](http://www.zeldman.com/2017/01/03/kiss-my-classname) à propos de cette pratique. **Je faisais partie de ce dernier groupe**. J'étais une adepte de BEM, convaincue par une approche que j'avais adoptée pour ses avantages et que je défendais comme on soutient une équipe sportive. J'ai rejeté le utility-first parce qu'il impliquait que ma méthode préférée et familière n'était plus bonne.

Depuis, j'ai **beaucoup** approfondi le sujet. J'ai étudié les design patterns et la programmation fonctionnelle. Cela m'a permis de **réviser radicalement mon jugement**.

[CSS Tricks](https://css-tricks.com/growing-popularity-atomic-css/) et [Adam Wathan](https://adamwathan.me/css-utility-classes-and-separation-of-concerns) ont fait un travail brillant en nous emmenant dans un voyage du CSS "régulier" au utility-first, et en expliquant le "pourquoi" derrière cela. Plutôt que de paraphraser, je vais me concentrer sur **les critiques récurrentes du utility-first** et démystifier les idées reçues.

### « Autant utiliser les styles en ligne »

Les gens comparent souvent le CSS utility-first à l'application de règles CSS aux nœuds HTML via l'attribut `style`. Cette façon de styliser est unanimement considérée comme une mauvaise pratique, et nous avons depuis évolué vers des feuilles de style séparées et des abstractions de classes.

**Le CSS utility-first n'est pas différent**. Toutes les styles sont définies et maintenues séparément. Cela permet la réutilisation du code, l'utilisation de pseudo-classes, de pseudo-éléments, de pré-processeurs, et la mise en cache du navigateur.

Pourtant, les détracteurs de l'atomic CSS l'associent hâtivement aux styles en ligne. Les classes atomiques sont petites, elles n'ont souvent qu'une seule règle, et elles sont nommées de manière _fonctionnelle_ plutôt que _sémantique_.

Tout cela étant dit, le fait que cela _semble_ identique ne signifie pas que cela _est_ identique. Comprendre comment ces deux pratiques diffèrent est la clé pour saisir les avantages du utility-first.

**Les styles en ligne vous permettent de faire tout ce que vous voulez**. Vous n'avez pas à suivre de définition préexistante. Vous réécrivez tout à partir de zéro chaque fois que vous stylisez un nouveau nœud HTML. Des éléments similaires finissent avec du code dupliqué, ce qui rend la page inutilement plus lourde. Si vous n'êtes pas prudent, il est facile d'ignorer les solutions préexistantes et de réinventer la roue à chaque fois.

```
<h2 style="font-size: 16px; font-weight: bold; color: purple">Stranger Things</h2><p style="font-size: 13px; font-style: italic">Stranger Things est une série télévisée américaine de science-fiction et d'horreur...</p><h2 style="font-size: 16px; font-weight: bold; color: purple">Game of Thrones</h2><p style="font-size: 13px; font-style: italic">Game of Thrones est une série télévisée américaine de fantasy...</p>
```

_Inutilement verbeux, taille de fichier plus lourde, plusieurs sources de vérité pour un seul concept de design._

```
<button style="padding: 5px 8px; font-size: 13px">Bouton</button><button style="padding: 0 8px; font-size: 13px; line-height: 23px">Bouton</button><button style="display: flex; padding: 0 8px; font-size: 13px; height: 23px; align-items: center">Bouton</button>
```

_Trois tentatives pour résoudre le même problème. Cela est facilement induit par l'absence d'une seule source de vérité, et susceptible de causer des incohérences visuelles._

**Les classes utilitaires exposent une API bien définie que vous pouvez utiliser pour composer des composants plus complexes**. Vous ne réécrivez pas les styles ; au lieu de cela, vous vous appuyez sur des classes qui définissent les styles et les comportements une fois pour toutes.

```
// HTML
```

```
<h2 class="font-16 font-bold font-purple">Stranger Things</h2><p class="font-13 font-italic">Stranger Things est une série télévisée américaine de science-fiction et d'horreur...</p><h2 class="font-16 font-bold font-purple">Game of Thrones</h2><p class="font-13 font-italic">Game of Thrones est une série télévisée américaine de fantasy...</p>
```

```
// CSS
```

```
/* Tailles de police */
```

```
.font-13 { font-size: 13px } .font-16 { font-size: 16px }...
```

```
/* Styles de police */
```

```
.font-bold { font-weight: bold }.font-italic { font-style: italic }...
```

```
/* Couleurs de police */
```

```
.font-purple { color: purple }...
```

L'utilisation d'un ensemble défini de règles CSS existantes, peu importe leur granularité, vous oblige à choisir des styles parmi une **liste limitée**. Vous n'avez pas une liberté totale comme avec les styles en ligne. Vous maintenez un catalogue cohérent de styles _autorisés_, et vous les utilisez pour _composer_ des composants plus grands.

Cette approche impose la cohérence en limitant les façons dont vous pouvez styliser les éléments. Au lieu d'avoir accès à plus de 16 millions de couleurs, vous n'avez accès qu'au nombre de couleurs définies dans votre thème.

**Cela fournit également une seule source de vérité**. Au lieu de redéclarer la même `couleur` pour chaque élément qui l'utilise, vous la définissez une fois dans une classe et utilisez cette classe partout où vous en avez besoin. De plus, l'utilisation de styles séparés (avec des classes atomiques ou non) vous donne accès aux pseudo-classes et pseudo-éléments, aux pré-processeurs, à la mise en cache... toute une série d'avantages qui ne sont pas disponibles avec les styles en ligne.

Vous pourriez argumenter que cela n'a pas d'importance si les styles atomiques sont limités : les mélanger sans précaution peut entraîner des mises en page incohérentes comme avec les styles en ligne. Mais c'est **un problème humain, pas technique**. Vous obtenez exactement le même problème avec n'importe quelle approche, et n'importe quel langage d'ailleurs, que vous soyez capable de définir une portée ou non. Si vous ne suivez pas les règles, les guides de style et les meilleures pratiques que votre équipe a mises en place, vous êtes le seul à blâmer. Pas le programme, pas le langage, et pas l'architecture.

### « Cela viole la séparation des préoccupations »

L'un des plus grands arguments contre le CSS fonctionnel est qu'il va à l'encontre de la séparation des préoccupations. Que le CSS devrait strictement être responsable du style, et que le HTML devrait structurer sémantiquement la page. Que, en utilisant des classes atomiques et en composant des composants dans le HTML, vous déléguez en quelque sorte le style au HTML au lieu de le faire en CSS.

**C'est une vision extrême, et finalement déformée, de ce que signifie « séparation des préoccupations »**.

Il y a quelques années, j'étais en entretien d'embauche avec un développeur front-end qui m'a parlé de son mépris total pour Bootstrap. Selon lui, utiliser du balisage supplémentaire pour créer une grille était une hérésie : c'est un travail pour le CSS, et uniquement pour le CSS. Le HTML devrait être à 100 % ignorant de la façon dont il est rendu.

Le problème avec ce genre de réflexion est qu'elle est **profondément impratique**. Elle élève les principes de conception à un niveau dogmatique, ignorant les cas d'utilisation concrets et le contexte. Elle vous pousse à être plus préoccupé par le fait de cocher toutes les cases des « bonnes pratiques » que par la résolution de problèmes réels.

Adam Wathan [l'explique bien (voir : « Séparation des préoccupations » est un homme de paille)](https://adamwathan.me/css-utility-classes-and-separation-of-concerns) : lorsqu'il s'agit de HTML et de CSS, vous ne pouvez pas le regarder d'un point de vue strict de « séparation des préoccupations ». **C'est une relation de « qui dépend de qui »**.

**Ne vous y trompez pas** : simplement parce que la composition de style est effectuée dans le document HTML, cela ne signifie pas qu'elle est faite _en HTML_. Nous n'utilisons pas d'attributs _style_ ou _align_ sur les nœuds HTML. Nous assemblons des morceaux que nous avons définis dans une feuille de style appropriée, _en CSS_. Notre HTML devient un _consommateur_ de notre API CSS. Comme Vue.js l'explique dans leur [documentation](https://vuejs.org/v2/guide/single-file-components.html#What-About-Separation-of-Concerns), la séparation des préoccupations n'est pas égale à la séparation des types de fichiers. Vos styles peuvent être composés sur des nœuds HTML, **c'est toujours un travail CSS**.

### « Cela alourdit le HTML »

Lorsque les gens mentionnent l'alourdissement du code, ils veulent généralement dire l'une des deux choses suivantes (ou les deux) : du code qui est [**difficile à lire**](https://frontstuff.io/in-defense-of-utility-first-css#cest-moche-et-difficile-a-lire), et une **base de code plus lourde**.

La complexité de votre mise en page doit exister _quelque part_. Une approche basée sur les composants ne supprime pas le « bloat », elle le _déporte_ simplement vers la feuille de style. Même ainsi, parce que vos composants plus grands réutilisent les mêmes styles atomiques que d'autres, **vous finissez inévitablement avec du code dupliqué**.

```
$green: #74b759;
```

```
.component {  &-title {    color: $green;    font-weight: bold;  }}
```

```
.widget {  &-title {    color: $green;    font-style: italic;  }}
```

```
.footer {  &-links {   color: $green;   text-decoration: underline;  }}
```

_Même avec Sass, vous obtenez des règles dupliquées dans le code source. `@mixin` peut aider, mais vous obtenez toujours des doublons dans le CSS compilé._

Maintenant, je sais ce que vous pensez. Nous avons `@extend`. C'est un cas d'utilisation idéal pour cela, non ?

Pas si vite.

`@extend` peut éviter la duplication des règles dans le CSS compilé, mais le méga-sélecteur séparé par des virgules qu'il générera pourrait finir par être **beaucoup plus lourd que si vous aviez dupliqué la règle**. Tant pour éviter le bloat.

Vous concaténez également des classes non liées **et les déplacez toutes en haut**, là où le premier `@extend` prend place. Cela peut rapidement entraîner des problèmes de spécificité et des remplacements étranges. Sans compter que vous ne pouvez pas `@extend` une classe ou un placeholder externe depuis une requête média. Donc oui, définitivement pas une solution miracle.

D'un point de vue de la taille du fichier, **vous ne devriez pas vous inquiéter des noms de classe répétés dans le HTML**. C'est pour cela que Gzip existe. L'algorithme _deflate_ a été [spécifiquement conçu](http://www.gzip.org/algorithm.txt) pour gérer les chaînes dupliquées, donc il n'y a aucun intérêt à supprimer des caractères dans votre HTML. La taille du fichier résultant fera **peu ou pas de différence** que vous utilisiez quelques classes ou beaucoup.

En revanche, plus un _sélecteur_ est répété dans une feuille de style, **plus votre navigateur a de travail à faire pour résoudre tous les styles**. Si vous avez une seule classe `.title-green` pour un style donné, elle correspond simplement à tous les `.title-green` de la page. Mais si vous avez de nombreuses classes faisant la même chose (en utilisant `@mixin`) ou des sélecteurs similaires faisant des choses différentes (en utilisant `@extend`), cela sera plus coûteux pour le navigateur à correspondre.

Le « bloat » HTML n'a pas d'importance, **mais le CSS oui**. Le réseau et le moteur ne se soucient pas du nombre de classes que vous avez dans votre HTML, mais la façon dont vous écrivez votre CSS compte. Si votre processus de prise de décision tourne autour des performances, assurez-vous de concentrer votre attention sur les bonnes choses.

### « BEM suffit »

OOCSS et toutes les méthodes dérivées (SMACSS, BEM, etc.) ont considérablement amélioré la façon dont nous gérons le CSS. Le CSS utility-first est un héritier de cette approche : il définit également des _objets_ réutilisables.

Le problème avec BEM est qu'il se concentre sur la construction de composants en premier. Au lieu de chercher les plus petits motifs insécables, vous construisez des _blocs_ et leurs _éléments_ enfants. BEM fait un excellent travail de namespacing et de prévention des fuites de style, mais sa nature orientée composants conduit inévitablement à une [abstraction prématurée](http://wiki.c2.com/?PrematureAbstraction). Vous créez un composant pour un cas d'utilisation spécifique et vous ne le réutilisez jamais (un composant de barre de navigation, par exemple).

BEM vous encourage à utiliser des _modificateurs_ pour gérer les variations des composants. Cela peut sembler intelligent au début, mais malheureusement conduit à d'autres problèmes. Vous finissez par créer des tonnes de modificateurs que vous n'utilisez qu'une seule fois pour un cas d'utilisation spécifique. Pire encore : d'un composant à l'autre, vous pourriez finir avec des modificateurs similaires, brisant davantage le principe [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

```
.card {  background: white;  border: 1px solid grey;  text-align: justify;}
```

```
.card--left {  text-align: left;}
```

```
.card--right {  text-align: right;}
```

```
.tooltip {  background: black;  color: white;  text-align: center;}
```

```
/* Oups, on dirait qu'il y a des règles dupliquées là-bas ! */
```

```
.tooltip--left {  text-align: left;}
```

```
.tooltip--right {  text-align: right;}
```

À grande échelle, les composants peuvent devenir difficiles à modifier sans casser les instances dans tout un projet. L'abstraction prématurée empêche les composants d'évoluer et de se diviser en entités indépendantes si nécessaire. Les modificateurs se multiplient dans une tentative de corriger cela, résultant en des variations non réutilisables pour des cas d'utilisation uniques, et des rustines de correction lorsque nous réalisons que notre composant fait trop de choses.

BEM est une excellente tentative de résoudre les problèmes inhérents au CSS, mais en faire l'approche CSS principale de votre projet apporte tous les problèmes que vous rencontrez lorsque vous favorisez l'héritage plutôt que la composition.

### « C'est tout un autre langage à apprendre en plus du CSS »

Cette affirmation peut être faite pour tout système de nommage pour tout projet spécifique, quelle que soit la méthodologie que vous choisissez. Votre écosystème de noms de classes CSS est une couche d'abstraction au-dessus du CSS pur. Que vous utilisiez des noms sémantiques comme `.card` ou des noms fonctionnels comme `.bg`, les nouveaux contributeurs devront se familiariser avec ce que fait chaque classe et quand l'utiliser.

Vous ne pouvez pas échapper à l'utilisation d'une interface de nommage entre votre HTML et CSS, à moins que vous ne soyez prêt à décrire votre balisage exact en CSS ou à écrire des styles en ligne. En fin de compte, les noms de classes fonctionnels sont [plus faciles à comprendre](https://frontstuff.io/in-defense-of-utility-first-css#cest-moche-et-difficile-a-lire) car ils décrivent le style. Vous savez ce qu'ils font sans avoir à chercher les styles réels, tandis que les noms sémantiques vous obligent à regarder le rendu ou à parcourir le code.

### « C'est difficile à maintenir »

Lorsque les gens disent que le CSS utility-first est difficile à maintenir, ils mentionnent souvent que lorsque quelque chose change dans le design, vous devez le changer partout. Vous avez des boutons avec des coins réguliers et vous décidez de les rendre arrondis, donc vous devez ajouter la classe utilitaire `.rounded-corners` sur chaque bouton dans le code. Pourtant, tout l'intérêt du utility-_first_ est que vous commencez par composer avec des classes utilitaires, puis créez des composants lorsque vous commencez à identifier des motifs répétitifs.

Un bouton est un candidat idéal et évident pour être abstrait en son propre composant. Vous n'avez peut-être même pas besoin de passer par la phase "utility-first, puis composant" pour ce cas. Lorsque cela concerne des composants plus grands, privilégier la composition _en premier_ est le meilleur choix pour la maintenabilité. Pourquoi ? **Parce qu'il est plus sûr d'ajouter ou de supprimer des classes sur un nœud HTML spécifique** que d'ajouter ou de supprimer des styles dans une classe qui s'applique à de nombreux éléments.**

Trop souvent, j'ai été soumise à des changements de design, et j'ai dû dupliquer des composants existants pour les faire se comporter différemment parce que je n'avais pas d'autre choix. Même lorsqu'un designer fournit tous les designs au début d'un projet, et même si vous faites un excellent travail pour identifier les composants avant de coder, **vous ne pouvez pas prédire l'avenir**.

Disons que les designs initiaux ont des cartes blanches avec une ombre portée en retrait et un petit ruban dans le coin.

```
// CSS
```

```
.card {  position: relative;  background: white;  padding: 22px;  border: 1px solid lightgrey;  text-align: justify;  border-radius: 5px;  box-shadow: 0 0 5px 0 rgba(0, 0, 0, .2);  overflow: hidden;}
```

```
.card::after {  position: absolute;  top: -11px;  right: 9px;  display: block;  width: 10px;  height: 50px;  background: red;  transform: rotateZ(-45deg);  content: '';}
```

```
// HTML
```

```
<div class="card">...</div>
```

Cette solution est simple, sémantique et réutilisable. Vous gérez tout en CSS et avez un HTML minimal à écrire. Mais soudain, vous recevez de nouveaux designs pour de nouvelles pages, et ils utilisent la carte sans le ruban. Maintenant, vous devez trouver un moyen de supprimer le ruban pour ces nouvelles cartes.

```
.card-no-ribbon::after {  display: none;}
```

Le problème est que cette classe _annule_ quelque chose qui a été précédemment conçu. Devoir _ajouter_ une classe pour _supprimer_ une fonctionnalité est un anti-pattern : **c'est contre-intuitif et difficile à maintenir**. Lorsque vous décidez de changer le comportement de la classe de base, vous devez surveiller le modificateur d'annulation pour vous assurer qu'il fonctionne toujours.

Nous devons maintenant ajouter un autre ruban en bas à gauche.

```
.card::before,.card::after {  /* code partagé */}
```

```
.card::before {  top: -11px;  right: 9px;}
```

```
.card::after {  bottom: -11px;  left: 9px;}
```

Mais maintenant, nous devons mettre à jour `.card-no-ribbon` !

```
.card-no-ribbon::before,.card-no-ribbon::after {  display: none;}
```

Cela, ici, **est l'anti-pattern de la classe de base fragile en action**. Parce que votre classe de base a été abstraite trop tôt, fait trop de choses et doit maintenant évoluer, vous ne pouvez pas l'éditer sans vous soucier des effets secondaires possibles. Si de nouvelles personnes commencent à contribuer au projet, ces risques sont multipliés par dix.

La seule option qui vous reste à ce stade est de faire un refactoring : avoir une classe `.card` nue comme classe de base, et ajouter les rubans avec les modificateurs `.card--top-ribbon` et `.card--bottom-ribbon`. Mais maintenant, vous devez éditer toutes les classes `.card` existantes dans votre code qui _doivent_ avoir un ruban.

**Les refactorings précoces sont un bon indicateur de non-maintenabilité**.

Vous pourriez argumenter qu'un développeur intelligent _aurait pu_ le voir venir. Qu'il _aurait dû_ faire une classe de base `.card` nue et un modificateur `.card--ribbon`, dès le départ.

**Cela fait en réalité un plaidoyer _en faveur_ du utility-first et de la composition**.

Vous prenez la décision de décomposer un élément de design donné que vous avez jugé trop monolithique, afin qu'il soit plus facile à faire évoluer. **C'est une bonne décision**. Plus vous avancez, plus vous réaliserez que cela mène au utility-first.

Vous pourriez penser que ce n'est pas le cas, et que votre travail est de _prévoir_ le minimum vital pour un composant donné. Mais à moins que vous ne possédiez une boule de cristal, cette évaluation est risquée. C'est également une vision à court terme. Et si des parties de votre composant doivent être étendues à d'autres composants ? Par exemple, et si vous avez maintenant besoin de boutons avec des rubans ? Si vous dupliquez la classe `.card--ribbon`, votre code n'est plus DRY, ce qui le rend encore plus difficile à maintenir. Alors ? Faire un mixin et l'importer dans les deux modificateurs ? Encore une fois, c'est du travail supplémentaire et du code "mouillé".

La meilleure solution pour ce cas d'utilisation est d'écrire une seule classe utilitaire pour le ruban, et des modificateurs pour les tailles et les couleurs si nécessaire. Cela vous permet d'avoir **une seule source de vérité** et d'utiliser le ruban où vous le souhaitez. Si vous devez mettre des rubans sur des avatars, des panneaux, des listes non ordonnées, des modales, vous pouvez le faire sans avoir à écrire une seule ligne de CSS supplémentaire.

**C'est la définition de la scalabilité et de la maintenabilité**. Tout ce que vous avez à faire est de réutiliser le code disponible que vous avez écrit _proactivement_, au lieu d'avoir à ajuster le code existant _réactivement_.

```
.ribbon {  position: relative;  overflow: hidden;}
```

```
.ribbon::after {  position: absolute;  display: block;  top: -11px;  right: 9px;  width: 10px;  height: 50px;  background: red;  transform: rotateZ(-45deg);  content: '';}
```

_En décomposant les designs en petits éléments, nous écrivons un code beaucoup plus réutilisable._

Qualifier le CSS utility-first de "non maintenable" est absolument inexact. En fait, **il peut être la méthodologie CSS la plus maintenable et scalable à ce jour**.

Vous ne pouvez pas prédire l'avenir. C'est pourquoi vous devriez toujours privilégier la composition plutôt que l'héritage. **Un bon signe d'une base de code saine et scalable est la façon dont les choses se passent lorsque vous devez la changer**.

Si un nouveau changement vous rend anxieux parce que vous pourriez casser quelque chose, c'est un signe de mauvaise conception. Mais je vais plus loin en disant que si vous devez écrire un nouveau CSS pour faire faire à un composant existant quelque chose qu'un autre composant fait déjà, votre code n'est pas aussi scalable que vous le pensez.

Si vous devez réutiliser un comportement qui existe quelque part, **vous ne devriez pas avoir à écrire un nouveau code**. Vous devriez pouvoir faire confiance et utiliser ce que vous avez déjà écrit et partir de là. Vous avez une seule source de vérité sur laquelle vous pouvez vous appuyer, au lieu de deux ou plusieurs variations légèrement différentes que vous ne devez pas oublier de maintenir à jour. **C'est la définition de la maintenabilité**.

### « C'est moche et difficile à lire »

Vous vous souvenez de l'émoi lorsque BEM a commencé à devenir populaire ? Moi oui. Je me souviens de nombreuses personnes qui ont rejeté tout cela à cause de sa syntaxe. Louant le modèle, mais dégoûtées par l'idée d'enchaîner deux tirets bas ou deux tirets.

En tant qu'êtres humains, il est dans notre nature d'être facilement rebutés par ce qui nous est peu familier. Pourtant, laisser des considérations cosmétiques subjectives se mettre en travers d'une technique potentiellement utile est là où les développeurs devraient tracer la ligne. Notre travail est de **résoudre des problèmes**. Notre principale préoccupation devrait être **l'utilisateur final**.

Regardez le code source de nombreux grands projets : la plupart ont fini par adopter BEM. Il est peu probable que tous leurs développeurs front-end aient été convaincus dès le début.

Surmonter les sentiments initiaux, surtout s'ils sont motivés par des préférences personnelles, n'est pas si difficile **lorsque vous mettez le succès d'un projet en premier**.

Maintenant, sur le sujet de la lisibilité, je comprends que de longues chaînes de classes peuvent être "effrayantes" lorsque vous ouvrez un fichier pour la première fois. Ce n'est pas une tâche insurmontable cependant. Un code plus verbeux est un compromis de la composition, mais c'est une **inconvénient bien moindre que la non-scalabilité**.

Je n'utilise pas de raccourcis comme `.pt-8` ou `.bb-lemon` dans mon propre code. Je privilégie les noms de classes complets comme `.padding-top-8` et `.border-bottom-lemon`, qui sont beaucoup plus faciles à lire. L'autocomplétion résout le problème de devoir taper de longs noms de classes, et il existe des outils que vous pouvez utiliser pour ré-hacher les noms de classes en des noms plus petits pour la production. Je doute que cela fasse une différence significative pour vos performances, mais bon, si cela vous fait du bien de raser des octets, allez-y ?

En fin de compte, la nature des noms de classes fonctionnels pourrait en fait être **plus expressive**. Il est facile pour votre cerveau de faire le lien entre une telle classe et ce qui se passe à l'écran. Même si vous ne voyez pas comment elle est rendue, vous pouvez avoir une assez bonne idée de ce que `.hidden` ou `.opacity-6` sont censés faire.

```
<blockquote class="border-thick-left-red padding-left-medium font-navy">  <p>Vous savez comment ils appellent un Quarter Pounder avec du fromage à Paris ?</p></blockquote>
```

_Stylistiquement parlant, il est assez facile de savoir ce qui se passe ici._

Les noms de classes sémantiques ne transmettent pas la même chose. Cela fonctionne pour les petits composants comme les boutons ou les alertes, qui sont suffisamment courants pour être facilement reconnus. Pourtant, plus un composant devient grand et complexe, moins il est évident de savoir quel nom de classe correspond à quel élément à l'écran, ou à quoi il ressemble.

```
<div class="entry">  <h2 class="entry-title">The Shining</h2>  <div class="widget widget-lead">    <div class="widget-content">      <p>Son souffle s'arrêta dans un hoquet. Une terreur presque somnolente s'insinua dans ses veines...</p>    </div>    <div class="author">      <img class="author-avatar" src="...">      <h3 class="author-name">Stephen King</h3>      <p>Stephen Edwin King (né le 21 septembre 1947) est un auteur américain d'horreur, de fiction surnaturelle, de suspense, de science-fiction et de fantasy...</p>      <div class="btn-group">        <a class="btn" href="#">Site Web</a>        <a class="btn" href="#">Twitter</a>      </div>    </div>  </div></div>
```

_Plus difficile de savoir quelle classe fait quoi sans passer par la feuille de style._

À cet égard, les classes fonctionnelles sont beaucoup plus faciles à comprendre que les noms de classes sémantiques. Elles demandent moins de temps de rattrapage et moins de changement de fichiers. En fin de compte, elles vous donnent exactement l'information que vous cherchez de toute façon.

### « Ce n'est pas comme ça qu'on écrit du CSS »

**La spécificité CSS est une _fonctionnalité_, pas un bug.** Utilisez-la correctement, et elle vous donnera un contrôle incroyable.

C'est ce que disent les vétérans du CSS lorsqu'un autre article sur les dangers de la spécificité apparaît. Et techniquement **ils ont raison** : le système de priorité CSS n'est pas un accident. Il dérange généralement les personnes qui ne maîtrisent pas le CSS en raison du manque de portée. Mais une langue n'est pas cassée parce qu'elle ne se comporte pas comme ce à quoi vous êtes habitué. Les règles CSS imbriquées sont comme `!important` : elles sont pratiques, mais ont été si mal utilisées pendant des années que nous les voyons maintenant comme quelque chose à _éviter_.

La spécificité doit être utilisée de manière proactive, pas réactive. Elles doivent être des _décisions de conception_, pas une solution rapide lorsque vos styles ne s'appliquent pas. Harry Roberts l'explique bien dans [CSS Guidelines](https://cssguidelin.es/#specificity) :

> « Le problème avec la spécificité n'est pas nécessairement qu'elle est élevée ou basse ; c'est le fait qu'elle est si variable et qu'on ne peut pas s'en désengager : la seule façon de la gérer est de devenir de plus en plus spécifique. »

La spécificité est un outil puissant, mais elle doit être utilisée avec la plus grande prudence et une bonne vision à long terme du projet. Utilisez-les mal, et vous ressentirez la douleur de devoir revenir en arrière. Garder une spécificité basse évite les problèmes : elle repose uniquement sur l'ordre source, ce qui est [beaucoup plus facile à gérer](https://www.xfive.co/blog/itcss-scalable-maintainable-css-architecture). Avec le CSS atomique, si un style ne s'applique pas, le corriger est aussi simple que d'ajouter ou de supprimer une classe sur un nœud HTML. Vous n'avez pas à remettre en question la structure de votre feuille de style, ce qui est beaucoup plus facile et plus sûr à gérer.

```
// CSS
```

```
.color-navy {  color: navy;}
```

```
.color-red {  color: red;}
```

```
// HTML
```

```
<div class="color-red color-navy">  <p>- À qui est cette moto ?</p>  <p>- C'est un chopper, bébé.</p>  <p>- À qui est ce chopper ?</p>  <p>- C'est à Zed.</p>  <p>- Qui est Zed ?</p>  <p>- Zed est mort, bébé, Zed est mort.</p></div>
```

_Voulez-vous que le texte soit bleu marine ? Pas besoin de toucher au CSS. Il suffit de supprimer la classe `.color-red` de la `<div>` englobante. Si vous avez besoin que l'un des enfants soit rouge, alors déplacez `.color-red` sur lui.

> « Si une fonctionnalité est parfois dangereuse, et qu'il existe une meilleure option, alors utilisez toujours la meilleure option. » — Douglas Crockford

Utiliser ou non la spécificité n'est pas une question de montrer à quel point vous maîtrisez le CSS et comment _vous_, contrairement aux autres, pouvez le garder sous contrôle. Il s'agit de **comprendre les avantages et les inconvénients des fonctionnalités à votre disposition**, et de faire des choix dans l'intérêt du projet.

### « Vous finissez avec beaucoup de CSS inutilisé »

Disons que vous utilisez des maps Sass pour [générer vos classes utilitaires](http://frontstuff.io/generate-all-your-utility-classes-with-sass-maps). Couleurs, tailles de police, arrière-plans, tout est automatiquement compilé en CSS propre et prêt à l'emploi. Le problème est que si vous n'utilisez pas _tout_, vous vous retrouvez avec des octets inutiles en production. Cela peut facilement être corrigé avec [UnCSS](https://github.com/giakki/uncss).

UnCSS est excellent pour dépoussiérer vos feuilles de style, mais il vient avec **deux mises en garde** : il ne fonctionne que sur les fichiers HTML (donc, pas de PHP et pas de fichiers de modèle) et il ne prend en compte que le JavaScript qui est exécuté au chargement de la page (pas les classes ajoutées lors des interactions utilisateur, par exemple). Si vous utilisez un langage comme PHP pour rendre vos pages, vous pouvez ajouter une tâche dans votre flux de déploiement qui compile les pages en HTML temporaire et exécute UnCSS dessus. Pour le deuxième problème, vous pouvez utiliser l'option `ignore` pour lister les classes ajoutées lors des interactions utilisateur.

Maintenant, il est également important de réfléchir à ce problème. Le coût des classes inutilisées est des feuilles de style plus lourdes (plus longues à télécharger) et un temps de parsing plus long. Si vous en avez beaucoup, et par là j'entends un grand pourcentage de vos styles totaux, **cela peut nuire aux performances**. Si vous n'en avez que quelques-unes ici et là, **l'impact sera négligeable**.

Maintenir votre base de code CSS est votre travail en tant que développeur. Peu importe la méthodologie que vous choisissez, vous devez garder un œil sur le projet et vous assurer de supprimer le code mort lorsque les choses changent.

**Être négligent avec cela est ainsi que vous finissez avec beaucoup de classes inutilisées, pas parce que vous en générez certaines**.

Besoin d'une classe de couleur de texte uniquement pour la couleur principale ? Faites une classe pour celle-ci uniquement. Besoin d'arrière-plans pour la plupart des couleurs du thème, mais incertain de les utiliser toutes immédiatement ? Générez ces fichues classes. Elles seront prêtes lorsque vous en aurez besoin, vous n'aurez pas à les maintenir lorsque vous ajouterez de nouvelles couleurs, et le code supplémentaire ne coûtera _rien_. **Ce n'est pas là que se trouvent les goulots d'étranglement de votre application**. Si vous avez des problèmes de performances, il y a un million d'autres choses à considérer avant même de regarder votre CSS.

### « Cela rend difficile de savoir ce qui est disponible à utiliser »

Lorsque votre base de code CSS est une grande collection de petites classes utilitaires, la lecture du code source ne vous aidera pas à obtenir une bonne vue d'ensemble des styles disponibles. Mais **est-ce le rôle du code source de toute façon** ?

Ce n'est certainement pas le cas. C'est pour cela que les **guides de style** existent.

Explorer le code source est _loin_ d'être suffisant pour bien comprendre comment une API complète est conçue. Cela n'est pas limité au CSS atomique : les projets OOCSS ou BEM, même petits, peuvent atteindre un niveau de sophistication qui nécessite au moins un `README`.

Pouvez-vous imaginer devoir revenir à une version non minifiée de la feuille de style principale de Bootstrap chaque fois que vous ne vous souvenez pas si c'est `.col-md-offset-6` ou `.col-offset-md-6` ? Est-ce que quelqu'un de nouveau dans Bootstrap comprendrait ce que signifie une telle classe sans un peu de littérature sur le fonctionnement de la grille ? La documentation, les guides de style et les références d'API sont conçus pour nous aider à comprendre les systèmes complexes. Bien sûr, cela ne signifie pas que la documentation devrait justifier une mauvaise conception et des conventions de nommage peu claires, mais penser que vous devriez être en mesure de comprendre un projet entier uniquement en lisant le code source est une pure fantaisie.

Il existe de nombreux outils pour vous aider à générer de la documentation directement à partir de votre code. J'utilise [KSS](http://warpspire.com/kss/syntax) pour la plupart de mes projets, mais CSS-Tricks partage une [liste d'alternatives](https://css-tricks.com/options-programmatically-documenting-css). Essayez-les !

### « Les classes utilitaires doivent être utilisées avec des composants »

Oui. Absolument. C'est précisément pourquoi cela s'appelle utility-_first_ et non utility-_only_.

Le utility-first ne consiste pas à abandonner complètement les composants. Cela signifie que vous devriez commencer par des classes utilitaires, en tirer le meilleur parti, et n'abstraire que lorsque vous voyez des motifs répétitifs. Vous permettez à votre projet de croître tout en restant flexible, et identifiez les vrais composants au fil du temps, lorsque les motifs commencent à émerger.

Il est crucial de comprendre qu'un composant n'est pas _juste_ un "bloc" de même apparence que vous _pouvez_ réutiliser. C'est un motif qui est fortement lié à votre projet spécifique. Bien sûr, vous allez probablement utiliser des tonnes de `.btn` et `.modal`, donc il est logique de les abstraire tôt. Mais êtes-vous sûr que vous allez jamais réutiliser `.testimonial` ? Ou au moins le réutiliser _assez_ pour que cela vaille la peine d'être un nouveau composant ? Aura-t-il toujours la même apparence dans tous les contextes, ou est-il spécifique à la page d'accueil ? Gardez vos options ouvertes. Il est beaucoup plus facile d'abstraire plus tard un style composite en un composant que d'essayer d'en annuler un.

### « Cela rend le redesign/théming un cauchemar »

Parce que le CSS atomique est fortement lié à votre design, cela peut rendre les choses plus difficiles lorsque vous devez faire un redesign ou développer un thème alternatif. Ce n'est pas impossible, et il y a quelques choses que vous pouvez faire pour rendre votre CSS utility-first plus adapté à ces types de besoins.

Vous pouvez commencer par garder les noms de classes pas trop spécifiques. Au lieu de `.margin-bottom-8`, vous pouvez utiliser un nom plus abstrait comme `.margin-bottom-xxs`. De cette façon, vous pouvez changer la valeur sans rendre les noms invalides.

Une autre approche serait de créer des **alias**. Imaginez que vous construisez une application qui a un mode clair et un mode sombre : certaines couleurs changeraient, d'autres non. Nous ne voulons pas rendre toutes nos utilitaires de couleur contextuelles : `.background-primary` et `.background-secondary` ne nous disent pas quelle couleur se cache derrière la classe. Vous ne voulez pas d'un système de couleur entier comme celui-ci. Pourtant, vous pourriez toujours avoir des utilitaires de couleur avec des noms de couleur appropriés (`.background-lime` ou `.background-red`), et générer des alias pour ceux qui pourraient avoir besoin de changer pour des raisons de théming.

```
// CSS
```

```
/* Arrière-plans */
```

```
.background-lime {  background: #cdf2b0;}
```

```
.background-off-white, .background-light {  background: #ebefe8;}
```

```
.background-dark-grey, .background-dark {  background: #494a4f;}
```

```
/* Couleurs */
```

```
.color-lime {  color: #cdf2b0;}
```

```
.color-off-white, .color-light {  color: #ebefe8;}
```

```
.color-dark-grey, .color-dark {  color: #494a4f;}
```

```
// HTML
```

```
<div class="background-light">  <h2 class="color-lime">Ézéchiel 25:17</h2>  <p class="color-dark">Le chemin de l'homme juste est entouré de toutes parts par les injustices des égoïstes et la tyrannie des hommes mauvais...</p></div>
```

À partir de là, tout ce que vous avez à faire est d'écrire une fonction JavaScript qui bascule toutes les classes `.*-light` et `.*-dark`. Et pour les éléments qui n'ont pas besoin de changer, vous pouvez utiliser les classes de couleur originales.

Cette méthode fonctionne bien, mais si vous avez beaucoup de classes à basculer, cela peut finir par nuire aux performances. Les manipulations du DOM sont coûteuses. Vous voulez les réduire autant que possible si vous le pouvez. Heureusement, il existe une technique astucieuse impliquant des variables CSS (merci à Adam Wathan pour l'avoir imaginée) qui simplifie tout.

```
// CSS
```

```
:root {  --green: #42f49b;  --off-white: #ebefe8;  --dark-grey: #494a4f;}
```

```
.theme-dark {  --background: var(--dark-grey);  --text: var(--off-white);}
```

```
.theme-light {  --background: var(--off-white);  --text: var(--dark-grey);}
```

```
.color-lime {  color: var(--green);}
```

```
.color-theme {  color: var(--text);}
```

```
.background-theme {  background: var(--background);}
```

```
// HTML
```

```
<div class="theme-light">  <div class="background-theme">  <h2 class="color-lime">Ézéchiel 25:17</h2>  <p class="color-theme">Le chemin de l'homme juste est entouré de toutes parts par les injustices des égoïstes et la tyrannie des hommes mauvais...</p>  </div></div>
```

Nous avons défini des couleurs avec des variables CSS et attribué différentes valeurs pour chaque contexte. Selon la classe englobante, [toutes les couleurs changeront grâce à l'héritage des ancêtres](https://jsfiddle.net/hurmktbz). Si vous deviez permettre le changement de thème, tout ce que vous auriez à faire est de changer `.theme-light` en `.theme-dark` sur la `<div>` parente, et toutes les couleurs s'adapteraient.

Cette technique ne fonctionne que si vous n'avez pas à supporter Internet Explorer et Edge en dessous de la version 15. Sinon, optez pour la première technique et utilisez le système d'héritage des ancêtres CSS pour éviter d'avoir à basculer trop de variables. Si vous devez attribuer une couleur de texte à un bloc entier, **définissez-la sur le parent au lieu des enfants**.

```
/* Non */<div class="background-light">  <h2 class="color-lime">Ézéchiel 25:17</h2>  <p class="color-dark">Le chemin de l'homme juste est entouré de toutes parts par les injustices des égoïstes et la tyrannie des hommes mauvais.</p>  <p class="color-dark">Béni soit celui qui, au nom de la charité et de la bonne volonté, guide les faibles à travers la vallée des ténèbres, car il est vraiment le gardien de son frère et le chercheur des enfants perdus.</p>  <p class="color-dark">Et je frapperai avec une grande vengeance et une colère furieuse ceux qui tenteraient d'empoisonner et de détruire mes frères.</p>  <p class="color-dark">Et tu connaîtras mon nom est le Seigneur lorsque je déposerai ma vengeance sur toi.</p></div>
```

```
/* Oui */<div class="background-light color-dark">  <h2 class="color-lime">Ézéchiel 25:17</h2>  <p>Le chemin de l'homme juste est entouré de toutes parts par les injustices des égoïstes et la tyrannie des hommes mauvais.</p>  <p>Béni soit celui qui, au nom de la charité et de la bonne volonté, guide les faibles à travers la vallée des ténèbres, car il est vraiment le gardien de son frère et le chercheur des enfants perdus.</p>  <p>Et je frapperai avec une grande vengeance et une colère furieuse ceux qui tenteraient d'empoisonner et de détruire mes frères.</p>  <p>Et tu connaîtras mon nom est le Seigneur lorsque je déposerai ma vengeance sur toi.</p></div>
```

### Accepter le changement, dans la raison

Avoir des opinions fortes est formidable. Tout ne doit pas être réglé en trouvant un terrain d'entente. Mais il y a une ligne claire à tracer entre **avoir des opinions** et **être réticent au changement**.

Nous, en tant que développeurs, **devons être les premiers à accepter le changement**. En repensant à ma première réaction envers le CSS utility-first, je réalise à quel point il est important de garder l'esprit ouvert au lieu de se précipiter pour choisir un camp. **Peu importe à quel point nous pensons être expérimentés**. L'expérience est formidable, mais elle peut aussi nous faire croire que nous avons déjà tout ce dont nous avons besoin pour prendre des décisions et que nous n'avons pas besoin d'approfondir pour comprendre de nouveaux concepts.

**Le développement logiciel change tous les jours**. Notre industrie est encore jeune, et nous découvrons les choses au fur et à mesure. Cela ne signifie pas que nous devons jeter le passé et refactoriser continuellement tous nos projets pour suivre les dernières tendances. Les connaissances passées sont le fondement des découvertes d'aujourd'hui. Mais simplement parce que quelque chose est éprouvé et vrai, cela ne signifie pas qu'il est gravé dans le marbre. Il est important d'aborder la nouveauté avec un esprit critique.

Nous passerons probablement du CSS utility-first à un moment donné, comme nous avons dépassé de nombreuses choses que nous considérions comme le summum du développement front-end. En attendant, essayons de rester aussi ouverts d'esprit que possible, et **faisons ce qui est le mieux pour l'industrie, les projets et les utilisateurs**.

Vous voulez en savoir plus sur le CSS utility-first et comment l'utiliser dans vos projets ? Allez lire [On the Growing Popularity of Atomic CSS](https://css-tricks.com/growing-popularity-atomic-css/) sur CSS Tricks et [CSS Utility Classes and "Separation of Concerns"](https://adamwathan.me/css-utility-classes-and-separation-of-concerns) sur le blog d'Adam Wathan. Vous pouvez également consulter les bibliothèques utility-first sur cette [liste sélectionnée](https://css-tricks.com/need-css-utility-library/) par CSS Tricks.

Publié à l'origine sur [frontstuff.io](https://frontstuff.io/in-defense-of-utility-first-css).