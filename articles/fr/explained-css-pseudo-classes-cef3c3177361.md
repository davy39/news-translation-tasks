---
title: Comment fonctionnent les pseudo-classes CSS, expliqué avec du code et de nombreux
  diagrammes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-06T06:24:33.000Z'
originalURL: https://freecodecamp.org/news/explained-css-pseudo-classes-cef3c3177361
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FypLaInuQOolvpO95NtBIQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment fonctionnent les pseudo-classes CSS, expliqué avec du code et de
  nombreux diagrammes
seo_desc: 'By Nash Vail

  Let’s be honest — there are times when CSS can really hurt your brain. It’s hard
  enough to center an element inside its parents.

  Today, we’re going to make sense of an even more challenging aspect of CSS: pseudo-classes.


  Obligatory Fami...'
---

Par Nash Vail

Soyons honnêtes — il arrive que CSS puisse vraiment vous donner mal à la tête. Il est déjà assez difficile de centrer un élément à l'intérieur de ses parents.

Aujourd'hui, nous allons nous attaquer à un aspect encore plus complexe de CSS : les pseudo-classes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZPlE0Td0GCO2mt3Ivrmp5g.gif)
_Gif obligatoire de Family Guy sur CSS_

Les pseudo-classes que je vais aborder ici se déclinent en deux types.

* Les sélecteurs *-of-type
* Les sélecteurs *-child

Vous pourriez vous dire : « Mais je suis ici pour apprendre les pseudo-classes. Pourquoi parlons-nous de sélecteurs ? » Eh bien, ce sont pratiquement la même chose, et j'utiliserai ces termes de manière interchangeable.

Les pseudo-classes sont parfois difficiles à comprendre, principalement parce qu'elles sont présentées de manière abstraite. Je vais donc adopter une approche différente ici et vous aider à les comprendre en dessinant un arbre DOM.

#### Le balisage et l'arbre

Commençons par examiner ce bloc de HTML. J'utiliserai ce code dans tous mes exemples.

```
<body>  <div class="main">     <a href="#">Lien Interne 1</a>     <a href="#">Lien Interne 2</a>     <ul>       <a href="#">Lien Interne Interne 1</a>       <li>         <a href="#">Élément de Liste 1</a>       </li>       <li>         <a href="#">Élément de Liste 2</a>       </li>     </ul>     <a href="#">Lien Interne 3</a>  </div>  <a href="#">Lien Externe 1</a>  <a href="#">Lien Externe 2</a></body>
```

Je vais maintenant convertir ce code en quelque chose de plus visuel et plus intuitif : un arbre.

L'élément body suivant a 3 enfants, _.main_ et deux éléments _anchor_.

```
<body>  <div class="main">   ...  </div>  <a href="#">Lien Externe 1</a>  <a href="#">Lien Externe 2</a></body>
```

Voici à quoi ressemble la relation entre _body_ et ses trois enfants lorsqu'elle est représentée sous forme d'arbre :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0J4m0pNfNUUe-JE9dPIbHw.png)
_Fig. 1_

Une chose à garder à l'esprit est que l'ordre dans lequel les enfants sont placés dans l'arbre est important. Les enfants placés de haut en bas dans le code sont placés de gauche à droite dans l'arbre.

Ensuite, examinons la div _.main_ :

```
<div class="main">   <a href="#">Lien Interne 1</a>   <a href="#">Lien Interne 2</a>   <ul>     ...   </ul>   <a href="#">Lien Interne 3</a></div>
```

.main a 4 enfants. Les deux premiers sont des éléments _anchor_, puis une _ul_ et enfin un autre élément anchor.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b1bt8tsEPJ7L1jJNkSB1WQ.png)
_Fig. 2_

De la même manière, nous descendons chaque niveau de nesting et dessinons l'arbre complet à partir du code HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xn3NJH7ajQ0t-nSQWkr2HA.png)
_Fig. 3 — Représentation arborescente du code HTML_

Pour que cet article vous soit utile, il est important que vous compreniez cet arbre.

« Ha ha, belle blague ! » « Merci ! » Incrémentez le compteur de blagues à 1, et passons à notre toute première pseudo-classe.

