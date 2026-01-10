---
title: Comment les animations fonctionnent dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-17T14:08:45.000Z'
originalURL: https://freecodecamp.org/news/how-react-native-animations-work
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/poster.jpg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: Comment les animations fonctionnent dans React Native
seo_desc: 'By Mehul Mohan

  React Native is a great framework that lets you create cross platform mobile applications.
  It''s especially helpful if you''re a web developer and want a fast, low cost solution
  to develop native mobile applications that work on both And...'
---

Par Mehul Mohan

React Native est un excellent framework qui vous permet de créer des applications mobiles multiplateformes. Il est particulièrement utile si vous êtes un développeur web et que vous souhaitez une solution rapide et peu coûteuse pour développer des applications mobiles natives qui fonctionnent à la fois sur Android et iOS. Bonus : vous n'avez pas à dépenser des sommes folles pour des équipes iOS, Android et web séparées. 

Cela non seulement réduit vos coûts, mais vous permet également de partager une grande partie de votre base de code entre les trois builds (Android, iOS et Web), ce qui facilite les modifications et le déploiement des mises à jour. 

React Native vous permet également de travailler très près du système d'exploitation réel, ce qui est important pour les tâches critiques en termes de performance comme les animations. 

Les animations sont une partie intégrante de toute application car elles la rendent interactive et plus attrayante pour l'utilisateur final. Mais souvent, en travaillant avec des animations, vous pouvez avoir l'impression de travailler avec une boîte noire. 

