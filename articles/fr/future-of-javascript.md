---
title: Pourquoi JavaScript est le langage de programmation de l'avenir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-04T16:40:11.000Z'
originalURL: https://freecodecamp.org/news/future-of-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/jsposter.jpg
tags:
- name: ecmascript
  slug: ecmascript
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Pourquoi JavaScript est le langage de programmation de l'avenir
seo_desc: 'By Mehul Mohan

  JavaScript was the first programming language I picked up. Well, I actually started
  with HTML and CSS. Just like many other web developers, going with JavaScript was
  a no-brainer. This is simply because it blends so well with HTML and ...'
---

Par Mehul Mohan

JavaScript était le premier langage de programmation que j'ai appris. En fait, j'ai commencé avec HTML et CSS. Comme beaucoup d'autres développeurs web, choisir JavaScript était une évidence. Cela s'explique simplement par le fait qu'il se marie si bien avec HTML et CSS, et qu'il améliore même vos compétences en HTML/CSS. J'ai développé des applications et des jeux dans divers autres langages de programmation, notamment Java, Swift, C++, Dart. Mais la flexibilité que JavaScript offre est inégalée - même si cela peut être considéré comme mauvais pour les débutants car il donne beaucoup plus d'options que nécessaire pour accomplir une tâche simple.

Aujourd'hui, JavaScript est l'un des langages les plus puissants de la planète grâce à ses performances et son omniprésence.

Personnellement, je pense que JavaScript a le potentiel de s'imposer dans de nombreuses industries populaires comme le Machine Learning et l'analyse de données, où Python règne encore. Cela se produit même maintenant avec des outils comme Tensorflow.js !

Cependant, ce n'était certainement pas le cas pour JavaScript auparavant. Auparavant, c'était un langage faible et peu performant, et il était mal vu. JavaScript était pour les "perdants".

Mais ce n'est plus le cas. Voyons comment JavaScript a retourné la situation au cours des 10 dernières années, pourquoi il est devenu plus fort que jamais, et pourquoi il est là pour rester.

# V8 : La bête qui alimente JavaScript

V8 est en fait un moteur JavaScript. Qu'est-ce qu'un moteur JavaScript, pourriez-vous demander ? Un moteur JavaScript est un interpréteur qui exécute le code JavaScript. Un moteur JavaScript peut être implémenté comme un interpréteur standard, ou un compilateur juste-à-temps (JIT) qui compile JavaScript en bytecode sous une certaine forme.

V8 est le moteur JIT JavaScript et WebAssembly open source haute performance de Google, écrit en C++. Il est utilisé dans Chrome et dans Node.js, entre autres. V8 peut fonctionner de manière autonome, ou peut être intégré dans n'importe quelle application C++.

C'est le logiciel qui optimise grandement votre code JS et le convertit en code machine pour que le CPU l'exécute. Certaines des tâches que V8 gère sont :

1. Collecte des déchets
2. Compilation en code machine
3. Mise en cache en ligne
4. Compression des pointeurs
5. et bien plus d'optimisations

En fait, la compression des pointeurs est une technique très récente dans V8 pour améliorer l'optimisation de la mémoire sans affecter les performances. Si vous êtes un geek, vous pouvez en savoir plus sur la façon dont elle est implémentée sur le blog officiel de V8.

Le point à retenir est que vous pouvez écrire du JavaScript et dormir tranquille la nuit car votre code JS est entre de très bonnes mains.

# Écosystème et communauté matures

JavaScript possède l'un des écosystèmes les plus matures - sinon LE plus mature - qu'un langage de programmation puisse avoir. La communauté pour JavaScript est vaste, et la barrière à l'entrée est extrêmement basse.

Vous pouvez lancer un navigateur (trouvé sur 100 % des ordinateurs personnels), ouvrir la console, et vous trouverez un moteur JS qui attend que vous exécutiez du code ! Ce n'était jamais le cas avec d'autres langages de programmation de cette complexité.

Comme si la vaste communauté ne suffisait pas, nous avons les systèmes de packages `npm` et `yarn`. Vous le nommez et il y a un package pour cela sur le registre `npm` - tout, de la création de chaînes aléatoires à la gestion des flux et des tampons en JavaScript. Il y a un dicton très célèbre parmi les développeurs JavaScript :

