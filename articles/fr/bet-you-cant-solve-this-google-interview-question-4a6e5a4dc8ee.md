---
title: Je parie que vous ne pouvez pas résoudre cette question d'entretien de Google.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-29T14:09:14.000Z'
originalURL: https://freecodecamp.org/news/bet-you-cant-solve-this-google-interview-question-4a6e5a4dc8ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9vrgCN2D53GLsxAHB_Xx4Q.png
tags:
- name: algorithms
  slug: algorithms
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Je parie que vous ne pouvez pas résoudre cette question d'entretien de
  Google.
seo_desc: 'By Kevin Ghadyani

  Breaking tough problems into small pieces.

  I wanted to see someone else’s take on software engineering and started binge watching
  TechLead on YouTube. I spent the next few days coming up with various solutions
  to an interview questi...'
---

Par Kevin Ghadyani

#### Décomposer les problèmes difficiles en petits morceaux.

_Je voulais voir le point de vue de quelqu'un d'autre sur l'ingénierie logicielle et j'ai commencé à regarder en boucle TechLead sur YouTube. J'ai passé les jours suivants à trouver diverses solutions à une question d'entretien qu'il a posée en travaillant chez Google._

### Cette vidéo m'a excité

TechLead a abordé une **question qu'il a posée dans plus de 100 entretiens chez** **Google**. Cela m'a donné envie de réfléchir à une solution en RxJS. Cet article va cependant passer en revue les méthodes traditionnelles.

Le vrai but de sa question est d'obtenir des informations de la part de l'interviewé. Va-t-il poser les bonnes questions avant de coder ? La solution va-t-elle s'intégrer dans les directives du projet ? Il note même que cela n'a aucune importance si vous obtenez la bonne réponse. Il veut comprendre comment vous pensez et si vous pouvez même comprendre le problème.

Il a parlé de quelques solutions, une qui était récursive (limitée par la taille de la pile), une autre qui était itérative (limitée par la taille de la mémoire). Nous allons examiner ces deux méthodes et plus encore !

### La question de TechLead

Dans sa question, il nous demande de prendre cette grille d'items et d'obtenir le compte du plus grand bloc contigu où toutes les couleurs sont les mêmes.

