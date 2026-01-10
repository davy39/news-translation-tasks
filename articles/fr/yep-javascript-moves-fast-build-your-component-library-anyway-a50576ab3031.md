---
title: Oui, JavaScript évolue rapidement. Construisez votre bibliothèque de composants
  quand même.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T13:05:16.000Z'
originalURL: https://freecodecamp.org/news/yep-javascript-moves-fast-build-your-component-library-anyway-a50576ab3031
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JFxS_dW4owpFE2ZvJyk1Zw.png
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Oui, JavaScript évolue rapidement. Construisez votre bibliothèque de composants
  quand même.
seo_desc: 'By Cory House

  Here’s a question I’ve heard a few times recently:


  “What if we create a component library in React/Vue/Angular/whatever and a new component
  technology replaces it?”


  That’s not a question of if. It’s a question of when. These technolog...'
---

Par Cory House

Voici une question que j'ai entendue plusieurs fois récemment :

> « Et si nous créons une bibliothèque de composants dans React/Vue/Angular/autre et qu'une nouvelle technologie de composants la remplace ? »

Ce n'est pas une question de si. C'est une question de quand. Ces technologies sont devenues extrêmement populaires, mais elles ne sont pas la fin du jeu. Comme toutes les technologies, quelque chose de mieux finira par arriver et les remplacer.

Mais ce fait est largement irrelevant. Établir une bibliothèque de composants réutilisables pour votre entreprise aujourd'hui reste absolument crucial.

Voici pourquoi.

### Allez plus vite aujourd'hui

Les composants réutilisables aident votre équipe à aller plus vite en créant des abstractions de plus haut niveau. Les composants éliminent la fatigue décisionnelle en appliquant de manière programmatique une approche standardisée. Prenez simplement l'exemple d'un composant `TextInput` pour formulaire avec des opinions fortes.

Il peut éliminer toutes les décisions suivantes :

1. Dois-je mettre l'étiquette au-dessus de l'entrée ou à côté ?
2. Dois-je afficher les erreurs de validation à droite ou en dessous de l'entrée ?
3. De quelle couleur doit être l'erreur ?
4. Comment dois-je marquer les champs obligatoires ?
5. Dois-je valider les champs obligatoires au blur ou à la soumission ?
6. Combien d'espacement dois-je placer entre l'étiquette et l'entrée ?

La liste continue. Ce ne sont pas des questions que vos designers et développeurs devraient se poser chaque fois qu'ils créent un nouveau formulaire.

### Appliquer la cohérence

Les composants réutilisables appliquent la cohérence de l'interface utilisateur. Votre entreprise compte probablement de nombreux développeurs. Pourtant, votre travail est de construire une application qui **semble avoir été construite par un seul développeur.**

Pour cela, il est crucial d'utiliser des composants réutilisables. Copier/coller n'est pas un modèle de conception. Si les designers et les développeurs ont la liberté de recommencer à zéro encore et encore, votre application deviendra rapidement un patchwork de looks, de sensations et de technologies différents.

### Améliorer les performances

Dans une application rendue côté client, chaque fois que vous utilisez un composant, vous améliorez les performances. Pourquoi ? Parce que cela minimise la taille du bundle de l'application et son empreinte mémoire. Utiliser un composant une deuxième fois **ne nécessite aucun téléchargement supplémentaire et presque aucune mémoire supplémentaire.**

Sans bibliothèque de composants, votre équipe est très susceptible d'inclure du JavaScript en double qui résout les mêmes problèmes de manière légèrement différente, ce qui alourdira le bundle et ralentira les performances. Pire encore, ils sont susceptibles de prendre une autre bibliothèque concurrente et ainsi obliger les utilisateurs à télécharger plusieurs bibliothèques complètes qui font la même chose.

### Moins de maintenance

Plus de code entraîne plus de maintenance. Plus de maintenance entraîne des coûts plus élevés et plus de personnes, ce qui crée une surcharge de communication supplémentaire qui vous ralentit encore plus. Les composants réutilisables minimisent la quantité de code que vous devez créer et maintenir aujourd'hui.

### Mises à jour plus faciles plus tard

Enfin, oui, éventuellement, la technologie de composants que vous utilisez aujourd'hui deviendra obsolète. Mais en créant une bibliothèque de composants réutilisables aujourd'hui, vous minimisez la surface à mettre à jour plus tard.

Il est beaucoup plus facile de migrer une application soigneusement composée car vous pouvez remplacer les composants existants un par un. Ce n'est pas si facile lorsque votre application est un patchwork de technologies et de modèles différents. Les composants réutilisables minimisent la surface que vous devrez mettre à jour plus tard.

### Faible investissement

Une bibliothèque de composants ne nécessite pas réellement beaucoup de travail. Par exemple, si vous choisissez React, vous n'avez pas besoin (et généralement ne devriez pas) de partir de zéro. Il existe [littéralement des dizaines de bibliothèques de composants matures](https://github.com/enaqx/awesome-react#components) parmi lesquelles choisir et des centaines de composants autonomes également.

Utilisez une bibliothèque de composants populaire comme point de départ et ajustez-la à vos besoins. Faites-moi confiance, cela ne doit pas prendre longtemps et les avantages sont significatifs.

Alternativement, vous pourriez choisir de créer des composants CSS simples comme base. Un exemple de cette approche est [Stacks de StackOverflow](https://stackoverflow.design). L'avantage de cette approche est double :

1. Si vous passez à une nouvelle technologie à l'avenir, la base CSS simple que vous utilisez en arrière-plan dans vos composants JavaScript peut être réutilisée.
2. Si votre entreprise utilise actuellement plusieurs approches de composants telles que React, Angular et/ou Vue, alors cette approche CSS peut être utilisée comme base pour toutes.

L'inconvénient ? Vous devez construire vos composants à partir de zéro afin qu'ils utilisent votre base de composants CSS simple.

Ma préférence ? Utilisez une bibliothèque de composants JavaScript existante comme base pour minimiser la quantité de code que vous devez écrire pour commencer.

### Résumé

Ne laissez pas l'innovation rapide de JavaScript vous effrayer à l'idée d'investir dans une bibliothèque de composants réutilisables pour votre entreprise. Oui, la technologie d'aujourd'hui sera éventuellement remplacée, mais le changement est la seule constante dans la technologie. Pour toutes les raisons ci-dessus, les composants réutilisables valent la peine d'être adoptés aujourd'hui.

Vous cherchez plus de détails sur la façon de faire cela ? J'ai récemment publié « [Création d'une bibliothèque de composants React réutilisables](https://app.pluralsight.com/library/courses/react-creating-reusable-components/table-of-contents) » sur Pluralsight. ([essai gratuit](https://help.pluralsight.com/help/free-trial-10-days-andor-200-minutes))

### Vous cherchez plus sur React ? ⚔️

J'ai écrit [plusieurs cours sur React et JavaScript](http://bit.ly/psauthorpageimmutablepost) sur Pluralsight.

![Image](https://cdn-media-1.freecodecamp.org/images/ukD8krGR7M8AnnK7lzjsuLRcFnAOUcCPEIZr)

Cory House est l'auteur de plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur [Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel, MVP Microsoft, et forme des développeurs logiciels à l'international sur les pratiques de développement front-end. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).