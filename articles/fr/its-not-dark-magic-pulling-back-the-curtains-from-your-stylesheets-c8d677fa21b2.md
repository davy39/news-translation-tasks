---
title: CSS n'est pas de la magie noire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-09T22:44:24.000Z'
originalURL: https://freecodecamp.org/news/its-not-dark-magic-pulling-back-the-curtains-from-your-stylesheets-c8d677fa21b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TqpR80LFFl09NnOpISdXJg.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: CSS n'est pas de la magie noire
seo_desc: 'By aimeemarieknight

  Pulling Back The Curtains on Your Stylesheets


  If you’re a web developer, chances are you’re going to have to write some CSS from
  time to time.

  When you first looked at CSS, it probably seemed like a breeze. You added some borders...'
---

Par aimeemarieknight

#### Lever le voile sur vos feuilles de style

![Image](https://cdn-media-1.freecodecamp.org/images/HTLeseY5v-uus9eTzCqV9gMAvHIGKPM3JQCi)

Si vous êtes un développeur web, il est probable que vous devrez écrire du CSS de temps en temps.

Lorsque vous avez regardé CSS pour la première fois, cela semblait probablement simple. Vous avez ajouté des bordures ici, changé des couleurs là. JavaScript est la partie difficile du développement front-end, n'est-ce pas ?

À un moment donné, au cours de votre progression en tant que développeur web, cela a changé ! Ce qui est pire, c'est que de nombreux développeurs de la communauté front-end ont fini par considérer CSS comme un langage jouet.

La vérité, cependant, est que lorsque nous rencontrons un obstacle, beaucoup d'entre nous ne comprennent pas vraiment ce que notre CSS fait sous le capot.

Pendant les deux premières années après mon bootcamp, j'ai fait du JavaScript full stack et j'ai ajouté un peu de CSS ici et là. En tant que panéliste sur [JavaScript Jabber](https://devchat.tv/js-jabber/my-js-story-aimee-knight), j'ai toujours eu l'impression que JavaScript était mon pain et mon beurre, alors c'est ce sur quoi j'ai passé le plus de temps.

L'année dernière, cependant, j'ai décidé de me concentrer sur le front-end et j'ai réalisé que je n'étais tout simplement pas capable de déboguer mes feuilles de style de la même manière que je le faisais avec mon JavaScript !

Nous aimons tous faire des blagues à ce sujet, mais combien d'entre nous ont réellement pris le temps d'essayer de comprendre le CSS que nous écrivons ou lisons. Combien d'entre nous ont réellement débogué un problème de manière raisonnable jusqu'à la couche d'abstraction la plus basse suivante lorsque nous rencontrons un obstacle ? Au lieu de cela, nous nous contentons de la première réponse de StackOverflow, de hacks, ou nous laissons simplement le problème de côté.

Trop souvent, les développeurs sont complètement perplexes lorsque le navigateur rend le CSS de manière inattendue. Ce n'est pas de la magie noire cependant, et en tant que développeurs, nous savons que les ordinateurs ne font que parser nos instructions.

La connaissance des internes peut également être utile pour le débogage avancé et l'optimisation des performances. Alors que de nombreuses conférences discutent de la manière de corriger les bugs courants, ma conférence (et cet article) se concentreront sur le pourquoi en plongeant profondément dans les internes du navigateur pour voir comment nos styles sont parsés et rendus.

### Le DOM et le CSSOM

Tout d'abord, il est important de comprendre que les navigateurs contiennent un moteur JavaScript et un moteur de rendu. Nous nous concentrerons sur ce dernier. Par exemple, nous discuterons des détails qui concernent WebKit (Safari), Blink (Chrome), Gecko (Firefox) et Trident/EdgeHTML (IE/Edge). Le navigateur subira un processus qui inclut la conversion, la tokenisation, l'analyse lexicale et le parsing, qui construit finalement le DOM et le CSSOM.

À un niveau élevé, vous pouvez les considérer comme suit :

* **Conversion** : Lecture des octets bruts de HTML et de CSS depuis le disque ou le réseau.
* **Tokenisation** : Découpage de l'entrée en morceaux (ex : balises de début, balises de fin, noms d'attributs, valeurs d'attributs), suppression des caractères non pertinents tels que les espaces blancs et les sauts de ligne.
* **Analyse lexicale** : Comme le tokeniseur, mais il identifie également le type de chaque token (ce token est un nombre, ce token est une chaîne littérale, ce autre token est un opérateur d'égalité).
* **Parsing** : Prend le flux de tokens du lexer, interprète les tokens en utilisant une grammaire spécifique et le transforme en un arbre de syntaxe abstraite.

Une fois que les deux structures d'arbre sont créées, le moteur de rendu attache ensuite les structures de données dans ce qu'on appelle un arbre de rendu dans le cadre du processus de mise en page.

L'arbre de rendu est une représentation visuelle du document qui permet de peindre le contenu de la page dans le bon ordre. La construction de l'arbre de rendu suit l'ordre suivant :

* En commençant à la racine de l'arbre DOM, parcourez chaque nœud visible.
* Omettez les nœuds non visibles.
* Pour chaque nœud visible, trouvez les règles CSSOM correspondantes appropriées et appliquez-les.
* Émettez des nœuds visibles avec du contenu et leurs styles calculés.
* Enfin, générez un arbre de rendu qui contient à la fois les informations de contenu et de style de tout le contenu visible à l'écran.

Le CSSOM peut avoir des effets drastiques sur l'arbre de rendu mais aucun sur l'arbre DOM.

### Rendu

Suite à la mise en page et à la construction de l'arbre de rendu, le navigateur peut enfin procéder à la peinture réelle de l'écran et à la composition. Prenons un bref moment pour distinguer quelques termes ici.

* **Mise en page** : Inclut le calcul de l'espace qu'un élément occupera et de sa position à l'écran. Les éléments parents peuvent affecter les éléments enfants et parfois vice versa.
* **Peinture** : Le processus de conversion de chaque nœud dans l'arbre de rendu en pixels réels à l'écran. Il implique de dessiner du texte, des couleurs, des images, des bordures et des ombres. Le dessin est généralement fait sur plusieurs couches et plusieurs tours de peinture peuvent être causés par le chargement de JavaScript qui modifie le DOM.
* **Composition** : L'action d'aplatir toutes les couches en l'image finale visible à l'écran. Puisque des parties de la page peuvent être dessinées sur plusieurs couches, elles doivent être dessinées à l'écran dans le bon ordre.

Le temps de peinture varie en fonction de la construction de l'arbre de rendu et plus la largeur et la hauteur de l'élément sont grandes, plus le temps de peinture sera long.

L'ajout de différents effets peut également augmenter le temps de peinture. La peinture suit l'ordre dans lequel les éléments sont empilés dans leurs contextes d'empilement (de l'arrière vers l'avant), ce que nous aborderons lorsque nous parlerons de z-index plus tard. Si vous êtes un apprenant visuel, il y a une excellente démonstration de [peinture](https://www.youtube.com/watch?v=ZTnIxIA5KGw).

Lorsque les gens parlent d'accélération matérielle dans les navigateurs, ils font presque toujours référence à la composition accélérée, ce qui signifie simplement utiliser le GPU pour composer le contenu d'une page web.

La composition permet des augmentations de vitesse assez importantes par rapport à l'ancienne méthode qui utilisait le CPU de l'ordinateur. La propriété will-change est une propriété que vous pouvez ajouter pour tirer parti de cela.

Par exemple, lors de l'utilisation de transformations CSS, la propriété will-change permet de suggérer au navigateur qu'un élément DOM sera transformé dans un proche avenir. Cela permet de déléguer certaines opérations de dessin et de composition au GPU, ce qui peut grandement améliorer les performances des pages avec beaucoup d'animations. Elle offre des gains similaires pour la position de défilement, le contenu, l'opacité et le positionnement en haut ou à gauche.

Il est important de comprendre que certaines propriétés provoqueront une nouvelle mise en page, tandis que d'autres propriétés ne provoqueront qu'un nouveau rendu. Bien sûr, en termes de performance, il est préférable de ne déclencher qu'un nouveau rendu.

Par exemple, les changements de couleur d'un élément ne provoqueront qu'un nouveau rendu de cet élément, tandis que les changements de position de l'élément provoqueront une nouvelle mise en page et un nouveau rendu de cet élément, de ses enfants et éventuellement de ses frères et sœurs. L'ajout d'un nœud DOM provoquera une nouvelle mise en page et un nouveau rendu du nœud. Les changements majeurs, comme l'augmentation de la taille de la police d'un élément html, provoqueront une nouvelle mise en page et un nouveau rendu de l'arbre entier.

Si vous êtes comme moi, vous êtes probablement plus familier avec le DOM qu'avec le CSSOM, alors plongeons un peu dans cela. Il est important de noter que par défaut, CSS est traité comme une ressource bloquant le rendu. Cela signifie que le navigateur suspendra le rendu de tout autre processus jusqu'à ce que le CSSOM soit construit.

Le CSSOM n'est également pas en correspondance 1 à 1 avec le DOM. Display none, les balises script, les balises meta, l'élément head, etc. sont omis car ils ne sont pas reflétés dans le rendu.

Une autre différence entre le CSSOM et le DOM est que l'analyse CSS utilise une grammaire sans contexte. En d'autres termes, le moteur de rendu n'a pas de code qui remplira la syntaxe manquante pour CSS comme il le fera lors de l'analyse HTML pour créer le DOM.

Lors de l'analyse HTML, le navigateur doit prendre en compte les caractères environnants et il a besoin de plus que la spécification puisque le balisage pourrait contenir des informations manquantes mais devra toujours être rendu quoi qu'il arrive.

Cela dit, faisons un récapitulatif.

* Le navigateur envoie une requête HTTP pour la page
* Le serveur web envoie une réponse
* Le navigateur convertit les données de réponse (octets) en tokens, via la tokenisation
* Le navigateur transforme les tokens en nœuds
* Le navigateur transforme les nœuds en arbre DOM
* Attend la construction de l'arbre CSSOM

### Spécificité

Maintenant que nous avons une meilleure compréhension de la manière dont le navigateur fonctionne sous le capot, examinons certaines des zones de confusion les plus courantes pour les développeurs. Tout d'abord, la spécificité.

À un niveau très basique, nous savons que la spécificité signifie simplement appliquer les règles dans le bon ordre de cascade. Il existe de nombreuses façons de cibler une balise spécifique en utilisant des sélecteurs CSS, et le navigateur a besoin d'un moyen de négocier quels styles appliquer à une balise spécifique. Les navigateurs prennent cette décision en calculant d'abord la valeur de spécificité de chaque sélecteur.

Malheureusement, le calcul de spécificité a déconcerté de nombreux développeurs JavaScript, alors plongeons plus profondément dans la manière dont ce calcul est fait. Nous utiliserons un exemple de div avec une classe "container". À l'intérieur de cette div, nous aurons une autre div avec un id "main". À l'intérieur de celle-ci, nous aurons une balise p qui contient une balise d'ancrage. Sans regarder plus loin, savez-vous de quelle couleur sera la balise d'ancrage ?

```
#main a {   color: green;}
```

```
p a {   color: yellow;}
```

```
.container #main a {  color: pink;}
```

```
div #main p a {   color: orange;}
```

```
a {   color: red;}
```

La réponse est rose, avec une valeur de 1,1,1. Voici les autres résultats :

* `div #main p a: 1,0,3`
* `#main a: 1,0,1`
* `p a: 2`
* `a: 1`

Pour déterminer le nombre, vous devez calculer ce qui suit :

* **Premier nombre** : Le nombre de sélecteurs d'ID.
* **Deuxième nombre** : Le nombre de sélecteurs de classe, de sélecteurs d'attributs (ex : `[type="text"]`, `[rel="nofollow"]`), et de pseudo-classes (ex : `:hover`, `:visited`).
* **Troisième nombre** : Le nombre de sélecteurs de type et de pseudo-éléments (ex : `::before`, `::after`).

Donc, pour un sélecteur qui ressemble à ceci :

```
#header .navbar li a:visited
```

La valeur sera 1,2,2 car nous avons un ID, une classe, une pseudo-classe et deux sélecteurs de type (`li`, `a`). Vous pouvez lire les valeurs comme si elles étaient simplement un nombre, par exemple 1,2,2 est 122. Les virgules sont là pour vous rappeler que ce n'est pas un système en base 10. Vous pourriez techniquement avoir une valeur de spécificité de 0,1,13,4 et 13 ne déborderait pas comme le ferait un système en base 10.

### Positionnement

Deuxièmement, je veux prendre un moment pour discuter du positionnement. Le positionnement et la mise en page vont de pair comme nous l'avons vu plus tôt dans cet article.

La mise en page est un processus récursif qui peut être déclenché sur l'ensemble de l'arbre de rendu à la suite d'un changement de style global, ou de manière incrémentielle où seules les parties sales de la page seront mises en page. Une chose intéressante à noter si nous repensons à l'arbre de rendu est qu'avec le positionnement absolu, l'objet mis en page est placé dans l'arbre de rendu à un endroit différent de celui de l'arbre DOM.

On me demande également fréquemment d'utiliser flexbox plutôt que les floats. Bien sûr, flexbox est génial d'un point de vue utilisabilité, mais lorsqu'il est appliqué au même élément, une mise en page flexbox se rendra en environ 3,5 ms alors qu'une mise en page flottante peut prendre environ 14 ms. Donc, il est payant de maintenir vos compétences CSS autant que vos compétences JavaScript.

### Z-Index

Enfin, je veux discuter du z-index. Au premier abord, cela semble simple. Chaque élément dans un document HTML peut être soit devant soit derrière chaque autre élément dans le document. Il ne fonctionne également que sur les éléments positionnés. Si vous essayez de définir un z-index sur un élément sans position spécifiée, cela ne fera rien.

La clé pour déboguer les problèmes de z-index est de comprendre les contextes d'empilement et de toujours commencer à l'élément racine des contextes d'empilement. Un contexte d'empilement est simplement une conceptualisation tridimensionnelle des éléments HTML le long d'un axe z imaginaire par rapport à l'utilisateur faisant face au viewport. En d'autres termes, ce sont des groupes d'éléments avec un parent commun qui avancent ou reculent ensemble.

Chaque contexte d'empilement a un seul élément HTML comme élément racine et lorsque les propriétés z-index et position ne sont pas impliquées, les règles sont simples. L'ordre d'empilement est le même que l'ordre d'apparition dans le HTML.

Vous pouvez cependant créer de nouveaux contextes d'empilement avec des propriétés autres que z-index et c'est là que les choses se compliquent. L'opacité, lorsque sa valeur est inférieure à un, le filtre lorsque sa valeur est autre que none, et mix-blend-mode lorsque sa valeur est autre que normal créeront en fait de nouveaux contextes d'empilement.

Juste un rappel, le mode de fusion détermine comment les pixels d'une couche spécifique interagissent avec les pixels visibles des couches en dessous.

La propriété transform déclenche également un nouveau contexte d'empilement lorsque sa valeur n'est pas none. Par exemple, `scale(1)` et `translate3d(0,0,0)`. Encore une fois, pour rappel, la propriété scale est utilisée pour ajuster la taille, et translate3d déclenche le GPU pour les transitions CSS, les rendant plus fluides.

Ainsi, vous n'avez peut-être toujours pas l'œil pour le design, mais espérons que vous partez maintenant en tant que guru CSS ! Si vous êtes intéressé à aller encore plus loin, j'ai compilé des ressources supplémentaires que j'ai également utilisées [ici](https://gist.github.com/AimeeKnight/77b36738ec876965c6db5c6d39f4ef4f).