---
title: Comment utiliser la position CSS pour mettre en page un site web (avec exemple
  de code)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-07T19:22:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-position-to-layout-a-website-with-example-code-38592bb9e276
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9cRn62IAywuaywMSJ2X6_g.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
- name: Website design
  slug: website-design
seo_title: Comment utiliser la position CSS pour mettre en page un site web (avec
  exemple de code)
seo_desc: 'By Jessica Chan

  Using CSS position to layout elements on your website can be hard to figure out.
  What’s the difference between absolute, relative, fixed, and sticky? It can get
  confusing pretty quickly.

  To help, this tutorial will guide you through a...'
---

Par Jessica Chan

Utiliser la position CSS pour disposer les éléments sur votre site web peut être difficile à comprendre. Quelle est la différence entre absolute, relative, fixed et sticky ? Cela peut devenir confus assez rapidement.

Pour vous aider, ce tutoriel vous guidera à travers toutes les propriétés de position CSS. Et vous pourrez obtenir des mises en page de site web pixel perfect !

%[https://www.youtube.com/watch?v=hkjjCnRFDug]

### Que fait la position CSS ?

En utilisant CSS, vous pouvez disposer visuellement tous vos éléments sur votre page web. Par exemple, vous pouvez positionner un élément tout en haut de votre page, ou 50px en dessous de l'élément précédent.

Pour contrôler précisément comment un élément apparaîtra dans la mise en page, vous devez utiliser la propriété CSS `position`. De plus, vous pouvez utiliser d'autres propriétés liées à la position : `top`, `right`, `bottom`, `left` et `z-index`. (Nous approfondirons cela plus tard.)

La propriété `position` peut prendre cinq valeurs différentes : `static`, `relative`, `absolute`, `fixed` et `sticky`.

Cela semble beaucoup, mais ne vous inquiétez pas !

Voici comment chaque valeur de la position CSS fonctionne :

### 1. Static

`Position: static` est la valeur par défaut qu'un élément aura. Cela signifie que si vous ne déclarez pas `position` pour un élément en CSS, il sera automatiquement défini sur `static`.

> _Il est important de noter que avoir une position statique est la même chose que de ne pas définir la propriété `position` du tout. (Cela entrera en jeu un peu plus tard avec le positionnement absolu.)_

Les éléments positionnés de manière statique apparaîtront sur la page dans ce que nous appelons le flux normal. Par exemple, si vous avez plusieurs éléments `<div>` les uns après les autres, ils apparaîtront sur la page directement les uns en dessous des autres.

Voici une rapide démonstration pour illustrer la position statique. Nous utilisons le balisage HTML suivant :

```
<div class="parent purple"></div>
```

```
<div class="another green"></div>
```

Et voici le CSS que nous utilisons :

```css
.first { 
   // Aucune position définie, donc c'est statique 
} 
.another { 
   // Aucune position définie, donc c'est statique 
   top: 50px; 
}
```

Le deuxième élément a une propriété `top` définie sur `50px`. Vous penseriez que cela le déplacerait vers le bas de 50px, n'est-ce pas ?

Cependant, voici à quoi cela ressemblera sur une page web :

![Image](https://cdn-media-1.freecodecamp.org/images/nE-u6IOvcuqDCbvpCGOUUyNNpIrzrC94gu8I)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/XQKLdR" rel="noopener" target="_blank" title=")_

Puisque les deux éléments ont une position statique, aucune des propriétés CSS de mise en page n'aura d'effet. Cela rend la propriété `top` sans effet sur la façon dont le deuxième élément est affiché.

Ainsi, le deuxième élément se retrouve directement sous le premier élément, sans espace entre eux.

Comment pouvons-nous corriger cela ? Passons à la position suivante :

### 2. Relative

`Position: relative` est similaire à `static` en ce sens que les éléments positionnés de manière relative suivront le flux normal de la page web. Mais la principale différence est que l'utilisation de `relative` déverrouillera les autres propriétés de mise en page CSS.

Pensez-y de cette manière : vous définissez l'élément pour qu'il soit positionné par rapport aux autres éléments de la page.

Voyons à quoi cela ressemble, et ajustons notre CSS comme ceci :

```
.first { 
   position: static; 
} 
.another { 
   position: relative; 
   top: 50px; 
}
```

Tout le CSS est exactement le même, sauf que nous avons changé le deuxième élément pour utiliser `position: relative`. Cela rend le `top: 50px` fonctionnel !

![Image](https://cdn-media-1.freecodecamp.org/images/WW2W75wz3QauqDbhgwlDpH80GcRbr1W63XX0)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/bJePJe" rel="noopener" target="_blank" title=")_

Vous pouvez voir que le deuxième élément est maintenant 50px en dessous du premier, ajoutant cet espace entre eux.

### Éléments parent et enfant positionnés de manière relative

Essayons un autre exemple, en utilisant un élément parent avec un élément enfant imbriqué à l'intérieur. Les deux ont `position: relative` défini.

Voici le HTML pour cela :

```html
<div class="parent purple"> 
   <div class="child magenta"></div> 
</div>
```

Et nos styles CSS :

```css
.parent { 
   position: relative; 
} 
.child { 
   position: relative; 
   top: 0px; 
   left: 0px; 
}
```

Et voici à quoi ce code ressemblera en réalité :

![Image](https://cdn-media-1.freecodecamp.org/images/j4ia5pGejB3E0xyKGWOMMSxo6wYNyT3Lqbot)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/oOLKBK" rel="noopener" target="_blank" title=")_

Vous pouvez voir que l'élément enfant rose est bien imbriqué à l'intérieur de l'élément parent violet. L'enfant est également positionné aussi près que possible du haut et de la gauche à l'intérieur du parent. (Il ira aussi haut que le texte du parent)

La position relative est relativement simple, n'est-ce pas ? Eh bien, accrochez-vous, car les choses vont devenir folles avec `position absolute`.

### 3. Absolute

`Position: absolute` fera qu'un élément soit sorti de ce flux normal de la page web.

Attendez, que signifie cela ?

Auparavant, en utilisant le positionnement statique ou relatif, les éléments étaient bien affichés les uns en dessous des autres, selon leur ordre dans le balisage HTML. Mais avec le positionnement absolu, l'élément est complètement sorti de ce flux entier.

Pour aider à expliquer, faisons une comparaison pour illustrer la différence entre le positionnement relatif et absolu.

Dans l'exemple précédent, nous avions un élément parent avec un élément enfant, tous deux positionnés de manière relative. Et l'enfant était imbriqué à l'intérieur de l'élément parent.

Changeons cet enfant pour qu'il soit positionné de manière absolue dans le parent !

Notre CSS ressemblera maintenant à ceci :

```
.parent { 
   position: relative; 
} 
.child { 
   position: absolute; 
   top: 0px; 
   left: 0px;
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/fVmPUWI3fHrC2dhTDK8v-Wny4cZhCh-aUDRc)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/RORXWN" rel="noopener" target="_blank" title=")_

L'élément enfant rose semble maintenant très différent de notre dernier exemple.

Bien qu'il soit toujours dans les limites de l'élément parent, il est positionné tout en haut et tout à gauche du parent. Il couvre même le contenu textuel du parent !

Cela est dû aux styles `top: 0px` et `left: 0px` de l'enfant, combinés avec le fait que l'enfant est positionné de manière absolue. Dans le flux normal des choses, les éléments ne seraient pas au-dessus (et ne couvriraient pas) d'autres éléments.

Mais puisque l'enfant est absolu, il est essentiellement sur une couche différente de celle des éléments normaux. Il peut donc être positionné au-dessus de ce qui se trouve sur la page web.

Mais il restera dans les limites de l'élément parent - tant que le parent a sa position définie. Ce qui nous amène à notre prochain point.

Il y a un autre aspect délicat des éléments enfants avec positionnement absolu...

### Un élément positionné de manière absolue doit se positionner par rapport à un ancêtre positionné.

Lorsque vous sortez un élément du flux normal en utilisant `position: absolute`, il recherchera un élément ancêtre qui a sa propre position définie. Cela permet à l'enfant de savoir par rapport à quel élément il doit se positionner.

Alors, que se passe-t-il si un élément enfant est positionné de manière absolue, mais que l'élément parent n'a pas de position définie ?

Voici notre CSS pour cette illustration :

```css
.parent { 
   // Aucune position définie, donc c'est statique 
} 
.child { 
   position: absolute; 
   top: 0px; 
   left: 0px; 
}
```

Et voici à quoi ressemblerait la page web résultante :

![Image](https://cdn-media-1.freecodecamp.org/images/USE0MNOMfgjm5aUE3mxezET6AqB2v-bDZtV9)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/EJgxYm" rel="noopener" target="_blank" title=")_

L'enfant a maintenant échappé aux limites de l'élément parent, puisque le parent n'a pas de position définie. Et l'enfant est remonté jusqu'à l'élément (grand)parent suivant, dans ce cas l'élément `<body>`, ce qui est aussi loin qu'il peut aller.

(Une métaphore quelque peu triste serait que cet enfant "orphelin" cherche dans l'arbre généalogique quelqu'un qui sera son "parent".)

**C'est une cause majeure de comportement inattendu en CSS pour de nombreux développeurs.**

Si vous pouvez vous souvenir de toujours définir l'élément parent d'un élément enfant pour qu'il ait `position` défini sur `relative` ou `absolute` (dans la plupart des cas), vous éviterez que vos éléments enfants ne remontent la page vers qui sait où ?

Donc, pour résumer le positionnement relatif et absolu :

> _La principale différence entre le positionnement relatif et absolu est que `position: absolute` sortira complètement un élément enfant du flux normal du document. Et cet enfant sera positionné par rapport au premier élément parent qui a sa propre position définie._

Les deux dernières valeurs de `position`, `fixed` et `sticky`, sont similaires à certains égards à `position: absolute`. Mais elles sont également liées à votre position de défilement sur la page.

Examinons cela :

### 4. Fixed

`Position: fixed` sortira l'élément du flux normal et le positionnera également au même endroit dans le viewport (ce qui est visible à l'écran). Cela signifie que le défilement n'affectera pas du tout sa position.

Voyons à quoi cela ressemble dans le code. Voici notre HTML :

```html
<div class="first purple"> 
   Lorem ipsum dolor sit amet, consectetur adipiscing elit....
</div> 
<div class="another green"></div>
```

Et dans notre CSS, nous avons défini le deuxième élément pour qu'il soit `position: fixed` :

```
.first { 
   position: relative; 
} 
.another { 
   position: fixed; 
   top: 0px; 
   left: 0px; 
}
```

Et voici à quoi cela ressemblera :

![Image](https://cdn-media-1.freecodecamp.org/images/0Aixaa9pedgy2gBfA-UDyPzY9XbIG6U1962O)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/rbMNVj" rel="noopener" target="_blank" title=")_

L'élément fixe vert restera positionné dans le coin supérieur gauche du viewport. Et si vous faites défiler, l'élément violet défilera normalement vers le haut, mais l'élément vert restera collé à l'endroit où nous l'avons positionné.

> **_Astuce_**_: Un élément fixe doit avoir une position `top` ou `bottom` définie. Si ce n'est pas le cas, il n'existera tout simplement pas sur la page._

`Position: fixed` est couramment utilisé pour créer des barres de navigation toujours fixées en haut. C'est une propriété super utile !

Ensuite, nous examinerons le positionnement sticky, qui est similaire au positionnement fixe mais avec un petit extra.

### 5. Sticky

Les éléments `Position: sticky` se comporteront initialement comme des éléments `position: relative`, mais si vous continuez à faire défiler, ils seront sortis du flux normal et se comporteront comme des éléments `position: fixed` là où vous les avez positionnés.

Cela peut être vraiment utile si vous souhaitez coller un élément qui est initialement plus bas sur la page en haut de l'écran.

Dans cet exemple de code, nous avons notre élément sticky vert entre deux éléments violets contenant beaucoup de texte. (Tant mieux pour le défilement !)

```html
<div class="first purple"> 
   Lorem ipsum dolor sit amet, consectetur adipiscing elit.... 
</div> 
<div class="another green"></div> 
<div class="purple"> 
   Lorem ipsum dolor sit amet, consectetur adipiscing elit.... 
</div>
```

Et le CSS pour notre élément sticky :

```
.first { 
   position: relative; 
} 
.another { 
   position: sticky; 
   top: 0px; 
}
```

Et voici à quoi cela ressemble sur la page web !

![Image](https://cdn-media-1.freecodecamp.org/images/sXZdc3S5-X8saH18qUoFelbM7dHHa9SBiYzX)
_Voir le code original sur [Codepen](https://codepen.io/thecodercoder/pen/oOzBYd" rel="noopener" target="_blank" title=")_

Lorsque vous faites défiler la page vers le bas, lorsque vous voyez l'élément vert entrer dans le viewport, il semble être un élément normal, positionné de manière relative. Mais lorsque vous continuez à faire défiler, au lieu de sortir de la page, il deviendra fixe et restera collé en haut du viewport.

Tout comme les éléments fixes, un élément sticky doit avoir `top` ou `bottom` défini dans le CSS. S'il ne l'a pas, l'élément continuera à se comporter comme s'il était positionné de manière relative, et ne deviendra jamais sticky.

> **_Une note sur la compatibilité des navigateurs:_**

> _Actuellement, `position: sticky` n'a pas un support complet sur tous les navigateurs. Les versions plus récentes des navigateurs le supportent, mais aucune version d'IE ne le fait. Cela peut être important si vous travaillez sur un projet client où le support d'IE 11 est nécessaire. Vous pouvez consulter le support actuel sur [CanIUse.com](https://caniuse.com/#feat=css-sticky)_

### En conclusion

J'espère que vous avez trouvé ce tutoriel et ces exemples de code sur le positionnement CSS utiles ! Si vous avez des questions ou des commentaires, n'hésitez pas à laisser un commentaire ci-dessous ?

_Autres ressources :_

* [Mozilla Developer Network : CSS Position](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
* [CSS Tricks : position](https://css-tricks.com/almanac/properties/p/position/)

#### **Vous voulez plus ?**

<p>Je crée un cours sur le design responsive ! <a href="https://coder-coder.com/responsive-design-beginners/">Inscrivez-vous ici</a> pour recevoir un email lorsque ce sera publié.</p>

<p>J'écris des tutoriels sur le développement web sur mon blog <a href="https://coder-coder.com" rel="noopener">coder-coder.com</a>, je poste des mini-conseils sur <a href="https://www.instagram.com/thecodercoder/" rel="noopener">Instagram</a> et des tutoriels de codage sur <a href="https://www.youtube.com/c/codercodertv">YouTube</a>.</p>