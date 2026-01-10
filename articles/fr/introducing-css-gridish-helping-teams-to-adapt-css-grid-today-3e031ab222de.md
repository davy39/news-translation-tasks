---
title: 'Présentation de CSS Gridish : Un outil open source pour aider votre équipe
  à adopter CSS Grid dès aujourd''hui'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-23T14:18:07.000Z'
originalURL: https://freecodecamp.org/news/introducing-css-gridish-helping-teams-to-adapt-css-grid-today-3e031ab222de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JobvUFgnKW070EmCAmLpIg.gif
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Présentation de CSS Gridish : Un outil open source pour aider votre équipe
  à adopter CSS Grid dès aujourd''hui'
seo_desc: 'By James Y Rauhut

  Today, I’m excited to introduce a new open-source tool from IBM called CSS Gridish!

  CSS Gridish takes design specs of your product’s grid and builds out several resources
  for your team to use:


  A sketch file with artboards and grid/...'
---

Par James Y Rauhut

Aujourd'hui, je suis ravi de vous présenter un nouvel outil open source d'IBM appelé [CSS Gridish](https://github.com/ibm/css-gridish) !

CSS Gridish prend les spécifications de conception de la grille de votre produit et génère plusieurs ressources pour votre équipe à utiliser :

* Un fichier Sketch avec des planches et des paramètres de grille/mise en page pour les designers
* Du code CSS/SCSS utilisant CSS Grid avec un repli CSS Flexbox pour les développeurs
* Une [extension Google Chrome](https://chrome.google.com/webstore/detail/ebhcneoilkamaddhlphlehojpcooobgc) pour que chacun puisse vérifier l'alignement d'une page web

L'objectif est d'aider les équipes à adopter CSS Grid plus rapidement et à permettre des mises en page plus complexes. Pour montrer à quel point l'outil est polyvalent, voici quelques exemples de grilles de [Bootstrap](https://github.com/IBM/css-gridish/tree/master/examples/bootstrap), [Carbon Design System](https://github.com/IBM/css-gridish/tree/master/examples/carbon) et [Material Design](https://github.com/IBM/css-gridish/tree/master/examples/material).

### Pourquoi les développeurs d'IBM ont créé cela

La nouvelle spécification CSS Grid est formidable pour la conception web. Désormais, les designers peuvent accorder autant d'attention à l'axe y qu'à l'axe x par le passé. Des projets [left](https://slack.engineering/rebuilding-slack-com-b124c405c193) et [right](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4) commencent à documenter leur transition vers CSS Grid.

De nombreuses équipes IBM sont impatientes d'utiliser CSS Grid, mais doivent surmonter quelques obstacles. CSS Gridish aide en abordant ces obstacles.

![Image](https://cdn-media-1.freecodecamp.org/images/Ui9S0UFPRKRi50UBf0pzqBCiscncZK4vZpuA)
_La capture d'écran du haut est une page chargée sur Chrome utilisant CSS Grid. La capture d'écran du bas est la même page sur IE 11 utilisant CSS Flexbox. ([Source](https://ibm.github.io/css-gridish/examples/material/example.html" rel="noopener" target="_blank" title="))_

#### Compatibilité des navigateurs

CSS Grid bénéficie actuellement d'un excellent support des navigateurs (~75%). Pourtant, de nombreux produits doivent encore servir les navigateurs restants. Par exemple, ibm.com reçoit encore 10% de son trafic depuis Internet Explorer. Il faut beaucoup de travail supplémentaire pour supporter ces anciens navigateurs.

Alors que CSS Gridish génère toujours `yourGrid.css` qui utilise CSS Grid, il génère également un fichier que nous appelons `yourGrid-legacy.css`. Ce fichier hérité ne sert toujours que du code CSS Grid si un navigateur le supporte. Si le navigateur ne supporte pas CSS Grid, l'utilisateur reçoit un repli flexbox. Ajoutez les classes supplémentaires pour `yourGrid-legacy.css` et vous avez ajouté une compatibilité ascendante !

Que faire si vous n'avez plus besoin de supporter les anciens navigateurs ? Il suffit de passer à `yourGrid.css` pour réduire les précieux kilooctets de l'expérience.

#### Relier la conception et le code

De grands outils ont émergé, créant une seule source de vérité pour la conception et le code, comme [React Sketchapp](https://github.com/airbnb/react-sketchapp) et [Lona](https://github.com/airbnb/Lona). Ces outils garantissent que les designers et les développeurs utilisent les mêmes composants.

![Image](https://cdn-media-1.freecodecamp.org/images/dvsiIMI7i-5Qk9JyfLXaVKtYOUtPTwxLV-Xc)
_Utilisez l'[extension Chrome](https://chrome.google.com/webstore/detail/css-gridish/ebhcneoilkamaddhlphlehojpcooobgc" rel="noopener" target="_blank" title=") pour CSS Gridish pour examiner les pages web avec les mêmes paramètres de grille et de mise en page que sur vos planches Sketch._

Nous espérons apporter cette même unité d'équipe à la grille. Les planches pour Sketch et le code pour le développement web sont générés à partir du même fichier de configuration. Bien que le fichier de configuration de la grille ne soit pas parfait, nous voulons que CSS Gridish lance une conversation sur les normes de grille dans des outils similaires.

De plus, il est facile pour les détails de conception de se perdre dans la transition vers le développement. C'est pourquoi nous avons créé une extension Google Chrome pour examiner votre travail codé. L'extension Chrome peut être configurée avec le fichier de configuration de la grille de votre équipe pour voir la même grille et la même mise en page que le fichier Sketch avec les mêmes raccourcis (CTRL+G et CTRL+L). Les développeurs aiment utiliser l'extension avec le fichier Sketch qu'ils implémentent ouvert. Les designers adorent examiner les pages web codées avec celle-ci.

#### Respecter l'ensemble de la page

En utilisant CSS Grid, un développeur peut suivre la conception de la grille en commençant par la première couche de HTML. Mais les choses deviennent plus difficiles lorsque le développeur doit travailler à l'intérieur de différentes sections et d'autres nœuds. Cela est dû au fait que `display: subgrid` gagne encore en [support des navigateurs](https://caniuse.com/#feat=css-display-contents).

CSS Gridish contourne cela en s'appuyant sur des unités de largeur de viewport au lieu d'unités de pourcentage relatives. Vous pouvez intégrer autant d'éléments `.yourGrid-grid` les uns dans les autres, mais toujours respecter les colonnes et les lignes de la page. Le seul inconvénient que nous avons trouvé à cela est que les navigateurs traitent l'unité `vw` différemment avec les barres de défilement. Cela peut être contourné avec une marge sur votre grille.

### Comment cela fonctionne

La seule entrée dont CSS Gridish a besoin est un fichier json appelé `css-gridish.json`. Le fichier accepte vos spécifications de conception de grille et des options pour l'endroit/comment les fichiers générés sont enregistrés. Pour l'instant, CSS Gridish fait quelques hypothèses sur votre conception de grille :

* Les gouttières extérieures sont de moitié la taille des gouttières intérieures
* Vos colonnes principales sont fluides au lieu de largeurs fixes

**Astuce :** Pour les meilleurs résultats dans Sketch, nous vous recommandons de rendre vos points de rupture de grille, marges et gouttières divisibles par la hauteur de la ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/WNtMemAeOorDqjE9u12JyFZu3NVHEMcPK7r8)
_Tandis que le designer de la grille spécifie les dimensions en rouge (plus le nombre de colonnes), un développeur est fourni avec les valeurs utiles en bleu._

CSS Gridish est ensuite exécuté en ligne de commande avec simplement `npx css-gridish`. Vous devriez alors voir un dossier avec tous les fichiers pour que votre équipe utilise votre grille ! Le grand avantage de CSS Gridish est qu'il facilite l'utilisation de CSS Grid pour les nouveaux utilisateurs. Après que les utilisateurs aient appris les classes détaillées dans la documentation, ils utiliseront généralement seulement deux règles :

```
.myElement {    grid-column: 1 / span 4; // Étendre sur quatre colonnes à partir de la première ligne    grid-row: 4 / span 8; // Étendre sur huit lignes à partir de la quatrième ligne}
```

Le code de repli flexbox fonctionne de manière similaire à la plupart des frameworks de grille avec un nom de classe BEM reconnaissable.

Par défaut, le code fonctionne avec des colonnes fluides et des lignes fixes. Il permet également l'inverse avec des classes modificatrices utiles. Vous utiliserez la classe de ligne fluide pour créer des formes comme des carrés qui s'adaptent à la largeur de l'écran de l'utilisateur.

Un piège lors de l'utilisation du code CSS Gridish est que nous n'utilisons pas la propriété de gap de CSS Grid pour les gouttières. Au lieu de cela, il y a des classes de remplissage qui sont de moitié la taille d'une gouttière que vous appliquez pour respecter la gouttière. Cela est dû à l'impossibilité d'ignorer les écarts pour des situations comme les couleurs de fond et les médias en pleine taille. Espérons que la prochaine version de la spécification CSS Grid résoudra cela.

### L'avenir

CSS Gridish vise à faire adopter CSS Grid par plus de produits plus rapidement et à faciliter la transition pour les utilisateurs et les équipes.

À long terme, nous espérons que cela encouragera une idée appelée bibliothèques de composants bidimensionnels. L'industrie a connu une forte ère de bibliothèques de composants qui remplissent la largeur dans laquelle les utilisateurs placent un composant. Maintenant avec CSS Grid, nous pouvons créer des composants qui remplissent également la hauteur dans laquelle ils sont placés. Cela offre plus de possibilités créatives à ceux qui créent un système de conception et plus de flexibilité aux équipes qui l'utilisent.

En attendant, veuillez utiliser et contribuer à CSS Gridish. Il y a encore beaucoup de travail à faire !

Si cela vous aide, veuillez laisser une étoile à [CSS Gridish](https://github.com/ibm/css-gridish) !

James Y Rauhut ([@seejamescode](https://twitter.com/seejamescode)) est un designer ATX travaillant pour IBM Design. Il aime coder, rechercher et faire de son mieux pour Dieu. L'article ci-dessus est personnel et ne représente pas nécessairement les positions, stratégies ou opinions d'IBM.

Un merci spécial à [Hayley Hughes](https://twitter.com/hayhughes) pour le logo discotastique. De plus, les personnes suivantes ont été d'une grande aide pour le projet lui-même : [Trevor Wong](https://github.com/electrostaticfleece), Daniel Kuehn, [Seth Johnson](https://twitter.com/sethrrr), Chiu-Ping Chiu, [Jen Downs](https://github.com/jendowns), [Josh Black](https://twitter.com/__joshblack), [Jessica Tremblay](https://twitter.com/poofichu), [Maranda Bodas](https://twitter.com/Maranda_Bodas), [Wonil Suh](http://www.wonilsuh.com/), [Quincy Larson](https://twitter.com/ossia), et toute la communauté FED@IBM.