---
title: Comment utiliser les wireframes avec les design systems
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-17T17:06:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-wireframes-with-design-systems-46f3040829b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J7kjxgTFCyTHqm28222z6g.png
tags:
- name: Design
  slug: design
- name: Design Systems
  slug: design-systems
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: '#wireframe'
  slug: wireframe
seo_title: Comment utiliser les wireframes avec les design systems
seo_desc: 'By Leon Barnard

  In my 10+ years as a UX designer, one of the most frequent questions I’m asked about
  wireframes is how much visual detail to put into them.

  There’s an attractive elegance to a simple black and white sketch, but it can sometimes
  lead t...'
---

Par Leon Barnard

En tant que designer UX depuis plus de 10 ans, l'une des questions les plus fréquentes que l'on me pose sur les wireframes est de savoir combien de détails visuels y inclure.

Il y a une élégance attrayante dans un simple croquis en noir et blanc, mais cela peut parfois laisser des lacunes dans la compréhension partagée de ce à quoi le produit final ressemblera vraiment.

Les wireframes excellent lors des premières phases du développement produit, lorsque l'idéation et l'itération rapide sont les plus valorisées. Mais ce qui les rend idéaux pour cette phase les dessert également lors de la phase suivante, lorsque la précision au pixel et les détails visuels sont requis pour l'implémentation.

