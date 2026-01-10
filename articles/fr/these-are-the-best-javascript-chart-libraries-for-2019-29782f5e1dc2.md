---
title: Voici les meilleures bibliothèques de graphiques JavaScript pour 2019
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T21:37:15.000Z'
originalURL: https://freecodecamp.org/news/these-are-the-best-javascript-chart-libraries-for-2019-29782f5e1dc2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Aom0Yz2zVQZdBiiByborCA.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Voici les meilleures bibliothèques de graphiques JavaScript pour 2019
seo_desc: 'By Arthur Puszynski

  First, a brief history:

  With data collection and use continuing to increase exponentially, the need to visualize
  this data is becoming more important. Developers seek to consolidate millions of
  database records into beautiful char...'
---

Par Arthur Puszynski

D'abord, un bref historique :

Avec la collecte et l'utilisation des données continuant à augmenter de manière exponentielle, le besoin de visualiser ces données devient de plus en plus important. Les développeurs cherchent à consolider des millions d'enregistrements de base de données en de beaux graphiques et tableaux de bord que les humains peuvent interpréter rapidement et intuitivement.

La technologie de visualisation des données a continué à s'améliorer au cours de la dernière décennie et de nombreuses bibliothèques de graphiques avancées sont désormais disponibles pour les consommateurs. Au début des années 2000, la génération de graphiques était dominée par des graphiques bitmap d'images côté serveur. Des plugins tels que Flash et Silverlight offraient une expérience de graphique plus interactive, mais avec un lourd tribut sur la vitesse de téléchargement, la durée de vie de la batterie et les ressources système.

Avec l'explosion de l'utilisation des mobiles et des tablettes, les plugins n'étaient plus supportés sur les principales plateformes et les développeurs ont dû passer à des technologies client ouvertes qui pouvaient fonctionner partout. En même temps, l'avènement des écrans à très haute résolution et le zoom plus courant grâce aux gestes tactiles ont mis en avant les graphiques vectoriels indépendants de la résolution.

Nous entrons dans l'ère actuelle de la visualisation des données, dominée par JavaScript et SVG (Scalable Vector Graphics). Les graphiques fonctionnent désormais sur tous les navigateurs, sans plugins spéciaux, supportent l'interactivité et les animations et ont une apparence nette même sur les appareils à la résolution la plus élevée. En examinant plus de 50 bibliothèques de visualisation, ces 9 produits se sont distingués :

#### [**D3.js**](https://d3js.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/S6EaFX5GX8yUIDvllrXDeYc2fONsQL-8jMUL)

D3.js est une bibliothèque JavaScript graphique très extensive et puissante. Elle vous permet de lier des données arbitraires à un Document Object Model (DOM), puis d'appliquer des transformations pilotées par les données au document.

D3 va bien au-delà des bibliothèques de graphiques typiques, incluant de nombreux autres petits modules techniques tels que les axes, les couleurs, les hiérarchies, les contours, les facilités, les polygones, et plus encore. Tout cela rend la courbe d'apprentissage assez raide.

Essayer de créer un graphique simple peut être compliqué. Tous les éléments, y compris les axes et autres éléments de graphique, doivent être définis explicitement. De nombreux exemples montrent comment CSS peut être utilisé pour styliser les éléments de graphique. Aucune fonctionnalité basée sur les graphiques ne s'applique automatiquement. Si vous voulez entrer dans les détails et utiliser la créativité pour contrôler pleinement chaque élément, c'est le meilleur choix. Travailler contre la montre pour répondre aux exigences d'un projet de visualisation de données, ce n'est peut-être pas le meilleur choix en partant de zéro.

D3.js peut être un bloc de construction pour une bibliothèque de graphiques. Les développeurs ont utilisé D3 pour faciliter l'utilisation de solutions de graphiques qui le consomment, comme NVD3.

D3.js est open source et gratuit à utiliser.

#### [**JSCharting**](https://jscharting.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/hTX6DIAPWYObB4LCQ--zfJIRrW1q85peGy3A)

La bibliothèque de graphiques JSCharting supporte un grand nombre de types de graphiques, y compris les cartes, les diagrammes de Gantt, les graphiques boursiers et d'autres qui nécessitent souvent des bibliothèques séparées pour être utilisés. Elle inclut des cartes intégrées de tous les pays du monde et une bibliothèque d'icônes SVG. Une suite de micro-graphiques autonomes peut être rendue dans n'importe quelle étiquette de graphique ou dans n'importe quel élément div d'une page. Les contrôles UI (UiItems) sont également inclus, permettant des graphiques interactifs plus riches. Pour contrôler les données ou les variables de visualisation en temps réel est facile et les graphiques peuvent être exportés aux formats SVG, PNG, PDF et JPG.

La galerie est divisée en types de graphiques et en échantillons de fonctionnalités. Le style des graphiques est poli et donne des graphiques d'apparence propre. Les visuels globaux offrent une expérience de graphique propre et professionnelle.

