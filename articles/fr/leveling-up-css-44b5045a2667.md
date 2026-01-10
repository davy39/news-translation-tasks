---
title: Passer au niveau supérieur en CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-21T16:20:42.000Z'
originalURL: https://freecodecamp.org/news/leveling-up-css-44b5045a2667
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pctGU4jDyVlIT2GbiiQ3SQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Passer au niveau supérieur en CSS
seo_desc: 'By Jonathan Z White

  CSS seems easy at first. After all, it’s just styling, right?

  But, give it time. Soon, CSS will show you the true depths of its complexity.

  There are four things you can do to stay sane while using CSS at scale: use proper
  semanti...'
---

Par Jonathan Z White

Le CSS semble facile au premier abord. Après tout, ce n'est que du style, n'est-ce pas ?

Mais, donnez-lui du temps. Bientôt, le CSS vous montrera la véritable profondeur de sa complexité.

Il y a quatre choses que vous pouvez faire pour rester sain d'esprit tout en utilisant le CSS à grande échelle : utiliser une sémantique appropriée, modulariser, adopter une convention de nommage et suivre le principe de responsabilité unique.

#### Utiliser une sémantique appropriée

En HTML et CSS, il y a le concept de balisage sémantique. La sémantique est le sens des mots et leurs relations. Dans le contexte de l'HTML, cela signifie utiliser des balises de balisage appropriées. Voici un exemple classique.

```
<!-- mauvais --><div class="footer"></div>
```

```
<!-- bon --><footer></footer>
```

Le HTML sémantique est assez simple. En revanche, le CSS sémantique est beaucoup plus abstrait et subjectif. Écrire du CSS sémantique signifie choisir des noms de classes qui transmettent une signification structurelle et fonctionnelle. Trouvez des noms de classes faciles à comprendre. Assurez-vous qu'ils ne sont pas trop spécifiques. Ainsi, vous pouvez réutiliser vos classes.