En conséquence, beaucoup de gens (et j'en ai fait partie) tentent d'incorporer des détails esthétiques et fins dans leurs wireframes en ajustant les polices, en ajoutant des couleurs et en utilisant d'autres effets visuels.

Cela peut souvent mener à la confusion lorsque ces wireframes proto-haute fidélité sont utilisés comme spécifications d'implémentation et envoyés "par-dessus le mur" à l'équipe de développement. La plupart des outils de wireframing ne sont pas optimisés pour créer des artefacts qui ressemblent et se comportent comme un produit fini. Pourtant, créer des rendus polies de chaque écran ou un prototype haute fidélité est chronophage et [peut ne pas bien se traduire dans le produit final de toute façon](https://blog.teamtreehouse.com/rapidly-prototype-websites).

Mais, existe-t-il une autre façon ?

**Bien sûr que oui** ! Une méthode où vous pouvez garder vos wireframes de basse fidélité, tout en atteignant cette compréhension partagée puissante de l'apparence et du comportement implémentés.

#### Les Design Systems à la Rescue

Une alternative à l'utilisation des wireframes au-delà de leurs limites est de les garder de basse fidélité et de laisser un autre outil spécifier l'apparence et le comportement.

Dans cet article, je vais expliquer pourquoi, pour les applications et sites web au moins, un excellent outil pour ce travail est un **design system**.

Avant de plonger, définissons ce qu'est un design system.

Comme leur précurseur, les guides de style, les design systems définissent l'apparence et le comportement de l'application. Ils vont cependant un peu plus loin, car ils définissent souvent le **comportement** également et sont soutenus par du code fonctionnel.

Les grandes entreprises utilisent des design systems depuis longtemps. Jusqu'à récemment, ils étaient trop intensifs en main-d'œuvre pour les petites entreprises, car ils nécessitaient souvent des designers et développeurs dédiés travaillant en dehors des équipes produit principales.

Voici un exemple, issu du [IBM Carbon Design System](https://www.carbondesignsystem.com), montrant l'apparence et le code pour les boutons.

![Image](https://cdn-media-1.freecodecamp.org/images/Dy85oSgyI4dmDfnQAxbaHCZgDf1mgSOSC4fu)
_[Carbon Design System](https://www.carbondesignsystem.com" rel="noopener" target="_blank" title=") boutons_

Le paysage des design systems a changé après la sortie du framework [Bootstrap](http://getbootstrap.com/) en 2011. Il s'agit d'un kit de démarrage gratuit pour le développement web qui fournit des templates HTML conformes et robustes, ainsi que des styles CSS généralement esthétiques, personnalisables selon votre marque.

Il inclut sa propre grille et ses définitions de typographie, ainsi que des styles pour les boutons, formulaires, et plus encore. En bref, il élimine une grande partie du travail difficile pour démarrer un projet web et s'assurer qu'il fonctionne sur tous les navigateurs.

Bootstrap et d'autres frameworks similaires ont été utilisés comme base pour les design systems des petites entreprises qui n'ont pas les ressources pour construire les leurs.

Comme vous pouvez le voir ci-dessous, Bootstrap est très similaire aux design systems d'entreprise comme celui montré ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/iXL3oSzH7bcl5cyVfkIKyGwKG3duYSHVMEKn)
_[Bootstrap](http://getbootstrap.com" rel="noopener" target="_blank" title=") boutons_

#### Design Systems + Wireframes en Pratique

L'avantage principal de l'association d'un design system avec un outil de wireframing est qu'il peut vous libérer de l'inquiétude concernant l'apparence, le comportement et les détails lors de la création de wireframes. Pourtant, ils fournissent des rendus parfaits au pixel des composants du produit final.

Lorsque vous savez déjà à quoi un bouton (ou un onglet, un menu, etc.) va ressembler et quelles seront ses transitions d'état lorsque vous cliquez dessus, alors vous n'avez pas besoin de le styliser dans votre wireframe. Le noir et blanc et [Balsamiq Sans](http://balsamiq.com/products/mockups/font/) suffisent amplement.

> _Avoir un design system de référence peut vous permettre de passer directement des wireframes au code sans laisser la vision finale indéfinie._

Voici comment vous pouvez les associer. Vous verrez qu'ils s'entendent plutôt bien ensemble !

Si vous avez déjà un design system, c'est parfait. Sinon, vous pouvez commencer par un téléchargement personnalisé de [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) ou [Foundation](https://foundation.zurb.com/sites/download.html/). L'étape suivante est de créer une correspondance entre celui-ci et les contrôles de votre outil de wireframing.

Une correspondance signifie essentiellement développer un accord partagé de "ceci signifie cela". Vous pouvez le faire en créant un document montrant ces correspondances ou simplement en organisant une réunion avec les équipes de design et de développement autour d'un écran pour le déterminer.

Voici un exemple de la façon dont vous pourriez faire correspondre certains contrôles [Balsamiq](https://balsamiq.com) aux composants Bootstrap (vous pourriez également commencer avec la bibliothèque [Bootstrap Wireframes To Go](https://wireframestogo.com/#/search=bootstrap)).

![Image](https://cdn-media-1.freecodecamp.org/images/5-jQm4qhKNfVlQHNjMfmrj7lztq1qq5g4U5z)
_Correspondance simple des contrôles de wireframe aux contrôles d'interface utilisateur codés_

> **_Note:_** _Il est acceptable d'utiliser un peu de couleur, mais cela ne doit être utilisé que dans la mesure nécessaire pour indiquer les états et les sélections, par exemple._

Avoir ce type de correspondance signifie que **les développeurs n'ont plus à se demander si les couleurs dans le wireframe doivent être utilisées dans leur code**. Ils peuvent simplement traduire dans leur tête qu'un bouton bleu dans le wireframe signifie en réalité un bouton vert dans l'interface utilisateur (si c'est la couleur que vous utilisez), et que les fil d'Ariane séparés par le caractère `&`gt; doivent en réalité être séparés par le caractère / dans l'application, par exemple.

Vous pouvez également étendre votre design system en créant vos propres contrôles Balsamiq en tant que [Symboles](https://docs.balsamiq.com/desktop/symbols/) pour les faire correspondre à d'autres composants de votre bibliothèque, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/C1NnmuTJ85ig6LUsmdiItM2ujt7SrqnBgIqs)
_Symboles Balsamiq correspondant aux composants du design system_

Cette correspondance peut évoluer et grandir au fil du temps, au fur et à mesure que les besoins et le langage de design changent dans votre organisation.

Voici un exemple simple montrant à quoi un wireframe terminé pourrait ressembler lorsqu'il est construit en conjonction avec un design system.

> _Note : Le bleu dans le wireframe n'a pas besoin de signifier bleu dans le produit final._

![Image](https://cdn-media-1.freecodecamp.org/images/c9J061zS0hvTuedNOF6BW1I4BzgrHEAjWVYl)
_Créé dans Balsamiq_

![Image](https://cdn-media-1.freecodecamp.org/images/NXKeYs7lM8jkV2Arf5x6ewTbt4y2rVazGyMn)
_Créé avec du code_

Du wireframe au code fonctionnel sans artefacts de design supplémentaires entre les deux !

Avoir un design system signifie également que vous réutilisez le même code dans toutes les parties de votre application, de sorte que différents développeurs produisent la même interface utilisateur, ce qui conduit à de meilleures normes et à une plus grande cohérence. Et si le design system est mis à jour, les wireframes n'ont pas besoin de changer.

Enfin, **les designers peuvent s'appuyer davantage sur les contrôles standard de l'outil** plutôt que de passer des heures à essayer de reproduire l'apparence par eux-mêmes, ce qui raccourcit à la fois les cycles de design et de développement.

#### Résumé

Bien sûr, rien ne fonctionne pour tout le monde. Cette approche n'est pas garantie de fonctionner pour tous les projets ou organisations. Par exemple, elle est mieux adaptée aux équipes internes.

Les clients extérieurs à votre organisation sont plus susceptibles de vouloir voir une maquette haute fidélité. De plus, la plupart des design systems de départ sont pour des produits basés sur le web. Les modèles et exemples de design systems pour applications de bureau et mobiles sont moins courants.

Enfin, et peut-être surtout, vous devez avoir **une bonne communication entre les équipes de design et de développement** pour que cette approche fonctionne.

Une grande partie de la compréhension partagée de la connexion entre les wireframes et les design systems est créée en **en parlant**. L'annoncer par email ou simplement le publier sur votre intranet seul ne fonctionnera probablement pas. Les équipes en cascade et les équipes distantes essayant cela pourraient ne pas s'en sortir aussi bien.

Cela dit, cela offre de nombreux avantages pour de nombreuses équipes, tels que :

* Gain de temps lors de la création de wireframes
* Aucune divergence entre le wireframe et la réalité
* Bon pour les méthodologies Lean/Agile où les livrables n'ont pas besoin d'être si formels
* Bon pour les petites équipes et les startups avec peu de ressources (surtout lorsqu'elles utilisent des frameworks)
* Différentes compétences peuvent être appliquées à différentes zones de design (par exemple, designers visuels et développeurs pour le design system, designers d'interaction ou chefs de projet pour les wireframes)
* Les processus de design (wireframes vs. création de design system) peuvent être effectués indépendamment, ce qui entraîne moins de goulots d'étranglement
* Plus de cohérence de l'interface utilisateur dans le produit

### Plus de Ressources sur les Design Systems

* [Galerie de Design Systems](https://designsystemsrepo.com/design-systems/)
* ["Concevoir des Design Systems"](https://clearleft.com/posts/designing-design-systems)
* ["Commencer avec les Bibliothèques de Motifs"](https://alistapart.com/blog/post/getting-started-with-pattern-libraries)
* [Introduction à l'Atomic Design](http://atomicdesign.bradfrost.com/chapter-1/)
* [Outil de Design System Pattern Lab](https://patternlab.io)
* [Ressources de Guide de Style de Site Web](http://styleguides.io/)