### Pseudo-classe #1 :only-of-type

Toutes les pseudo-classes suivent le même format :

```
ce-que-vous-voulez-selectionner:filtre { /* styles */ }
```

_ce-que-vous-voulez-selectionner_ peut être utilisé pour sélectionner tout ce qui existe sous forme de collection dans le DOM. Ici, permettez-moi de vous montrer un exemple :

```
a:only-of-type {   border: 2px solid black;}
```

Dans l'extrait de code montré ci-dessus, _ce-que-vous-voulez-selectionner_ sont les éléments anchor (la balise _a_), et le _filtre_ est _only-of-type_. Nous verrons dans un instant ce que fait ce sélecteur.

Tout d'abord, j'ai préparé un [codepen](http://codepen.io/nashvail/pen/VKkXLB) si vous êtes trop paresseux pour créer un projet de test. Je vous en prie, ami !

Vous pouvez suivre, voir les changements, vous perdre, puis revenir à cet article pour l'explication. Vous faites votre part, je fais la mienne.

Voici ma part, expliquant le code montré ci-dessus. Nous commencerons par sélectionner tout ce qu'il y a, puis nous filtrerons progressivement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uBjIeeXnjBgkB2GApFiiGQ.png)
_Fig. 4 — sélection de tout_

Remarquez comment la sélection a été faite ? Chaque section dans l'arbre (numérotée de 1 à 5) a des éléments avec un parent commun. Le parent de la Section 1 est _body_, le parent de la Section 2 est ._main_, et ainsi de suite. **Encore une fois, remarquez que chaque section correspond à un niveau plus profond dans le nesting du code**.

Ensuite, puisque les éléments anchor sont _ce-que-vous-voulez-selectionner_, nous allons faire exactement cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bxFbXy1QDeGf-84KSJNxDg.png)
_Fig. 5 — sélection des seuls éléments anchor_

Nous avons sélectionné tous les éléments anchor dans chacune des sections et les avons numérotés consécutivement de gauche à droite. Et comme je l'ai mentionné, l'ordre — de gauche à droite — est important.

C'est là que la partie _ce-que-vous-voulez-selectionner_ se termine et que le filtrage commence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WwCVWx4UKJ5bdPUV1e4vXQ.png)
_Fig. 6 — Sélection des éléments anchor de type unique._

_only-of-type_ parcourt chaque section et ne sélectionne que les éléments anchor qui sont les seuls éléments anchor dans leur section respective. Remarquez comment les sections 3, 4 et 5 sont les seules sections avec des éléments anchor ? Comme le montre la figure 6, ce sont ceux qui sont sélectionnés et déclarés lorsqu'un style est appliqué.

### Pseudo-classe #2 :first-of-type

Passons rapidement à la partie où nous finissons de sélectionner tous les « _ce-que-vous-voulez-selectionner_ » (éléments anchor dans notre cas).

![Image](https://cdn-media-1.freecodecamp.org/images/1*bxFbXy1QDeGf-84KSJNxDg.png)
_Fig. 7 — Sélection des seuls éléments anchor._

Le filtre _first-of-type_ se traduit par la sélection dans chacune des sections de la première occurrence de l'élément anchor.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PJExtAelKm7-Xdt31Dw6cA.png)
_Fig. 8 — Sélection des éléments anchor de premier type._

Voici à quoi ressemble le code qui accomplit cela :

```
a:first-of-type {   border: 2px solid black;}
```

Au cas où vous auriez oublié le travail acharné que j'ai fait pour vous en configurant le CodePen, voici à nouveau le [lien](http://codepen.io/nashvail/pen/VKkXLB) pour voir ce que le code produit dans un navigateur.

### Pseudo-classe #3 :last-of-type

Si vous ne pouvez pas le deviner par le nom, _last-of-type_ est l'exact opposé de _first-of-type_. Ce qui signifie donc que dans chaque section de l'arbre, au lieu de sélectionner la première occurrence, sélectionnez les dernières.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dWlzrEMXkZueTDY52sGLzg.png)
_Fig. 9 — sélections :last-of-type_