![Image](https://cdn-media-1.freecodecamp.org/images/yyrMjdPvw0sg5HIt4VuAds-N8kaRzRRYSbvF)

Pour illustrer de bons noms de classes sémantiques, voici un exemple simplifié du CSS de Medium.

```
<div class="stream">  <div class="streamItem">    <article class="postArticle">      <div class="postArticle-content">        <!-- contenu -->      </div>    </article>  </div></div>
```

À partir du code, vous pouvez immédiatement discerner la structure, le rôle et la signification. La classe parente est _stream_, une liste d'articles. La classe enfant est _streamItem_, un article réel dans la liste. Il est clair comment le parent et l'enfant sont liés l'un à l'autre. De plus, ces classes sont utilisées sur chaque page qui présente des articles.

**Vous devriez pouvoir lire le HTML et le CSS comme un livre. Cela devrait raconter une histoire. Une histoire a des personnages et des relations entre eux. Un CSS plus sémantique rendra finalement votre code plus maintenable.**

Pour plus de lectures, consultez [What Makes for Semantic Class Names](https://css-tricks.com/semantic-class-names/), [Naming CSS Stuff is Really Hard](https://seesparkbox.com/foundry/naming_css_stuff_is_really_hard), et [Semantics and Sensibility](http://csswizardry.com/2010/08/semantics-and-sensibility/). Pour une lecture plus longue, voir [About HTML semantics and front-end architecture](http://nicolasgallagher.com/about-html-semantics-front-end-architecture/).

#### Modulariser

À l'ère des bibliothèques basées sur les composants comme React, la modularisation est reine. Pensez aux composants comme des modules composables créés en décomposant les interfaces. Ci-dessous se trouve le flux de la page d'accueil de Product Hunt. En guise d'exercice, décomposons le flux en divers composants.

![Image](https://cdn-media-1.freecodecamp.org/images/qn3PmKMtX13dZnlW731iQrpEe6ZrlHuxZrRR)

Chaque contour coloré représente un composant. Le _stream_ a de nombreux _stream items_.

```
<div class="stream">  <div class="streamItem">    <!-- info produit -->  </div></div>
```

La plupart des composants peuvent être décomposés en composants encore plus petits.

![Image](https://cdn-media-1.freecodecamp.org/images/qqC0-2MOiyGpdsUwCN2zGwPrYb7fHO8rpaPa)

Chaque _stream item_ a une _thumbnail_ et des informations sur un produit en vedette.

```
<!-- COMPOSANT STREAM --><div class="stream">  <div class="streamItem">
```

```
    <!-- COMPOSANT POST -->    <div class="post">      <img src="thumbnail.png" class="postThumbnail"/>      <div class="content">        <!-- info produit -->      </div>    </div>
```

```
  </div></div>
```

Parce que le composant _stream_ est indépendant de ses enfants et vice versa, vous pouvez facilement ajuster ou remplacer la classe _post_ sans apporter de modifications significatives à la classe _stream_.

Penser en composants vous aidera à découpler votre code. Plus votre code est [découplé](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), plus l'interdépendance entre vos classes est faible. Cela rend votre code plus facile à modifier et à travailler à long terme.

![Image](https://cdn-media-1.freecodecamp.org/images/DpFUVLga0pYDsb5XJMLIIYwdHrMuWrINHQ53)
_[Conception pilotée par les composants](https://dribbble.com/shots/1200218-iOS-7-UI-Components" rel="noopener" target="_blank" title=")_

Lorsque vous modularisez votre CSS, commencez par décomposer votre conception en composants. Vous pouvez le faire avec du papier et un crayon ou dans un programme comme Illustrator ou Sketch. L'identification des composants vous donnera une idée de la manière de nommer vos classes et de leurs relations les unes avec les autres.

Pour en savoir plus sur le CSS piloté par les composants, consultez [CSS Architectures: Scalable and Modular Approaches](https://www.sitepoint.com/css-architectures-scalable-and-modular-approaches/), [Writing Modular CSS with Sass](http://sassbreak.com/writing-modular-css-with-sass/), et [Modularizing Your Front-End Code for Long Term Maintainability and Sanity](http://www.berndtgroup.net/thinking/blog/development/modularizing-your-front-end-code-for-long-term-maintainability-and-sanity).

#### Choisir une bonne convention de nommage

Il existe des dizaines de conventions de nommage CSS. Certaines personnes jurent par leur choix de convention, affirmant que la leur est meilleure que les autres. En vérité, la meilleure convention de nommage est différente pour chaque personne. Le meilleur conseil que j'ai jamais reçu à ce sujet est : choisissez la convention de nommage qui a le plus de sens pour vous.

Voici une courte liste de certaines des conventions de nommage que les gens utilisent :

* [Object oriented CSS OOCSS](https://www.smashingmagazine.com/2011/12/an-introduction-to-object-oriented-css-oocss/)
* [Block element modifier (BEM)](http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/)
* [Scalable and modular architecture for CSS (SMACSS)](https://smacss.com/)
* [Atomic](http://acss.io/)

L'une de mes conventions de nommage préférées est BEM. BEM signifie block, element, et modifier. [Yandex](https://www.yandex.com/), l'équivalent russe de Google, l'a inventée pour résoudre les problèmes qu'ils avaient avec leur base de code CSS à grande échelle.

![Image](https://cdn-media-1.freecodecamp.org/images/jNU5gEtp8a0Ku5SeEbCkecynENpEi1FRHNfd)

BEM est l'une des conventions de nommage les plus simples — mais aussi les plus strictes.

```
.block {}.block__element {}.block--modifier {}
```

Les blocs représentent des classes de niveau supérieur. Les éléments sont des enfants de blocs. Et les modificateurs représentent différents états.

![Image](https://cdn-media-1.freecodecamp.org/images/mlPg8sX2LVJoMRvDG9JJedkJMaNcoXayNf5C)

```
<div class="search"> <input type="search__btn search__btn--active" /></div>
```

Dans l'exemple ci-dessus, la classe _search_ est le bloc et _search button_ est son élément. Si nous voulons modifier l'état du bouton, nous pouvons ajouter un modificateur comme _active_.

Une chose à retenir à propos des conventions de nommage est que, quelle que soit la convention de nommage CSS que vous préférez, vous hériterez souvent ou travaillerez sur des bases de code avec des normes différentes. Soyez ouvert à l'apprentissage de nouvelles normes et à des façons alternatives de penser au CSS.

Vous pouvez en savoir plus sur BEM dans [Getting your head 'round BEM syntax](http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/), [BEM 101](https://css-tricks.com/bem-101/), et [Intro to BEM](http://getbem.com/introduction/). Pour des lectures générales sur différentes conventions, consultez [OOCSS, ACSS, BEM, SMACSS: what are they? What should I use?](http://clubmate.fi/oocss-acss-bem-smacss-what-are-they-what-should-i-use/)

#### Suivre le principe de responsabilité unique

Le principe de responsabilité unique stipule que chaque module ou classe doit avoir la responsabilité d'une seule partie de la fonctionnalité fournie par le logiciel, et que cette responsabilité doit être entièrement encapsulée par la classe.

Dans le contexte du CSS, le principe de responsabilité unique signifie que les morceaux de code, les classes et les modules doivent ne faire qu'une seule chose. Lorsqu'il est appliqué à l'organisation des fichiers CSS, cela signifie que les composants autonomes comme les carrousels et les barres de navigation doivent avoir leur propre fichier CSS.

```
/components   |- carousel  |- |- carousel.css  |- |- carousel.partial.html  |- |- carousel.js  |- nav  |- |- nav.css  |- |- nav.partial.html  |- |- nav.js
```

Un autre modèle courant dans l'organisation des fichiers est le regroupement des fichiers par fonctionnalité. Par exemple, dans l'extrait ci-dessus, tous les fichiers liés au composant carrousel sont regroupés ensemble. L'adoption de cette approche facilite la recherche de fichiers.

En plus de séparer les styles des composants, il est bon de séparer le style global en utilisant le principe de responsabilité unique.

```
/base  |- application.css   |- typography.css  |- colors.css  |- grid.css
```

Dans l'exemple, chaque préoccupation de style est séparée dans son propre fichier. Ainsi, si vous voulez mettre à jour vos couleurs, vous savez exactement où chercher.

Quelle que soit la convention d'organisation de fichiers que vous utilisez, laissez le principe de responsabilité unique vous guider dans vos décisions. Si un fichier commence à devenir trop volumineux, envisagez de le partitionner en fonction de ce qui a du sens logique.

Pour plus d'informations sur les structures de fichiers et l'architecture CSS, lisez [Aesthetic Sass 1: Architecture and Style Organization](https://scotch.io/tutorials/aesthetic-sass-1-architecture-and-style-organization) et [Scalable and Maintainable CSS Architecture](https://www.xfive.co/blog/itcss-scalable-maintainable-css-architecture/).

Lorsque le principe de responsabilité unique est appliqué aux classes CSS individuelles, cela signifie que chaque classe doit avoir une seule fonction. En d'autres termes, séparez les styles en différentes classes en fonction des préoccupations. Voici un exemple classique :

```
.splash {  background: #f2f2f2;  color: #fffff;  margin: 20px;  padding: 30px;  border-radius: 4px;  position: absolute;  top: 0;  right: 0;  bottom: 0;  left: 0;}
```

Dans l'exemple ci-dessus, nous mélangeons les préoccupations. La classe _splash_ contient non seulement la logique de présentation et de style pour elle-même, mais aussi pour ses enfants. Pour remédier à cela, nous pouvons diviser le code en deux classes séparées.

```
.splash {  position: absolute;  top: 0;  right: 0;  bottom: 0;  left: 0;}
```

```
.splash__content {  background: #f2f2f2;  color: #fffff;  padding: 30px;  border-radius: 4px;}
```

Maintenant, nous avons un _splash_ et un _splash content_. Nous pouvons utiliser _splash_ comme une classe générique full-bleed qui prend n'importe quel enfant. Toutes les préoccupations de l'enfant, dans ce cas le _splash content_, sont découplées du parent.

Vous pouvez en savoir plus sur l'application de l'approche de responsabilité unique au style et aux classes dans [The single responsibility principle applied to CSS](http://csswizardry.com/2012/04/the-single-responsibility-principle-applied-to-css/) et [Single Responsibility](http://drewbarontini.com/articles/single-responsibility/).

#### Simplicité plutôt que complexité

Demandez à n'importe quel bon développeur front-end ou architecte CSS et ils vous diront qu'ils n'ont jamais été entièrement satisfaits de leur code. Écrire du bon CSS est un processus itératif. Commencez simplement, suivez les conventions de base du CSS et les guides de style, et itérez à partir de là.

J'aimerais savoir comment vous abordez le CSS. Quelle est votre convention de nommage préférée ? Comment organisez-vous votre code ? N'hésitez pas à laisser un mot ou à [Tweeter](https://twitter.com/JonathanZWhite) à moi.

_P.S. Si vous avez aimé cet article, cela signifierait beaucoup si vous cliquiez sur le bouton de recommandation ou le partagiez avec des amis._

Si vous voulez plus, vous pouvez me suivre sur [Twitter](https://twitter.com/JonathanZWhite) où je poste des divagations sans sens sur le design, le développement front-end, les bots et l'apprentissage automatique.

![Image](https://cdn-media-1.freecodecamp.org/images/vrXsHfyC6Zrydfu2I1P39nztEF4vxmX5Kaze)

![Image](https://cdn-media-1.freecodecamp.org/images/-SA2S2gIS-E3xoiLUKa127Ol4drHzo6noOO2)