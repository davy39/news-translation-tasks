---
title: Comment écrire du HTML/CSS plus rapidement avec les codes raccourcis Emmet
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2020-09-22T17:16:17.000Z'
originalURL: https://freecodecamp.org/news/write-html-css-faster-with-emmet-cheat-codes
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/fCC_-Emmet.png
tags:
- name: efficiency
  slug: efficiency
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: Visual Studio Code
  slug: vscode
seo_title: Comment écrire du HTML/CSS plus rapidement avec les codes raccourcis Emmet
seo_desc: 'Emmet is one of my favorite built-in features of VS Code. It is also available
  as an extension in other code editors.

  Think of Emmet as shorthand. With it, you can easily write a lot of code quickly.
  It dramatically speeds up your HTML & CSS workflow...'
---

Emmet est l'une de mes fonctionnalités intégrées préférées de VS Code. Il est également disponible en tant qu'extension dans d'autres éditeurs de code.

Considérez Emmet comme un raccourci. Avec lui, vous pouvez facilement écrire beaucoup de code rapidement. Il accélère considérablement votre flux de travail HTML & CSS.

Comprendre comment utiliser Emmet est littéralement un superpouvoir. Certains l'ont même appelé un code de triche pour la programmation. 💡

Et ce n'est qu'une des nombreuses fonctionnalités intégrées incroyables de VS Code.

Récemment, j'ai lancé un cours complet et détaillé appelé [**Devenez un SuperHéros de VS Code**](https://courses.codestackr.com/vs-code-superhero?coupon=LAUNCH).\*\*\*\* Il couvre tous les aspects de VS Code en profondeur.

Cet article est basé sur l'une des 11 sections du cours : **Écriture & Formatage de Code**.

## HTML

Avec Emmet, vous pouvez créer rapidement un modèle HTML en un clin d'œil. Dans un fichier HTML, tapez simplement `!` et vous verrez qu'Emmet apparaît comme une suggestion. Appuyez ensuite sur `Entrée`. Vous avez maintenant une page web HTML basique et vide prête à l'emploi.

Si vous n'avez jamais vu de HTML auparavant et que vous n'avez aucune idée de ce que tout cela signifie, ne vous inquiétez pas. Je démontre simplement les capacités de VS Code et d'Emmet. Vous n'avez pas besoin de savoir ce que tout cela signifie pour l'instant.

### Balises de base

Pour créer des balises HTML de base, tapez simplement le nom de la balise et appuyez sur `Entrée`. Remarquez comment Emmet place votre curseur à l'intérieur de la balise. Vous êtes maintenant prêt à continuer à taper à l'intérieur de la balise.

* Essayez de taper : `div` puis `Entrée`, ou `h1 Entrée`, ou `p Entrée`.

* Ceux-ci fonctionnent également : `bq` pour un `<blockquote>`, `hdr` pour un `<header>`, `ftr` pour un `<footer>`, `btn` pour un `<button>`, et `sect` pour une section.

### Classes

Si vous êtes familier avec CSS, Emmet utilise la même méthode pour faire référence aux classes en utilisant un `.`. Pour définir une classe avec la balise, ajoutez-la simplement comme ceci :

* `div.wrapper` → `<div class="wrapper"></div>`

* `h1.header.center` → `<h1 class="header center"></h1>`

### Identifiants

Les identifiants fonctionnent de manière très similaire :

* `div#hero` → `<div id="hero"></div>`

### Combinaison

Vous pouvez les combiner :

* `div#hero.wrapper` → `<div id="hero" class="wrapper"></div>`

### Attributs

Nous pouvons également spécifier des attributs pour les balises :

* `img[src="cat.jpg"][alt="Cute cat pic"]` → `<img src="cat.jpg" alt="Cute cat pic" />`

### Contenu

Pour inclure du contenu dans la balise, nous enveloppons simplement le contenu dans des accolades, `{ }`.

* `p{This is a paragraph}` → `<p>This is a paragraph</p>`

### Frères et enfants

