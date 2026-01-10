---
title: La différence entre width et flex-basis dans Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T23:34:52.000Z'
originalURL: https://freecodecamp.org/news/flexboxs-flex-basis-explained-83d1a01413b7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fWJygbRiTbvHTJwgsBbhYA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La différence entre width et flex-basis dans Flexbox
seo_desc: 'By Kyle Gallagher

  Understanding the weird parts



  When I first started learning Flexbox, the thing that struck me curious the most
  was “Why did they add this flex-basis in?” I mean, I have width…Why is there also
  a flex-basis?

  “Dynamic Constraint”

  I ...'
---

Par Kyle Gallagher

#### Comprendre les parties étranges

![Image](https://cdn-media-1.freecodecamp.org/images/1*fWJygbRiTbvHTJwgsBbhYA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ia0zd9YdOzAN5afQcjB00Q.png)

Lorsque j'ai commencé à apprendre Flexbox, la chose qui m'a le plus intrigué était « Pourquoi ont-ils ajouté flex-basis ? » Je veux dire, j'ai width… Pourquoi y a-t-il aussi flex-basis ?

#### « Contrainte dynamique »

J'ai lu plusieurs articles sur le sujet. Tous affirmaient une différence entre width et flex-basis. Aucun n'expliquait vraiment en quoi consistait cette différence, cependant.

Après beaucoup d'expérimentations et quelques bons vieux bidouillages, j'en suis arrivé à la conclusion que le but principal de flex-basis était de fournir une contrainte « dynamique ». Mais que veux-je dire exactement par là ? Une contrainte « dynamique ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*T2E-Y40hzQczgj0gJNemQg.png)

Je pars du principe que vous êtes déjà familier ou au moins généralement acquainted avec CSS et Flexbox.

Je ne vais pas entrer dans les détails de CSS ou Flexbox qui vous enseigneraient les concepts de base de l'un ou de l'autre.

#### Ce qu'il faut savoir

Je vais également utiliser SCSS, et non CSS natif, ainsi que la méthode « Block-Element-Modifier (BEM) ». La raison en est que je pense qu'il est plus facile d'être concis de cette manière. Vous devrez donc comprendre les bases de SCSS et de la nesting. BEM devrait être auto-descriptif dans les exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pszJVENDOJ9zQ4pFv0cjZg.png)

Le but de cet article est de simplifier l'énigme qui semble exister sur Internet concernant flex-basis. J'ai souvent vu la réponse « vous utilisez flex-basis au lieu de width » comme réponse à son utilité. Bien sûr, cela est tout à fait acceptable pour la plupart des cas, bien qu'il soit possible de l'utiliser de manière plus avancée. Il semble que le potentiel de flex-basis ait échappé à beaucoup depuis quelque temps (bien sûr, pas à tous), mais j'ose dire à **beaucoup**. 

Je veux essayer de vous convaincre dans cet article que flex-basis de Flexbox **n'est pas un remplacement pour width (ou height)**. C'est un tout nouvel outil avec son propre ensemble de possibilités.

![Image](https://cdn-media-1.freecodecamp.org/images/1*622Amc8qMCdhubJLXIxX0A.png)

### Le cœur du sujet

Maintenant que j'ai dit ces choses… La partie suivante consiste à expliquer et à montrer exactement de quoi je parle ici. Comme vous le savez peut-être, lorsque vous travaillez avec Flexbox, vous pouvez utiliser flex-basis à la place de width.

#### Exemples visuels

Dans l'exemple ci-dessus, nous avons un élément « inner » qui résidera à l'intérieur de l'élément « outer ». L'élément outer est notre Flexbox et l'élément inner a un flex-basis de 400px.

Le HTML pour ce qui précède pourrait ressembler à ceci :

Résultant en une boîte grise qui fait exactement 400px de large sur 250px de haut au centre de notre écran comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nM0mmpE3WsKmFS5LcRRybA.jpeg)

Dans l'exemple ci-dessus, notre wrapper _.element_ a par défaut une flex-direction qui est **row (de gauche à droite)** et non column (de haut en bas). Retenez cela. Bientôt, nous allons changer cela en column et vous allez voir de quoi parle tout cet article. Cette nature dynamique de flex-basis de Flexbox.

#### Rendre les choses « dynamiques »

Changeons donc le code pour montrer cette « nature dynamique ». Pour ce faire, tout ce que nous avons à faire est de changer l'élément outer pour qu'il ait une (_flex-direction: column_) et de changer la _height_ en _width_ sur l'élément inner (le HTML ne change pas).

Changer la flex-direction modifie la direction que flex-basis affectera. Ainsi, flex-basis est à la fois width et height. Dans l'exemple ci-dessus, flex-basis entraînera désormais un bloc de 400px de haut contre le rectangle de 400px de large que nous avons vu précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jQjetbcp_cqMuy0EY1Puag.jpeg)

