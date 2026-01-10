---
title: Une nouvelle façon de construire des visualisations dynamiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-11T14:26:08.000Z'
originalURL: https://freecodecamp.org/news/a-new-way-of-building-dynamic-visualisations-5c732091a3c1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pXitH0oMDdrvQRHjFsNM5g.png
tags:
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Reactive Programming
  slug: reactive-programming
- name: technology
  slug: technology
seo_title: Une nouvelle façon de construire des visualisations dynamiques
seo_desc: 'By Sushrut Shivaswamy

  The Flux architecture gained popularity after Facebook adopted it. It’s a way of
  managing the state of React components so that the flow of the data through the
  app is unidirectional.

  The advantages of this approach are that the...'
---

Par Sushrut Shivaswamy

L'architecture Flux a gagné en popularité après son adoption par Facebook. C'est une façon de gérer l'état des composants React de sorte que le flux des données à travers l'application soit unidirectionnel.

Les avantages de cette approche sont que l'application est composée de quelques composants étatiques qui transmettent l'état aux composants enfants imbriqués. Une caractéristique de React qui complète vraiment cette approche de gestion d'état est que React nous permet d'écrire l'UI comme une fonction de l'état. Cela signifie que, à mesure que l'état se propage dans la hiérarchie des composants de l'application, les composants changent automatiquement la vue pour refléter les changements d'état.

JSX, un système de templating utilisé par React, permet la création de composants réutilisables en un seul fichier.

Il se prête également très bien à la création d'une démarcation entre la structure du DOM et les comportements qui y sont associés.

* JSX donne une vue claire de la structure du DOM qui est plus intuitive que les plusieurs lignes de JavaScript nécessaires pour créer la même structure DOM.
* Les comportements associés à la structure DOM — comme les gestionnaires d'événements onClick, onHover — sont gérés comme des fonctions membres du composant.
* Toute modification de la structure DOM nécessite que l'utilisateur appelle **setState pour changer l'état du composant au lieu de modifier directement le DOM**. Cela facilite le débogage de l'application et garantit que l'application est toujours dans un état défini.

Cependant, à mesure que la complexité de l'application augmentait, l'approche Flux a également commencé à montrer ses limites.

Quelques composants étatiques transmettant l'état aux composants enfants semblent bien pour les petites applications. Mais, à mesure que la complexité de la hiérarchie des composants augmente, les composants étatiques doivent partager l'état entre eux.

Bien qu'il soit possible de partager l'état entre différents composants/classes en JavaScript via des variables communes ou, de préférence, le modèle Observateur, à mesure que le nombre de composants augmente, il devient plus difficile de maintenir l'application.

La simplicité des composants réagissant aux changements d'état est brouillée par les complexités de la conception orientée objet.

### **Graphiques — pourquoi sont-ils difficiles à créer ?**

Les avancées dont ont bénéficié les applications web n'ont pas changé la façon dont les bibliothèques de graphiques sont conçues. Un graphique est également un composant de présentation et peut techniquement être qualifié d'UI. Un graphique est également composé d'éléments DOM qui contrôlent son apparence visuelle.

Cependant, les graphiques diffèrent sur un aspect clé : les développeurs ne traitent pas le SVG comme du DOM. Techniquement, la balise `<svg>` n'est même pas un HTMLElement comme les autres éléments DOM et se trouve dans un espace de noms séparé. Le SVG est seulement connu pour sa capacité à s'adapter à toute taille de viewport et à maintenir la résolution de l'image à un niveau constant. C'est la mesure dans laquelle la plupart des développeurs le connaissent.

De plus, les balises utilisées pour créer une image SVG comme `<point>`, `<rect />` et `<polyline />` semblent très « mathématiques ». Cela fait que les développeurs évitent de comprendre comment les structures SVG fonctionnent réellement.

Même ceux qui travaillent avec des applications qui utilisent intensivement le SVG sont généralement ignorants de son fonctionnement interne. Ils utilisent d'autres bibliothèques comme [snap](http://snapsvg.io/) ou d3 pour éviter la difficulté de comprendre ce qui se passe sous le capot.

Ayant évité la complexité sous-jacente de la balise SVG, il semble facile de modéliser des constructions SVG complexes.

#### Géométrie

Prenons l'exemple d'un graphique à barres.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TODhoVI3-CTxOhWU.png)
_Un beau graphique à barres._

