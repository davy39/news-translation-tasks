---
title: Analyse de données appliquée – Comment utiliser le théorème de Bayes et d'autres
  concepts pour améliorer votre entreprise
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-24T21:36:59.000Z'
originalURL: https://freecodecamp.org/news/applied-data-analytics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fbd63f349c47664ed825300.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
seo_title: Analyse de données appliquée – Comment utiliser le théorème de Bayes et
  d'autres concepts pour améliorer votre entreprise
seo_desc: "By Adam Naor\nI have written about Data Analytics on freeCodeCamp before.\
  \ \nIn my previous posts I have provided examples and concepts tied to the foundations\
  \ of data analytics. And I discussed how you can use the frameworks of this discipline\
  \ to work ..."
---

Par Adam Naor

J'ai déjà écrit sur l'analyse de données sur freeCodeCamp.

Dans mes précédents articles, j'ai fourni des exemples et des concepts liés aux fondements de l'analyse de données. Et j'ai discuté de la manière dont vous pouvez utiliser les frameworks de cette discipline pour travailler sur des ensembles de problèmes dans plusieurs domaines académiques et professionnels.

Étant donné que la communauté freeCodeCamp est remplie de personnes qui aiment la technologie et veulent exploiter les logiciels et le matériel pour créer des produits utiles et intéressants, j'ai voulu approfondir l'analyse de données appliquée et comment elle peut vous aider professionnellement.

Plus précisément, je veux discuter de la manière de penser – et ensuite d'appliquer – l'analyse de données aux problèmes commerciaux lors de la création d'entreprises ou de produits.

Pour cet article, je me concentre sur seulement trois concepts fondamentaux :

1. Le théorème de Bayes
2. La régression vers la moyenne
3. Le ratio risque-rendement

## Comment appliquer le théorème de Bayes au World Wide Web

Examinons la construction de sites web et voyons ce que cela nous apprend sur le théorème de Bayes.

D'abord, un peu de contexte.

Pour de nombreux entrepreneurs internet, la construction d'un site web ou l'automatisation des e-mails sont les premières étapes pour tester une idée, recueillir des commentaires des utilisateurs et monétiser des produits.

Mais comment savoir quel type de site web construire ? Et comment savoir si votre site web ou vos programmes de marketing d'affiliation performant bien ?

L'analyse de données fournit des réponses directionnelles importantes.

Lors de la construction d'un site web ou d'un produit logiciel, il est utile d'être passionné. Mais la passion seule ne suffit pas pour obtenir des résultats réussis. La passion, associée aux données, peut débloquer de nouvelles perspectives et valeurs.

Jetez un coup d'œil à ce graphique de flux comportemental de Google Analytics pour un chatbot Wordpress. Que voyez-vous ?

![Image](https://lh3.googleusercontent.com/OESTKKmHh4BadRHGLyhRrR7SxBFq6FRTvlP4TVN7bBkPvSyNivTw4MSNS3q70hu1mvmDHSDdeEcSJfbmWZC_jDF5FcKblgDnPtUiiAVffvD3yWGa4nt3wkYoqWQcHblNk1a6LBHt)

Un concept critique en analyse de données est le théorème de Bayes. Il décrit la probabilité d'un événement, basée sur la connaissance préalable de conditions qui pourraient être liées à l'événement.

Par exemple, supposons que le risque qu'un utilisateur quitte mon site web est connu pour augmenter à mesure que l'utilisateur passe moins de temps sur la page d'accueil. Le théorème de Bayes permet d'évaluer plus précisément le risque qu'un individu quitte (en le conditionnant sur le temps passé sur la page d'accueil) plutôt que de simplement supposer que l'individu est typique de la population dans son ensemble.

Réfléchissez à cela un instant. Les implications pour la manière dont vous concevez et construisez des produits sont profondes.

En exploitant le théorème de Bayes, je peux mieux comprendre comment les utilisateurs passent du temps sur mon site et où et pourquoi ils sont susceptibles de partir.

Sans l'application de ce théorème, je pourrais examiner à tort tous les utilisateurs comme s'ils avaient les mêmes attributs – alors qu'en réalité, ce n'est pas le cas.

Un utilisateur qui passe plus de temps sur la page d'accueil est plus susceptible de passer plus de temps sur les pages de branche et donc d'être un meilleur client (dans le cas d'un site web que j'ai construit).

Défiez-vous d'appliquer le théorème de Bayes à votre apprentissage et travail actuels. En calculant les probabilités conditionnelles – et en utilisant le passé pour aider à guider l'avenir – que pouvez-vous faire différemment ? Ou mieux ?

## Régression vers la moyenne

Le deuxième concept fondamental de l'analyse de données que je trouve particulièrement pertinent pour la technologie et l'apprentissage des logiciels est la régression vers la moyenne. Ce concept existe partout – et, comme nous allons le discuter, c'est à la fois une bonne et une mauvaise nouvelle.