« Et les sections avec un seul élément anchor ? », pas très content que vous ayez posé cette question. C'est assez simple de voir que si une section n'a qu'un seul élément anchor, il passe évidemment le filtre _only-of-type_, mais pas seulement. Puisqu'il n'y a pas d'éléments anchor précédant ou suivant cette balise particulière, il passe également les filtres _first-of-type_ et _last-of-type_ (par exemple, les balises _a_ des sections 4 et 5).

### Pseudo-classe #4 :nth-of-type(nombre/an + b/pair/impair)

Et maintenant, nous arrivons enfin à la partie juteuse de l'article, il y a du CSS simple avec quelques garnitures de mathématiques de cinquième année, j'espère que vous apprécierez le savourer.

Commençons par déclarer le style suivant.

```
a:nth-of-type(1) {   border: 2px solid black;}
```

Cela semble un peu cryptique mais est en réalité assez simple. Pour lire le sélecteur, prenez simplement le nombre entre parenthèses et remplacez _nth_ dans le nom du sélecteur par la forme **ordinale** de ce nombre. C'est un autre mot anglais fantaisiste pour vous, pour être honnête...

D'accord, en revenant, _a:nth-of-type(1)_ peut donc se lire comme _a:first-of-type_ et sans surprise, il fonctionne exactement comme _a:first-of-type_ et aboutit à la sélection des éléments comme montré ci-dessous ; simplement les éléments anchor qui sont les premiers de leur type dans leur section respective.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PJExtAelKm7-Xdt31Dw6cA.png)
_Fig. 10 — Les gens lisent-ils même ces légendes ?_

C'est bien et joli, mais essayons quelque chose de différent ici.

```
a:nth-of-type(0) {   border: 2px solid black;}
```

Si vous avez deviné correctement, ce que je suis sûr que vous n'avez pas fait, aucun élément anchor n'est sélectionné dans ce cas. Comme la numérotation des types (et des enfants comme nous le verrons) dans chaque section commence à 1 et non à 0, il n'y a pas d'éléments anchor « 0 » dans aucune des sections et donc _a:zeroth-of-type_ ne sélectionne rien. Et il en sera de même pour _a:nth-of-type(5)_ ou _a:nth-of-type(6/7/8)_ car il n'y a pas de _a:fifth-of-type_ ou _a:sixth/seventh/eighth-of-type_ dans aucune des sections.

Mais si nous allions de l'avant et utilisions...

```
a:nth-of-type(2) {   border: 2px solid black;}
```

... il est assez clair que les sections 1 et 2 ont un élément anchor de _second-of-type_ et donc ce sont ceux qui sont sélectionnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o7aTc-EJF53N7bAHs2Ssxg.png)
_Fig. 11 — :nth-of-type(2) ou lu comme :second-of-type_

De même, juste pour renforcer le point ici, si nous allions de l'avant et déclarions le style suivant,

```
a:nth-of-type(3) {   border: 2px solid black;}
```

il sélectionnera les troisièmes éléments anchor dans la deuxième section car la section 2 est la seule section avec un élément anchor de :_third-of-type_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ob0gZ_tJhflq73RCzbyFkw.png)
_Fig. 12 — :nth-of-type(3) ou lu comme :third-of-type_

Assez simple, n'est-ce pas ? Mais les nombres ne sont pas la seule chose que vous pouvez passer dans _:nth-of-type(...)_, ce type est plus puissant que cela, vous pouvez également passer des formules de la forme _(a*n) + b_ (ou pour plus de brièveté _an + b_). Où _a_ et _b_ sont des constantes et _n_ est une valeur >= 0. Comment avez-vous aimé la garniture mathématique, monsieur ? Ne vous inquiétez pas, tout cela aura du sens dans une seconde.

Considérons le style suivant

```
a:nth-of-type(n) {  border: 2px solid black; }
```

La formule qui est passée dans le sélecteur ci-dessus est _(1 * n) + 0 [= n]_, _a_ est 1, b est 0 et _n_ est bien, n. Ce qui se passe ensuite, c'est que, à partir de 0, la valeur numérique de _n_ est incrémentée et insérée dans la formule et la sélection est faite. Par conséquent, _a:nth-of-type(n)_ se traduit essentiellement par