Nous adoptons traditionnellement une approche de découpe et divisons un graphique en parties :

* axe x
* axe y
* barres

Un développeur expérimenté remarquerait que le mot axe a été écrit deux fois dans la liste ci-dessus. Alors créons une couche d'abstraction appelée `Axis` dont les sous-classes peuvent hériter.

Pour rendre les barres, nous pouvons créer une classe séparée appelée `Bar` qui utilise l'échelle fournie par la classe `axis`. Comme les graphiques existent sous diverses formes, il est plus logique d'avoir une couche d'abstraction appelée `Geometry` dont d'autres classes peuvent hériter, notamment `Bar`, `Point`, `Line` et `Area`. À mesure que des graphiques plus complexes sont créés, plusieurs nouveaux types de géométrie peuvent être ajoutés pour rendre différents types de graphiques.

En suivant la méthodologie ci-dessus, un graphique comprend trois ou plusieurs composants étatiques qui utilisent les propriétés des autres pour rendre un graphique significatif.

Pour mettre à jour ou améliorer le graphique, un développeur est censé **connaître l'état à muter dans chacun de ces composants**. Comme l'état est dispersé dans divers composants, même les changements simples prennent beaucoup de temps pour les nouveaux développeurs. **L'ordre des changements d'état devient également pertinent.**

Dans l'exemple ci-dessus, la géométrie utilise l'échelle des axes. Pour que le graphique soit redimensionné, la plage de chaque axe doit être mise à jour **avant** de mettre à jour la `Geometry`.

Ne pas suivre cet ordre entraînera des artefacts visuels — car la géométrie serait déformée en raison d'une échelle invalide. Dans le pire des cas, l'échec de cette **séquence ordonnée d'opérations** pourrait laisser le graphique dans un état indéfini.

Avoir une interconnectivité entre les graphiques aggrave encore ce problème. L'orchestration des changements d'état s'étend sur plusieurs graphiques/composants interactifs.

Avoir autant de composants interactifs avec des relations dirigées peut également entraîner des dépendances cycliques entre les composants.

C'était un problème qui a également tourmenté les frameworks de développement d'UI jusqu'à ce que le développement d'applications web avec une seule source de vérité devienne la norme. La bibliothèque la plus influente dans la direction du passage aux applications web avec une seule source de vérité était Redux.

**Note** : La section suivante explique comment l'utilisation de Redux facilite le développement d'applications web. N'hésitez pas à la sauter si vous connaissez déjà Redux.

### **Redux**