![Image](https://cdn-media-1.freecodecamp.org/images/8cutcgfaNmVt7vKWuMzsb8HBpeGqPQfpusw5)

![Image](https://cdn-media-1.freecodecamp.org/images/bfHFxc9XC9hALpkzPjx0ReJezLbhsOwKj5u9)

Quand j'ai entendu sa question et vu l'image, je me suis dit "oh, il faut que je fasse de la modélisation 2D d'image pour résoudre ça". Cela semble presque impossible à répondre pendant un entretien.

Mais après qu'il l'a expliqué plus en détail, ce n'est vraiment pas le cas. Vous traitez les données qui ont déjà été capturées, pas en analysant une image. Je réalise maintenant que l'image est en fait un contre-sens.

### Modélisation des données

Avant d'écrire du code, vous devez définir votre modèle de données. _Je ne peux pas insister assez sur ce point._ Avant de coder quoi que ce soit d'aussi avancé, déterminez d'abord avec quoi vous travaillez et rassemblez les exigences métier.

Dans notre cas, TechLead a défini beaucoup de ces exigences pour nous :

* Concept d'un carré coloré ou "nœud" comme nous l'appellerons.
* Il y a 10K nœuds dans notre ensemble de données.
* Les nœuds sont organisés en colonnes et en lignes (2D).
* Le nombre de colonnes et de lignes peut être inégal.
* Les nœuds ont des couleurs et un moyen de désigner les adjacences.

Nous pouvons également déduire plus d'informations de nos données :

* Aucun deux nœuds ne se chevaucheront.
* Les nœuds ne seront jamais adjacents à eux-mêmes.
* Un nœud n'aura jamais d'adjacences dupliquées.
* Les nœuds qui se trouvent sur les côtés et les coins manqueront d'une ou deux adjacences respectivement.

Ce que nous ne savons pas :

* Le ratio des lignes par rapport aux colonnes
* Le nombre de couleurs possibles.
* Les chances d'avoir une seule couleur.
* La distribution approximative des couleurs.

Plus vous êtes de niveau élevé en tant que développeur, plus vous saurez poser ces questions. Ce n'est pas une question d'expérience non plus. Bien que cela aide, cela ne vous rend pas meilleur si vous ne pouvez pas identifier les inconnues.

Je ne m'attends pas à ce que la plupart des gens identifient ces inconnues. Jusqu'à ce que je commence à travailler l'algorithme dans ma tête, je ne les connaissais pas toutes non plus. Les inconnues prennent du temps à identifier. C'est beaucoup de discussions et d'allers-retours avec les gens du métier pour trouver tous les problèmes.

En regardant son image, il semble que la distribution soit aléatoire. Il n'a utilisé que 3 couleurs et n'a jamais dit le contraire, donc nous ferons de même. Nous supposerons également qu'il est probable que toutes les couleurs soient les mêmes.

Puisque cela pourrait tuer notre algorithme, je vais supposer que nous travaillons avec une grille de 100x100. Ainsi, nous n'avons pas à traiter les cas particuliers de 1 ligne et 10K colonnes.

Dans un cadre typique, je poserais toutes ces questions dans les premières heures de la découverte des données. C'est ce qui intéressait vraiment TechLead. Allez-vous commencer par coder une solution aléatoire ou allez-vous essayer de comprendre le problème ?

Vous allez faire des erreurs dans votre modèle de données. Je sais que j'en ai fait en écrivant cet article pour la première fois, mais si vous planifiez à l'avance, ces problèmes seront beaucoup plus faciles à gérer. J'ai fini par devoir réécrire seulement de petites portions de mon code à cause de cela.

### Création du modèle de données

Nous devons savoir comment les données arrivent et dans quel format nous voulons les traiter.

Puisque nous n'avons pas de système en place pour traiter les données, nous devons créer une visualisation nous-mêmes.

Les blocs de construction de base de nos données :

* Couleur
* ID
* X
* Y

Pourquoi avons-nous besoin d'un ID ? Parce que nous pourrions rencontrer le même item plus d'une fois. Nous voulons éviter les boucles infinies, donc nous devons marquer où nous avons été dans ces cas.

De plus, des données comme celles-ci seront généralement assignées à un type d'ID, de hachage ou d'autre valeur. C'est un identifiant unique afin que nous ayons un moyen d'identifier ce nœud particulier. Si nous voulons connaître le plus grand bloc contigu, nous devons savoir quels nœuds sont dans ce bloc.

Puisqu'il a structuré les données dans une grille, je vais supposer que nous les recevrons avec des valeurs X et Y. En utilisant simplement ces propriétés, j'ai pu générer du HTML pour m'assurer que ce que nous générons ressemble à ce qu'il nous a donné.

Cela a été fait en utilisant un positionnement absolu, tout comme son exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/FnotsmhGfdMNEN3E3ZULDKyx1ylLuTcxQGC1)
_Réponse : 3_

Cela fonctionne même avec un ensemble de données plus grand :

![Image](https://cdn-media-1.freecodecamp.org/images/f7rYzIBdkhETCos4Ul3l8GRxPrtqozd-0qHi)
_Réponse : 18_

Voici le code qui génère les nœuds :

Nous prenons nos colonnes et nos lignes, créons un tableau 1D à partir du nombre d'items, puis générons nos nœuds à partir de ces données.

Au lieu d'une `color`, j'utilise `colorId`. D'abord, parce que c'est plus propre pour la randomisation. Ensuite, nous devrions généralement chercher la valeur de la couleur nous-mêmes.

Bien qu'il ne l'ait jamais explicitement mentionné, il n'a utilisé que 3 valeurs de couleur. Je limite également notre ensemble de données à 3 couleurs. Sachez simplement qu'il pourrait y avoir des centaines de couleurs et que les algorithmes finaux n'auraient pas besoin de changer.

En tant qu'exemple plus simple, voici une liste de nœuds 2x2 :

### Traitement des données

Peu importe la méthode que nous allons utiliser, nous voulons connaître les adjacences pour chacun de ces nœuds. Les valeurs X et Y ne suffiront pas.

Ainsi, étant donné un X et un Y, nous devons déterminer comment trouver les valeurs X et Y adjacentes. C'est assez simple. Nous trouvons simplement les nœuds plus et moins 1 sur X et Y.

J'ai écrit une fonction d'assistance pour cette partie de la logique :

La façon dont nous générons les nœuds, il existe en fait une méthode mathématique pour déterminer les ID des nœuds adjacents. Au lieu de cela, je vais supposer que les nœuds arriveront dans notre système dans un ordre aléatoire.

J'ai fait passer tous les nœuds par une deuxième passe pour ajouter les adjacences :

J'ai évité de faire des optimisations inutiles dans ce code de préprocesseur. Cela n'affectera pas nos statistiques de performance finale et ne servira qu'à simplifier nos algorithmes.

J'ai continué et changé le `colorId` en `color`. C'est complètement inutile pour nos algorithmes, mais je voulais faciliter la visualisation.

Nous appelons `getNodeAtLocation` pour chaque ensemble de valeurs X et Y adjacentes et trouvons notre `northId`, `eastId`, `southId` et `westId`. Nous ne transmettons pas nos valeurs X et Y puisqu'elles ne sont plus nécessaires.

Après avoir obtenu nos ID cardinaux, nous les convertissons en un seul tableau `adjacentIds` qui n'inclut que ceux qui ont une valeur. Ainsi, si nous avons des coins et des côtés, nous n'avons pas à nous soucier de vérifier si ces ID sont nuls. Cela nous permet également de parcourir un tableau au lieu de noter manuellement chaque ID cardinal dans nos algorithmes.

Voici un autre exemple 2x2 utilisant un nouvel ensemble de nœuds passés par `addAdjacencies` :

### Optimisations de pré-traitement

Je voulais simplifier grandement les algorithmes pour cet article, donc j'ai ajouté une autre passe d'optimisation. Celle-ci supprime les ID adjacents qui ne correspondent pas à la couleur du nœud actuel.

Après avoir réécrit notre fonction `addAdjacencies`, voici ce que nous avons maintenant :

J'ai simplifié `addAdjacencies` tout en ajoutant plus de fonctionnalités.

En supprimant les nœuds qui ne correspondent pas en couleur, notre algorithme peut être sûr à 100 % que tous les ID dans la propriété `adjacentIds` sont des nœuds contigus.

Enfin, j'ai supprimé tous les nœuds qui n'ont pas d'adjacences de même couleur. Cela simplifie encore plus nos algorithmes, et nous avons réduit le nombre total de nœuds à seulement ceux qui nous intéressent.

### La mauvaise façon — Récursion

TechLead a déclaré que nous ne pouvions pas faire cet algorithme de manière récursive car nous atteindrions un débordement de pile.

Bien qu'il ait partiellement raison, il existe quelques moyens d'atténuer ce problème. Soit en itérant, soit en utilisant la récursion terminale. Nous verrons l'exemple itératif, mais JavaScript n'a plus la récursion terminale comme fonctionnalité native du langage.

Bien que nous puissions encore simuler la récursion terminale en JavaScript, nous allons garder cela simple et créer une fonction récursive typique à la place.

Avant de plonger dans le code, nous devons déterminer notre algorithme. Pour la récursion, il est logique d'utiliser une [recherche en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_recherche_en_profondeur). Ne vous inquiétez pas de connaître le terme informatique. Un collègue l'a mentionné lorsque je lui montrais les différentes solutions que j'avais trouvées.

#### L'algorithme

Nous commencerons par un nœud et irons aussi loin que possible jusqu'à ce que nous ayons atteint un point final. Ensuite, nous reviendrons et prendrons le prochain chemin de branchement jusqu'à ce que nous ayons scanné l'ensemble du bloc contigu.

C'est une partie de cela. Nous devons également garder une trace de l'endroit où nous avons été et de la longueur du plus grand bloc contigu.

Ce que j'ai fait, c'est diviser notre fonction en 2 parties. L'une conserverait la plus grande liste et les ID précédemment scannés tout en parcourant chaque nœud au moins une fois. L'autre commencerait à un nœud racine non scanné et effectuerait notre traversée en profondeur.

Voici à quoi ressemblent ces fonctions :

Fou, non ? J'ai même hésité à montrer le code parce qu'il devient si compliqué.

Pour simplifier cela, allons étape par étape.

#### La fonction récursive

`getContiguousIds` est notre fonction récursive. Cela est appelé une fois pour chaque nœud. Chaque fois qu'elle retourne, vous obtenez une liste mise à jour des nœuds contigus.

Il n'y a qu'une seule condition dans cette fonction : _notre nœud est-il déjà dans la liste ?_ Si ce n'est pas le cas, appelez `getContiguousIds` à nouveau. Lorsqu'elle retourne, nous aurons une liste mise à jour des nœuds contigus qui retourne à notre réducteur et est utilisée comme état pour le prochain `adjacentId`.

Vous vous demandez peut-être où nous ajoutons des valeurs à `contiguousIds`. Cela se produit lorsque nous `concat` le nœud actuel à `contiguousIds`. Chaque fois que nous récursons plus loin, nous veillons à ajouter le nœud actuel à la liste des `contiguousIds` avant de parcourir ses `adjacentIds`.

Ajouter toujours le nœud actuel garantit que nous ne récursons pas indéfiniment.

#### La boucle

La deuxième moitié de cette fonction parcourt également chaque nœud une fois.

Nous avons un réducteur entourant la fonction récursive. Celui-ci vérifie si notre code a été scanné. Si c'est le cas, continuez à boucler jusqu'à ce que nous trouvions un nœud qui ne l'a pas été ou jusqu'à ce que nous sortions de la boucle.

Si notre nœud n'a pas été scanné, appelez `getContiguousIds` et attendez qu'il soit terminé. Cela est synchrone, mais cela peut prendre un certain temps.

Une fois qu'il revient avec une liste de `contiguousIds`, vérifiez ceux-ci par rapport à la liste `largestContiguousIds`. Si elle est plus grande, stockez cette valeur.

En même temps, nous allons ajouter ces `contiguousIds` à notre liste `scannedIds` pour marquer où nous avons été.

C'est assez simple lorsque vous voyez tout cela.

#### Exécution

Même avec 10K items, cela n'a pas rencontré de problèmes de débordement de pile avec 3 couleurs randomisées. Si je changeais tout pour utiliser une seule couleur, j'ai pu rencontrer un débordement de pile. C'est parce que notre fonction récursive passait par 10K récursions.

### Itération séquentielle

Puisque la mémoire est plus grande que la pile d'appels de fonction, ma prochaine pensée était de faire toute l'opération dans une seule boucle.

Nous allons garder une trace d'une liste de listes de nœuds. Nous continuerons à les ajouter et à les lier ensemble jusqu'à ce que nous sortions de la boucle.

Cette méthode nécessite que nous gardions toutes les listes de nœuds possibles en mémoire jusqu'à ce que nous ayons terminé la boucle. Dans l'exemple récursif, nous n'avons gardé que la plus grande liste en mémoire.

Un autre exemple fou. Décomposons cela depuis le début. Nous parcourons chaque nœud une fois. Mais maintenant, nous devons vérifier si notre id est dans la liste des listes de nœuds : `contiguousIdsList`.

Si elle n'est dans aucune liste de `contiguousIds`, nous l'ajouterons ainsi que ses `adjacentIds`. Ainsi, lors du parcours, quelque chose d'autre s'y liera.

Si notre nœud est dans l'une des listes, il est possible qu'il soit dans plusieurs d'entre elles. Nous voulons lier toutes celles-ci ensemble et supprimer celles qui ne sont pas liées de la `contiguousIdsList`.

C'est tout.

Après avoir établi une liste de listes de nœuds, nous vérifions laquelle est la plus grande, et nous avons terminé.

#### Exécution

Contrairement à la version récursive, celle-ci _termine_ lorsque tous les 10K items sont de la même couleur.

Autrement, c'est assez lent ; beaucoup plus lent que je ne l'avais initialement prévu. J'avais oublié de tenir compte du parcours de la liste de listes dans mes estimations de performance, et cela a clairement eu un impact sur les performances.

### Itération aléatoire

Je voulais prendre la méthodologie derrière la méthode récursive et l'appliquer de manière itérative.

J'ai passé une bonne partie d'une nuit à essayer de me souvenir comment changer l'index dans la boucle dynamiquement, puis je me suis souvenu de `while(true)`. Cela fait si longtemps que j'ai écrit des boucles traditionnelles, que j'avais complètement oublié cela.

Maintenant que j'avais mon arme, je suis passé à l'attaque. Comme j'ai passé beaucoup de temps à essayer d'accélérer les versions observables (plus sur cela plus tard), j'ai décidé d'aller paresseusement et de muter les données à l'ancienne.

Le but de cet algorithme était de toucher chaque nœud exactement une fois et de ne stocker que le plus grand bloc contigu :

Même si je l'ai écrit comme la plupart des gens le feraient probablement, c'est de loin le moins lisible. Je ne peux même pas vous dire ce qu'il fait sans le parcourir moi-même d'abord de haut en bas.

Au lieu d'ajouter à une liste d'ID précédemment scannés, nous supprimons les valeurs de notre tableau `remainingNodes`.

Paresseux ! Je ne recommanderais jamais de faire cela vous-même, mais j'étais au bout de ma corde en créant ces exemples et je voulais essayer quelque chose de différent.

#### La décomposition

J'ai divisé cela en 3 sections séparées par des blocs `if`.

Commençons par la section du milieu. Nous vérifions les `queuedIds`. Si nous en avons, nous faisons une autre boucle à travers les éléments en file d'attente pour voir s'ils sont dans notre `remainingNodes`.

Dans la troisième section, cela dépend des résultats de la deuxième section. Si nous n'avons pas de `queuedIds`, et que `remainingNodesIndex` est `-1`, alors nous avons terminé avec cette liste de nœuds et nous devons commencer à un nouveau nœud racine. Le nouveau nœud racine est toujours à l'index `0` parce que nous supprimons notre `remainingNodes`.

En haut de notre boucle, j'aurais pu utiliser `while(true)`, mais je voulais une sortie au cas où quelque chose tournerait mal. Cela a été utile pendant le débogage puisque les boucles infinies peuvent être pénibles à résoudre.

Après cela, nous supprimons notre nœud. Nous l'ajoutons à notre liste de `contiguousIds`, et nous ajoutons les `adjacentIds` à la file d'attente.

#### Exécution

Cela s'est avéré être presque aussi rapide que la version récursive. C'était le plus rapide de tous les algorithmes lorsque tous les nœuds sont de la même couleur.

### Optimisations spécifiques aux données

#### Regroupement des couleurs similaires

Puisque nous savons que seuls les bleus vont avec les bleus, nous aurions pu regrouper les nœuds de couleurs similaires pour la version d'itération séquentielle.

Le fait de le diviser en 3 tableaux plus petits réduit notre empreinte mémoire et la quantité de boucles que nous devons faire dans notre liste de listes. Cependant, cela ne résout pas la situation où toutes les couleurs sont les mêmes, donc cela ne corrigerait pas notre version récursive.

Cela signifie également que nous pourrions effectuer l'opération en multithreading, réduisant le temps d'exécution de près d'un tiers.

Si nous exécutons celles-ci séquentiellement, nous devons simplement exécuter la plus grande des trois en premier. Si la plus grande est plus grande que les deux autres, vous n'avez pas besoin de les vérifier.

#### Taille maximale possible

Au lieu de vérifier si nous avons la plus grande liste à certains intervalles, nous pourrions vérifier à chaque itération.

Si le plus grand ensemble est supérieur ou égal à la moitié des nœuds disponibles (5K ou plus), il est évident que nous avons déjà le plus grand.

En utilisant la version d'itération aléatoire, nous pourrions trouver la taille de la plus grande liste jusqu'à présent et voir combien de nœuds restent. S'il y en a moins que la taille de la plus grande, nous avons déjà la plus grande.

#### Utiliser la récursion

Bien que la récursion ait ses limitations, nous pouvons toujours l'utiliser. Tout ce que nous avons à faire est de vérifier le nombre de nœuds restants. Si c'est en dessous de la limite de la pile, nous pouvons passer à la version récursive plus rapide. Risqué, mais cela améliorerait certainement le temps d'exécution à mesure que vous avancez dans votre boucle.

#### Utiliser une boucle `for`

Puisque nous connaissons notre nombre maximal d'items, il y aura un bénéfice mineur à passer de la fonction `reduce` à une boucle `for` traditionnelle.

Pour une raison quelconque, les méthodes `Array.prototype` sont [incroyablement lentes par rapport aux boucles `for`](https://itnext.io/speed-up-javascript-array-processing-8d601c57bb0d).

#### Utiliser la récursion terminale

De la même manière que je n'ai pas abordé les versions observables dans cet article particulier, je pense que la récursion terminale nécessite un article à part entière.

C'est un grand sujet avec beaucoup à expliquer, mais bien qu'elle permettrait à la version récursive de fonctionner, elle pourrait ne pas être plus rapide que la boucle `while` comme vous pourriez vous y attendre.

### RxJS : Maintenabilité vs Performance

Il existe des moyens de réécrire ces fonctions où vous aurez plus de facilité à les comprendre et à les maintenir. La solution principale que j'ai trouvée utilisait RxJS dans le style Redux-Observable, mais sans Redux.

C'était en fait mon défi pour l'article. Je voulais coder les méthodes régulières, puis diffuser les données en utilisant RxJS pour voir jusqu'où je pouvais les pousser.

J'ai fait 3 versions en RxJS et j'ai pris quelques libertés pour accélérer le temps d'exécution. Contrairement à mes articles sur les transducteurs, les trois se sont avérées plus lentes même si j'ai augmenté les lignes et les colonnes.

J'ai passé mes nuits de cette semaine-là à rêver de solutions possibles et à passer au peigne fin chaque ligne de code. Je me suis même allongé par terre, j'ai fermé les yeux et j'ai réfléchi, réfléchi, réfléchi. Chaque fois, j'ai eu de meilleures idées mais j'ai continué à rencontrer les limitations de vitesse de JavaScript.

Il y a toute une liste d'optimisations que j'aurais pu faire, mais au détriment de la lisibilité du code. Je ne voulais pas cela (j'en ai quand même utilisé une).

J'ai finalement réussi à faire fonctionner l'une des solutions observables — maintenant la plus rapide — en moitié moins de temps. C'était la meilleure amélioration globale.

La seule fois où j'ai pu battre l'itération séquentielle gourmande en mémoire avec les observables, c'était lorsque chaque nœud est de la même couleur. C'était la seule fois. Techniquement, cela bat aussi la version récursive car elle provoque un débordement de pile dans ce scénario.

Après tout ce travail pour comprendre comment diffuser les données avec RxJS, j'ai réalisé que c'était bien trop pour cet article. Attendez-vous à un futur article pour passer en revue ces exemples de code en détail.

Si vous voulez voir le code en avance, vous pouvez le consulter sur GitHub :
[https://github.com/Sawtaytoes/JavaScript-Performance-Interview-Question](https://github.com/Sawtaytoes/JavaScript-Performance-Interview-Question)

### Statistiques finales

En général, le plus grand bloc contigu était en moyenne de 30 à 80 nœuds.

Voici mes chiffres :

Peu importe le nombre de fois où j'ai exécuté les tests, les positions relatives de chaque méthode sont restées les mêmes.

La méthode Redux-Observable Concurrent a souffert lorsque tous les nœuds étaient de la même couleur. J'ai essayé plusieurs choses pour la rendre plus rapide, mais rien n'a fonctionné :/.

### Développement de jeux

Je suis tombé sur ce code deux fois dans ma carrière. C'était à une échelle beaucoup plus petite, en Lua, et cela s'est produit en travaillant sur [mon jeu indépendant Pulsen](https://pulsengame.com/game).

Dans une situation, je travaillais sur une carte du monde. Elle avait une liste prédéfinie de nœuds, et je traitais cette liste en temps réel. Cela permettait d'appuyer sur `[GAUCHE]`, `[DROITE]`, `[HAUT]`, et `[BAS]` pour vous déplacer sur la carte du monde même si l'angle était légèrement décalé.

J'ai également écrit un générateur de nœuds pour une liste inconnue d'items avec des valeurs X et Y. Ça vous dit quelque chose ? J'ai aussi dû centrer cette grille à l'écran. C'était beaucoup plus facile à faire en HTML que dans le moteur de jeu. Bien que, centrer un tas de divs positionnés de manière absolue n'est pas facile non plus.

Dans ces deux solutions, le temps d'exécution en temps réel n'était pas un gros problème parce que j'ai fait beaucoup de prétraitement lorsque vous avez chargé le jeu.

Je veux souligner que la question de TechLead pourrait être quelque chose que vous rencontrez dans votre carrière ; peut-être, mais il est rare que la vitesse soit un facteur dans les applications JavaScript typiques.

D'après les autres vidéos de TechLead, il utilisait Java chez Google. Je suppose que les postes pour lesquels il interviewait se souciaient de la vitesse d'exécution. Ils avaient probablement un tas de tâches de travail traitant d'énormes morceaux de données, donc une solution comme celle-ci aurait pu être nécessaire.

Mais ensuite, cela aurait pu être un travail sur HTML et CSS, et il se moquait simplement de l'interviewé ; qui sait !

### Conclusion

Comme vous l'avez vu avec les statistiques finales, le code qui avait l'air le pire était presque le plus rapide et accomplissait toutes nos exigences. Bonne chance pour maintenir ce truc !

D'après ma propre expérience, j'ai passé plus de temps à développer les versions non-RxJS. Je pense que c'est parce que les versions plus rapides nécessitaient une réflexion holistique. Redux-Observable vous permet de penser en petits morceaux.

C'était un problème vraiment amusant et frustrant à résoudre. Cela semblait vraiment difficile au début, mais après l'avoir décomposé en morceaux, tous les morceaux se sont assemblés :).

### Plus de lectures

Si vous voulez lire plus sur la performance de JavaScript, consultez mes autres articles :

* [Accélérer le traitement des tableaux JavaScript](https://itnext.io/speed-up-javascript-array-processing-8d601c57bb0d)
* [Utiliser les transducteurs pour accélérer les tableaux JavaScript](https://itnext.io/using-transducers-to-speed-up-javascript-arrays-92677d000096)

Si vous avez aimé ce que vous avez lu, consultez mes autres articles sur des sujets similaires qui ouvrent les yeux :

* [Callbacks : Le guide définitif](https://itnext.io/the-definitive-guide-to-callbacks-in-javascript-44a39c065292)
* [Promesses : Le guide définitif](https://itnext.io/promises-the-definitive-guide-6a49e0dbf3b7)
* [Feature Flags : Soyez vraiment agile](https://itnext.io/feature-flags-be-truly-agile-820ff50294c)
* [Faire du caca à partir d'emojis de nourriture](https://itnext.io/an-emoji-lovers-guide-to-functional-programming-part-1-241d8d4c9223)