Cela ne fait que s'améliorer. Nous pouvons également spécifier des frères et des enfants en utilisant les caractères `+` et `>`.

* `section+section` → `<section></section><section></section>`

* `ul>li` → `<ul><li></li></ul>`

### Remonter

Vous devez essayer de visualiser ce que vous construisez dans votre tête en tapant le raccourci Emmet. Dans cet exemple, nous allons "remonter" l'arbre en utilisant `^`.

`div+div>p>span+em^bq`

Résultat :

```html
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```

Ici, nous voulions que le blockquote soit au même niveau que le paragraphe. Pour cette raison, nous avons dû "remonter". Sinon, il serait à l'intérieur du paragraphe.

### Groupement

Si votre structure est très complexe, vous pouvez regrouper les balises au lieu de naviguer en remontant.

Dans cet exemple, nous allons créer un en-tête et un pied de page sans remonter en utilisant des parenthèses `( )`.

`div>(header>ul>li>a)+footer>p`

Résultat :

```html
<div>
    <header>
        <ul>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>
```

### Multiplication et $

Nous pouvons générer plusieurs balises en multipliant (`*`) et numérotons les éléments en séquence en utilisant un signe dollar (`$`).

* `ul>li*5` → `<ul><li></li><li></li><li></li><li></li><li></li></ul>`

* `ul>li{Item $}*3` → `<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>`

Vous pouvez même personnaliser la séquence de numérotation en ajoutant des zéros, en commençant par un nombre spécifique, et même en inversant la direction.

Ajouter des zéros : `ul>li.item$$$*5`

Résultat :

```html
<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
    <li class="item004"></li>
    <li class="item005"></li>
</ul>
```

Commencer par un nombre spécifique : `ul>li.item$@3*5`

Résultat :

```html
<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>
```

Inverser la direction : `ul>li.item$@-*5`

Résultat :

```html
<ul>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>
```

Inverser la direction à partir d'un nombre spécifique : `ul>li.item$@-3*5`

Résultat :

```html
<ul>
    <li class="item7"></li>
    <li class="item6"></li>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
</ul>
```

### Noms de balises implicites

Il existe certaines balises qui n'ont pas besoin d'être tapées et peuvent être implicites.

* Une classe définie initialement sans balise sera implicite comme un `<div>`.
  `.wrapper` → `<div class="wrapper"></div>`

* Une classe définie dans une balise d'emphase sera implicite comme un `<span>`.
  `em>.emphasis` → `<em><span class="emphasis"></span></em>`

* Une classe définie dans une liste sera implicite comme un élément de liste.
  `ul>.item` → `<ul><li class="item"></li></ul>`

* Une classe définie dans un tableau sera implicite comme un `<tr>` et dans une ligne serait un `<td>`.
  `table>.row>.col` → `<table><tr class="row"><td class="col"></td></tr></table>`

### Envelopper avec des balises

Il y aura des moments où vous aurez du code existant que vous souhaitez envelopper avec une balise. Nous pouvons le faire facilement avec Emmet.

Il suffit de surligner le code que vous souhaitez envelopper et d'ouvrir la palette de commandes (`F1`). Ensuite, recherchez `Emmet: Wrap with Abbreviation`. Vous verrez alors une boîte de dialogue où vous pourrez taper l'élément.

`test` → `<div>test</div>`

Vous pouvez également utiliser la syntaxe standard Emmet dans cette boîte de dialogue. Essayez d'envelopper du texte avec `span.wrapper`.

Par défaut, cette fonctionnalité n'est pas assignée à un raccourci clavier. Donc, si vous l'utilisez souvent, vous pouvez ajouter un raccourci personnalisé pour cela.

### Lorem Ipsum

"Lorem Ipsum" est un texte factice utilisé par les développeurs pour représenter des données sur une page. Tapez simplement `lorem` et appuyez sur `Entrée`. Emmet générera 30 mots de faux texte que vous pouvez utiliser comme remplissage dans votre projet.

