---
title: Qu'est-ce que l'analyse de données ? Une introduction à 30 000 pieds des concepts
  clés de l'analyse de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T21:17:10.000Z'
originalURL: https://freecodecamp.org/news/a-30-000-foot-introduction-to-data-analytics-and-its-foundational-components
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98b0740569d1a4ca1b7c.jpg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
seo_title: Qu'est-ce que l'analyse de données ? Une introduction à 30 000 pieds des
  concepts clés de l'analyse de données
seo_desc: 'By Adam Naor

  Data analytics is the process of inspecting, cleansing, transforming, and modeling
  data with the goal of discovering useful information.

  Data analytics is everywhere in the modern world: it helps inform the technology
  we use, how softwar...'
---

Par Adam Naor

L'analyse de données est le processus d'inspection, de nettoyage, de transformation et de modélisation des données dans le but de découvrir des informations utiles.

L'analyse de données est partout dans le monde moderne : elle aide à informer la technologie que nous utilisons, la manière dont les logiciels sont construits et les façons dont les produits sont développés.

Dans cet article, je vais couvrir les principes fondamentaux de l'analyse de données et comment les appliquer, en fournissant des exemples que vous pouvez déployer pour capturer et obtenir des informations significatives à partir de vos données.

Je vais également partager des exemples de la manière dont l'analyse de données est utilisée dans une variété de produits que vous connaissez probablement - l'optimisation de sites web, les applications de santé et de régime, l'agriculture et l'assurance, pour n'en nommer que quelques-uns.

Si vous partagez ma conviction que les données sont un guide qui peut informer vos décisions, cela mérite une étude plus approfondie.

## Questions d'exemple

Tout d'abord, voyez si vous pouvez répondre à ces questions. 

Si celles-ci ne vous viennent pas facilement, ne vous inquiétez pas. 

Je vais vous guider à travers l'apprentissage des bases de l'analyse de données afin que vous puissiez aborder chacune de ces questions avec confiance.

Le gestionnaire d'une opération de vente au détail sur Internet vendant un seul produit a constaté que les personnes qui visitent le site web achètent le produit 26 % du temps. Il a également découvert que le comportement des clients semble être indépendant.

Supposons que exactement 8 clients potentiels visitent le site chaque jour. Imaginez que le gestionnaire est sur un plan d'incitation qui lui paie 300 $ pour toute journée où le site génère trois ventes ou plus. Sinon, son salaire est de 100 $ par jour.

a. Quelle est la probabilité qu'il gagne les 300 $ n'importe quel jour au hasard ?

Réponse : ~35%

b. Quelle est la valeur attendue de son salaire n'importe quel jour au hasard ?

Réponse : 170 $

c. Le gestionnaire se voit offrir son choix entre deux régimes d'incitation alternatifs, selon lesquels il recevra soit (a) aucun salaire de base, mais une commission de 75 $ par vente, soit (b) un salaire fixe de 160 $ par jour, soit (c) le plan original décrit ci-dessus. 

Quel plan devrait-il choisir s'il veut maximiser la valeur attendue de ses gains ? 

Réponse : le plan original

## Les bases de l'analyse de données

Analysons comment penser aux données et bâtir sur ces apprentissages afin que vous puissiez répondre aux questions ci-dessus.

Le premier aspect de l'analyse de données que nous devons apprendre est qu'il existe différents types de données. Simple, non ?

C'est sûr.

Les données peuvent être catégorielles (genre, lieu, etc.) ou numériques (nombre de clients, utilisateurs actifs, etc.). 