Les échantillons inclus utilisent un objet de configuration pour personnaliser les graphiques. Les paramètres pour créer et contrôler les types de graphiques sont très simples à utiliser. Peu de paramètres de propriété sont nécessaires pour spécifier des types de graphiques plus complexes et JSCharting a des valeurs par défaut fortes et dynamiques, ce qui signifie qu'il tente de choisir les meilleurs paramètres pour les scénarios automatiquement.

La documentation inclut de nombreux tutoriels et des descriptions complètes des propriétés de l'API. De nombreuses propriétés incluent des exemples d'utilisation et des liens vers des échantillons.

JSCharting est gratuit pour un usage non commercial et personnel et propose également des options de licence commerciale qui incluent tous les types de graphiques et produits pour un seul frais.

#### [**Highcharts**](https://www.highcharts.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/2syqkeQ3kQi2mhDSFfsqV57jiG810QWR7b7G)

Highcharts est une bibliothèque de graphiques JavaScript populaire utilisée par de nombreuses grandes entreprises du monde. Les graphiques sont générés en utilisant SVG et reviennent à VML pour la compatibilité ascendante jusqu'à IE6/IE8. Les graphiques de démonstration démontrent un ensemble de fonctionnalités assez riche mais ne sont pas visuellement impressionnants. La documentation générale inclut des tutoriels pour de nombreux sujets pertinents et la documentation de l'API est complète.

Le graphique utilise des options de configuration pour créer des graphiques et l'API est facile à utiliser.

Highcharts est gratuit pour un usage non commercial et personnel. Une licence commerciale est requise pour d'autres usages et les graphiques boursiers, les cartes et les diagrammes de Gantt sont licenciés séparément.

#### [**amCharts**](https://www.amcharts.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/g5AOK1ltx8xdH2JFXp3iw7fcZAYJ5pthfFdG)

amCharts a récemment sorti leur version 4 qui ajoute un moteur d'animation SVG puissant permettant de créer des scènes semblables à des films.

Les graphiques de démonstration ont une très belle apparence. La plupart des démonstrations offrent un certain nombre de palettes et une interface utilisateur de curseur pour ajuster les variables de graphique en temps réel. La documentation inclut de nombreux tutoriels et des descriptions complètes des propriétés de l'API.

Créer un graphique semble légèrement différent de l'approche basée sur la configuration, et utilise plutôt une API plus déclarative. Cela nécessite légèrement plus de code pour configurer les graphiques mais offre une meilleure expérience de complétion de code.

amCharts propose une licence gratuite avec des graphiques marqués et des licences payantes pour d'autres usages.

#### [**Google Charts**](https://developers.google.com/chart/)