> Ce qui peut être fait en JavaScript, sera finalement fait en JavaScript

C'est drôle, mais en secret, je crois cela.

Si vous entrez en tant que débutant, il y a très peu de chances que vous rencontriez un problème que personne n'a rencontré auparavant. Cela est dû au fait que toutes les erreurs possibles pour les problèmes simples de JavaScript ont probablement déjà été posées et archivées sur des sites comme Stack Overflow.

Des frameworks et des bibliothèques comme React, Angular et Vue ouvrent la voie à la manière dont les applications futures doivent être construites. Ils changent la perspective vers une programmation déclarative plutôt qu'impérative, le "quoi" plutôt que le "comment". Cela permet aux développeurs de créer des applications de qualité sans se soucier du code sous-jacent à haute performance.

## Omniprésence

JavaScript est présent sur :

1. Front end (Navigateurs)
2. Back end (Node, Deno)
3. Android/iOS (React Native, NativeScript, etc.)
4. Bureau (Electron)
5. Hybride (Ionic)

Qu'est-ce qui rend cela possible ? Les moteurs JS comme V8 sont écrits en C/C++ et peuvent même être compilés sur des systèmes embarqués ! Pour les autres plateformes, comme les navigateurs sont toujours présents (comme sur Android/iOS), ils sont livrés avec un moteur JS qui peut ensuite être utilisé pour exécuter n'importe quel code JS, même pour les applications natives dans le cas de React Native.

## Fonctionnalités de pointe et avancées

Les normes JavaScript sont dirigées par la communauté ECMA-262 TC39, et ces personnes sont rapides ! ECMAScript publie une nouvelle norme de JavaScript chaque année (voir les nouvelles fonctionnalités d'ECMAScript2020 !). En tant que développeur, vous pouvez même demander que de nouvelles fonctionnalités soient ajoutées au langage.

Par exemple, voici quelques fonctionnalités de pointe en attente qui pourraient être ajoutées à JavaScript dans un avenir proche :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-04-at-10.03.59-PM.png)

Vous pouvez trouver toutes les propositions ici : [TC39 Proposals](https://github.com/tc39/proposals).

## JavaScript est RAPIDE et SCALABLE

Bien sûr, rien ne bat vraiment C/C++/Rust, mais JavaScript est rapide - dans le sens où V8 peut générer un code hautement optimisé en surveillant l'exécution de votre code, en retardant les parties de l'exécution qui ne sont pas utilisées, et en optimisant les segments de code qui sont utilisés encore et encore. Surtout lorsqu'il est comparé à ses concurrents les plus proches comme Python. Avec les avancées de V8, il devient encore plus performant et efficace en mémoire.

JavaScript (Node) est hautement scalable (avec des sur-ensembles comme TypeScript). Fonctionnant sur une architecture mono-thread, les gens critiquent souvent Node pour son manque d'environnement multi-thread, mais la réalité est que cela n'a pas beaucoup d'importance.

La manière dont vous scalez les applications Node n'est pas similaire à la manière dont vous scaleriez une application multi-thread. Node signifie littéralement "nœud" - un seul nœud dans un arbre de processus. Node est scalable en exécutant plusieurs instances et en gérant le cluster.

JavaScript mène le modèle de programmation asynchrone piloté par événements de l'industrie, et n'a pas besoin de threads pour scaler. Au lieu de cela, des processus Node individuels pourraient être engendrés pour gérer et utiliser le cœur CPU complet. Plus d'informations sur le scaling de Node plus tard !

## Conclusion

J'adore JavaScript, et en l'utilisant, j'ai créé une plateforme de développement pour des développeurs comme vous. Là, vous pouvez non seulement apprendre JavaScript, mais aussi divers autres langages comme C, C++, Java, Node, Python, et plus encore ! [Rejoignez ici gratuitement](https://codedamn.com) et apprenez avec d'autres développeurs directement depuis votre navigateur !

JavaScript est là pour rester et dominer l'industrie cette décennie. Êtes-vous d'accord ? Dites-le-moi sur mes comptes [twitter](https://twitter.com/mehulmpt) et [Instagram](https://instagram.com/mehulmpt) - restons en contact !