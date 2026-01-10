---
title: 'Naviguer les eaux : entre Bokeh et D3'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T17:45:35.000Z'
originalURL: https://freecodecamp.org/news/charting-the-waters-between-bokeh-and-d3-73b3ee517478
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WQF5AwtvsAmBFFB1BcRDvg.png
tags:
- name: data visualization
  slug: data-visualization
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: 'tech '
  slug: tech
seo_title: 'Naviguer les eaux : entre Bokeh et D3'
seo_desc: 'By Mandi Cai

  Introduction

  There comes a time in the life of a budding “low-key but also high-key trying to
  become a front-end designer and developer” when they must enter the world of charting
  libraries.


  Navigating uncharted waters

  Charting librarie...'
---

Par Mandi Cai

### **Introduction**

Il arrive un moment dans la vie d'un "low-key mais aussi high-key essayant de devenir designer et développeur front-end" où il doit entrer dans le monde des bibliothèques de graphiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lvrEEYhc7DAyPXJQ5pRxkQ.png)
_Naviguer dans des eaux *inexplorées*_

Les bibliothèques de graphiques produisent des visualisations basées sur des données. Elles sont la raison pour laquelle vous pouvez rapidement comprendre les tendances de l'espérance de vie sur [FiveThirtyEight](http://fivethirtyeight.com/) ou évaluer le sentiment national à propos d'une prochaine élection présidentielle (aïe) sur [The New York Times](https://www.nytimes.com/).

Pensez aux graphiques que vous pouvez créer dans [Google Sheets](https://www.google.com/sheets/about/), sauf que maintenant vous avez des droits de visualisation et d'édition directs sur la bibliothèque qui alimente ces [graphiques](https://developers.google.com/chart/). Vous êtes le maître de ces blocs de construction de bas niveau constituant un "graphique".

Plusieurs bibliothèques de graphiques sont écrites en JavaScript, un langage plus familier pour les développeurs web que la plupart des autres, ce qui rend leur apprentissage moins intimidant. Lorsqu'elles sont exécutées correctement, les bibliothèques de graphiques ont le pouvoir de transmettre un message puissant _et_ de vous offrir l'opportunité de voir de sérieux bonbons visuels.

Récemment, notre équipe a été chargée de créer une interface qui devait intégrer une bibliothèque de graphiques pour atteindre l'objectif. Par conséquent, nous avons dû choisir une bibliothèque qui satisfaisait nos cas d'utilisation spécifiques. Si vous évaluez correctement vos besoins et choisissez une bibliothèque qui les satisfait tous, la vie est parfaite.

Cependant, les bibliothèques ne sont jamais une solution universelle. Plus souvent qu'autrement, votre hypothèse initiale qu'une bibliothèque est le choix parfait sera incorrecte en raison d'obstacles imprévus qui surgissent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xYV02tF4HbAVzeQI9id8VQ.png)
_Quand rien ne fonctionnait_

Peut-être vous demandez-vous : "Quelles sont ces options ?", "Comment avez-vous abordé le choix d'une option ?" ou "Pourquoi vous sentiez-vous stupide ?" (référence au message Slack ci-dessus).

Cet article décrira notre processus de choix d'une bibliothèque de graphiques parmi la myriade de bibliothèques JavaScript actuellement disponibles, la décision critique de passer entre deux bibliothèques de graphiques ([Bokeh](https://bokeh.pydata.org/en/latest/docs/dev_guide/bokehjs.html) et [D3.js](https://d3js.org/)), ainsi que les avantages et inconvénients de chacune. Pour moi, c'était un territoire "inexploré", et si vous vous sentez de la même manière à propos des bibliothèques de graphiques ou de la visualisation de données en général, vous vous sentirez mieux après avoir lu ceci.

Commençons !

### Pourquoi nous avons essayé Bokeh en premier

Nos besoins se divisaient en deux catégories : **vitesse** et **interactivité**. Parce que nous manipulions de grandes quantités de données, notre visualisation devait pouvoir se mettre à jour à la vitesse de l'éclair (ou au moins à une vitesse sans lag perceptible).

Notre application devait également avoir l'interactivité souhaitée que nous avions imaginée pour l'utilisateur. Dans un scénario idéal, la bibliothèque inclurait déjà certaines de ces fonctions interactives que nous pourrions facilement intégrer, au lieu de devoir les écrire à partir de zéro.

Entrez [Bokeh](https://bokeh.pydata.org/en/latest/).

#### **À propos de Bokeh**

Bokeh est une bibliothèque principalement destinée à la création de visualisations dans le navigateur à partir de grands ensembles de données ou de flux de données. Vous créez ces visualisations en utilisant Python. Ensuite, l'API [JavaScript](https://bokeh.pydata.org/en/latest/docs/dev_guide/bokehjs.html) de Bokeh prend votre script Python et rend les graphiques ou les diagrammes en plus de gérer les interactions UI dans le navigateur.

Vous pouvez également choisir d'utiliser le serveur Bokeh pour gérer le flux de vos données. Dans la documentation de Bokeh 0.12.13, il est indiqué : "Cette capacité à synchroniser entre Python et le navigateur est le principal objectif du serveur Bokeh."

![Image](https://cdn-media-1.freecodecamp.org/images/1*mPrYowYw8llGQq_xW5AQEQ.png)
_[Image source](https://bokeh.pydata.org/en/latest/_images/bokeh_serve.svg" rel="noopener" target="_blank" title=")_

#### **Avantages**

Bokeh est magique pour de nombreuses raisons. Il rend d'abord en utilisant WebGL avec un repli sur HTML5 Canvas, fournit plusieurs outils intégrés pour interagir avec les graphiques, gère des ensembles de données extrêmement volumineux, et finalement, crée quelque chose qui peut être mis sur le web immédiatement.

La capacité de naviguer entre Python et JavaScript est également incroyablement puissante pour les graphiques car Python vous permet de tirer parti de structures de données utiles et d'outils d'analyse de données, tandis que JavaScript traduit les données manipulées en visualisations compatibles avec les navigateurs.

#### **Inconvénients**

Un inconvénient de Bokeh, cependant, est qu'il est limité dans le degré d'interactivité qu'une visualisation peut avoir. Bokeh vous permet de "graphiquer" dans le sens plus conventionnel—il offre une toile 2-D, de type grille avec des axes comme base. Et c'est bien, car souvent c'est ce dont l'utilisateur a besoin et veut. Les utilisateurs expérimentés de Bokeh peuvent créer de très belles choses (voir des exemples [ici](https://bokeh.pydata.org/en/latest/docs/gallery/lorenz.html)).

Mais si je voulais créer une visualisation qui sort des caractéristiques conventionnelles d'un graphique, comme simuler des forces entre des atomes et déplacer les atomes, je ne sais pas comment je pourrais accomplir cela dans Bokeh.

Bokeh est également destiné au développement en Python, pas en JavaScript. Ci-dessous se trouvent des exemples de graphiques à barres dans Bokeh utilisant Python. C'est super simple et propre.

_Graphique à barres Bokeh utilisant Python (via Jupyter Notebook)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*36USbyrMq0o8Ou8dcfyjUg.png)

Avant de commencer à utiliser Bokeh, nous avons pris la décision consciente de scripter en JavaScript au lieu de Python parce que toute notre application web était et est construite sur un framework JavaScript. Aucune de la documentation de Bokeh n'est en JavaScript (elle est en Python, comme vous pourriez vous y attendre), et tenter de comprendre l'API JavaScript s'est avéré difficile.

Si vous travaillez avec des glyphes de bas niveau, il est vrai que tout ce qui est possible en Python est possible en JavaScript avec Bokeh. **Cependant, si vous commencez tout juste à apprendre les deux langages comme c'était mon cas, la traduction de la syntaxe entre les deux n'est pas intuitive.**

De plus, il y a des limitations aux API JavaScript de haut niveau `Bokeh.Charts` et `Bokeh.Plotting`—certaines sont obsolètes, d'autres rendent très difficile la modification des caractéristiques du graphique. Les exemples ci-dessous sont mes tentatives de création de graphiques Bokeh en JavaScript.

_Graphique à barres de bas niveau Bokeh utilisant JavaScript_

_Graphique à barres de haut niveau Bokeh utilisant l'API JavaScript Bokeh.Charts_

Plus d'informations sur le développement en JavaScript avec Bokeh [ici](https://bokeh.pydata.org/en/latest/docs/user_guide/bokehjs.html). Comme vous pouvez le voir, JavaScript avec la bibliothèque de Bokeh perd les lignes de code plus simples que nous avons observées lors du développement avec Python. Je pense qu'il a fallu environ une heure de bidouillage dans la console pour ajouter un contour blanc aux barres et un titre dans mon graphique de haut niveau, ce qui réitère ma lutte pour naviguer en dehors des limites de l'API JavaScript `Bokeh.Charts` lorsque vous voulez changer les détails visuels du graphique.

Enfin, il y a **plus de documentation et d'utilisation active d'autres bibliothèques de graphiques**, comme [D3.js](https://d3js.org/) ou [three.js](https://threejs.org/), par rapport à Bokeh. Avec plus de contributeurs et d'utilisateurs actifs d'une bibliothèque, vient une probabilité plus élevée de trouver la solution dont vous avez besoin pour corriger un bug spécifique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*v0QlVyNIuLNCZHvwe_86GA.png)
_**61 501** résultats pour D3 sur Stack Overflow_

![Image](https://cdn-media-1.freecodecamp.org/images/1*DOmNQfwWqYUhrCPZW63YAg.png)
_**24 126** résultats pour three.js sur Stack Overflow_

![Image](https://cdn-media-1.freecodecamp.org/images/1*-B_U3GwyOuEUqmjY5JGgTw.png)
_**3 405** résultats pour Bokeh sur Stack Overflow_

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

### Pourquoi nous sommes passés à D3

Nous étions donc coincés. Nous avions atteint le point de "cette bibliothèque convient à nos besoins en quelque sorte mais c'est une douleur de continuer à faire des choses en JavaScript et peut-être que nous allons atteindre le plafond un jour lorsque nous réaliserons que nous avons besoin de quelque chose qui n'est pas disponible dans Bokeh pour le moment." Cool.

Entrez [D3](https://d3js.org/).

Notre préoccupation initiale avec D3 était qu'il rendrait nos visualisations trop lentement, étant donné les expériences passées avec le rendu des SVG dans le navigateur avec de grandes quantités de données. Nous savions également que la courbe d'apprentissage pour D3 était significativement plus élevée que celle de Bokeh.

Mais nous étions toujours optimistes étant donné la popularité de D3, la quantité infinie d'applications D3 magnifiquement documentées, et notre attitude "Get Sh*t Done"... alors nous avons décidé de l'essayer quand même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8GeqmkIGqTkOhDpZKh4vhQ.png)
_Get Shit Done par [Tyler Somers](https://dribbble.com/shots/1685729-Get-Shit-Done" rel="noopener" target="_blank" title=")_

#### **À propos de D3**

D3.js est une bibliothèque JavaScript qui met l'accent sur la liaison de données. Elle vous donne le pouvoir unique de générer des éléments dans le DOM et de lier des données aux éléments simultanément. Avec une bibliothèque entièrement pilotée par les données, vous pouvez ajouter des éléments dynamiquement lors de l'ajout ou de la suppression de points de données et effectuer des transitions entre les ensembles de données. D3 offre également plus de contrôle sur l'esthétique et l'interactivité du résultat final, ce qui signifie que vous pouvez vous permettre de créer les visualisations les plus [bizarres/merveilleuses](https://mviz.omid.al/).

#### **Avantages**

À notre grande surprise, les visualisations D3 que nous avons créées avec nos ensembles de données étaient très fluides. Nous avons rapidement réalisé que D3 est structuré spécifiquement pour un rendu rapide, malgré les tableaux massifs que nous passions à la bibliothèque.

Au lieu de passer les points de données un par un et de générer le SVG respectif, ce qui peut être assez fastidieux, D3 vous permet de lier l'ensemble de votre jeu de données à vos SVG avant qu'ils n'existent. Les SVG sont ensuite générés en rafale et associés à leur point de données respectif en une seule fois.

C'est comme un chef dans la cuisine qui reçoit une liste de commandes en une fois et peut préparer la nourriture dans un ordre qui élimine le temps d'attente inutile, plutôt que d'attendre toujours de recevoir la prochaine commande après avoir préparé un plat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3jhabDKWXszldm7yKjg9g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zQNWTtb8B0IqkpxbK6JZKQ.png)
_Visualisation de la liaison de données aux éléments DOM de l'explication de Mike Bostock sur les [sélections D3](https://bost.ocks.org/mike/selection/" rel="noopener" target="_blank" title=")_

Le meilleur aspect de D3 est qu'il offre de nombreuses opportunités pour des interactions fluides et des transitions entre les ensembles de données. Parce que notre objectif ultime était et est d'autonomiser l'utilisateur, nous voulions créer une visualisation qui inviterait un individu à interagir avec elle.

D3 est également destiné au développement JavaScript. Il n'y aurait plus de "creusement sous le capot" de l'API JavaScript comme nous le faisions avec Bokeh. L'exemple de graphique à barres que j'ai créé en utilisant BokehJS précédemment dans cet article est montré ci-dessous en utilisant la bibliothèque D3.

_Graphique à barres D3_

Oui, il y a des lignes de code plus complexes par rapport au code requis pour un graphique Bokeh. Cela a pris plus de temps et d'énergie à apprendre. Mais vous avez un contrôle complet sur _chaque_ petit détail de votre graphique, et tout est documenté quelque part en ligne (probablement via le créateur, [Mike Bostock](https://bl.ocks.org/mbostock)). C'est plutôt génial.

Enfin, il y a eu une utilisation extensive de D3 ces dernières années pour visualiser les [élections américaines de 2017](http://fivethirtyeight.com/features/election-update-women-are-defeating-donald-trump/), [le mouvement des populations de réfugiés](http://www.therefugeeproject.org/), [les taux de vaccination des nourrissons pour l'OMS](https://hi.stamen.com/visualizing-infant-vaccination-rates-for-the-world-health-organization-d484789505b1), et d'innombrables autres tendances et histoires. Par conséquent, D3 a attiré une quantité **significative** d'exposition et d'attention, ce qui conduit à plus d'utilisateurs actifs et à de nouvelles façons d'utiliser la bibliothèque chaque jour.

Lors du choix d'une bibliothèque pour le long terme et en gardant à l'esprit que vos coéquipiers devront également l'apprendre éventuellement, il est absolument crucial de considérer la communauté actuelle et future de contributeurs de la bibliothèque. Une bibliothèque avec une communauté continuellement prospère est idéale, et D3 semble favoriser ce type de communauté.

#### **Inconvénients**

La courbe d'apprentissage initiale est plus élevée pour D3 par rapport à Bokeh, en supposant que vous développez en Python avec Bokeh. JavaScript est plus verbeux que Python. Cependant, si comme nous vous prévoyez de développer en JavaScript, cela vaut la peine de se frayer un chemin à travers les tutoriels D3.

Il est **difficile** de comprendre comment fonctionnent les sélections, ce que signifient .enter() et .exit(), et la _magie_ qui se produit avec une simple ligne de code (.transition() quelqu'un ?). MAIS — une fois que vous avez compris la structure unique de D3 qui suppose que les choses existent avant qu'elles n'existent, les possibilités sont infinies.

En fin de compte, les avantages de D3 ont surpassé l'effort et le temps d'apprentissage, et nous avions un pressentiment que le passage à D3 serait un bon investissement à long terme.

### Conclusion

Voilà ! Nous utilisons et apprenons toujours activement D3 alors que nous intégrons la bibliothèque dans notre application et notre équipe. Bien que le fait que nous avancions avec D3 ne signifie pas que nous n'utiliserons pas Bokeh pour une autre application à l'avenir. Il y a des avantages et des inconvénients à chaque bibliothèque de graphiques, et il est important de réfléchir constamment pour déterminer si vous devez continuer avec votre bibliothèque actuelle ou commencer à explorer d'autres options.

Avant de choisir une bibliothèque de graphiques, connaissez vos besoins spécifiques et n'ayez pas peur de plonger tête la première dans les eaux inexplorées des bibliothèques de graphiques avec ces besoins à l'esprit. Si quelque chose ne fonctionne pas du premier coup, essayez quelque chose de nouveau qui semble prometteur.

Il s'agit d'explorer, de documenter et de faire le point avec vous-même et vos coéquipiers pour continuer à faire évoluer le projet de manière productive.

En avant !

![Image](https://cdn-media-1.freecodecamp.org/images/1*9r5Z2AM84c4LHIHx7Hs0eA.png)
_Source [ici](https://www.xkcd.com/688/" rel="noopener" target="_blank" title=")_

Si vous avez des commentaires, des corrections, des suggestions, ou si vous voulez simplement discuter, n'hésitez pas à m'envoyer un e-mail à mandicai@gmail.com. Vous pouvez trouver certains de mes travaux à [http://mandilicai.com/](http://mandilicai.com/).