```
a:nth-of-type(0) {  border: 2px solid black; } // n = 0a:nth-of-type(1) {  border: 2px solid black; } // n = 1a:nth-of-type(2) {  border: 2px solid black; } // n = 2a:nth-of-type(3) {  border: 2px solid black; } // n = 3a:nth-of-type(4) {  border: 2px solid black; } // n = 4
```

```
...
```

Par conséquent, cela aboutit à la sélection de tous les éléments anchor.

Considérons un autre exemple

```
a:nth-of-type(2n + 1) {  border: 2px solid black; }
```

En commençant par 0 et en insérant incrémentiellement les valeurs de _n_ dans la formule, cela génère les sélecteurs suivants.

```
// n = 0 implique (2 * 0) + 1 = 1a:nth-of-type(1) { border: 2px solid black; }
```

```
// n = 1 implique (2 * 1) + 1 = 3a:nth-of-type(3) { border: 2px solid black; }
```

```
// n = 2 implique (2 * 2) + 1 = 5 - Aucune sélection puisque aucun fifth-of-type n'est présent dans aucune des sectionsa:nth-of-type(5) { border: 2px solid black; }...
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*QrQj3hZlegF3D-kv7yB0gA.png)
_Fig 13 — sélections nth-of-type(2n+1)_

Outre les nombres et les formules qui génèrent des nombres, vous pouvez passer soit des chaînes _even_ soit _odd_. _even_ sélectionne toutes les occurrences paires d'un élément d'un type particulier dans une section, c'est-à-dire _:second-of-type_, _:fourth-of-type_, _:sixth-of-type_, etc., et d'autre part, évidemment, _:nth-of-type(odd)_ sélectionne toutes les occurrences impaires, c'est-à-dire _:first-of-type_, _:third-of-type_, _:fifth-of-type_, etc.

### Pseudo-classe #5 :nth-last-of-type(nombre/an + b/pair/impair)

Ce sélecteur fonctionne exactement comme le précédent, mais avec une petite différence. Voyez par vous-même...

```
a:nth-last-of-type(1) {  border: 2px solid black; }
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*8iEbmV82IuBJ7jyYiyx_AA.png)
_Fig. 14 — nth-last-of-type(1)_

Remarquez comment dans chaque niveau, la numérotation des types d'ancre est faite de droite à gauche au lieu de gauche à droite. C'est la seule différence. _last-of-type_ accepte les nombres et les formules et even/odd tout comme _nth-of-type_ sauf que lors de la sélection, le dernier type est traité comme le premier, l'avant-dernier comme le deuxième, l'avant-avant-dernier comme le troisième et ainsi de suite...

Avec cela, nous arrivons à la fin des sélecteurs *_-of-type_. J'espère que ce fut un voyage amusant pour vous, nous avons commencé avec _only-of-type_, puis nous sommes passés à _first-of-type_, _last-of-type_ et nous avons plongé profondément dans _nth-of-type(...)_ et _nth-last-of-type(...)_. Si à un moment donné vous avez perdu pied et êtes tombé, je vous encourage à jouer avec ce stylo et à relire l'explication.

D'accord, il est temps de passer à la suivante dans ce coin moins visité du parc à thème CSS. Une autre catégorie de pseudo-sélecteurs/classes que nous allons explorer sont les classes *_-child_. Avec une compréhension claire de la manière dont les sélecteurs *_-of-type_ fonctionnent, saisir le concept derrière les sélecteurs *_-child_ devrait être un jeu d'enfant pour vous. « Jeu d'enfant ? Qu'est-ce que c'est ? Est-ce une unité de mesure ? » Non, mon ami, cela signifie une tâche extrêmement facile. Bon, commençons avec notre tout premier sélecteur _*-child_, :_only-child_.

### Pseudo-classe enfant #1 :only-child

Considérons le style suivant.

```
a:only-child {   border: 2px solid black;}
```