Alors, apprenons comment les animations fonctionnent dans React Native. Vous pouvez commencer à apprendre les animations dans React Native à partir de zéro avec [cette playlist YouTube gratuite](https://www.youtube.com/playlist?list=PLYxzS__5yYQmdfEyKDrlG5E0F0u7_iIUo).

# L'API Animated

React Native expose une API appelée Animated. Elle se compose de nombreuses choses merveilleuses comme des valeurs animables, des animations de type spring/timing, et des événements. Mais nous ne sommes pas ici pour discuter de l'API – je vais laisser cela à la [documentation officielle](https://reactnative.dev/docs/animations#__docusaurus) et à ma [playlist YouTube](https://www.youtube.com/playlist?list=PLYxzS__5yYQmdfEyKDrlG5E0F0u7_iIUo). Ils font un bien meilleur travail pour couvrir cela pour vous.

Ce que nous voulons discuter ici, en fait, c'est comment React Native anime les éléments à l'écran et ce qui se passe sous le capot.

# Deux façons d'animer

Vous devriez savoir [comment React Native fonctionne sous le capot](https://www.freecodecamp.org/news/how-react-native-constructs-app-layouts-and-how-fabric-is-about-to-change-it-dd4cb510d055/) grâce à mon autre article. (Donnez-lui une lecture rapide si vous ne l'avez pas encore fait.) Puisque React Native utilise React et JavaScript, il existe précisément 2 façons d'effectuer des animations à l'écran. 

Tout d'abord, clarifions un fait. React Native construit des vues natives réelles à l'écran, et non celles rendues via des navigateurs web intégrés comme Ionic. En raison de cela, si vous souhaitez animer une vue de quelque manière que ce soit, cela doit finalement être fait sur la vue native. 

JavaScript doit communiquer avec le système d'exploitation d'une manière ou d'une autre pour indiquer que la vue doit être mise à jour. JavaScript s'exécute dans un thread différent de celui de l'interface utilisateur (thread principal), et seul ce thread de l'interface utilisateur peut mettre à jour les vues. Ainsi, JS doit utiliser le pont fourni par React Native pour sérialiser et communiquer ces données au système d'exploitation.

## Faire le travail en JS et mettre à jour la vue native

Cette approche signifie que vous prenez une vue qui est déjà visible à l'écran de l'utilisateur, et vous travaillez sur ce qui doit être fait pour sa prochaine position dans le thread JavaScript. Les étapes ressemblent à peu près à ceci :

1. L'animation commence
2. JavaScript exécute la fonction `requestAnimationFrame` - une fonction qui **essaie** de s'exécuter à 60 appels/seconde (60 FPS)
3. JavaScript calcule la prochaine position/opacité/transformation/ce que vous animez sur la vue.
4. JavaScript sérialise cette valeur et l'envoie via le pont.
5. À l'autre extrémité du pont, Java (Android) ou Objective C (iOS) désérialise cette valeur et applique les transformations données sur la vue mentionnée.
6. Le cadre est mis à jour à l'écran.

Avez-vous vu ce qui s'est passé là ? Aucune des étapes ne ré-affiche réellement un composant React Native. Cela signifie que l'API Animated "contourne" en fait la philosophie de React de ne pas muter les variables "state". 

La bonne nouvelle : cela est en fait utile dans le cas des animations car ce serait beaucoup trop lent et mauvais pour les performances si nous laissions React ré-afficher un composant 60 fois par seconde !

C'est bien et bon, mais il y a un problème très fondamental ici. JavaScript est mono-thread. Ainsi, la nature asynchrone de JavaScript ne fonctionne pas ici car les animations sont une tâche liée au CPU. Examinons les avantages et les inconvénients de cette approche.

### Avantages

1. Vous pouvez avoir des animations très sophistiquées écrites en JS et visibles sous forme d'animations natives.
2. Plus de contrôle sur l'état de l'animation

### Inconvénients

1. Pénalité de performance énorme si votre thread JavaScript est super occupé.
2. Si le pont est occupé, il y a une diminution des performances lorsque l'OS/JS veulent communiquer entre eux.

Cet inconvénient est un gros inconvénient, soyons honnêtes. Il y a une vidéo plus bas dans l'article qui vous montre en fait ce problème en temps réel. Vous verrez comment JS gâche complètement les animations lorsque le thread JavaScript devient occupé.

### Pourquoi les animations JS laguent-elles ?

Les animations réalisées en JS commenceront à laguer lorsque l'animation est en cours et que l'utilisateur (ou l'application) demande une autre action qui doit être gérée par le thread JS. 

Par exemple, imaginez qu'une animation est en cours. Cela signifie que JS est occupé à exécuter la fonction `requestAnimationFrame`. En supposant que les mises à jour ne sont pas trop lourdes, supposons qu'un utilisateur commence à appuyer sur un bouton à l'écran qui incrémente un compteur. 

Maintenant, avec `requestAnimationFrame` appelé fréquemment, votre arbre virtuel React est également ré-affiché encore et encore afin de tenir compte de l'augmentation du compteur. 

Les deux sont des tâches liées au CPU s'exécutant sur un seul thread, il y aura donc un impact sur les performances. `requestAnimationFrame` commencera à sauter des images en raison du travail supplémentaire effectué par le thread JS. 

Tout cela signifie que vous obtiendrez une animation très saccadée.

## Animations avec le pilote natif

Ne vous inquiétez pas, car React Native vous permet en fait d'exécuter des animations sur le pilote natif également ! Que veux-je dire par là, pourriez-vous demander ?

Eh bien, simplement, cela signifie que React Native décharge le travail d'animation du thread JS vers le thread UI (le système d'exploitation) et le laisse gérer l'animation de l'objet. Cela présente plusieurs avantages :

1. Le thread JS (et le pont React Native) est maintenant libre pour gérer d'autres tâches intensives comme les appuis répétés de l'utilisateur.
2. Les animations sont beaucoup plus fluides car il n'y a pas de surcharge de sérialisation/désérialisation et de communication via le pont.

Comment React Native y parvient-il ? Les développeurs de React Native vous permettent, en tant que développeur, de fournir une propriété appelée `useNativeDriver` sous forme de valeur booléenne lors de la construction d'un objet d'animation. 

Lorsque cette valeur est définie sur true, React Native, avant de démarrer l'animation, sérialise tout l'état de l'animation et ce qui doit être fait à l'avenir. Il le transfère ensuite une fois via le pont vers le système d'exploitation. 

À partir de ce moment, le code Java (Android) ou Objective C (iOS) exécute les animations au lieu que JavaScript calcule la prochaine image d'animation et envoie ces données encore et encore via le pont.

Cela accélère considérablement les animations et les animations s'exécutent plus fluidement, surtout sur les appareils bas de gamme. Regardons une démonstration vidéo des animations natives par rapport aux animations basées sur JS dans React Native :

%[https://www.youtube.com/watch?v=lsRf_PspjSs]

Dans ce cas, les étapes ressemblent à peu près à ceci :

1. L'animation commence
2. JS sérialise les informations d'animation et les envoie via le pont.
3. À l'autre extrémité, le système d'exploitation reçoit ces informations et exécute l'animation de manière native.

C'est tout ! Les animations sont beaucoup plus légères pour le thread JS maintenant. Plus de `requestAnimationFrame` s'exécutant sans fin.

Cependant, cette méthode a sa propre part d'avantages et d'inconvénients. 

### Avantages :

1. Animations plus rapides
2. Thread JS non bloquant
3. Pont moins encombré

### Inconvénients :

1. Moins de contrôle sur les animations (JS ne peut pas voir ce qui se passe à l'écran une fois que l'animation "automatique" commence)
2. Moins de propriétés à manipuler - le pilote natif ne prend pas en charge toutes les propriétés à animer. Par exemple, `width` ou `height` ne sont pas animables de manière native, mais `opacity` et `transform` le sont.

Dans de nombreux cas, vous constaterez que vous pouvez contourner un ensemble différent d'animations en utilisant `useNativeDriver: true` pour créer un effet similaire qui ne peut pas être obtenu sans définir `useNativeDriver: false`. 

L'équipe React Native travaille à ajouter la prise en charge de plus de propriétés en ce moment, mais pour l'instant, je pense que cela fonctionne très bien.

## Conclusion

Cet article vous a montré comment les animations React Native fonctionnent réellement sous le capot et pourquoi elles sont belles. 

Que pensez-vous de cet article ? Dites-le-moi en me connectant sur mes comptes [Instagram](https://instagram.com/mehulmpt) et [Twitter](https://twitter.com/mehulmpt) ! Nouveau dans React Native ? Commencez à l'apprendre sur [codedamn](https://codedamn.com) - une plateforme pour les développeurs pour apprendre et se connecter !

Paix !