![Image](https://cdn-media-1.freecodecamp.org/images/fPisdLR3HjGBrfbCAzc75uXc5IO9wsf2wj-f)

Les graphiques Google sont puissants et faciles à utiliser.

Les graphiques exemples ont une apparence propre et sont faciles à regarder. La galerie et la galerie étendue montrent de nombreux types de graphiques, mais en appuyant sur le menu hamburger, on découvre plus de types (comme le calendrier) qui ne sont pas montrés dans ces listes de galerie.

Chaque type de graphique a un tutoriel dédié avec des exemples en direct. Les tutoriels incluent du code pour les fonctionnalités associées et des listes d'API. C'est une expérience agréable pour commencer avec une nouvelle bibliothèque de graphiques.

Les graphiques sont personnalisés en utilisant l'objet d'options de configuration. Les ensembles de données sont peuplés en utilisant une classe DataTable qui peut être consommée par tous les graphiques. Chaque type de graphique a des options uniques listées dans les tutoriels spécifiques au type. La nomination des propriétés est standardisée et de nombreuses options fonctionnent sur tous les types.

Les graphiques Google sont gratuits, mais il y a un avertissement. C'est un service web et il ne peut pas être hébergé localement. Dans le passé, Google a retiré des API, donc si votre utilisation est critique, vous voudrez peut-être choisir une autre option.

#### [**ZingChart**](https://www.zingchart.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/7UxG9uthgcsC-fYPf0GEXgJY6A3X6C187ggy)

ZingChart offre de nombreux types de graphiques et s'intègre avec Angular, React et d'autres frameworks. Il a un ensemble de fonctionnalités solide avec de nombreuses options de personnalisation.

Les graphiques de démonstration montrent une gamme de thèmes de style, certains ayant meilleure apparence que d'autres, mais les options pour les styliser selon les besoins sont là. Les démonstrations ne montrent pas tous les types de graphiques disponibles.

La documentation inclut des tutoriels pour tous les types disponibles, un bon nombre de fonctionnalités et une liste complète de l'API.

ZingChart utilise des options de configuration pour personnaliser les graphiques. Les exemples incluent de nombreux paramètres de propriété tels que le style de police. Ceux-ci peuvent gêner la compréhension des paramètres requis pour un graphique donné.

ZingChart peut être utilisé gratuitement avec un branding. Des licences payantes sont disponibles pour un usage sans branding.

#### [**FusionCharts**](https://www.fusioncharts.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/b7k3uk0H59ImJz2wBVa6zBRCx8J6euicz1ZW)

FusionCharts existe depuis de nombreuses années, commençant comme un plugin de graphique basé sur Flash. C'est une bibliothèque de visualisation de graphiques robuste. Elle supporte de nombreux formats de données, y compris XML, JSON et JavaScript, fonctionne dans les navigateurs modernes et est compatible avec les versions antérieures jusqu'à IE6. De nombreux frameworks JavaScript et langages de programmation côté serveur sont également supportés.

La galerie de graphiques inclut un grand nombre d'exemples et ils ont une apparence visuelle propre.

La documentation inclut de bonnes descriptions de l'API et des exemples de chaque type de graphique. Les propriétés de configuration sont regroupées par tâches et fonctionnalités de graphique.

Les graphiques sont créés en utilisant des options basées sur la configuration et sont relativement faciles à utiliser. La liste des propriétés peut être longue lorsque l'on creuse plus profondément dans l'API. Toutes les propriétés de configuration sont peu profondes, comme {chartLeftMargin, showAlternateHGridColor}. Cela semble être une tentative d'améliorer la complétion de code.

FusionCharts est gratuit pour un usage personnel avec un branding de graphique. Des licences payantes sont disponibles pour un usage sans branding et commercial.

#### [**KOOLCHART**](https://www.koolchart.com/)

![Image](https://cdn-media-1.freecodecamp.org/images/3iWJw51bCnMDw4QKpjP-0k-lZsoX0DUNnzL5)

KoolChart est une bibliothèque de graphiques JavaScript basée sur la toile HTML 5. Un produit de mappage et de grille est également disponible.

Leur nouvelle version 5 inclut un ensemble de fonctionnalités plus interactif et un style mis à jour. Les visuels sont propres et modernes. L'utilisation de la toile offre de meilleures performances au détriment d'être basée sur le raster.

Les exemples utilisent une chaîne XML pour appliquer les options de graphique, ce qui semble moins pratique que d'autres approches. Ces options ressemblent à du HTML5 mais sont définies via une chaîne JavaScript.

L'API est bien documentée avec des exemples de graphiques pour chaque propriété. Un manuel PDF de 173 pages est également disponible.

Une période d'essai de deux mois est disponible pour l'évaluation. Une licence est requise après l'expiration de la période d'essai.

#### [**Chart.js**](https://www.chartjs.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/ewHuQvOha7Jgzn2rLM8jzoz5caFNhU7IuQCw)

Chart.js est une bibliothèque JavaScript open source supportant 8 types de graphiques. C'est une petite bibliothèque js de seulement 60 ko. Les types incluent les graphiques en ligne, les graphiques à barres, les graphiques en aire, les radars, les camemberts, les bulles, les nuées de points et les graphiques mixtes. Une série temporelle est également supportée. Elle utilise l'élément canvas pour le rendu et est réactive au redimensionnement de la fenêtre pour maintenir la granularité de l'échelle. Elle est compatible avec les versions antérieures jusqu'à IE9. Des polyfills sont disponibles pour fonctionner avec IE7 également.

Les visuels des exemples ont une apparence assez moderne et incluent des animations initiales lors du dessin pour la première fois. Il s'anime en douceur lors de l'ajout de séries ou de points de données en temps réel. Les options de graphique peuvent être modifiées après et l'appel à une fonction update() redessine le graphique.

Le code source des exemples n'est pas montré dans la galerie du site web mais est disponible dans le dépôt GitHub. Les options de configuration sont utilisées pour créer et modifier les graphiques. L'API des options est propre et intuitive.

La documentation est complète et inclut des tutoriels avec l'API des propriétés et des extraits de code.

Chart.js est une bibliothèque open source et gratuite à utiliser pour un usage personnel et commercial, ce qui est un plus. Le nombre limité de types peut être un problème pour des exigences de tableau de bord plus avancées.

#### **Conclusion**

L'écosystème des bibliothèques de graphiques JavaScript a considérablement évolué au cours de la dernière décennie. Aujourd'hui, il existe un grand nombre de produits de graphiques qui répondent à des exigences très diverses, servant une large gamme de projets à travers des centaines de types de graphiques. La plupart des bibliothèques fournissent une version d'essai gratuite ou marquée, vous permettant d'évaluer l'efficacité des graphiques avec vos propres données, chargement et complexité de projet.

Il est facile pour la plupart des bibliothèques de graphiques de gérer des ensembles de données simples et curatés et des visualisations statiques. Cependant, les graphiques peuvent ne pas toujours gérer les choses en douceur lorsque des données dynamiques du monde réel sont visualisées. Plus de travail peut être nécessaire pour ajuster et arranger les éléments afin que les graphiques apparaissent correctement et ce réglage manuel peut se briser lorsque de nouvelles données dynamiques sont visualisées.

Pour sélectionner la meilleure solution de graphique JS pour vos besoins uniques, je recommande de tester vos propres données contre quelques-unes des bibliothèques listées ci-dessus pour garantir un ajustement idéal pour vos projets actuels et futurs.