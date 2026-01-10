---
title: 'Ligne par ligne : astuces CSS avancées pour les listes et menus déroulants
  cliquables'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-18T04:19:44.000Z'
originalURL: https://freecodecamp.org/news/mostly-css-drop-down-combo-boxes-4ff4bb182ff7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LL8iCzq1GKLgtaP_Y_be7w.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Ligne par ligne : astuces CSS avancées pour les listes et menus déroulants
  cliquables'
seo_desc: "By David Piepgrass\nFor as long as I can remember, there were always two\
  \ kinds of selectors.\n\nThere was the kind where the text on top could be edited,\
  \ and the kind where it couldn’t. HTML includes the second kind, no problem:\n<select>\n\
  \    <option>App..."
---

Par David Piepgrass

Pour autant que je me souvienne, il y avait toujours deux types de sélecteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/2abIBTqGwaakCmqxPmiGqUF8ldqbzZlfMBnR)

Il y avait le type où le texte en haut pouvait être édité, et le type où il ne le pouvait pas. HTML inclut le deuxième type, sans problème :

```html
<select>
    <option>Pomme</option>  
    <option>Banane</option>  
    <option>Cerise</option>  
    <option>Ronce</option>
</select>
```

Mais j'ai été choqué d'apprendre que le premier type n'existe pas en HTML. Oh, il y a une chose appelée `[datalist](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)`, mais elle ne fonctionne pas correctement — les utilisateurs ne peuvent pas cliquer sur quelque chose pour voir la liste entière, et dès que vous commencez à taper, les éléments commencent immédiatement à disparaître s'ils ne commencent pas par la même chaîne que celle tapée par l'utilisateur.

Mais CSS est un outil de style d'une puissance impressionnante : des [jeux vidéo](http://victordarras.fr/cssgame/) [entiers](https://codepen.io/elad2412/full/hBaqo/) ont été construits à partir de CSS, HTML et quelques fichiers image. (Super, je viens de perdre la moitié de mon audience.)

Cela ne signifie pas que CSS peut faire **n'importe quoi**, mais cela signifie qu'il existe au moins des "astuces" pour accomplir une grande variété de tours. Ceux d'entre vous qui ont fini de jouer à des jeux sont probablement intéressés à apprendre quelques trucs du métier, et je pense qu'il y a beaucoup à apprendre en découvrant comment faire une boîte combinée.

Dans cet article, vous apprendrez comment fonctionne cette chose :

