---
title: Atténuer les monolithes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-05T05:03:40.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-deckee-tech-mitigating-monoliths-2a8dcb8603a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sF9GxDUdfNJr7UbmxP64Sw.jpeg
tags:
- name: Devops
  slug: devops
- name: Microservices
  slug: microservices
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Atténuer les monolithes
seo_desc: 'By Ian Belcher

  How we pivoted our tech stack to a service-based, developer experience-focused design

  This article documents the problems we experienced with monolithic architecture,
  our transition to a new service-based system, and the results we hav...'
---

Par Ian Belcher

#### Comment nous avons pivoté notre stack technique vers une conception basée sur les services, axée sur l'expérience des développeurs

Cet article documente les problèmes que nous avons rencontrés avec l'architecture monolithique, notre transition vers un nouveau système basé sur les services, et les résultats que nous avons observés depuis sa mise en œuvre.

# Le problème

En 2015, nous avons lancé un produit minimum viable — un [monolithe](https://en.wikipedia.org/wiki/Monolithic_application), construit sur un CMS fonctionnant dans une stack LAMP. Le CMS en question est respecté mais a atteint un point de déclin dans son cycle de vie, arguably en raison d'une mauvaise gestion.

Les coûts liés au développement et à la livraison de notre projet avaient commencé à augmenter de manière exponentielle :

* Notre seule option réalisable était de scaler verticalement et il était beaucoup plus difficile de mettre en œuvre une haute disponibilité ou des systèmes redondants. Les mises à niveau continues de notre serveur hôte principal étaient accompagnées d'une augmentation des coûts unitaires de nos ressources.
* Nous étions exclusivement liés à un langage et à ses performances. PHP est excellent pour certaines tâches, mais pas pour _toutes les tâches_. En fait, il échoue considérablement pour certaines choses où d'autres langages excellent.

![Image](https://cdn-media-1.freecodecamp.org/images/vJfBq96Xgl07jwErzY-lGLeOJox6-ltenZ2c)

* La conception interne du CMS fonctionnait mal selon les normes d'aujourd'hui. Certains hacks de base ont amélioré cela de plusieurs ordres de grandeur, mais le site fonctionnait toujours mal en raison d'un certain nombre de décisions de conception en amont sous-optimales.
* Alors que nous continuions à développer le projet à partir de ses racines en tant que produit minimum viable, nous avons atteint un point de complexité où plus d'ajouts ou de changements de fonctionnalités étaient accompagnés d'un facteur de coût constamment croissant.
* En raison de la complexité croissante, l'expérience des développeurs était mauvaise. De nombreux développeurs attestent que, une fois qu'un projet dépasse un certain niveau de complexité, le bon développement de qualité diminue en raison des changements dans un domaine ayant des conséquences imprévues dans d'autres domaines apparemment sans rapport.
* L'utilisation d'un CMS signifiait que notre produit était presque entièrement dépendant de la qualité d'une équipe de [développeurs en amont](https://en.wikipedia.org/wiki/Upstream_(software_development)) d'une petite entreprise privée. Les décisions qu'ils prenaient nous impactaient. En effet, nous externalisions de nombreuses tâches importantes à cette entreprise, comme notre sécurité.
* Le couplage serré dans le système CMS principal nous empêchait d'essayer de nouvelles technologies. Par exemple, une interaction directe avec la base de données pouvait être trouvée dans presque _toutes_ les parties de la base de code, supprimant notre capacité à changer ou à mettre à jour la technologie de la base de données.

Nous avons atteint deux conclusions importantes : notre stack technique monolithique continuerait à nous empêcher d'atteindre nos objectifs à court terme, et nos objectifs à long terme deviendraient rapidement impossibles d'un point de vue produit et d'un point de vue capital humain.

Comme toute bonne organisation apprenante, nous n'allions pas refaire ces erreurs. Après de nombreuses heures de réflexion supplémentaire, nous sommes arrivés à cette hypothèse :

> La conception monolithique facilite, impose et est en quelque sorte elle-même un anti-pattern.

Un bon développement consiste en une séparation claire des préoccupations. Un bon développement consiste en une classification élevée et une encapsulation bien conçue des données et des fonctionnalités.

Le [God class](https://en.wikipedia.org/wiki/God_object) anti-pattern et la [Loi de Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter) nous disent que nous devrions limiter les connaissances dans un domaine spécifique à ce qui est requis. Alors pourquoi ces principes sont-ils souvent mis en œuvre uniquement au niveau du langage ?

![Image](https://cdn-media-1.freecodecamp.org/images/XNPWJXnob5kiTywos6EaNFmOEodjlRk5L0u0)

De manière _abstraite_, les systèmes monolithes sont une 'God class'. Ils fonctionnent comme un seul contrôleur lourd — un objet global qui est injecté lors de l'instanciation avec toutes les dépendances de votre système. Ils imposent des contraintes telles que les choix du système d'exploitation ou du langage, où certaines tâches sont beaucoup mieux adaptées à d'autres configurations.

Par définition, un monolithe a une connaissance complète de l'ensemble du système. Par conséquent, dans la plupart des cas, un développeur travaillant sur un monolithe nécessite également une connaissance complète pour travailler sur ce projet de manière efficace et efficiente.

Le développeur a besoin de cette connaissance pour prendre des décisions correctes qui concernent la séparation nette des responsabilités entre différentes zones de la base de code. Lorsque toutes vos classes fonctionnent 'côte à côte', il est facile de prendre la mauvaise décision quant à ce qui doit être fait et où.

![Image](https://cdn-media-1.freecodecamp.org/images/VDleTZEZcncRW6cT0i7iSqdKHyMTkj752T4y)

### Notre solution

Sur la base de notre hypothèse, nous avons conclu que le système actuel était irréparable, et qu'une reconstruction complète selon un modèle de conception de service produirait un système qui éviterait les divers problèmes que nous avons identifiés.

Nous avons créé une matrice décrivant ce que nous voulions réaliser avec le nouveau système :

![Image](https://cdn-media-1.freecodecamp.org/images/WmKdhMuAyiTjUKSII2fYfujFqYIywl-6YiJc)

**L'expérience des développeurs (DX)** définit la première moitié de notre matrice. Le calibre souhaité des développeurs que nous voulons sont ceux qui recherchent une opportunité de travailler sur des choses qu'ils aiment et qui les challengent. Pour créer une excellente DX, notre base de code devait fournir un écosystème que les développeurs talentueux trouveraient engageant, tout en évitant les pièges que nous avions rencontrés dans la conception monolithique.

**La livraison du produit** façonne la seconde moitié de notre matrice. La phrase '_le contenu est roi_' est toujours vraie, mais la performance d'un site web est également devenue un facteur majeur, tant du point de vue de l'utilisateur que des moteurs de recherche. Favoriser une excellente DX était important, mais il était _impératif_ que le nouveau site web performe mieux pour nos utilisateurs.

Voici une ventilation des quatre principaux composants de la matrice et de ce que nous visions à réaliser.

#### Agilité

> La complexité tue. La complexité aspire la vie des utilisateurs, des développeurs et de l'informatique. La complexité rend les produits difficiles à planifier, construire, tester et utiliser. La complexité introduit des défis de sécurité. La complexité cause de la frustration chez les administrateurs. Et avec le temps, à mesure que les produits logiciels mûrissent — même avec les meilleures intentions — la complexité est inévitable. **— [Ray Ozzie](https://en.wikipedia.org/wiki/Ray_Ozzie)**

> Solution : Réduire la complexité = coût financier plus bas, meilleure DX, courbes d'apprentissage plus basses.

La complexité au sein d'un système se comporte comme un virus. Plus il y a de complexité présente, plus elle grandit. Réduire et séparer les parties complexes du système empêche la croissance de la complexité dans d'autres zones.

La conception basée sur les services peut mettre le virus en quarantaine. Un monolithe facilite la propagation de la complexité. (Lors du développement initial du nouveau système, [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) a servi de bon rappel de ce fait).

Lorsque le code est simple, il est plus facile de le rendre efficace et performant dans ce qu'il fait et plus agréable à travailler. L'« art » du développement devient le résultat, pas le code lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/Hyxsm1FpFY-c3Jrij8satF87eSLlwsn7LBxI)

Séparer les zones de préoccupation en limites de niveau système (ce que font les services) signifie que les développeurs n'ont plus besoin de connaître l'ensemble du système pour travailler efficacement dessus. Ils reçoivent une interface définie (par exemple, une API HTTP, une socket ou un message AMQP) au _niveau système_, pas au niveau du langage, et peuvent se voir attribuer une responsabilité réelle pour ce service.

Cette séparation signifie qu'un développeur à qui l'on donne la responsabilité d'un service peut effectivement changer la technologie sous-jacente (comme le langage, le système d'exploitation ou la technologie de persistance utilisée) sans que les autres membres de l'équipe le sachent. Cela permet des essais de performance et des plongées profondes et évite le besoin de former toute l'équipe pour tenir compte des changements.

La réduction de la complexité et la ségrégation qui résultent de la conception de services créent une base de code avec un facteur d'agilité élevé. Les nouveaux développeurs peuvent commencer à commiter dès leur premier jour, car la lecture et la compréhension de l'ensemble de la base de code au niveau des services impliquent généralement quelques centaines de lignes de code.

#### Stabilité

> La plupart des logiciels aujourd'hui sont très similaires à une pyramide égyptienne avec des millions de briques empilées les unes sur les autres, sans intégrité structurelle, mais simplement réalisées par la force brute et des milliers d'esclaves. **— [Alan Kay](https://en.wikipedia.org/wiki/Alan_Kay)**

> Solution : Minimiser et atténuer les dépendances = moindre exposition à la volatilité de l'industrie et aux ruptures, capacité de gestion accrue et meilleure DX

La volatilité et le taux de changement dans l'industrie du logiciel surpassent la plupart des autres industries, pourtant la plupart des gens dans l'industrie du logiciel choisissent d'accepter ces risques plutôt que de les atténuer.

Un certain nombre de ruptures à grande échelle résultant d'un manque d'atténuation des changements en amont se sont déjà produites cette année (voir [ici](https://medium.com/@azerbike/i-ve-just-liberated-my-modules-9045c06be67c) et [ici](https://medium.com/@xzyfer/why-node-sass-broke-your-code-and-semver-1b3e409c57b9)).

La conception de services favorise une plus grande séparation, spécificité et l'utilisation appropriée des dépendances. Cela permet une intégration planifiée des changements en amont — pas seulement lorsque votre CI se casse.

L'utilisation de code tiers (surtout avec les flux de travail standard des packages tels que npm et al.) est la même chose que de donner aux développeurs en dehors de votre équipe un accès en écriture à votre base de code sans les vérifications normales telles que les PR ou les revues. L'inclusion de code tiers doit être justifiée, soigneusement choisie et ensuite validée. Une meilleure gestion des dépendances signifie que votre équipe peut se concentrer davantage sur la construction, pas sur la rétro-ingénierie.

#### Évolutivité

Au niveau sysops, il est bien connu que la conception de services permet une évolutivité plus gérable par rapport aux monolithes. Il est courant pour les équipes de migrer de la conception monolithique pour cette raison.

Ce qui n'est pas si apparent avant cette transition est la réduction des coûts unitaires des ressources qui se produit avec la conception de services, même sur des systèmes qui n'ont pas besoin de scaler avec la demande.

De nombreux hôtes ont des coûts unitaires de ressources plus élevés pour les machines plus grandes (c'est-à-dire que 80 $ achèteront 8 Go 4 cœurs 80 Go si vous achetez une instance, ou 8 Go 8 cœurs 240 Go si vous achetez huit instances de 10 $).

![Image](https://cdn-media-1.freecodecamp.org/images/bCEOAUGVxsNHkV8t0Rg26x9pkK0WZHx1OzVv)

Cette réduction des coûts s'accompagne de l'avantage d'une fiabilité plus élevée, car la conception de services offre une meilleure portée pour la gestion de l'état. Par exemple, si un service plante, votre système entier ne tombe pas en panne — tout continue et ce service est redémarré et réajouté à votre cluster.

#### Vitesse du site

Une erreur très courante a été commise sur notre précédent site monolithique. Notre couche de vue était divisée entre deux technologies différentes : les templates PHP côté serveur et JavaScript côté client. Dans ces circonstances, il y avait plusieurs processus de rendu qui devaient avoir lieu à la fois côté client et côté serveur pour chaque vue de page.

Cela ajoutait une tonne de complexité pour les développeurs et ralentissait également considérablement le site.

> Solution : Mettre en œuvre une conception logicielle classique client-serveur, rendre le client autonome et utiliser le serveur uniquement pour la persistance.

D'un point de vue modèle-vue-contrôleur, la mise en œuvre d'une conception logicielle classique client-serveur signifie que votre couche de vue est très bien définie et encapsulée dans une seule zone de préoccupation.

De grands frameworks front-end sont devenus disponibles ces dernières années, ce qui permet de faire cela simplement et facilement.

Sur la plupart des sites web, presque tout ce qui est nécessaire pour afficher une page est livré de manière répétée (structure HTML, CSS, JavaScript) et le serveur agit généralement comme la partie qui remplit les données dans la structure HTML. Il est plus logique de livrer les exigences statiques une fois, puis de laisser le client remplir le HTML avec les données.

### Ce que nous avons appris jusqu'à présent

En interne, nous pensons avoir exceptionnellement bien livré sur les quatre composants de notre matrice. **Dans de futurs articles, j'explorerai chacun d'eux séparément en plus de détails et partagerai quelques métriques**. En attendant, voici quelques points clés que nous avons tirés du processus :

#### Construisez un cirque, pas un orchestre

Un monolithe nécessite que toute votre équipe travaille dans le même espace de code en même temps de manière coordonnée. Imaginez un orchestre : une erreur de n'importe quel membre affectera la performance de toute l'équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/T6A9NNwzL9VuCeQvOW1eKmy33lhHDziA4zQU)

Au lieu de cela, faites en sorte que votre production technique donne à vos développeurs l'espace dont ils ont besoin pour faire ce qu'ils font de mieux. La conception de services vous permet de créer un ensemble de 'numéros' bien exécutés et isolés.

#### Pensez comme un courtier en banque, pas comme un oiseau jardinier

Les dépendances en amont, le code tiers et les outils peuvent avoir des retours rapides mais viennent toujours avec une multitude de risques implicites, tandis que l'écriture de votre propre code 'adapté à l'usage' vous donnera plus d'efficacité et des niveaux de risque plus bas. Continuer à ramasser et à collecter des dépendances comme un oiseau jardinier augmente votre exposition à ces risques.

Au lieu de cela, pensez comme un courtier en banque et ne choisissez que les 'actions' les plus sûres avec de bons 'retours' pour limiter et atténuer votre exposition partout où c'est possible.

#### Les services agissent de la même manière que les classes bien définies

Le comportement d'un service est synonyme d'une classe au sein d'une base de code monolithique. Ils ont une interface publique, ils sont construits avec leurs dépendances requises et encapsulent leurs propres données et contrôlent leur accès.

Cependant, contrairement aux classes qui fonctionnent côte à côte, il est plus difficile pour un développeur de simplement changer la conception d'une interface pour répondre à ses besoins dans un contexte donné. Cette contrainte favorise une conception plus forte, centrée sur l'interface, ce qui conduit à un code de plus haute qualité et plus prévisible.

#### Le rendu côté serveur est l'inverse de la pratique typique du développement logiciel

Comme les applications qui fonctionnent sur votre ordinateur, console de jeu ou appareils, les serveurs agissent comme une couche de persistance centrale, pas comme un moteur de rendu. Le rendu de la vue côté serveur est un retour aux premiers jours de l'internet où les serveurs livraient des fichiers statiques. Cette pratique s'est propagée jusqu'au web d'aujourd'hui en raison des préférences de langage côté serveur des développeurs web.

Le navigateur web est une ressource intelligente, puissante, parfaitement scalable et gratuite. Utilisez son plein potentiel en produisant des pages web 'natives' qui fonctionnent dans le navigateur, pas sur votre serveur.

### Postscriptum

Si vous avez aimé cet article, veuillez cliquer sur le **bouton cœur** ci-dessous pour promouvoir une conversation plus approfondie.

Je suis CTO chez [Deckee](https://deckee.com) — nous aidons la communauté nautique à trouver, partager et discuter des choses qu'ils aiment.

Deckee est un employeur à action affirmative et nous sommes toujours à la recherche de développeurs audacieux et partageant les mêmes idées. Veuillez **inspecter** notre site pour plus de détails.