La régression vers la moyenne explique le phénomène qui se produit si un point d'échantillonnage d'une variable aléatoire est extrême (presque un point aberrant).

Les points futurs seront plus proches de la moyenne, ou de la moyenne, lors de mesures ultérieures.

Ce concept est très important lorsque l'on examine le trafic d'un site web, les ventes de commerce électronique, ou lors de la conduite de tests de qualité de produit.

Supposons que votre site web moyen est composé de X pages. Un ingrédient clé de votre succès sera la manière dont vos utilisateurs interagissent avec le contenu de vos pages. Et un facteur clé de cela est la réactivité et la rapidité de vos pages.


![Image](https://lh6.googleusercontent.com/yGqJiv-yP8OSfheFItbpzSfYTFymOi36z1GHfGKqnTc9iFNPv6CaFpswCNCekNRnMr8P-TRxKUGToak5tFBXTudrnnhBJMuRQDrjj6qcv2J3m341w_7t-BsVMZUiUa2bhsOvfnQd)

Dans Google Analytics (et d'autres logiciels d'analyse client pour mesurer les performances d'un site web), vous pouvez facilement mesurer votre temps de chargement moyen des pages.

Que vous attendriez-vous à ce qu'il se passe si l'une de ces pages s'ouvrait lentement – en neuf secondes – ou très rapidement – en 0,04 seconde ?

Sur la base des données, nous ne nous attendrions pas à ce que ces résultats aberrants se produisent à plusieurs reprises. En fait, nous nous attendons à ce que les points de données futurs soient plus proches de, ou égaux à, la moyenne.

Lorsque vous apprenez à coder ou à construire votre premier produit, assurez-vous de comprendre vos vraies moyennes. Si vous obtenez des données qui sont largement différentes, attendez-vous à ce que les données futures reviennent à la moyenne.

Cette connaissance peut vous aider à mieux comprendre l'avenir (parce que vous avez une idée de ce qui arrive) et, à ce titre, vous pouvez fixer vos attentes en conséquence.

## Ratio risque-rendement

Combien devriez-vous risquer pour un certain gain ? Le ratio risque-rendement est une mesure de rendement en termes de risque pour une période spécifique. Vous n'êtes peut-être pas intimement conscient de cette formule, mais je crois que vous devriez l'être.

Comment pouvez-vous construire un produit, faire un investissement dans une entreprise, ou solidifier les calendriers de lancement de votre logiciel sans une compréhension du risque et du rendement ?

On pourrait dire que vous ne pouvez pas.

Voici un exemple. Pour un site web, la majorité du trafic provient de la recherche organique, ou de l'optimisation pour les moteurs de recherche.

Cela signifie que le site web ne paie pas pour acquérir du trafic directement, mais qu'il est soumis aux caprices des algorithmes de recherche qui contrôlent le flux de visiteurs vers le site.


![Image](https://lh4.googleusercontent.com/AuiryshNihiRReIPTLBs8TvBtolVKlXFDSEFJzydb6WDnfgLxczNcHYrioCCP4VppmyiV6zLLknT7j0Mc6gUlttqxjE_gFz0m1xzO_YK2ys1sLPTtl_E-ZjPpF9Be6gW1oieIHs5)

Pensez-vous que ce site est surindexé sur la recherche ? Comment diversifieriez-vous le trafic pour obtenir des rendements similaires mais avec moins de risques ? Une façon est d'appliquer les principes de diversification, qui est une technique qui réduit le risque en allouant des ressources dans différentes catégories.

Si vous maximisez les rendements en investissant dans différents domaines qui réagiraient chacun différemment au même événement, votre site web (ou produit) peut réduire le risque tout en maintenant un fort potentiel de hausse.

## Tout rassembler : Appliquer l'analyse de données dans le monde réel

Comme je l'ai soutenu auparavant, l'analyse de données est le processus d'inspection, de nettoyage, de transformation et de modélisation des données dans le but de découvrir des informations utiles. Il existe de nombreux concepts qui méritent une plongée profonde dans ce domaine.

Lorsque vous pensez à appliquer l'analyse de données à votre travail – y compris la recherche, les défis de codage et les efforts de construction de produits – les plus impactants à comprendre et à appliquer sont le théorème de Bayes, la régression vers la moyenne et le ratio risque-rendement.

Peu importe si vous construisez une page de destination, un site web robuste, une application mobile ou des outils d'entreprise comme des logiciels d'engagement des employés. Les données sont vos amies.

Les données sont parmi les processus d'engagement contractuel les plus rapides et les plus rentables. Elles sont toujours présentes et prêtes à vous guider.

Si vous voulez construire de grands produits, vous aurez besoin de données. Vous aurez besoin de temps pour évaluer et utiliser ces données.

Et vous aurez besoin d'outils – comme ceux que fournit l'analyse de données – pour débloquer des perspectives et mieux servir vos utilisateurs.

C'est pourquoi l'analyse de données est importante à étudier, mais encore plus importante à appliquer en pratique.