*Si vous souhaitez jouer avec ce code vous-même, voici un [codepen](https://codepen.io/litonfiredesign/pen/wOeBjp) avec le code ci-dessus.*

#### Observation

Remarquez comment, dans le premier exemple, flex-basis prend le rôle de width, et dans le second exemple, le rôle de height. Flex-basis est à la fois width et height dans un Flexbox, selon la flex-direction. Plutôt cool !

### **Compréhension approfondie / Bonnes pratiques**

Voici quelques-unes des choses les plus importantes que j'ai apprises sur flex-basis lors de mon utilisation de flex-basis de Flexbox.

* Flex-basis contrôle soit « width » soit « height » en fonction de la flex-direction
* Flex-basis remplacera toute autre propriété _width:_ ou _height:_ si elle est spécifiquement déclarée autre que flex-basis: **auto** (auto par défaut)
* La forme abrégée pour flex-basis est (flex: $grow, $shrink, $size) et est définie à (flex: 0 1 **auto**) par défaut.
* Lorsque flex-basis est défini à **auto**, il vérifie d'abord une propriété width ou height (en fonction de la direction) **si aucune**, il **_utilise la taille du contenu de l'élément_**
* Flex-basis respectera toujours les paramètres _min_ / _max-width:_ ou height. Encore une fois, cela dépend de la _flex-direction:_
* Flex-basis dans une colonne remplace _height:_, ceci est important car bien que _width:_ respectera flex-shrink, _height:_ ne le fera pas. _(Cela peut causer des résultats confus et inattendus dans votre design.)_

#### Important à noter

Remarquez comment **auto** est en gras. Par défaut, si vous avez une width définie et que vous n'avez pas déclaré de valeur flex-basis, width fonctionnera normalement sur cet élément. Il n'y a pas de différence entre la manière dont _flex-basis:_ fonctionnera sur votre élément et la manière dont _width:_ fonctionnera sur votre élément. Width respectera même flex-shrink lors de l'utilisation de Flexbox.

Le facteur divergent entre width et flex-basis est la capacité dynamique de flex-basis à changer sa direction effective en fonction de la flex-direction.

#### La mise en garde

_height:_ en revanche, se comporte un peu différemment. La propriété height ne respecte pas flex-shrink de la même manière que width. Lorsque vous utilisez flex-direction _column_, vous devriez toujours utiliser flex-basis pour contrôler dynamiquement la taille de votre Flexbox afin d'obtenir des résultats cohérents et attendus.

**Prêtez également une attention particulière au point numéro 4 :**

* Lorsque flex-basis est défini à **auto**, il vérifie d'abord une propriété width ou height (en fonction de la direction) **si aucune**, il **_utilise la taille du contenu de l'élément_**

Cela signifie que flex-basis dimensionnera automatiquement l'élément en fonction de la taille du contenu (la taille de l'élément interne) lorsqu'il est défini à _flex-basis: auto._ Seulement s'il n'y a pas de _width:_ ou de _height:_ défini sur l'élément.

#### Bonnes pratiques

Je recommande, lorsque c'est possible, d'utiliser flex-basis plutôt que width ou height comme meilleure pratique, de cette manière vos résultats sont toujours cohérents. Sachant que _width:_ respectera flex-shrink et que _height:_ ne le fera pas, comprenez qu'il peut y avoir des différences dramatiques entre la manière dont width et height fonctionneront dans un Flexbox lorsque vous utilisez d'autres propriétés de Flexbox en conjonction, comme flex-wrap par exemple. Utilisez également la forme abrégée de flex pour des raisons de commodité, de cohérence et de lisibilité.

La forme abrégée pour flex-basis est (flex: $grow, $shrink, $size) et est définie à (flex: 0 1 **auto**) par défaut.

```
flex: 0 1 200px;
```

Il existe certains cas où vous devrez peut-être utiliser width ou height plutôt que flex-basis. Certains cas peuvent inclure des contournements de bugs de Flexbox. Une bonne ressource sur ce sujet est [Flexbugs](https://github.com/philipwalton/flexbugs). Flexbugs est également un bon endroit pour déterminer d'autres bonnes pratiques en fonction des navigateurs que vous prévoyez de supporter.

### **Ressources supplémentaires**

Dans l'exemple [_codepen_](https://codepen.io/litonfiredesign/pen/OaZLWd) suivant, je montre flex-wrap pour démontrer un exemple visuel des informations ci-dessus de cet article.

Utilisez ce [codepen](https://codepen.io/litonfiredesign/pen/OaZLWd) et examinez attentivement le code. Vous verrez comment j'utilise flex-basis une seule fois dans l'ensemble de la base de code pour contrôler plusieurs scénarios. Ce n'est qu'un petit exemple des cas d'utilisation possibles.

### **Conclusion**

Savoir que flex-basis est à la fois une contrainte de width et de height est un bon outil à avoir. Il est dynamiquement modifiable. En utilisant flex-basis, vous pouvez créer des éléments de design très intuitifs. Certains peuvent même changer lors d'un changement de flex-direction d'un Flexbox à un point de rupture crucial dans votre design, vous offrant ainsi une solution plus propre. Cette connaissance devrait également vous aider à concevoir mieux et avec plus de confiance avec Flexbox, puisque cette fonctionnalité est clé pour utiliser Flexbox à son plein potentiel.

Si vous pensez que j'ai oublié quelque chose, trouvé une faute de frappe, etc… faites-le moi savoir !

J'espère que cet article court et concis a été utile à quelqu'un. Si vous avez apprécié l'effort investi, n'hésitez pas à applaudir l'article ! ?

### **Rester en contact ?**

Si vous souhaitez discuter, le meilleur endroit pour me rejoindre est sur [linkedin](https://www.linkedin.com/in/litonfiredesign/) ou en me contactant via mon [site web](https://www.lofde.com/).

Je ferai de mon mieux pour répondre à tous les commentaires ou questions ici sur Medium.

Si vous utilisez les réseaux sociaux : [Instagram](https://www.instagram.com/litonfiredesign/) ou [Facebook](https://www.facebook.com/litonfiredesign/).

**Crédits photographiques :** ( Waterfall | Jared Erondu ) ( Chatter | Dan Wayman ) ( Disclaimer | Pop & Zebra ) ( Objective | Olav Ahrens Røtne ) et ( Let’s go | Goh Rhy Yan ). Toutes les photos proviennent de [Unsplash.com](https://unsplash.com/)