Certaines données sont discrètes (c'est-à-dire le nombre de candidats postulant à un emploi) et d'autres données sont continues (nombre infini de résultats possibles).

Avant d'analyser les données, prenez un moment pour comprendre les types de données que vous avez. 

Avez-vous des données continues ou discrètes ? Vos données sont-elles catégorielles ou numériques ?

Après avoir répondu à ces questions, vous êtes prêt à approfondir.

Les données ont trois types principaux de caractéristiques :  


1. Les données peuvent être transversales. Cela signifie que les données sont un instantané d'un modèle ou d'une tendance. Un exemple est les résultats d'une enquête, comme le recensement national.
2. Les données peuvent être une série temporelle. Un exemple est mes scores de test, les salaires gagnés sur une période de temps, ou comment les entreprises mesurent et appliquent des remises tout au long de l'année.
3. Il y a aussi les données de panel. Un exemple est les données qu'une entreprise pourrait stocker dans un CRM. Les données de panel permettent plusieurs sujets et plusieurs points dans le temps. Comme le stockage devient de plus en plus bon marché, cette forme de données devient plus courante.

Maintenant que vous connaissez les types de données et les caractéristiques principales des données, je veux fournir un aperçu de la manière dont les données sont distribuées. 

## Dispersion : Comment les données sont organisées

Des informations uniques peuvent être glanées en regardant la forme de vos données.

Les données peuvent être organisées via une tendance centrale.

Pour ce faire, ordonnez votre ensemble de données du plus petit au plus grand. 

Lorsque les données sont soigneusement alignées, vous pouvez commencer à voir la dispersion pour la première fois. 

En voyant à quel point les données sont dispersées, vous pouvez calculer la plage des données en soustrayant la valeur la plus grande de la valeur la plus petite.

Si les données ont une grande plage (la distance entre les valeurs minimale et maximale), alors on dit qu'elles ont une dispersion élevée.

Enfin, vous pouvez regarder toutes les données disponibles ou un instantané d'un ensemble de données. Vous pouvez facilement calculer la moyenne, la médiane et le mode.

Pensez à l'expérience de pensée suivante. Si vous placez votre main dans un bocal de M&M's et en sortez un rouge, que pouvez-vous déduire ? 

Probablement pas grand-chose. Laissez-nous expliquer pourquoi en définissant les intervalles de confiance.

## Intervalles de confiance

Un intervalle de confiance est une plage de valeurs qui est susceptible d'inclure une valeur de population avec un certain degré de confiance. 

Habituellement, il est exprimé en pourcentage selon lequel la moyenne de la population se situe entre un intervalle inférieur et supérieur.

Retour à notre exemple de M&M's.

Imaginez que vous faites cette activité (tirer un M&M d'un bocal imaginaire) un nombre infini de fois et obtenez le même résultat. En d'autres termes, vous ne voyez que des M&M's rouges. Que pourriez-vous dire alors ?

Vous constateriez qu'il est _probable_ que seuls des M&M's rouges existent dans le bocal. C'est une conclusion valide. 

Remarquez que nous ne disons pas « aucun autre type de M&M's n'existe ». Plutôt, vous dites qu'il y a une forte probabilité que seuls des M&M's rouges existent dans le bocal. 

Chaque fois que vous retirez un M&M, votre degré de confiance augmente.

## Échantillonnage vs Mesure de la population entière

Lors de la collecte de données, vous pouvez regarder une population ou vous pouvez échantillonner la population. 

Devez-vous regarder chaque M&M dans le monde pour dire qu'ils sont tous d'une certaine couleur ? Ou pourriez-vous regarder un échantillon aléatoire et tirer la même conclusion ?

Au cœur, c'est de cela qu'il s'agit avec l'échantillonnage.

Une population d'échantillonnage est la sélection d'un sous-ensemble (un échantillon statistique) d'individus au sein d'une population statistique pour estimer les caractéristiques de la population entière. 

Votre objectif ultime peut être de voir à quelle fréquence des événements se produisent ou combien de types de résultats apparaissent dans une distribution.

## Tout mettre ensemble : Échantillonnage et Valeur attendue

Les observations sont essentielles pour l'analyse de données car elles peuvent vous aider à répondre à des questions très spécifiques :  


1. À quelle fréquence les choses sont-elles susceptibles de se produire ?
2. Si vous avez certaines probabilités, quels sont les gains de cet événement se produisant (c'est-à-dire que vous serez payé si un certain événement se produit) ?  


Pour capturer la valeur attendue, vous devez connaître la probabilité d'un événement multipliée par le nombre de fois où l'événement se produit.

Les gains attendus peuvent augmenter à mesure qu'ils s'éloignent du point médian des données. Pensez à la probabilité de créer une entreprise très réussie. La plupart des entreprises ne font pas d'IPO. 

Mais pour celles qui le font, les gains sont très élevés. Lorsque j'ai commencé un site web pour aider les gens à travailler depuis chez eux, je pensais que les chances de succès étaient de 10 % au mieux.

Jeff Bezos a famously dit que les chances que Amazon soit un succès étaient de 30 %. 

Une mesure couramment utilisée de la dispersion (et donc de la probabilité d'un résultat) est l'écart-type, qui est simplement la racine carrée de la variance. 

La variance d'un ensemble de données est calculée en prenant la moyenne arithmétique des différences au carré entre chaque valeur et la valeur moyenne.

## Questions et réponses d'exemple

Cet article sert d'aperçu de haut niveau pour vous introduire aux composants fondamentaux clés de la statistique et de l'analyse de données.

Maintenant, essayez ces deux questions. 

Si vous pouvez les résoudre, c'est génial ! Pour les résoudre, pensez à la valeur attendue et aux gains.

Le concepteur et codeur de sites web John Bell aimerait déterminer s'il serait rentable de créer une entreprise de conception de sites web. 

John croit qu'il y a quatre niveaux possibles de demande pour ses services : 

* Très faible demande — 1 % des entreprises utiliseraient le service ; John perdrait 100 000 $.
* Faible demande — 5 % des entreprises utiliseraient le service ; John gagnerait 10 000 $.
* Demande modérée — 10 % des entreprises utiliseraient le service ; John gagnerait 25 000 $.
* Forte demande — 29 % des entreprises utiliseraient le service ; John gagnerait 75 000 $.

Sur la base des expériences passées en codage et en construction de sites web, John attribue les probabilités suivantes aux différents niveaux de demande :

```
P(très faible demande) = 0,20
P(faible demande) = 0,50
P(demande modérée) = 0,20
P(forte demande) = 0,10
```

(a) Établissez l'arbre de décision et calculez la valeur attendue de l'offre du service.

```
.2 * (-100,000) + .5 * (10,000) + .2 * (25,000) + .1 * (75,000) 
= $ -2,500
```

(b) Calculez la valeur attendue avec des informations parfaites pour le gain de John.

```
.5*100,000 + .2*25,000 + .1*75,000 = $17,500
```

En d'autres termes, John croit qu'il gagnera 17 500 $ s'il ouvre son entreprise de conception de sites web. 

Avec cette orientation prospective, John peut décider s'il veut passer à l'étape suivante ou chercher des voies alternatives pour ses compétences et son temps.

## Réflexions finales sur l'analyse de données

Cet article est une introduction et devrait vous aider à aiguiser votre appétit pour approfondir. 

L'apprentissage de l'analyse de données vous aidera à mieux comprendre les logiciels et comment construire des produits. Comme le scénario avec John ci-dessus, vous pouvez utiliser l'analyse de données pour prendre des décisions mieux informées et prospectives.

Vous pouvez prendre des risques et comprendre les probabilités de succès et d'échec. Vous pouvez utiliser le principe de comptage pour déterminer vos actions actuelles.

L'analyse de données vous aidera également à mieux comprendre comment la technologie transforme les environnements hors ligne et donc à devenir un consommateur plus réfléchit.

La gamme d'utilisations pour l'analyse de données est incroyablement large. Prenez un moment et demandez-vous quels domaines de la science, de la technologie, des affaires, des logiciels ou de la conception de produits vous trouvez les plus intéressants. 

Maintenant, conceptualisez comment l'analyse de données influence profondément tous ces domaines.

Pensez au corps humain.

Les produits de santé, les programmes de marketing de bien-être et les applications d'exercice utilisent tous l'analyse de données pour optimiser les exercices pour le corps humain sur la base des données que nous émettons (pensez : fréquences cardiaques, niveaux d'oxygène dans le sang, schémas de sommeil). 

Ces outils utilisent l'analyse de données pour évaluer les personnalisations en temps réel (échantillonnage), l'authentification biométrique et l'analyse des sentiments.

Pensez aux logiciels.

Les outils d'automatisation des flux de travail à faible code utilisent l'analyse de données pour des expériences prédictives et permettent aux développeurs de différents niveaux d'expérience de créer des applications avec une logique pilotée par modèle. Les modules de données sont prédéfinis. 

Tout comme avec les logiciels, l'éducation est transformée par l'analyse de données. L'apprentissage en ligne pour les écoles et les applications de codage pour les enfants s'appuient sur l'analyse de données pour la gestion des risques (quand les étudiants prennent du retard) et la rétention des contenus.

Pensez à la manière dont le risque est évalué.

L'échantillonnage est utilisé pour changer la manière dont les compagnies d'assurance évaluent les polices d'assurance. De plus en plus d'institutions financières et de sociétés d'assurance utilisent l'analyse de données pour évaluer la qualité du crédit, pour évaluer et commercialiser les contrats d'assurance, et pour automatiser l'interaction avec les clients.

Pensez à la conception de sites web.

Que vous souhaitiez ou non appliquer l'analyse de données pour construire la prochaine grande chose, l'analyse de données vous aidera à mesurer ce qui compte et à transformer les données en informations exploitables.

Pensez à l'agriculture.

Les cultivateurs de plantes high-tech comme JoyOrganics et TakeSpruce utilisent le suivi du cycle de la graine à la vente pour suivre les plantes à travers les étapes de la culture à la récolte à l'extraction. 

Les agriculteurs utilisent l'analyse de données pour trouver des signaux de rendements plus élevés et non corrélés et optimiser la croissance.

Pensez à la qualité de l'air intérieur et au traitement du langage naturel. 

Ou à la manière dont les logiciels CRM sont construits, ou comment les gens communiquent en temps réel. 

En bref, pensez au monde moderne. 

Tous ces produits utilisent l'analyse de données pour calculer les erreurs d'échantillonnage, les écarts-types et les régressions afin d'assurer la qualité des produits et la satisfaction des clients.

Mais avant de calculer ces statistiques plus compliquées, chaque entreprise ou domaine commence par des composants fondamentaux. Chaque domaine mesure la fréquence, la dispersion, les moyennes et les écarts-types. 

Sur ces blocs de construction, l'analyse de données peut transformer les données en informations exploitables.

Plus important encore, toutes ces industries utilisent l'analyse de données pour faire des compromis de type go/no et pour comprendre plus profondément comment les utilisateurs utilisent les outils et les produits qu'ils construisent.

En explorant ces sujets plus en profondeur, vous pouvez sans aucun doute adopter une mentalité de constructeur plus holistique et implacable.

Si ce n'est que pour cela, l'étude de l'analyse de données rend ce résultat digne d'intérêt.