![Image](https://cdn-media-1.freecodecamp.org/images/biYH9OqxjvdVcIPN3FqUvR-VDiNaQilF2jwx)

Sous Windows, nous les appelons "boîtes combinées", car elles combinent une partie supérieure (généralement un champ de texte) avec une partie popup (généralement une liste déroulante).

### Comment l'utiliser

La boîte combinée peut être construite à partir de divs et/ou de spans. Rappelez-vous simplement qu'un analyseur HTML a quelques règles de imbrication. Par exemple, il ne permet pas à `p` d'être un ancêtre de `div` ou `ul`, et `span` ne peut pas être un ancêtre de `p` ou `div`. (Ces règles ne s'appliquent pas au code JavaScript/React qui modifie le DOM)

CSS s'attendra à trois enfants : d'abord la partie supérieure (contenu à toujours afficher), puis `**<span class=**`"downarrow" **tabindex=**"-1"**></span>** pour la flèche vers le bas, et enfin le contenu à afficher à l'intérieur de la boîte déroulante :

```html
<div class="combobox">
  <div>Boîte combinée simple</div>
  <div tabindex="-1" class="downarrow"></div>
  <div>
    Contenu du popup déroulant ici
  </div>
</div>
```

Par défaut, le menu déroulant ne s'ouvre que lorsque la flèche vers le bas (▼) est cliquée. Pour faire en sorte que la boîte s'ouvre lorsque le contenu supérieur est cliqué, vous devez ajouter la classe `dropdown` à la `combobox`, et ajouter un attribut `tabindex="0"` au premier enfant :

```html
<div class="combobox dropdown">
  <div tabindex="0">Boîte combinée simple</div>
  <div tabindex="-1" class="downarrow"></div>
  <div>
    Contenu du popup déroulant ici
  </div>
</div>
```

**Note :** `tabindex="-1"` signifie "vous pouvez cliquer pour lui donner le focus, mais vous ne pouvez pas le focaliser en utilisant Tab sur le clavier". `tabindex="0"` signifie "vous pouvez le focaliser avec un clic ou avec la touche de tabulation, et le navigateur choisira l'ordre dans lequel différents éléments sont focalisés par la touche Tab." Contrairement à un élément `<select>`, la boîte popup ne pourra pas sortir de la fenêtre du navigateur (ceci peut être une limitation intentionnelle de tout le contenu défini par l'utilisateur — si le contenu défini par l'utilisateur pouvait s'étendre au-delà du bord de la zone de la page, il pourrait y avoir un risque de sécurité de sites web essayant de confondre ou de tromper les utilisateurs.)

En bonus, vous pourrez faire une liste déroulante qui n'est **pas** une boîte combinée avec la classe `dropdown` seule :

```html
<div class="dropdown">
   *** <span tabindex="0">Menu déroulant</span> *** 
   <div>
     Contenu du popup déroulant ici
   </div>
</div>
```

Ceci est destiné à être un menu déroulant cliquable (si vous voulez un menu déroulant qui s'ouvre au survol de la souris au lieu du clic de la souris, il existe déjà [de nombreux autres tutoriels](https://www.google.com/search?num=20&q=pure+css+hover+menu) à ce sujet.)

Dans ce cas, le dernier élément contient le contenu déroulant et tous les autres enfants sont toujours visibles, mais seuls les éléments avec un attribut `tabindex` peuvent être cliqués pour ouvrir la zone popup.

Vous pouvez éditer en toute sécurité la marge et la bordure d'une boîte combinée et de ses enfants sans perturber son comportement, sauf une chose : ne laissez pas `padding-right` devenir trop petit car la flèche vers le bas ▼ est affichée dans le padding — sa taille doit être d'au moins `1em`.

#### Résumé

* La classe `combobox` est pour une boîte combinée
* La classe `dropdown` est pour les menus et les boîtes combinées qui se déroulent lorsque le contenu supérieur est cliqué (rappellez-vous `tabindex="0"`)
* La classe `downarrow` ajoute l'icône de flèche vers le bas (`tabindex="-1"` est requis, car il ne peut pas être ajouté via CSS.)
* Le dernier enfant de `combobox` ou `dropdown` est le contenu déroulant.

Et vous pouvez [prévisualiser la démo avec le code source](https://codepen.io/qwertie/pen/QBYMdZ).

### Fonctionnalités CSS dont nous aurons besoin

Nous aurons besoin de **beaucoup** de choses pour cela. Voici une liste (n'hésitez pas à sauter et à lire plus tard.)

#### Sélecteurs

**Sélecteurs de base :**   
`.a` signifie "correspondre aux éléments avec `class='a'`".  
`A, B` signifie "correspondre au sélecteur `A` ou au sélecteur `B`".  
`A B` signifie "correspondre à un élément `B` qui a un élément `A` comme ancêtre".  
`A > B` signifie "correspondre à un élément B dont le parent est un élément A".

`**:first-child**` **pseudo-sélecteur :**  
`*:first-child` signifie "correspondre à n'importe quel élément tant qu'il est le premier enfant d'un élément parent".

**`:last-child` pseudo-sélecteur :**  
`*:last-child` signifie "correspondre à n'importe quel élément tant qu'il est le dernier enfant d'un autre élément". Par exemple, `.combobox > *:last-child` trouve le dernier enfant de n'importe quel élément avec `class="combobox"`.

`**:empty**` **pseudo-sélecteur :**  
`.downarrow:empty` signifie "correspondre à un élément avec `class="downarrow"` s'il n'a rien dedans (même pas du texte brut)".

`**:only-child**` **pseudo-sélecteur :**  
`*:only-child` signifie "correspondre à n'importe quel élément s'il est le seul enfant d'un autre élément".

`**:not**` **pseudo-sélecteur :**  
`.dropdown:not(.sticky)` signifie "correspondre à un élément avec la classe `dropdown` s'il n'a pas la classe `sticky`".

`**:focus**` **pseudo-sélecteur :**  
`.downarrow:focus` signifie "correspondre à un élément avec la classe `downarrow` s'il a le **focus** parce qu'il a un `tabindex` et qu'il a été cliqué avec la souris ou sélectionné avec Tab".

`**:hover**` **pseudo-sélecteur :**  
`.foo:hover` signifie "correspondre à un élément avec la classe `foo` lorsque le pointeur de la souris est dessus".

`A ~ B` signifie "correspondre à `B` si un frère précédent a correspondu à `A`".

#### Styles

**Styles de base :**  
Assurez-vous de comprendre le [modèle de boîte](https://www.w3schools.com/css/css_boxmodel.asp) et ses divers styles associés (y compris `width`, `height`, `min-width` et `max-height`) avant de continuer. Vous devriez également connaître d'autres styles de base comme `font-size`, `font-family`, `color`, et `background-color`.

Vous devriez également connaître les unités, surtout les [unités les plus courantes](https://css-tricks.com/the-lengths-of-css/) :  
 `px`, `em`, `rem`, et `%`.

`**box-sizing: border-box**` **style**  
Cela signifie que la largeur et la hauteur d'un élément [incluent le padding et la bordure](https://css-tricks.com/international-box-sizing-awareness-day/).

`**display:**` **style**  
Nous utiliserons `display: block`, qui affiche un élément comme un "bloc", qui est comme un paragraphe en ce sens que deux blocs adjacents ont des sauts de ligne entre eux.

Nous utiliserons également `display: inline-block`, qui affiche un élément **en ligne**, comme une image d'icône dans un paragraphe, mais permet toujours les marges, les bordures et le padding.

Nous n'utiliserons pas explicitement `display: inline`, qui est utilisé pour les éléments qui n'ont pas de marges, de bordures ou de padding et qui n'ont pas besoin de sauts de ligne entre eux (`<b>comme ceci</b>`).

[En savoir plus](https://css-tricks.com/almanac/properties/d/display/) sur display.

`**position:**` **style**  
Dans la boîte combinée, nous verrons comment ce style est utilisé pour sortir les éléments du flux normal du document.

Les éléments ont normalement un style de `position: static`, ce qui signifie simplement "positionner normalement sur la page".

`position: relative` est comme `static`, sauf deux choses : premièrement, l'élément peut être décalé à gauche, à droite, en haut ou en bas sans affecter aucun autre élément.  
Cependant, la boîte combinée n'a pas besoin de cette fonctionnalité. Le deuxième effet de `relative` est de marquer l'élément comme "positionné".

Cela compte car une autre position, `absolute`, positionne un élément par rapport à son ancêtre "positionné" le plus proche. Plus précisément, le popup déroulant utilisera `position: absolute` afin de se positionner par rapport à la partie supérieure de la boîte combinée — donc la boîte combinée elle-même est marquée `relative`.

De plus, un élément `absolute` n'affecte pas le positionnement des autres éléments sur la page, pas même son propre élément parent, et c'est exactement ce que nous voulons pour une boîte popup.

`**left**`**, `top`, `right` et `bottom` styles**  
Ces styles sont utilisés avec `position: relative` et `position: absolute`, et ils fonctionnent un peu différemment pour chacun. Plus sur cela plus tard.

[En savoir plus](https://www.w3schools.com/css/css_positioning.asp) sur le positionnement.

`**outline:**` **style**  
Outline est une bordure supplémentaire dessinée à l'extérieur de la bordure normale d'un élément. Elle est normalement utilisée pour mettre en évidence un élément, comme pour indiquer qu'il a été "sélectionné" par un utilisateur. Comme les contours sont censés être temporaires, ils n'occupent pas d'espace sur la page — donc ajouter un contour ne repoussera pas les autres éléments.

`**box-shadow:**` **style**  
Dessine une ombre "sous" l'élément (en fait, l'ombre est dessinée **à l'extérieur** de l'élément, ce qui semble très étrange si l'élément n'a pas d'arrière-plan). Cela sera pratique pour le popup déroulant !

`**z-index:**` **style**  
Ce style change l'ordre dans lequel un élément est dessiné par le navigateur. Un **z-index plus élevé** fait qu'un élément est dessiné **plus tard** de sorte qu'il apparaît au-dessus des autres choses sur la page.

Nous aurons besoin d'un grand z-index pour notre popup déroulant afin qu'il apparaisse au-dessus de tout le reste. Les enfants du popup obtiendront un nouveau "contexte d'empilement", ce qui signifie essentiellement qu'ils seront automatiquement dessinés au-dessus du popup, ce qui est bien.

[Attention](https://www.smashingmagazine.com/2009/09/the-z-index-css-property-a-comprehensive-look/) : `z-index` ne fonctionne que sur les éléments "positionnés".

`**cursor:**` **style**  
Contrôle l'apparence du curseur de la souris [apparence](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor).

`**text-align:**` **style**  
Justification horizontale du texte [justification du texte](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align) (`left`, `right` ou `center`).

`**pointer-events:**` **style**  
Le paramètre `none` de ce style rend un élément "invisible" aux [clics de souris](https://developer.mozilla.org/en-US/docs/Web/CSS/pointer-events).

`**transform:**` **style**  
Vous permet de faire pivoter, redimensionner, incliner ou translater un bloc (ou un élément en ligne). Ces [transformations](https://www.w3schools.com/cssref/css3_pr_transform.asp) sont intelligentes et affectent également l'entrée de la souris.

Par exemple, vous pourriez faire pivoter le texte de 30 degrés et toujours le sélectionner avec la souris.

`**transition:**` **style**  
Active l'[animation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions) lorsque les styles changent.

`opacity:` **style**  
Un nombre entre 0 et 1 contrôle la facilité avec laquelle un élément est visible :   
`1` est la valeur normale qui rend un élément entièrement visible  
`0` rend un élément complètement invisible. (Contrairement à `visibility: hidden` et `display: none`, les autres façons de rendre quelque chose invisible, `opacity: 0` n'empêche pas la souris d'interagir avec l'élément.)

Dans cet article, nous utiliserons l'opacité pour l'animation — en animant la transition entre `opacity: 0` et `opacity: 1`, nous pouvons faire apparaître ou disparaître un élément.

#### Pseudo-élément

`**::before**` ou `**::after**` :   
Fait référence à un élément virtuel **dans** un élément précédemment sélectionné, avant ou après son contenu normal.

Par exemple, si vous écrivez `p::before { content: "!" }` alors `!` apparaîtra au début de chaque paragraphe.

Nous pouvons utiliser `content` avec `::before` ou `::after` pour dessiner la flèche vers le bas (▼).

### Préparation de l'apparence initiale

`.combobox` et `.dropdown` doivent être `relative` afin que le popup déroulant puisse être positionné par rapport à eux. `display: inline-block` permet à la boîte combinée d'avoir des marges, un padding et une bordure. Contrairement à `display: block`, il permet à d'autres éléments d'apparaître sur la même ligne (comme des étiquettes ou d'autres boîtes combinées.)

```css
.combobox, .dropdown { 
  /* "relative" et "inline-block" (ou juste "block") sont nécessaires
     ici pour que "absolute" fonctionne correctement dans les enfants */
  position: relative;
  display: inline-block;
}
```

Les boîtes combinées, mais pas les listes déroulantes, auront une bordure intégrée :

```css
.combobox {
  border: 1px solid #999;
  padding-right: 1.25em; /* laisser de la place pour ▼ */
}
```

La couleur `#999` est légèrement plus foncée que la bordure de l'élément `<select>` de Chrome, et légèrement plus claire que celle de l'élément `<select>` de FireFox, donc elle ne semble pas trop différente de l'un ou de l'autre.

#### Comment dessiner la petite flèche vers le bas (▼) ?

La difficulté ici est de contrôler sa hauteur. La boîte combinée peut avoir un contenu de taille imprévisible : petite police, grande police, une ligne ou deux lignes. Le "bouton" de flèche doit avoir la même hauteur pour qu'il fonctionne peu importe où l'utilisateur clique dessus — n'importe où dans la bordure devrait fonctionner.

**Alors, comment pouvons-nous faire en sorte que la flèche s'adapte à la hauteur de son frère de gauche ?**   
[CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) peut accomplir cela directement, mais il n'est pas supporté par tous les navigateurs. Peut-être que [Flexbox](https://stackoverflow.com/questions/29503227/how-to-make-flexbox-items-the-same-size) pourrait faire le travail aussi, mais j'ai décidé d'utiliser une vieille astuce pour la compatibilité avec les anciens navigateurs : le positionnement absolu.

Avec le positionnement absolu, je peux forcer la flèche à avoir la même hauteur que son conteneur.

L'inconvénient de cette approche est que la flèche existera en dehors du flux normal du document, donc le navigateur ne réservera aucun espace pour elle. Au lieu de cela, nous donnerons à la boîte combinée un peu de padding sur le côté droit (`1.25em` ci-dessus), et la flèche vivra dans le padding.

En mode de positionnement absolu, `top` aligne le bord supérieur d'un élément par rapport au bord supérieur de son conteneur : `top: 0` signifie que les deux bords supérieurs seront au même endroit. De même, `left: 0` aligne le côté gauche de l'élément au côté gauche du conteneur, et ainsi de suite.

Les coordonnées positives poussent l'élément "vers l'intérieur" par rapport au conteneur, donc `top: 10px` signifie "placer le haut de l'élément 10px vers le bas à partir du haut du parent", tandis que `bottom: 10px` signifie "placer le bas de l'élément 10px vers le haut à partir du bas du parent."

Dans ce cas, nous avons besoin de `top: 0; bottom: 0; right: 0; width: 1.25em` pour mettre la flèche sur le côté droit, de haut en bas.

```css
.combobox > .downarrow, .dropdown > .downarrow {
  display: block;     /* Autoriser la marge/bordure/padding/taille */
  position: absolute; /* En dehors du flux normal */
  top: 0;    /* Aligner le haut de la flèche avec le bord supérieur de la boîte combinée */
  bottom: 0; /* Aligner le bas de la flèche avec le bas de la boîte combinée */
  right: 0; /* Aligner le bord droit de la flèche avec le bord droit de la boîte combinée */
  width: 1.25em;
  
  cursor: default; /* Utiliser le curseur de flèche au lieu du I-beam */
  nav-index: -1; /* définit tabindex, non fonctionnel dans la plupart des navigateurs */
  border-width: 0;        /* désactiver par défaut */
  border-color: inherit;  /* copier la bordure du parent */
  border-left: inherit;   /* copier la bordure du parent */
}
```

Ici, `display: block` et `display: inline-block` ont le même effet, donc j'ai utilisé le plus court. J'ai également désactivé le curseur de souris en forme de I-beam normalement affiché sur le texte (puisque la flèche vers le bas compte comme du texte).

Il existe en fait un moyen de définir `tabindex` en CSS, il s'appelle `nav-index`. Mais la plupart des navigateurs ne le supportent pas, donc si vous trouvez que votre boîte combinée ne fonctionne que dans Opera, vous savez pourquoi.

Vous devez donc ajouter `tabindex="-1"` à côté de `class="downarrow"`.

Ce code désactive les bordures, avec la mise en garde que la couleur/style de la bordure doit être héritée de l'élément parent (la boîte combinée) si d'autres CSS augmentent `border-left-width`. Vous pouvez utiliser l'option `inherit` sur n'importe quel attribut qui n'hérite pas du parent par défaut, d'ailleurs.

J'ai décidé qu'il devrait y avoir une bordure gauche si le popup ne s'ouvre pas lorsque le côté gauche est cliqué. Ainsi, la flèche déroulante ressemble à un bouton, suggérant subtilement qu'elle peut être cliquée. Rappelez-vous le plan : seul `dropdown`, et non `combobox` seul, s'ouvrira lorsque le côté gauche sera focalisé.

Par conséquent, j'ajouterai une bordure lorsque `combobox` seul est utilisé :

```css
.combobox:not(.dropdown) > .downarrow {
  border-left-width: 1px;
}
```

Ensuite, si l'utilisateur nous a fourni un `<span class="downarrow"></span>` vide, nous devons ajouter magiquement le caractère de flèche vers le bas manquant en utilisant `::before` (ou `::after`) et `content` :

```css
.downarrow:empty::before {
  content: '▼';
}
```

La flèche vers le bas doit également être centrée dans l'élément `.downarrow`. `text-align: center` centra le texte horizontalement, mais le centrage vertical est délicat. `vertical-align: middle` ne fonctionne pas, car il est conçu pour aligner les éléments **en ligne** **avec le texte environnant**. Ce que nous voulons, c'est aligner notre pseudo-élément de flèche vers le bas avec le conteneur parent `.downarrow`.

Il y a une astuce :

```css
.downarrow::before, .downarrow > *:only-child {
  text-align: center; /* Centrer horizontalement */
  /* astuce de centrage vertical */
  position: relative; /* Permettre à l'élément d'être décalé */
  top: 50%;           /* Descendre de 50% de la taille du conteneur */
  transform: translateY(-50%); /* Monter de 50% de la taille de l'élément */
  display: block;     /* `transform` nécessite block/inline-block */
}
```

Rappelez-vous que nous ajoutons le contenu `::before` uniquement si le `.downarrow` est vide. Si l'utilisateur a fourni sa propre flèche personnalisée, nous voulons toujours la centrer, d'où le sélecteur `.downarrow > *:only-child`.

Et si la boîte combinée contient un élément `<input>`, elle ne doit pas avoir de bordure :

```css
.combobox > input {
  border: 0 /* la boîte combinée a déjà une bordure */
}
```

Cette prochaine partie est facultative, mais généralement le premier enfant d'une boîte combinée doit avoir une largeur de 100% de son parent `.combobox` afin que si la boîte combinée est plus large que son premier enfant, le premier enfant s'étire pour correspondre. Et au cas où l'utilisateur aurait construit la boîte combinée à partir de spans plutôt que de divs (peut-être pour qu'elle puisse être placée dans un `<p>`), il peut être judicieux de définir le premier enfant comme `inline-block` afin qu'il puisse avoir un padding et des marges.

```css
.combobox > *:first-child {
  width: 100%;
  box-sizing: border-box; /* donc 100% inclut la bordure et le padding */
  display: inline-block;
}
```

### Préparation de la liste déroulante

Initialement, nous voulons simplement qu'elle soit cachée, donc nous pouvons utiliser `display: none`.

Mais en préparation pour quand elle sera visible, définissons également quelques autres propriétés. Commencez par `position: absolute` pour qu'elle soit en dehors du flux normal du document (rappellez-vous qu'un élément `absolute` est positionné par rapport à son ancêtre `relative` le plus proche, qui est `.combobox` ou `.dropdown`). Lorsqu'il est affiché, il doit avoir une bordure et un arrière-plan, bien sûr, et aussi une ombre en dessous.

Ici vous voyez `box-shadow: 1px 2px 4px 1px #4448`, ce qui signifie "montrer une ombre 1px à droite de l'élément, 2px vers le bas, floutée de 4px, et faire l'ombre 1px plus grande que l'élément lui-même, avec une couleur de #4448". Nous avons également besoin d'un grand z-index pour que le popup apparaisse au-dessus de tout le reste :

```css
.dropdown > *:last-child,
.combobox > *:last-child {
  display: none;          /* caché par défaut */
  position: absolute;     /* en dehors du flux du document */
  left: 0;          /* Côté gauche du popup = côté gauche du parent */
  top: 100%;        /* Haut du popup = 100% en dessous du haut du parent */
  border: 1px solid #999; /* bordure grise */
  background-color: #fff; /* fond blanc */
  box-shadow: 1px 2px 4px 1px #4448; /* ombre derrière */
  z-index: 9999;          /* dessiner au-dessus de tout le reste */
  min-width: 100%;        /* >= 100% aussi large que son conteneur */
  box-sizing: border-box; /* largeur inclut la bordure et le padding */
}
```

Ici j'ai utilisé `left: 0` et `top: 100%` pour positionner correctement le popup, mais dans ce cas, il s'avère que la position **par défaut** du popup est pratiquement la même, donc ces styles ne sont pas vraiment nécessaires.

Pour rendre la boîte déroulante visible, tout ce dont nous avons vraiment besoin est `display: block`.

**Mais quels sélecteurs devons-nous utiliser pour que cela se produise ?**

```css
??? {
  display: block;
}
```

Le plus évident, la liste déroulante doit être affichée dans ces trois cas.

1. L'utilisateur a cliqué sur `.downarrow`
2. L'utilisateur a cliqué ou tabulé sur `.dropdown`
3. L'utilisateur a cliqué ou tabulé sur un enfant de `.dropdown`

La boîte déroulante est le dernier enfant, donc nous devrons combiner le sélecteur `*:last-child` avec `:focus` pour détecter quand l'une des choses ci-dessus a été cliquée ou tabulée :

```css
.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus              > *:last-child,
.dropdown > *:focus          ~ *:last-child {
  display: block;
}
```

Nous n'avons pas encore terminé, cependant. Que se passe-t-il si l'utilisateur clique sur une zone de texte ou un lien à l'intérieur de la boîte déroulante ? Le clic fera perdre le focus à `.downarrow` ou `.dropdown`, ce qui fera disparaître instantanément la boîte déroulante.

Dans le cas d'un lien, le navigateur focalise le lien lorsque le bouton de la souris est enfoncé, mais il ne suit pas le lien jusqu'à ce que le bouton de la souris soit relâché. Donc si la boîte déroulante disparaît instantanément, aucun lien dans la boîte déroulante ne peut être suivi !

Pour corriger cela, nous devons garder la boîte ouverte chaque fois que quelque chose à l'intérieur de `:last-child` a le focus :

```css
.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > *:last-child:focus-within,
.dropdown > *:last-child:focus-within {
  display: block;
}
```

**Attention :** Cela ne fonctionne pas dans Edge/IE (une solution de contournement est décrite ci-dessous).

Si la flèche vers le bas est cliquée une deuxième fois, nous devons masquer la boîte déroulante. Cela peut être accompli comme suit :

```css
.downarrow:focus {
  pointer-events: none; /* Fait que le deuxième clic ferme */
}
```

Cela rend le `.downarrow` invisible aux événements de la souris lorsqu'il a le focus, de sorte que lorsque vous cliquez dessus, vous cliquez en réalité sur ce qui se trouve derrière (le `.combobox`). Cela lui fait perdre le focus, ce qui à son tour fait disparaître la boîte déroulante.

Nous pouvons faire la même chose pour `.dropdown`, de sorte que cliquer à nouveau sur la zone supérieure d'un `.dropdown` le fasse disparaître :

```css
.dropdown > *:not(:last-child):focus,
.downarrow:focus,
.dropdown:focus {
  pointer-events: none; /* Fait que le deuxième clic ferme */
}
```

Cela fonctionne principalement. Mais si votre zone supérieure contient une zone de texte, il y a un effet secondaire puisque la zone de texte ne traitera pas normalement l'entrée de la souris. Cependant, j'ai constaté que la zone de texte reste utilisable.

Dans Firefox, vous pouvez cliquer et glisser pour sélectionner du texte si vous commencez lorsque le popup est fermé, mais cela ne fonctionne pas lorsque le popup est ouvert. Dans Edge, c'est l'inverse : vous pouvez cliquer et glisser pour sélectionner du texte uniquement lorsque le popup est ouvert. Dans les deux cas, c'est **basiquement** utilisable puisque l'utilisateur est susceptible de réessayer une fois si son entrée ne fonctionne pas la première fois.

Le comportement de Chrome est... incohérent. Dans tous les cas, pour obtenir un comportement parfait — où un clic ferme la boîte sans faire perdre le focus à la zone de texte — je pense que JavaScript est nécessaire.

### Dernières touches

La boîte combinée devrait normalement avoir une marge. Mais cela semble facultatif, puisque les contrôles `<input>` n'en ont pas par défaut :

```css
.combobox {
  margin: 5px;
}
```

Rendons cette chose plus cool en ouvrant la boîte avec une animation.

La propriété `transition` est le moyen le plus simple de faire des animations. En fait, pour nos besoins, une simple commande comme `transition: 0.4s;` active les animations pour tous les styles supportés. Mais jusqu'à présent, le seul style que nous changeons est `display`, et les changements de `display` ne peuvent pas être animés.

Alors essayons d'animer une transition de `opacity: 0` à `opacity: 1` en modifiant nos styles existants...

```css
.dropdown > *:last-child,
.combobox > *:last-child {
  display: none;
  /* 
     ... autres styles identiques à avant ...
  */
  opacity: 0;
  transition: 0.4s;
}

.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > *:last-child:focus-within,
.dropdown > *:last-child:focus-within {
  display: block;
  opacity: 1;
  transition: 0.15s;
}
```

Le temps de la transition contrôle combien de temps il faut pour **entrer** dans l'état actuel. Donc ce code devrait signifier "prendre 0.15 secondes pour **afficher** et 0.4 secondes pour **masquer**".

Mais **l'animation ne fonctionne pas**. Il [s'avère](https://stackoverflow.com/questions/39304002/css-transition-disabled-by-displaynone) que `display: hidden` bloque les animations. Au lieu de cela, nous devons utiliser l'une des **autres** façons de cacher les choses. Une autre façon de cacher les choses est avec `visibility: hidden`. Malheureusement, cela bloque partiellement les animations, aussi — l'animation pour afficher le popup fonctionne, mais l'animation pour masquer le popup ne fonctionne pas.

Nous ne pouvons pas compter sur `opacity: 0` **seul** pour masquer un élément, car la souris peut toujours interagir avec un élément qui a `opacity: 0`. Cependant, nous pouvons corriger cela avec `pointer-events: none`.

Ainsi, le fondu d'entrée et de sortie fonctionnel ressemble à ceci :

```css
.dropdown > *:last-child,
.combobox > *:last-child {
  display: block;
  /* 
     ... autres styles identiques à avant ...
  */
  transition: 0.4s;
  opacity: 0;
  pointer-events: none;
}

.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > *:last-child:focus-within,
.dropdown > *:last-child:focus-within {
  display: block;
  transition: 0.15s;
  opacity: 1;
  pointer-events: auto;
}
```

Un autre effet que nous pourrions ajouter est de déplacer le popup en position, comme en animant `top` :

```css
.dropdown > *:last-child,
.combobox > *:last-child {
  display: block;
  /* 
     ... autres styles identiques à avant ...
  */
  top: 0;
  opacity: 0;
  transition: 0.4s;
  pointer-events: none;
}

.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > *:last-child:focus-within,
.dropdown > *:last-child:focus-within {
  display: block;
  top: 100%;
  opacity: 1;
  transition: 0.15s;
  pointer-events: auto;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/mf6Fg50wbA1iptPpoqMItU5cEm2Uo0LwzErg)

J'ai décidé que c'était un peu "trop" et ne l'ai pas inclus dans la [version finale](https://codepen.io/qwertie/pen/QBYMdZ).

Enfin, nous devrions avoir un rectangle de focus — une bordure montrant lorsque la boîte combinée est "active".

Tout d'abord, ajoutons un rectangle de focus pour cette flèche vers le bas :

```css
.downarrow:focus {
  outline: 2px solid #48F8;
}
```

Idéalement, nous aurions un rectangle de focus pour la boîte combinée elle-même, comme ceci :

```css
.combobox:focus-within {
  outline: 2px solid #48F;
}
```

Cela fonctionne bien dans Chrome. Mais dans Firefox 61, le `outline` est étendu au-delà de la bordure pour englober toute la boîte popup également, ce qui semble un peu étrange, surtout si la boîte popup n'a pas la même largeur que la partie supérieure. Dans Edge, le contour n'apparaît pas du tout car Edge ne supporte pas `:focus-within` (voir ci-dessous). Alors, que pouvons-nous faire à la place ?

J'ai décidé d'utiliser ceci :

```css
.combobox > *:not(:last-child):focus {
  outline: 2px solid #48F8;
}
```

Cela dessine un contour autour de l'enfant focalisé au lieu de la boîte combinée elle-même. Mais cela semble parfois étrange aussi, si l'enfant n'a pas la même taille que la boîte combinée englobante. J'ai donc ajouté de la transparence (`#48F8` au lieu de `#48F`) pour la rendre moins visible, et donc moins étrange dans le pire des cas.

#### Collant

Les styles que nous avons jusqu'à présent gardent la boîte ouverte uniquement lorsque quelque chose est focalisé. Donc si vous cliquez sur du texte brut dans la zone popup, le popup se ferme. Pour la version finale, j'ai élargi la liste des raisons de garder le popup ouvert pour inclure un style `sticky` qui gardera le menu déroulant ouvert au survol de la souris, de sorte que le clic ne ferme pas la boîte.

```css
.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > *:last-child:focus-within,
.dropdown > *:last-child:focus-within,
.combobox > .sticky:last-child:hover,
.dropdown > .sticky:last-child:hover {
  display: block;
  top: 100%;
  opacity: 1;
  transition: 0.15s;
  pointer-events: auto;
}
```

Comme je l'ai discuté précédemment, des bugs se produisent lorsque la zone supérieure d'une boîte combinée contient une zone de texte. Pour vous permettre d'éviter facilement ce problème, j'ai ajusté le CSS existant afin que le style `pointer-events: none` **ne** soit **pas** appliqué si l'élément `.dropdown` a également la classe `sticky` :

```css
.dropdown:not(.sticky) > *:not(:last-child):focus,
.downarrow:focus,
.dropdown:focus {
  pointer-events: none; /* Fait que le deuxième clic ferme */
}
```

Enfin, si une liste `.dropdown` contient des liens, il y a un petit inconvénient. Après avoir cliqué sur un lien, la liste ne se fermera pas automatiquement puisque le lien a le focus et nous avons programmé le menu déroulant pour ne pas se fermer lorsqu'un enfant a le focus.

Pour éviter cela, j'ai ajouté la prise en charge d'une nouvelle classe `less-sticky`. Comme `sticky`, `less-sticky` garde le popup ouvert lorsque la souris le survole. Contrairement à `sticky`, `less-sticky` ne garde pas le popup ouvert lorsqu'un enfant a le focus.

Ainsi, notre nouvelle liste de sélecteurs devient assez longue :

```css
.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > .sticky:last-child:hover,
.dropdown > .sticky:last-child:hover,
.combobox > .less-sticky:last-child:hover,
.dropdown > .less-sticky:last-child:hover,
.combobox > *:last-child:focus-within:not(.less-sticky),
.dropdown > *:last-child:focus-within:not(.less-sticky) {
  display: block;
  opacity: 1;
  transition: 0.15s;
  pointer-events: auto;
  top: 100%;
}
```

Et nous n'avons même pas encore terminé, car cela n'est pas encore compatible avec Edge et Internet Explorer.

### Cas particuliers

Une fois que j'ai réussi à faire fonctionner ma boîte combinée parfaitement dans Firefox et Chrome, j'ai été consterné de la voir complètement laide et inutilisable dans Edge. Qu'est-ce qui a mal tourné ?

Tout d'abord, les bordures avaient disparu car Edge et IE ne supportent pas l'opacité des bordures, comme dans `rgb(200,150,100,50)` ou `#8888`. J'avais utilisé `#8888` comme bordure. Pour la faire fonctionner sur Edge, je l'ai changée en `#999`.

Une autre alternative est d'offrir une bordure non opaque juste pour Edge :

```css
border: 1px solid #888;  /* Edge/IE ne peut pas faire l'opacité de la bordure */
border: 1px solid #8888; /* Tous les autres navigateurs */
```

Deuxièmement, cliquez comme je pourrais — les divs déroulantes ne se déroulaient tout simplement pas !

En résolvant ce problème, j'ai appris quelque chose de nouveau — si un navigateur ne comprend pas un sélecteur utilisé dans une déclaration CSS, il **ignorera le bloc entier**.

Par exemple, si vous écrivez `.x, .y, .z:unknown { margin:1em }`, alors `x` et `y` n'auront pas de marges simplement parce que le navigateur ne comprend pas `unknown`.

Il s'est avéré qu'Edge ne comprend pas `:focus-within`, qui est ce qui permet à la zone déroulante de rester ouverte lorsqu'un élément `input` profondément dans la zone déroulante est cliqué. Le problème était que j'avais mélangé des sélecteurs supportés et non supportés ensemble.

Pour faire fonctionner Edge, j'ai dû répéter tout le bloc de styles "comment ouvrir la liste déroulante" séparément pour les sélecteurs qui utilisent `:focus-within`, afin que ces sélecteurs n'empêchent pas les autres sélecteurs de fonctionner.

Ensuite, comme solution de contournement pour le manque de `:focus-within`, j'ai décidé d'essayer de [détecter Edge](https://stackoverflow.com/questions/43528940/how-to-detect-ie-and-edge-browsers-in-css) et de garder automatiquement toute liste `.dropdown` ouverte lorsque la souris la survole dans ce cas. Ainsi, il est toujours possible d'utiliser un élément focalisé (comme un `a href` ou un `input`) à l'intérieur de la zone déroulante, bien qu'il disparaisse tôt si la souris s'en éloigne.

Le code pour tout cela est le suivant :

```css
/* Liste des situations dans lesquelles afficher la liste déroulante. */
.combobox > .downarrow:focus ~ *:last-child,
.dropdown:focus > *:last-child,
.dropdown > *:focus ~ *:last-child,
.combobox > .sticky:last-child:hover,
.dropdown > .sticky:last-child:hover,
.combobox > .less-sticky:last-child:hover,
.dropdown > .less-sticky:last-child:hover,
.combobox > *:last-child:focus:not(.less-sticky),
.dropdown > *:last-child:focus:not(.less-sticky) {
  display: block;
  opacity: 1;
  transition: 0.15s;
  pointer-events: auto;
}

/* focus-within n'est pas supporté par Edge/IE. Les sélecteurs non supportés 
   font que le bloc entier est ignoré, donc nous devons répéter tous 
   les styles pour focus-within séparément. */
.combobox > *:last-child:focus-within:not(.less-sticky),
.dropdown > *:last-child:focus-within:not(.less-sticky) {
  display: block;
  opacity: 1;
  transition: 0.15s;
  pointer-events: auto;
}

/* détecter Edge/IE et se comporter comme si less-sticky était activé pour tous
   les dropdowns (sinon les liens ne seront pas cliquables) */
@supports (-ms-ime-align:auto) {
  .dropdown > *:last-child:hover {
    display: block;
    opacity: 1;
    pointer-events: auto;
  }
}

/* détecter IE et faire la même chose. */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .dropdown > *:last-child:hover {
    display: block;
    opacity: 1;
    pointer-events: auto;
  }
}
```

Troisièmement, le style `outline` ne fonctionnait pas dans Edge. Une fois de plus, le problème était qu'Edge ne supporte pas les contours non opaques.

La solution est un style opaque spécial pour Edge :

```css
outline: 2px solid #8AF; /* Edge/IE ne peut pas faire la transparence du contour */  
outline: 2px solid #48F8;
```

Quatrièmement, j'avais placé deux boîtes combinées dans un élément `<label>`, et essayer d'ouvrir la deuxième ouvrait toujours la première à la place. Il s'avère que dans Edge, si vous utilisez une souris, vous ne pouvez sélectionner que le premier élément d'entrée dans un label.

Cinquièmement, les boîtes déroulantes n'avaient pas d'ombres. Une fois de plus, c'était parce que j'avais utilisé une ombre non opaque, et une fois de plus Edge avait besoin de son propre CSS spécial :

```css
box-shadow: 1px 2px 4px 1px #666; /* Edge ne peut pas faire l'opacité de l'ombre */
box-shadow: 1px 2px 4px 1px #4448;
```

Internet Explorer 11 a presque exactement les mêmes limitations, donc la correction d'Edge a principalement corrigé IE, sauf qu'une technique de détection de navigateur différente était nécessaire pour IE que pour Edge.

### Synchronisation du popup avec la zone supérieure

Malheureusement, CSS ne peut pas faire cela pour nous. Donc dans la démo finale, JavaScript est utilisé pour mettre à jour la partie supérieure de la boîte combinée lorsque la partie popup change. Par exemple, j'ai utilisé ce code basé sur jQuery pour mettre à jour la partie supérieure du sélecteur de couleur :

```js
function parentComboBox(el) {
  for (el = el.parentNode; el && 
    Array.prototype.indexOf.call(el.classList, "combobox") <= -1;)
    el = el.parentNode;
  return el;
}
$(".combobox .color").mousedown(function() {
  var c = this.style.backgroundColor;
  $(parentComboBox(this)).find(".color")[0].
    style.backgroundColor = c;
});
```

### Version finale

[Cliquez ici](https://codepen.io/qwertie/pen/QBYMdZ) pour voir la démo avec le code source sur CodePen.