La quantité de mots générés peut également être définie.

* `lorem10` vous donnera 10 mots de texte aléatoire.

### Mettre tout ensemble

Utilisons plusieurs choses que nous avons apprises jusqu'à présent. Essayez ceci :

`ul.my-list>lorem10.item-$*5`

Résultat :

```html
<ul class="my-list">
  <li class="item-1">Lorem ipsum dolor sit amet.</li>
  <li class="item-2">Numquam repudiandae fuga porro consequatur?</li>
  <li class="item-3">Culpa, est. Tenetur, deleniti nihil?</li>
  <li class="item-4">Numquam architecto corrupti quam repudiandae.</li>
</ul>
```

## CSS

En CSS, Emmet a une abréviation pour chaque propriété. Je ne vais pas toutes les lister, mais je vais souligner celles que j'utilise le plus. Pour voir la liste complète, consultez la feuille de triche Emmet [cheat-sheet](https://docs.emmet.io/cheat-sheet/).

### Position

* `pos` → `position:relative;` (par défaut relative)

* `pos:s` → `position:static;`

* `pos:a` → `position:absolute;`

* `pos:r` → `position:relative;`

* `pos:f` → `position:fixed;`

### Affichage

* `d` → `display:block;` (par défaut block)

* `d:n` → `display:none;`

* `d:b` → `display:block;`

* `d:f` → `display:flex;`

* `d:if` → `display:inline-flex;`

* `d:i` → `display:inline;`

* `d:ib` → `display:inline-block;`

### Curseur

* `cur` → `cursor:pointer;`

### Couleur

* `c` → `color:#000;`

* `c:r` → `color:rgb(0, 0, 0);`

* `c:ra` → `color:rgba(0, 0, 0, .5);`

* `op` → `opacity: ;`

### Marge et Remplissage

* `m` → `margin: ;`

* `m:a` → `margin:auto;`

* `mt` → `margin-top: ;`

* `mr` → `margin-right: ;`

* `mb` → `margin-bottom: ;`

* `ml` → `margin-left: ;`

* `p` → `padding: ;`

* `pt` → `padding-top: ;`

* `pr` → `padding-right: ;`

* `pb` → `padding-bottom: ;`

* `pl` → `padding-left: ;`

### Dimensionnement de boîte

* `bxz` → `box-sizing:border-box;`

### Largeur

* `w` → `width: ;`

* `h` → `height: ;`

* `maw` → `max-width: ;`

* `mah` → `max-height: ;`

* `miw` → `min-width: ;`

* `mih` → `min-height: ;`

### Bordure

* `bd` → `border: ;`

* `bd+` → `border:1px solid #000;`

* `bd:n` → `border:none;`

### Emmet est génial !

Avec Emmet, vous pouvez créer une structure HTML vraiment complexe avec une seule ligne. C'est vraiment génial. Et cela fonctionne également avec CSS.

Vous pouvez voir comment Emmet peut augmenter considérablement votre efficacité et votre vitesse lors de l'écriture de HTML et de CSS.

Si vous souhaitez augmenter davantage votre efficacité et votre vitesse tout en utilisant VS Code, consultez mon cours [**Devenez un SuperHéros de VS Code**](https://courses.codestackr.com/vs-code-superhero?coupon=LAUNCH).

Le cours approfondit ces concepts et vous aide à devenir un développeur super-héros rapide et efficace :)

![Jesse Hall (codeSTACKr)](https://www.freecodecamp.org/news/content/images/2020/06/footer-banner-1.png align="left")

Je suis Jesse du Texas. Consultez mes autres contenus et faites-moi savoir comment je peux vous aider dans votre parcours pour devenir développeur web.

* [Abonnez-vous à ma chaîne YouTube](https://youtube.com/codeSTACKr)

* Dites Bonjour ! [Instagram](https://instagram.com/codeSTACKr) | [Twitter](https://twitter.com/codeSTACKr)

* [Inscrivez-vous à ma Newsletter](https://codestackr.com/)