[Redux](https://redux.js.org/) est une bibliothèque développée par Dan Abhramov. Elle aide à soulager les développeurs en fournissant un moyen facile de maintenir l'état d'une application.

Redux a introduit le concept d'un magasin d'état qui agit comme la seule source de vérité pour l'ensemble de l'application. Au lieu que les composants mutent directement l'état, chaque composant envoie une action qui valide un changement dans le magasin d'état unifié.

Chaque action était identifiée par un **enum unique qui était journalisé chaque fois qu'un changement était validé dans le magasin d'état.** Cela facilitait le suivi de la manière dont le magasin d'état était muté.

Une fois qu'un changement était validé dans le magasin d'état, le nouvel état se propageait dans la hiérarchie des composants. Les composants se re-rendaient ou ignoraient le changement selon que la partie de l'état qui avait changé était pertinente pour eux. Les composants ne pouvaient plus muter l'état de manière isolée. Cela devait être fait à un niveau global.

**Le but principal est d'isoler la gestion de l'état des effets secondaires comme le rendu et la récupération des données du serveur. Toujours laisser l'application dans un état défini.**

Cela pose les bases d'un rendu de vue déterministe. Étant donné une séquence de changements d'état, vous obtiendrez toujours le même rendu de vue.

Ce niveau de rendu de vue déterministe est particulièrement utile pour les applications hors ligne. Ici, la séquence de mutations d'état qui se produit pendant que l'utilisateur est hors ligne peut être stockée et rejouée lorsque la connectivité est rétablie pour retrouver la même vue.

Le succès du modèle React-Redux a donné naissance à un certain nombre d'autres bibliothèques comme [Vue](https://vuejs.org/) et [Cycle](https://cycle.js.org/), ainsi que plusieurs autres implémentations du magasin d'état comme [MobX](https://mobx.js.org/index.html) et [Vuex](https://vuex.vuejs.org/en/intro.html).

### **Un regard plus attentif sur le SVG**

SVG signifie graphiques vectoriels scalables. La balise `svg` peut optionnellement contenir divers types de géométrie, qui exposent un certain nombre d'attributs DOM.

**Cercle** : `<circle />`

Attributs :

* **cx** : décalage x du cercle dans le viewport
* **cy** : décalage y du cercle dans le viewport
* **r** : rayon du cercle

**Polyligne** : `<polyline />`

Attributs :

* **points** : tableau de points (x, y) à travers lesquels une **ligne** est tracée.

**Polygone** : `<polygon />`

Attributs :

* **points** : tableau de points (x, y) pour construire un polygone.

**Texte** : `<text />`

Attributs :

* **x** : décalage x du texte dans le viewport
* **y** : décalage y du texte dans le viewport
* **innerText** : Le texte à afficher.

De nombreux autres types de géométrie sont disponibles dans la norme SVG, mais pour les besoins des graphiques, les éléments ci-dessus suffiront. Ces éléments géométriques peuvent également être stylisés avec du CSS normal.

### **Trouver un pont**

Ce sont les principes directeurs derrière le développement d'applications web modernes et le développement de bibliothèques de graphiques. Essayons d'isoler où le développement de bibliothèques de graphiques diffère des applications web :

* les **applications web** sont composées de nœuds DOM. Les **graphiques** sont composés de géométries SVG.
* les **applications web** peuvent être décomposées en sections réutilisables de DOM qui peuvent être modélisées comme des composants. Les **graphiques** ne sont pas modélisés comme un ensemble réutilisable de géométries.
* les frameworks d'**applications web** sont toujours couplés à un moteur de templating afin que la structure DOM puisse être modélisée en markup et que les comportements puissent en être séparés et écrits en JavaScript. Les **graphiques** n'ont pas de tel framework disponible.
* les frameworks d'**applications web** permettent d'incorporer un magasin d'état par l'utilisation d'un plugin. Les **graphiques** sont généralement modélisés comme des composants étatiques.

### **Remodeler la complexité des graphiques**

Un graphique est un outil visuel qui met en évidence la variation des champs dans les données en utilisant la géométrie.

Alors, comment cela fonctionne-t-il ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*sIbDX48h24oTItLL.png)
_Un beau nuage de points_

En regardant le graphique ci-dessus, que voyons-nous ? Des cercles décalés dans le viewport en fonction des champs présents dans les données.

Quoi d'autre ?

* Des graduations décalées le long du bas en fonction d'un champ dans les données.
* Des étiquettes de texte décalées le long du bas en fonction d'un champ dans les données.
* Même chose le long du côté gauche du graphique.

Décomposons-le au niveau des géométries.

Comment rendons-nous les cercles dans le nuage de points ?

`<circle cx="horsepowerScale()" cy="milesPerGallonScale()" cr="const" />`

Et les axes ? Axes X : Texte + Graduations

`<text x="horsepowerScale()" y="0">{{ text value }}</text>`

`<tick x="horsepwerScale()" y="0" />`

Il existe une structure SVG similaire pour l'axe y, sauf que la fonction d'échelle change et que les champs x, y sont inversés.

Le thème commun ci-dessus est que **le graphique est vu comme un arrangement significatif de géométrie** :

* chaque géométrie dans l'espace de noms SVG expose des attributs visuels
* la valeur de ces attributs est liée à une valeur calculée
* la valeur calculée dépend de l'échelle
* l'échelle dépend d'un champ dans les données et de la plage

#### **_Qu'est-ce qu'une échelle ?_**

Une échelle est une fonction qui mappe les données à une position dans le viewport.

Quelle est l'entrée de l'échelle ?

* le domaine du champ
* la longueur du viewport à mapper

Soit **R** la longueur du viewport et **D** le domaine des données.

* Alors nous pouvons définir une fonction d'échelle **S** comme suit :
* **_S = f(D, R) + b_**

où **b** est une constante.

#### **_Combien d'échelles un graphique doit-il avoir ?_**

Si vous pensez deux, alors vous avez tort.

L'échelle n'existe pas seulement le long des axes x et y. Les axes eux-mêmes ne sont présents dans un graphique que comme **ancres visuelles** afin que **les utilisateurs puissent aligner les variations de données le long de plusieurs dimensions.**

L'axe n'est que de la géométrie qui est rendue en utilisant une échelle.

#### **_Combien de dimensions y a-t-il ?_**

Ce n'est pas deux. Le viewport est bidimensionnel mais cela n'a rien à voir avec la dimensionnalité du graphique. La dimensionnalité d'un graphique est définie par le nombre de fonctions d'échelle utilisées.

Le concept global comprend deux termes simples : **Géométrie** et **Échelle**.

Chaque géométrie expose des attributs visuels qui contrôlent son apparence.

La valeur de ces attributs peut être liée à des fonctions d'échelle. La fonction d'échelle est liée à un champ particulier dans les données.

**Cela conduit à l'idée que chaque attribut visuel dans un graphique ne peut être lié qu'à un seul champ dans le tableau de données.**

Étant donné cette décomposition des graphiques, nous pouvons modéliser le nuage de points ci-dessus comme suit :

Le champ `Horsepower` est utilisé pour créer une fonction d'échelle appelée `horsepowerScale()`.

Le champ `Acceleration` est utilisé pour créer une fonction d'échelle appelée `accelerationScale()`.

Puisque nous ne faisons pas varier la taille des cercles, seules deux fonctions d'échelle sont nécessaires.

Tout cercle **i** dans le nuage de points peut être représenté comme

`<circle cx="horsepowerScale(ti)" cy="accelerationScale(ti)" cr="5" />`

où `ti` est le `i`ème tuple dans le tableau de données.

Étant donné que seules deux fonctions d'échelle ont été utilisées, la dimensionnalité du graphique ci-dessus devient deux.

**Si nous modulations également la taille de chaque cercle, en utilisant une fonction d'échelle liée à un autre champ, alors la dimensionnalité serait de trois.**

Faire cela donnerait ce qu'on appelle un « bubble chart ».

#### Grammaire des Graphiques

Cela est similaire à l'approche [Grammar of Graphics (GOG)](https://codewords.recurse.com/issues/six/telling-stories-with-data-using-the-grammar-of-graphics), où chaque graphique est défini par une marque (géométrie) et les encodages visuels utilisés par la marque.

Dans une approche GOG, le nuage de points serait représenté comme :

```
{
```

```
    mark: 'circle',
```

```
    encoding: {
```

```
        x: 'horsepower',
```

```
        y: 'acceleration'
```

```
    }
```

```
}
```

**Remarquez qu'il y a une correspondance un-à-un entre l'encodage d'une géométrie GOG et les attributs visuels exposés par la géométrie en SVG**.

L'axe peut également être rendu de manière similaire :

* L'axe x est une géométrie de graduation avec son attribut de décalage x lié à `horsepowerScale()` et son décalage y défini à 0.
* L'axe y est une géométrie de graduation avec son attribut de décalage y lié à `accelerationScale()` et son décalage x défini à 0.

Pour rendre le nuage de points avec tous ses éléments, le fragment de code suivant suffirait :

La décomposition des graphiques en une association entre les attributs visuels et une fonction d'échelle nous permet de voir un graphique comme une application web.

**Les frameworks d'applications web modélisent l'UI comme une fonction de l'état.**

**Les frameworks de graphiques devraient modéliser la géométrie comme une fonction de l'échelle.**

Ainsi, l'idée qui facilite le développement d'applications web peut facilement être étendue à la création de graphiques :

* Initialement, des données tabulaires sont fournies en entrée.
* Pour chaque champ dans le tableau de données, une fonction d'échelle est créée. La fonction d'échelle recalcule sélectivement les valeurs lorsqu'un champ dans la colonne est lié à des changements. La même fonction d'échelle est propagée dans toute l'application.
* Chaque géométrie est modélisée comme un composant qui expose des attributs visuels.
* La valeur de ces attributs visuels est liée à une fonction d'échelle qui réagit aux changements de données.
* Les collections de géométries peuvent être représentées en markup en utilisant un moteur de templating de choix comme hyperHTML, mustache ou handlebars. Idéalement, le moteur de templating devrait être introduit comme un plugin afin que nous puissions éviter d'écrire des liaisons pour différentes bibliothèques comme React et Angular.
* Le magasin d'état qui calcule sélectivement les échelles devrait également être introduit comme un plugin.

Voyons à quoi ressemblerait l'assemblage d'un graphique en utilisant les principes ci-dessus :

Nous utilisons React comme moteur de templating et Redux comme magasin d'état dans l'exemple ci-dessus.

L'approche ci-dessus est juste une implémentation approximative de ce à quoi ressemblerait un framework capable de modéliser des graphiques comme des applications web.

**Remarquez la séparation du moteur de templating et du magasin d'état de la logique de rendu réelle.**

### Points finaux

Idéalement, les géométries/graphiques que nous créons devraient être disponibles comme composants dans le framework de choix de l'utilisateur, ainsi que leur magasin d'état. Si cela semble impensable, restez calme. Cela a déjà été fait.

[SkateJS](http://skatejs.netlify.com/) est un compilateur qui crée des composants web mais permet à l'utilisateur de changer les moteurs de rendu internes.

**Les utilisateurs peuvent choisir entre React, Preact, lit-html ou étendre l'interface Renderer pour écrire la leur.** Le moteur de rendu par défaut modifie directement le DOM.

Nous pouvons être encore plus ambitieux dans ce que nous choisissons une fois que nous avons un rendu synchrone couplé à une gestion d'état.

Imaginez un composant `TickProvider` qui permet de rendre uniquement de petits groupes de géométrie dans une frame d'animation donnée ainsi que de nous permettre d'identifier les goulots d'étranglement dans notre pipeline de rendu.

Étant donné qu'un graphique est un arrangement significatif de géométrie, il s'ensuit que des groupes significatifs de géométrie devraient se rendre ensemble.

Dans l'exemple du nuage de points, pour chaque groupe de cercles qui se rendent, les sections correspondantes de la géométrie des axes x/y devraient également se rendre simultanément.

Si nous divisons le rendu en morceaux, où chaque morceau consiste en un groupe significatif de géométrie comme modélisé ci-dessus, nous pouvons supporter de belles transitions qui ajoutent à l'attrait visuel du graphique.

Un autre avantage d'un `TickProvider` est que nous pouvons profiler et nous assurer que chaque groupe de géométrie se rend complètement dans le temps alloué par tick. Cela aidera à éviter le gel de l'UI lorsque le nombre de géométries à rendre est très grand. Au lieu d'exécuter une boucle de rendu sur toute la collection de géométries, nous pourrions regrouper les appels de rendu en synchronisation avec les frames d'animation.

Nous pouvons également décomposer le calcul des valeurs des attributs visuels.

Considérons un tableau de données qui a **N** champs utilisés pour rendre des tableaux de bord avec l'approche ci-dessus.

Puisque nous utilisons un magasin d'état centralisé, nous pouvons calculer les valeurs des **N** fonctions d'échelle et les mémoriser. Elles n'ont besoin d'être recalculées que lorsque le champ de tableau de données associé change.

De plus, considérons l'équation ci-dessous qui calcule la valeur de **m** attributs visuels en fonction des fonctions d'échelle.

La 0ème valeur pour un attribut visuel **V**, qui est lié au champ 0 de **N**, peut être calculée comme suit :

V(0) = S(d0, R) + b0

* où d0 est le 0ème tuple de données du tableau de données
* R est la plage fournie comme prop au composant
* b0 est une constante

Si nous écrivons une série de telles équations ensemble, nous voyons ceci :

V(0) = S(d0, R) + b0

V(1) = S(d1, R) + b1

V(2) = S(d2, R) + b2

..

V(m) = S(dm, R) + bm

La fonction d'échelle elle-même peut être exprimée comme une équation linéaire. Nous avons un ensemble d'équations linéaires qui peuvent être calculées par lots pour calculer la valeur des attributs visuels.

Comment cela ?

L'arrangement ci-dessus ressemble étrangement à une matrice.

**Les calculs dans le navigateur sont lents, mais les calculs matriciels peuvent être accélérés en utilisant l'accélération GPU.**

Modéliser le graphique comme une géométrie en fonction de l'échelle pourrait donc nous aider à rendre les graphiques beaucoup plus rapidement, ainsi qu'à gérer de plus grands volumes de données avec un premier rendu rapide.

La visualisation de données est quelque chose qui nous aide à glaner des informations à partir de grandes quantités de données. L'impact qu'elle a sur la prise de décision augmente lentement avec de multiples organisations cherchant à prendre des décisions basées sur les données.

Il est sûr de dire que nous avons besoin d'une manière plus robuste, accessible et maintenable de développer des visualisations.

**Qu'en pensez-vous ?**