C'est la définition même de l'auto-explicatif et du direct. Le sélecteur dit de sélectionner tous les éléments anchor, à condition que l'élément anchor soit l'unique enfant de son parent, ou, en d'autres termes, de sélectionner tous les éléments anchor dont le parent n'a qu'un seul enfant et que cet enfant unique est un élément anchor.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bNZeHcGUOqswsJDMQFszzw.png)
_Fig. 15 — sélections a:only-child_

J'avais un ami qui n'était jamais le préféré de sa mère, et il était enfant unique. Je voulais juste glisser cela ici, en tout cas, remarquez que contrairement aux sélecteurs *_-of-type_, nous ne numérotons plus les types, mais les enfants, en commençant bien sûr par 1 (et non par 0). Comparé à _only-of-type_, l'élément anchor dans la section 3 n'est pas sélectionné car son parent (_ul_) a 3 enfants, donc même s'il (l'élément anchor de niveau 3) est un _only child of type 'a'_ de son parent, ce n'est pas l'unique enfant, il y a aussi 2 _li_.

### Pseudo-classe enfant #2 :first-child

Considérons la déclaration de style suivante.

```
a:first-child {   border: 2px solid black;}
```

Cela signifie simplement : sélectionnez tous les éléments anchor, mais avec une condition à l'esprit, l'élément anchor doit être le premier enfant de son parent. C'est tout, aucune explication supplémentaire n'est nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qLx7ELzLcCUWHY9xakrsfg.png)
_Fig. 16 — sélections a:first-child_

Si vous êtes un peu confus quant à la raison pour laquelle le _a_ de la section 1 n'a pas été sélectionné, c'est parce que le premier enfant de la section 1 (dont le parent est _body_) est _.main_, le premier _a_ de la section 1 est le deuxième enfant et n'a pas pu passer le filtre _first-child_, c'est la raison exacte pour laquelle le pauvre gars a fini par ne pas être sélectionné et s'est fait envoyer balader avec un gros hashtag. Continuons avec le suivant.

### Pseudo-classe enfant #3 :last-child

C'est la partie où les sélecteurs devraient commencer à devenir auto-explicatifs et où vous devriez commencer à penser que je suis stupide d'essayer de vous les expliquer. [Mais mon nom n'est pas blurryface et je me fiche de ce que vous pensez](http://genius.com/6273352). « Belle référence à twenty one pilots » oui je sais, merci. Maintenant, regardez la déclaration de style suivante.

```
a:last-child {   border: 2px solid black;}
```

_ce-que-vous-voulez-selectionner_ ? « Éléments anchor. » Et le _filtre_ que vous voulez utiliser ? _last-child._ Cela se traduit simplement par sélectionner ces éléments anchor qui sont le dernier enfant de leur parent. Ou, en d'autres termes, sélectionner les éléments anchor dont le parent a finalement décidé que ce n'était plus amusant et a arrêté après que ce gars soit né. Ci-dessous, voici à quoi ressemble l'arbre avec les sélections _:last-child_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PfU4UZ2kZvgWZlG-Pav05w.png)
_Fig. 16 — sélections :last-child._

### Pseudo-classe enfant #4 :nth-child(nombre/an+b/pair/impair)

J'espère que vous avez pu digérer la garniture mathématique que vous avez reçue la dernière fois, car cela va se reproduire, mais cette fois sur une croûte légèrement différente.

Maintenant, je voudrais que vous portiez toute votre attention et que vous la pointiez comme un laser sur l'exemple suivant.

```
a:nth-child(1) {  border: 2px solid black; }
```

C'est exactement la même chose que _:nth-of-type_, j'aurais pu lier cette section de l'article ici, mais les politiques de Medium ne le permettent pas, si vous voulez une piqûre de rappel, vous devrez faire défiler jusqu'à cette section. En laissant de côté les politiques de Medium qui pourraient changer à l'avenir, ce qui n'a pas changé, c'est le processus de décryptage des sélecteurs _nth_.

Tout comme avec _:nth-of-type_, dans le nom du sélecteur, prenez le nombre entre parenthèses et remplacez « _nth_ » par la forme ordinale de ce nombre. Par conséquent, le sélecteur montré dans l'exemple est équivalent à _a:first-child_ et fonctionne exactement de la même manière ; c'est-à-dire qu'il sélectionne tous les éléments anchor, à condition qu'ils soient le premier enfant de leur parent.

Cela devrait clouer la similitude entre les deux sélecteurs _nth_ (_nth-of-type_ et _nth-child_), mais nous allons quand même continuer et examiner un autre exemple.

```
a:nth-child(2n - 1) {  border: 2px solid black; }
```

Nous commençons par insérer incrémentiellement les valeurs de _n_ en commençant par 0 dans la formule, ce qui nous fait réaliser que le sélecteur montré ci-dessus est essentiellement équivalent à ceux montrés ci-dessous.

```
// n = 0 implique (2 * 0) - 1 = 0 - 1 = -1a:nth-child(-1) { border: 2px solid black; }  | Aucune sélection
```

```
// n = 1 implique (2 * 1) - 1 = 2 - 1 = 1a:nth-child(1) { border: 2px solid black; }
```

```
// n = 2 implique (2 * 2) - 1 = 4 - 1 = 3a:nth-child(3) { border: 2px solid black; }
```

```
// n = 3 implique (2 * 3) - 1 = 6 - 1 = 5a:nth-child(5) { border: 2px solid black; } | Aucune sélection supplémentaire...
```

Comme c'est le cas, si le sélecteur reçoit des nombres hors limites (comme -1, 5, 6... dans le cas ci-dessus), il les ignore simplement. Voici à quoi ressemble l'arbre avec _a:nth-child(2n-1)_ appliqué.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aXGTeApzv5e1c7CJdk-pvg.png)
_Fig. 17 — sélections :nth-child(2n-1)._

