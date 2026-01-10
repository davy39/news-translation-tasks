---
title: "Cours gratuit : Construire un blog à partir de zéro ?\r"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-20T00:06:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-and-develop-a-beautiful-blog-from-scratch-a0cd1af46845
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WdnElaIfE85DgLiNJynf0w.jpeg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: "Cours gratuit : Construire un blog à partir de zéro ?\r"
seo_desc: 'By ZAYDEK

  TIL…

  Free Course: Build A Blog From Scratch ?‍?

  It might be easier than imagined

  Before I get to the article, I just want to share that I’m building a product, and
  I would love to collect some data about how to better serve web developers. ...'
---

Par ZAYDEK

#### TIL

# Cours gratuit : Construire un blog à partir de zéro ?

#### Cela pourrait être plus facile que vous ne l'imaginez

Avant d'aborder l'article, je souhaite partager que je construis un produit et que j'aimerais collecter des données sur la manière de mieux servir les développeurs web. J'ai créé un [court questionnaire](https://twitter.com/username_ZAYDEK/status/1103914471267790854) à consulter avant ou après la lecture de cet article. Veuillez y jeter un coup d'œil — merci ! Et maintenant, revenons à notre programmation régulière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_L60Gs-iTza_LnBdwqzEiA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*t929RLZ28EvUsc5f3Hbh8Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*8xYM6BQXa7HNpMd2XMD5Lw.png)
_Le blog que nous allons construire. Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

Si vous êtes comme moi, vous êtes intéressé par le web et sa portée écrasante, mais vous êtes également submergé par le désordre d'informations que représente l'apprentissage du HTML et du CSS. Le problème, c'est que ces langages sont différents des autres domaines, comme les traitements de texte et les langages de programmation. **Le web est un autre monde**, et ce n'est pas la chose la plus joli qui soit.

Ayant appris un peu de web, je suis ici pour vous donner une petite poussée d'encouragement, car, **avec un peu de guidance**, ces domaines peuvent être beaucoup plus faciles que vous ne l'imaginez. Continuez à lire, et nous construirons un beau blog à partir de zéro. Nous apprendrons également quelques notions de [CSS Grid](https://scrimba.com/g/gR8PTE), [Flexbox](https://scrimba.com/g/gflexbox), et de Responsive Design.

Le but est de faire pour vous ce que j'ai fait pour moi-même ; **apprendre le HTML et le CSS à partir des premiers principes.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*f375llkXaEoZFZ7ag2gbFQ.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

#### J'ai également enseigné un [cours gratuit HTML/CSS](https://scrimba.com/g/gbuildablog) sur Scrimba où j'enseigne comment construire un beau blog à partir de zéro. [Cliquez ici pour vous inscrire !](https://scrimba.com/g/gbuildablog) ?

#### [Scrimba.com](https://scrimba.com/g/gbuildablog) est une plateforme interactive front-end où les sites web sont enregistrés comme des événements — pas des vidéos — et peuvent être modifiés ! ?

### D'où vient le HTML ?

Le HTML est un descendant du premier langage **méta** ou **balisage** : GML. Les lecteurs milléniaux comprennent maintenant que GML signifie **Generalized** Markup Language, mais ce n'est pas tout ce qu'il représente. C'est Charles **G**oldfarb, Edward **M**osher, et Raymond **L**orie qui ont créé ce que nous connaissons maintenant comme un langage **méta** ou **balisage** chez IBM. Et en 1996, Charles Goldfarb [a écrit](https://en.wikipedia.org/wiki/charles_goldfarb) :

> « J'ai donné à GML son nom actuel afin que nos initiales prouvent toujours d'où il venait. L'une des vérités laides du transfert de technologie est que les développeurs tendent à être reconnaissants pour le travail de recherche lorsqu'ils le reçoivent pour la première fois, et virtuellement oublieux à la fin d'un long cycle de développement... »

> — Charles Goldfarb, en [1996](https://en.wikipedia.org/wiki/charles_goldfarb)

GML est ensuite devenu **S**tandardisé, devenant ainsi SGML. Ensuite, Tim Berners-Lee, qui travaillait au CERN, a emprunté le ML de SGML (non, pas le machine learning, ou quoi que les hipsters l'appellent) pour créer HTML, où HT signifie **H**yper**T**ext.

Waouh, un mot cool. Et autant que je sache, il a des racines dans un environnement d'auteur interactif appelé HyperCard, de Bill Atkinson qui travaillait chez Apple. Pour une exploration plus approfondie, je vous propose les vidéos suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*4DSxCgGWawHSdvpZgLeZow.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*95_RjnFSh1VrE5srVzh2jw.png)
_Cliquez sur l'une ou l'autre pour en savoir plus_

Donc — faisons un récapitulatif. Le HTML n'a pas **simplement** pris le contrôle du monde. En fait, il y avait tout un monde avant le HTML. QUOI ? Je sais, je tremble de choc — mais je n'étais pas né — donc, il n'y avait pas vraiment de monde.

Et, le HTML doit beaucoup à ses prédécesseurs. Comme nous tous à nos parents. Néanmoins, c'est ainsi que nous créons du code à partir de texte. Maintenant, en quatre **leçons d'une minute**, je vais vous enseigner les bases du HTML, du CSS et du Responsive Design.

### HTML et CSS en 4 minutes

#### Première minute : Un site web peut être mieux compris comme un arbre web

```
<html>    <head></head>    <body></body></html>
```

Tous les sites web commencent leur vie ainsi. Cependant — et c'est terrible — il n'y a pas de contenu. Néanmoins, nous commençons ici parce que nous devons d'abord comprendre ce qu'est un site web. Pensez-y comme à un arbre — un arbre à l'envers — un **arbre** web. L'élément `html` est la **racine**, tandis que `head` et `body` sont les premières **branches** de notre **arbre** web :

```
   html <- racine   /  \head  body <- branches
```

L'élément `head` (ou **balise** — c'est la même chose) est pour les **métadonnées**, ou les informations **sur** notre site web. L'élément `body`, en revanche, est pour le contenu de notre site web. Et parce que le CSS est le style de notre site web, il va dans l'élément `head`, tandis que le contenu, comme les paragraphes, les vidéos de chats (≧∇≦), etc., vont dans l'élément `body`.

#### Deuxième minute : les éléments, ou balises, ont plusieurs apparences

```
<element><element>value</element><element attribute="value">value</element>
```

1. Le premier élément est un **élément auto-fermant**, où nous communiquons quelque chose au navigateur, mais il n'a pas non plus de valeur. Un exemple de cela est l'élément `<br>`, qui insère un saut de ligne.
2. Le deuxième élément est un **élément commun**, où nous communiquons **une** valeur comme appartenant à un élément. Par exemple, `<p>hello, world!</p>` est la valeur « hello, world! » comme appartenant à l'élément paragraphe.
3. Enfin, nous avons un **élément avec un attribut**. Et un attribut est ce à quoi il ressemble — *bon sang, c'est un attribut* ! Il donne à un élément plus de contexte ou de signification. Les attributs peuvent avoir plusieurs valeurs, et les éléments peuvent avoir plusieurs attributs. Attribut-ception.

```
<element attribute="value" attribute="value value">value</element>
```

Maintenant — je dois mentionner — nous ne créons pas les noms de nos éléments HTML. Nous les **empruntons** à une liste de quelque [100+ éléments](https://developer.mozilla.org/en/docs/Web/HTML/Element) qui sont prédéfinis. Bien sûr, cela rend certaines choses plus faciles, et d'autres beaucoup, beaucoup plus difficiles, comme la mémorisation !

#### Troisième minute : Comment HTML et CSS communiquent

```
<!DOCTYPE html><html>    <head>        <meta charset="UTF-8">        <style>
```

```
selector { property: value; }
```

```
        </style>    </head>    <body>        <element>value</element>    </body></html>
```

Le `!DOCTYPE html` spécifie que nous écrivons en HTML5 — comme supposé à [toutes les autres versions de HTML](https://meiert.com/en/indices/html-elements/) que nous voulons éviter. Et étant donné l'**élément auto-fermant** `meta` avec l'**attribut** `charset` et la **valeur** `UTF-8`, notre texte est encodé en Unicode. UTF-8 signifie **U**nicode **T**ransformation **F**ormat... **8**. Maintenant nous pouvons écrire en ????! Une fois, papa a décidé d'envoyer un SMS en utilisant uniquement des _emojis_.

> \_()_/

Nous avons également ajouté un élément `style` qui est l'un des points d'entrée disponibles pour le CSS. Où le `selector` **sélectionne** un élément et lui applique une `property` avec une `value` correspondante. Nous explorerons cela et plus encore dans la minute suivante.

Encore une fois — je dois mentionner — nous ne créons pas les noms de nos propriétés CSS. Nous les **empruntons** à une liste de quelque [centaines de propriétés](https://meiert.com/en/indices/css-properties/) qui sont prédéfinies. Bien sûr, cela rend certaines choses plus faciles, et d'autres beaucoup, beaucoup plus difficiles, comme ____________!

#### Quatrième minute : bonjour, monde !

```
<!DOCTYPE html><html>    <head>        <meta charset="UTF-8">        <style>
```

```
p { color: green; }
```

```
@media (max-width: 8.5in) { p { color: blue; } }@media (max-width: 5.0in) { p { color: red ; } }
```

```
        </style>    </head>    <body>        <p>hello, world!</p>    </body></html>
```

Notre site web n'est plus terrible ! Ce que nous avons, c'est « hello, world ! » en texte vert, et si la largeur de notre site web était redimensionnée à 8,5 pouces ou moins, il serait lu en bleu, et à 5 pouces ou moins, en rouge. Ici, nous avons utilisé des **media queries** pour remplacer le CSS dans certaines circonstances, comme la largeur de notre site web.

### Qu'est-ce qu'une réinitialisation CSS et un débogueur ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*NqINgpW_3YieQ1i4plm1oQ.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

Nous utilisons une réinitialisation pour garantir que notre design est cohérent, et un débogueur pour exposer les incohérences.

Nous avons besoin de notre réinitialisation, car les navigateurs sont opinatifs et **définissent** certaines propriétés CSS pour nous que nous voulons **supprimer**. Des réinitialisations CSS populaires existent, mais nous créerons la nôtre. Et nous avons besoin de notre débogueur pour maintenir le design de notre site web avec facilité.

Nous pouvons créer un dossier nommé `styles` pour héberger notre réinitialisation et notre débogueur :

```
styles/       reset.css       debug.css
```

Et pour **lier** nos nouveaux fichiers CSS à notre `index.html`, nous ajoutons des éléments `link` :

```
                <meta charset="UTF-8">        <link rel="stylesheet" href="styles/reset.css">        <link rel="stylesheet" href="styles/debug.css">        <style>        
```

#### Notre réinitialisation CSS

Parmi les propriétés que nous voulons supprimer, voici une courte liste :

```
:root { font: 20px/1.2 sans-serif; }
```

```
body, body * {    margin:          unset;    box-sizing:      unset;    padding:         unset;    font-size:       unset;    color:           unset;    text-decoration: unset;}
```

Ignorez la ligne 1. pour l'instant — commençons par `body, body * {  }` où nous sélectionnons le `body` et tous les éléments du `body` avec un `*`. L'astérisque signifie **sélectionner tous les enfants**. Souvenez-vous de notre **arbre** web ?

```
   html   /  \head  body <- sélectionné / \    \       p <- sélectionné
```

`body, body * {  }` sélectionne le `body` et — un `,` désigne et — `p` parce qu'il est l'un des enfants du `body`. Cela est connu comme la relation **parent-enfant**, où `body` est le parent et `p` est l'enfant. Et nous disons à ces éléments de `unset` les propriétés communes. Les propriétés que j'ai choisies ne sont qu'une courte liste. Voici un exemple de [l'une des réinitialisations CSS les plus célèbres](http://meyerweb.com/eric/tools/css/reset/) :

```
/* http://meyerweb.com/eric/tools/css/reset/   v2.0 | 20110126   License: none (public domain)*/
```

```
html, body, div, span, applet, object, iframe,h1, h2, h3, h4, h5, h6, p, blockquote, pre,a, abbr, acronym, address, big, cite, code,del, dfn, em, img, ins, kbd, q, s, samp,small, strike, strong, sub, sup, tt, var,b, u, i, center,dl, dt, dd, ol, ul, li,fieldset, form, label, legend,table, caption, tbody, tfoot, thead, tr, th, td,article, aside, canvas, details, embed,figure, figcaption, footer, header, hgroup,menu, nav, output, ruby, section, summary,time, mark, audio, video {    margin: 0;    padding: 0;    border: 0;    font-size: 100%;    font: inherit;    vertical-align: baseline;}/* HTML5 display-role reset for older browsers */article, aside, details, figcaption, figure,footer, header, hgroup, menu, nav, section {    display: block;}body {    line-height: 1;}ol, ul {    list-style: none;}blockquote, q {    quotes: none;}blockquote:before, blockquote:after,q:before, q:after {    content: '';    content: none;}table {    border-collapse: collapse;    border-spacing: 0;}
```

Yikes ! Revenons à **notre** réinitialisation. En haut, nous avons `:root { font: 20px/1.2 sans-serif; }`. Qu'est-ce que `:root` ? Souvenez-vous de notre **arbre** web ? C'est **la** racine, en d'autres termes, **l'**élément `html`. Ce pseudo-élément appartient à une classe spéciale d'éléments connue sous le nom de [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements), qui peuvent être utilisées pour mieux organiser et comprendre notre CSS.

WAAAIT ! N'avons-nous pas besoin d'un `*` pour **sélectionner tous les éléments enfants**, afin que leurs propriétés `font` soient définies ? Eh bien — excellente question — certaines propriétés, comme les propriétés de texte, héritent de leurs parents, et `font` le fait. Donc, au lieu de cela, nous pouvons définir `font` une fois dans `:root`, ce qui se propage à tous ses enfants. Property-ception.

#### Notre débogueur CSS

Un débogueur met en évidence le contenu et la bordure des éléments :

```
body * {    color:                 hsla(000, 100%, 100%, 0.88) !important;    background:            hsla(210, 100%,  50%, 0.33) !important;    outline: 0.25rem solid hsla(000, 100%, 100%, 0.50) !important;}
```

Voilà ! En seulement **trois** lignes, notre débogueur. Cette technique astucieuse **remplace** trois propriétés courantes : `color`, `background`, et `outline`. Nos couleurs sont composées de valeurs `hsla()`, qui est l'abréviation de **h**ue, **s**aturation, **l**uminance, et **a**lpha. Pour activer notre débogueur, nous lions le fichier.

Si nous voulons **désactiver** notre débogueur, nous pouvons **mal orthographier** le nom du fichier afin de le cacher du système de fichiers de notre ordinateur, par exemple :

```
<link rel="stylesheet" href="styles/-debug.css">
```

Ou simplement supprimer la ligne. ۹(^.^)۶

Notre débogueur utilise des valeurs `!important` hilarantes afin de déclarer que **dans aucune condition** ces propriétés ne peuvent être remplacées. Souvenez-vous des media queries ?

```
p { color: green !important; }
```

```
@media (max-width: 8.5in) { p { color: blue; } }@media (max-width: 5.0in) { p { color: red ; } }
```

Si nous avions spécifié que la couleur de notre `p` est `!important`, nos media queries seraient inertes, en raison de leur moindre importance.

### Rencontrez CSS Grid et Flexbox

![Image](https://cdn-media-1.freecodecamp.org/images/1*QPWoLoE0Vz1KkYBB6ESJ5Q.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

Je dirais qu'avant CSS Grid et Flexbox, concevoir pour le web était un voyage de héros.

Le problème, c'est que la conception web était autrefois un acte de jonglage de hacks où nous trompons le navigateur pour qu'il rende nos designs. Cela devient de moins en moins vrai avec le temps. Je ne suis pas religieux, mais _merci Dieu !_ — ou, _merci les ingénieurs de navigateurs !_ — grâce à quoi nous pouvons maintenant nous appuyer sur CSS Grid et Flexbox pour démarrer notre design.

Si vous n'êtes pas au courant, CSS Grid et Flexbox sont des technologies plus récentes intégrées dans les navigateurs modernes qui éliminent le voyage du héros de la conception web. Et CSS Grid et Flexbox sont amis — nous les utiliserons ensemble pour créer à la fois une **grille** et **flex** des éléments dans notre grille.

#### Notre première grille : HTML

```
        <body>        <article>            <p>ARTICLE</p>        </article>
```

```
        <article>            <p>ARTICLE</p>        </article>    </body>    
```

Souvenez-vous de notre **arbre** web ?

```
      body      /  \article  article    /      \   p        p
```

Nous créons un blog, donc chaque publication peut être considérée comme un `article`. Et nos `article`s contiennent un `p` de `ARTICLE` qui est une autre astuce que nous pouvons utiliser. Utiliser le **nom** de l'élément comme **valeur** de l'élément pour nous aider à comprendre où et ce que sont les choses. Value-ception.

#### Notre première grille : CSS

```
        <style>
```

```
article {    display: grid;    grid-template-columns: 1fr minmax(0, 8.5in) 1fr;
```

```
    height: 11in; /* temp fix */}
```

```
article * { grid-column: 2 / 3; }
```

```
    </style>    
```

Voici CSS Grid. D'abord, nous avons **sélectionné** l'article, et appliqué trois propriétés : `display` définit l'élément comme une grille, `grid-template-columns` modèle les colonnes, et `height` simule chaque `article` comme ayant la hauteur d'une page. Cependant, `height` est du code de colle et **sera** supprimé.

Concentrons-nous sur les deux lignes les plus importantes :

```
article   { grid-template-columns: 1fr minmax(0, 8.5in) 1fr; }article * { grid-column: 2 / 3; }
```

Ou, en d'autres temps :

> Tu auras trois colonnes,

> Dont la colonne centrale abritera tes enfants.

D'abord, si nous avions défini `grid-template-columns` à `1fr 1fr 1fr`, où `fr` est l'abréviation de **fr**action-unit, nos **trois** colonnes seraient divisées en **tiers**. Pourtant, notre colonne centrale a une largeur `minmax`, ce qui signifie qu'elle est **responsive**. À ou moins de `8.5in`, notre colonne centrale se rend à une largeur de `100%`, et nos colonnes les plus à gauche et à droite disparaissent, car il n'y a pas de reste.

Barre latérale : notez que le design responsive n'est pas limité aux media queries. C'est un exemple où notre design est **implicitement responsive**, par opposition à **explicitement responsive**. C'est le meilleur type de design responsive, car il n'est pas codé en dur. Et c'est l'une des raisons pour lesquelles CSS Grid et Flexbox sont si puissants.

Deuxièmement, pour communiquer que les enfants de `article` appartiennent à la colonne centrale, ou **commencent à la deuxième colonne** et **se terminent à la troisième**, nous définissons `grid-column` à `2 / 3`. Notez la différence subtile entre `grid-template-column` et `grid-column`, pour soit **modéliser les colonnes** soit **étendre les colonnes**.

CSS Grid est génial — et il l'est — mais maintenant nous allons nous appuyer sur Flexbox pour centrer notre texte `ARTICLE`. Ce que nous allons faire est créer une **Classe Utilitaire**, et c'est un autre paradigme pour écrire du CSS. Ici, nous utilisons le fait que les éléments peuvent avoir des attributs pour intégrer le style au `p` élément :

```
<p class="debug-center">ARTICLE</p>
```

> CSS dans HTML ?!

> (╯°□°）╯︵ ┻━┻

Voici ce qui se passe : les éléments ont un attribut **class**. Et nous pouvons utiliser cet attribut non seulement pour écrire du CSS pour les éléments, mais pour un type d'élément ou une classe d'élément. Cela signifie que nous pouvons réutiliser des classes sur plusieurs éléments, indépendamment de leur similitude. Hélas — rien n'a changé — nous devons également créer une classe `.debug-center` quelque part dans notre CSS. Que diriez-vous de notre débogueur :

```

```

```
.debug-center {    display:         flex;    justify-content: center;    align-items:     center;}
```

Notez que nous utilisons un préfixe `.` pour différencier les classes des éléments.

Maintenant, partout où un élément est attribué avec notre classe `debug-center`, son texte sera centré. D'abord, nous définissons `display` à `flex` faisant de n'importe quel élément un élément Flexbox par opposition à un élément CSS Grid. Ensuite, nous définissons `justify-content` à `center` pour centrer **horizontalement** et `align-items` à `center` pour centrer **verticalement**. Aaagh !

Imaginez ceci : nous utilisons Grid pour disposer le design de notre site web, et Flexbox pour flexer les éléments dans notre grille à une position souhaitée.

### Itérer notre grille

![Image](https://cdn-media-1.freecodecamp.org/images/1*a6AM78K5OOVNMx1flg8agQ.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

Nous avons un problème : sans `.debug-center` `ARTICLE` colle aux murs de gauche et de droite. Ce dont nous avons besoin, ce sont des gouttières verticales et horizontales pour que notre contenu puisse respirer. Aaah. Sinon, la lecture deviendrait frustrante et entraînerait une mauvaise expérience utilisateur. (｡･ω･｡)

Pour le remplissage vertical :

```
article {    padding: 0.5in 0;    }
```

Et pour le remplissage horizontal, nous pourrions utiliser le remplissage, et l'un ou l'autre fonctionnerait :

```
padding: 0.5in 0.5in;padding: 0.5in;
```

Cependant, nous voulons que nos gouttières soient réactives, donc nous utiliserons CSS Grid :

```
article {        grid-template-columns: 1fr 0.5in [start] 7.5in [end] 0.5in 1fr}
```

Ici, nous avons fait trois choses : 1. nous avons défini nos gouttières horizontales à `0.5in` (elles deviendront réactives — je le promets !). 2. notre colonne de contenu est passée de `8.5in` à `7.5in`, la somme étant **toujours** `8.5in`, et 3. nous avons créé des identifiants `start` et `end` pour nommer le début et la fin de notre colonne de contenu.

Lorsque nous avons ajouté de nouvelles colonnes, nous avons également dû mettre à jour `article *` :

```
article * { grid-column: 3 / 4; }
```

Mais compter les colonnes n'est pas idéal. Au lieu de cela — utilisons nos identifiants inventés :

```
article * { grid-column: start / end; }
```

Nous avons mis à jour notre grille sans rompre le flux de contenu, tant que nous continuons à utiliser les identifiants `start` et `end` que nous avons inventés. ⋈◍＞◡＜◍⋈

Enfin — comme promis — nous avons besoin que nos gouttières soient réactives. `minmax()` pour une raison ou une autre ne fonctionne pas ici, donc nous utiliserons des media queries :

```
@media (max-width: 8.5in) {    article {        grid-template-columns: 1fr 5% [start] 90% [end] 5% 1fr;    }}
```

Maintenant **à** ou **moins de** `8.5in`, `article` utilisera `%` au lieu de `in` pour diviser nos colonnes, et les colonnes les plus à gauche et à droite disparaîtront parce que — encore une fois — il n'y a pas de reste. Malgré tout cela, nous aurions pu définir `padding` à `0.5in 5%` pour obtenir le même effet, alors qu'est-ce qui se passe ? Lisez la suite !

### Itérer notre grille, encore

![Image](https://cdn-media-1.freecodecamp.org/images/1*u_0x1Nw7fXUujx0058UKqQ.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

Pour comprendre notre grille, utilisons des images pour étendre les colonnes, de `100%` à `8.5in` à `7.5in` sur le bureau, et de `100%` à `90%` sur le mobile. Cependant, pour la dernière image, celle de gauche en bas, nous devons ajouter _encore plus de colonnes_ à notre grille. AF)UBQWF*VBQPWIFB, n'est-ce pas ?

Ne soyez pas intimidé — CSS grid est génial. Ajoutons deux colonnes de plus :

```
article {        grid-template-columns:        1fr 0.5in [start] 1.25in 5in 1.25in [end] 0.5in 1fr;}
```

```
@media (max-width: 8.5in) {    article {        grid-template-columns:            1fr 5% [start] 15% 60% 15%[end] 5% 1fr;    }}
```

Nous avons divisé notre colonne de contenu en trois colonnes : `1.25in 5in 1.25in`. Nous avons également ajouté des pourcentages proportionnels pour notre media query : `15% 60% 15%`. Le plan est que le texte s'étende sur notre colonne de contenu `7.5in` d'origine, et que les petites images s'étendent sur notre nouvelle colonne `5in`.

Pour ajouter des images, nous utilisons l'élément `img` et son attribut `src` — source — :

```
                <article>            <img class="size-4" src="images/cosmos.jpg">            <img class="size-3" src="images/cosmos.jpg">            <img class="size-2" src="images/cosmos.jpg">            <img class="size-1" src="images/cosmos.jpg">        </article>        
```

Celles-ci sont locales, c'est-à-dire qu'elles sont sur notre ordinateur. Et si elles étaient distantes, c'est-à-dire sur un serveur :

```
<img src="https://website.com/images/cosmos.jpg">
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*WdnElaIfE85DgLiNJynf0w.jpeg)

Notez que chaque `img` a l'une des quatre classes : `size-*`. Et parce que nous voudrons plus que des images, comme des vidéos, pour étendre la grille de notre site web, il est préférable d'utiliser des classes afin que nous puissions réutiliser le CSS. Ces classes `size-*` sont également des Classes Utilitaires, donc changer la taille que nous voulons est simple.

Créons nos classes `size-*` pour qu'elles s'étendent sur différents ensembles de colonnes :

```
.size-1 { grid-column: 4 / 5; }.size-2 { grid-column: 3 / 6; }.size-3 { grid-column: 2 / 7; }.size-4 { grid-column: 1 / 8; }
```

Ce qui manque, c'est que nos `img` ne sont pas réactives. Nous avons besoin de :

```
img.size-1, img.size-2, img.size-3, img.size-4 { width: 100%; }
```

Parce que les `img` se rendent à leur taille réelle, par exemple, une image de 400 × 400 se rendant à 400px, nous avons dû remplacer ce comportement par le nôtre : `width: 100%`. Ainsi, lorsqu'une image est attribuée avec une classe `size-*`, elle peut redimensionner pour s'adapter aux colonnes qu'elle couvre. Notez que nous n'avons pas besoin de définir `height`.

### Ajout d'éléments de texte

![Image](https://cdn-media-1.freecodecamp.org/images/1*_Im48x4QvYjzs4bcWUhIug.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*OlaIElTR6e8Dn-SgIXK13Q.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

#### Liens vers le site web et le contenu

Maintenant que nous prenons notre `article` au sérieux, formalisons les choses :

```
                <article id="the-cosmos"></article>        
```

Maintenant, chaque article est **liable**. **Liable** ? Eh bien — les sites web sont des **liens** :

```
https://website.com/index.html
```

Et le contenu de notre site web, par exemple les `article`s, peut également être **lié** :

```
https://website.com/index.html#article
```

Ici, `article` est la valeur d'un attribut `id`, analogue à la liaison d'un timestamp dans une vidéo YouTube (par exemple, [celle-ci](https://www.youtube.com/watch?v=5TbUxGZtwGI&feature=youtu.be&t=4m7s)). Mieux que de suggérer « commencez à 4 minutes et 7 secondes » ou « lisez à partir du deuxième article », nous pouvons lier le contenu de notre site web, comme un timestamp dans une vidéo.

Pour lier un site web ou du contenu, nous utilisons l'élément `a` et l'attribut `href` :

```
                <article id="the-cosmos">            <a href="#the-cosmos">The Cosmos</a>        </article>        
```

Le texte « The Cosmos » lie maintenant le début de l'article : `#the-cosmos`.

**Cette idée de liaison (lier des sites web et du contenu dans des sites web) est l'un des points du HTML.** HyperCard a maîtrisé cela, mais au lieu de lier des sites web et du contenu, s'intéressait aux idées et aux associations. À l'époque, c'était 1987 et [le HTML a été proposé pour la première fois en 1989](http://info.cern.ch/Proposal.html). Regardez quelques secondes de la vidéo que j'ai publiée plus tôt — voici j'ai lié un timestamp :

#### Éléments de texte

Ajoutons des titres, une date de publication, du texte fort et mis en emphase, et des liens :

```
<article id="the-cosmos">
```

```
    <h1><a href="#the-cosmos">The Cosmos is all there is</a></h1>    <h2>Or ever was, or ever will be</h2>
```

```
    <time datetime="03-09-2014">MAR. 9, 2014</time>    <p><em>A generation ago</em>, the astronomer <a href="https://en.wikipedia.org/wiki/carl_sagan">Carl Sagan</a> stood here and launched hundreds of millions of us on a great adventure the exploration of the universe revealed by science. It's time to get going again. We're about to begin a journey that will take us from the infinitesimal to the infinite, from the dawn of time to the distant future. We'll explore galaxies and suns and worlds, surf the gravity waves of space-time, encounter beings that live in fire and ice, explore the planets of stars that never die, discover atoms as massive as suns and universes smaller than atoms.    </p>
```

```
    <img class="size-4" src="images/cosmos.jpg">
```

```
    <h3>COSMOS IS ALSO A STORY ABOUT US</h3>    <p>It's the saga of how wandering bands of hunters and gatherers found their way to the stars, one adventure with many heroes. To make this journey, we'll need imagination. But imagination alone is not enough because the reality of nature is far more wondrous than anything we can imagine. This adventure is made possible by generations of searchers strictly adhering to a simple set of rules test ideas by experiment and observation, build on those ideas that pass the test, reject the ones that fail, follow the evidence wherever it leads and question everything. <strong>Accept these terms, and the cosmos is yours.</strong>    </p>
```

```
</article>
```

Ce sont les lignes d'ouverture de notre astrophysicien personnel — Neil deGrasse Tyson — 2014 [Cosmos : A Spacetime Odyssey](https://en.wikipedia.org/wiki/cosmos:_a_spacetime_odyssey), une réimagination du Cosmos original de Carl Sagan en 1980 [Cosmos : A Personal Voyage](https://en.wikipedia.org/wiki/cosmos:_a_personal_voyage). C'est de la science-fiction sans le -fi. Et il est renouvelé en 2019 !

Ci-dessus, nous avons introduit quelques éléments : `h1`, `h2`, `h3`, `time`, `strong`, et `em`.

1. Les éléments `h1`–`h6` sont des **t**itres.
2. L'élément `time` **horodate** notre article. Nous pouvons mettre ce que nous voulons pour la valeur de l'élément, car les ordinateurs lisent la valeur de l'attribut `datetime`, qui doit être [lisible par machine](https://en.wikipedia.org/wiki/iso_8601).
3. L'élément `strong` est pour le texte **fort** et l'élément `em` est pour le texte _mis en emphase_. De plus, les éléments `h*` sont **forts**.

Notez que les éléments `h*` et `p` passent d'une ligne à l'autre, ou **bloc**, tandis que les éléments `time`, `strong`, et `em` ne le font pas. Cela est dû au fait que les navigateurs définissent le `display` des éléments `h*` et `p` à `block`, et le `display` des éléments `time`, `strong`, et `em` à `inline`.

#### Rems et ems

Lorsque ce n'est pas suffisant de bloquer les éléments d'une ligne à l'autre, nous utilisons des sauts de ligne pour qu'il soit plus facile de différencier les éléments les uns des autres, un peu comme le remplissage ou les gouttières. Nous pourrions utiliser des éléments `br` ici, mais **il est préférable d'utiliser du CSS superflu plutôt que du HTML superflu**.

Voici comment pousser le contenu de deux sauts de ligne, suivant les éléments `h2` et `p` :

```
h2, p { margin-bottom: 2.4rem; }
```

2.4rem ?

Souvenez-vous de notre réinitialisation ? Nous avons défini `font` à `20px/1.2 sans-serif`. Je ne l'ai pas expliqué à l'époque — et honte à moi — mais `2.4` correspond à deux sauts de ligne à une hauteur de ligne de `1.2`, par exemple, du texte à interligne simple. Un texte plus lisible pourrait être `1.5`, et du texte à double interligne pourrait être `2`.

*Ahem* Que sont les rems ?

*Ahem ahem* Et que sont les ems ?

`rem` est **root** `em` et les deux sont des multiplicateurs. `1rem` est `20px` et `1em` est la `font-size` du parent. Si nous avions défini nos sauts de ligne en `ems`, et non en `rems`, et que nous avions défini `h2` et `p` à différentes `font-size`, leurs sauts de ligne seraient différents ! Par conséquent, les sauts de ligne **cohérents** utilisent des `rem`s et les **incohérents** utilisent des `em`s.

Et c'est une idée puissante — écrire du CSS de sorte que le design soit _connecté_. Étant donné cet éclairage, je pense qu'il est bien plus sage de réfléchir au CSS **non pas en règles mais en relations**. Ainsi, si nous apportons un changement quelque part, **nous pouvons apporter un changement partout**.

> ...apporter un changement quelque part...

> ...apporter un changement partout...

![Image](https://cdn-media-1.freecodecamp.org/images/1*7GXOKQOfQIMWil-NSZ3x5g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*OqjIAjwtw6II60rIOOG_KA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7GXOKQOfQIMWil-NSZ3x5g.png)
_Un vrai emoji Apple. Il avait un [communiqué de presse](https://www.apple.com/newsroom/2017/07/apple-previews-new-emoji-coming-later-this-year/" rel="noopener" target="_blank" title=")_

#### Design responsive responsive

Et si nous écrivons du CSS en `rem`s et `em`s, et utilisons des media queries pour changer la `font-size` de `:root` ? Alors tout — et je veux dire **tout** — sera redimensionné proportionnellement. Nous pouvons aller encore plus loin et avoir plusieurs media queries pour plusieurs largeurs :

```
@media (max-width: 8.5in) { :root { font-size: 18px; } }@media (max-width: 5.0in) { :root { font-size: 16px; } }
```

Ce qui est incroyable avec cela, c'est que nous ne remplaçons pas seulement **une** propriété, nous remplaçons **la** propriété pour les `rem`s et les `em`s. Nous pouvons maintenant écrire du CSS qui n'est pas seulement responsive mais responsive à notre design responsive. C'est peut-être la phrase la plus importante de cet article entier :

> Nous pouvons écrire du CSS qui n'est pas seulement responsive mais responsive à notre design responsive.

Ce n'est pas seulement cool, c'est ainsi que nous **devrions** écrire du CSS. Les sites web ont tendance à être terribles, et je pense que cela peut se résumer à ceci : **lorsque nous écrivons du CSS, nous devrions écrire en systèmes de design et non en code en silo**. Lorsque nous utilisons des `rem`s et des `em`s en tandem avec des media queries, c'est **un** système de design et le code n'est pas en silo.

#### Styliser le texte

Pour l'amour du style, ajoutons-en un peu :

```
h1   { font: 700 2.0rem/1.2 ; color: hsl(000, 000%, 33%); }h2   { font: 400 1.5rem/1.2 ; color: hsl(000, 000%, 33%); }time { font: 700 1.0rem/1.2 ; color: hsl(250, 100%, 83%); }h3   { font: 700 1.0rem/1.2 ; color: hsl(250, 100%, 67%); }p    { font: 400 1.0rem/1.5 ; color: hsl(000, 000%, 33%); }
```

Les propriétés peuvent avoir des raccourcis comme nous l'avons vu auparavant ; `padding: 0.5in`, équivalent à `padding: 0.5in 0.5in`. Et ici, nous utilisons `font` pour combiner `font-weight`, `font-size`, et `line-height`. Après `font`, nous avons `color` avec des valeurs `hsl`, comme les valeurs `hsla` dans notre débogueur.

Un problème non résolu est notre élément `a`. Dans notre réinitialisation, nous avons annulé `color` et `text-decoration` rendant les liens indiscernables du texte. Nous avons annulé ces propriétés car `text-decoration: underline` est trop subtil. Donc voici comment nous pouvons leur donner un soulignement fort :

```
a { box-shadow: inset 0 -0.25em hsl(55, 100%, 75%); }
```

Nous inversons `box-shadow` pour créer un soulignement qui est à l'intérieur de l'élément. Si nous avions défini `inset` sans valeur négative, notre soulignement serait un surlignage. Nous utilisons également `em` pour que le soulignement s'adapte à sa `font-size`. C'est un exemple de quand nous voulons un redimensionnement incohérent, contrairement à nos sauts de ligne.

Il y a _beaucoup_ plus à `box-shadow` que cela : [cliquez pour en savoir plus](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow).

### Dernière étape : les dégradés

![Image](https://cdn-media-1.freecodecamp.org/images/1*UhJ0kyFv5WkJN8k80Lf7Iw.png)
_Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

_Wohoo !_ Tout ce dont nous avons besoin est un **indice** pour nos lecteurs quant à l'endroit où un `article` commence et se termine. Sans cela, les fins de chaque `article` sembleront une continuation sans fin, ce qui conduit à une mauvaise expérience utilisateur. Nous devons donc donner un indice à nos lecteurs... (▀̿Ĺ̯▀̿ ̿)

Ce que je propose est simple : un dégradé qui s'étend du haut de chaque `article` au bas de son élément `h2`. Et nous pouvons écrire notre dégradé en `em`s afin que lorsque notre site web se redimensionne, notre dégradé aussi :

```
article {        background: linear-gradient(hsl(55, 100%, 96%), white 6.83em);}
```

Ici, nous avons défini un dégradé de couleur à blanc, et utilisé `6.83em` pour que notre dégradé ne s'étende pas sur tout l'`article` mais se termine à l'équivalent du bas de notre élément `h2`. Cependant, la valeur exacte dépend.

Vous pouvez soit faire des maths pour déterminer la taille, par exemple `6.83em`, mais une autre technique consiste à définir une taille sur la couleur du haut, par exemple `hsl(55, 100%, 96%) 6.83em`. Une fois qu'elle est **égale à** ou **supérieure à** la taille de la couleur du bas, elle apparaîtra comme une ligne et non comme un dégradé, ce qui rendra intuitif ce qu'il faut changer.

### Félicitations ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*_L60Gs-iTza_LnBdwqzEiA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*t929RLZ28EvUsc5f3Hbh8Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*8xYM6BQXa7HNpMd2XMD5Lw.png)
_Le blog que nous avons construit ! Vous préférez la vidéo ? [Cliquez ici](https://scrimba.com/g/gbuildablog" rel="noopener" target="_blank" title=") pour ouvrir dans Scrimba_

Félicitations ! ۹(ˊᵕˋ)۶ Vous avez fait un pas dans un monde qui a désespérément besoin de meilleurs designers et ingénieurs. Et avec CSS Grid, Flexbox, Responsive Design et les débogueurs au niveau du navigateur, le développement pour le web n'a **jamais** été plus accessible.

#### N'oubliez pas qu'il y a un [cours gratuit](https://scrimba.com/g/gbulma) sur Scrimba où j'enseigne comment créer le même site web à partir de zéro. [Cliquez ici pour vous inscrire !](https://scrimba.com/g/gbulma)

![Image](https://cdn-media-1.freecodecamp.org/images/1*f375llkXaEoZFZ7ag2gbFQ.png)