Les gens de CSS Tricks ont un article très informatif appelé [Recettes utiles :nth-child](https://css-tricks.com/useful-nth-child-recipies/) que vous devriez consulter et mettre vos connaissances de :_nth-child_ à l'épreuve. Je vous lance un défi, mon ami.

Avec cela, nous passerons au dernier sélecteur de cet article qui, de manière ironique, est _:nth-last-child_. Putain ! pourquoi « ironiquement » est-il même un mot ?

### Pseudo-classe enfant #5 :nth-last-child(nombre/an + b/pair/impair)

Ce sélecteur fonctionne exactement comme _:nth-child_ sauf qu'il commence à sélectionner les éléments à partir de la direction opposée, tout comme ce professeur de lycée énervant qui posait des questions à la classe en commençant par les gens paisibles assis aux dernières tables. Dieu que je le détestais. Si vous regardez les arbres dessinés jusqu'à présent, les enfants sont numérotés de gauche à droite dans chaque section, mais ce sélecteur voit l'arbre comme ceci

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ChjMydCcmDb9TgFrY4htg.png)
_Fig. 18_

Les enfants dans chaque section sont numérotés de droite à gauche. Donc si nous allons de l'avant et appliquons le style suivant

```
a:nth-last-child(1) {  border: 2px solid black; }
```

les éléments anchor seront sélectionnés comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XBmBun1e7jY0aaHsBlZHlg.png)

Assez simple, n'est-ce pas ? Ce sélecteur accepte également très confortablement les formules (de la forme an + b) et les chaînes _even/odd_, les sélections, cependant, sont faites à partir de l'extrémité opposée.

D'accord, c'est là que notre voyage ensemble se termine. Vous pouvez payer votre ticket en tweettant cet article à vos amis développeurs.

J'espère que vous avez apprécié la lecture de cet article et que vous avez appris quelque chose de nouveau, y compris quelques nouveaux mots anglais brillants.

C'est Nash qui signe. Je vous verrai dans le prochain article. Suivez-moi sur [Twitter](http://twitter.com/NashVail) pour rester en contact. Je tweete beaucoup sur des trucs liés au développement.

#### Vous cherchez plus ? Je publie régulièrement sur mon [blog à l'adresse nashvail.me](https://nashvail.me). À bientôt, passez une bonne journée !

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZ2patu496gPkJOYXhb9MA.png)