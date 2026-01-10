---
title: Comment visualiser les algorithmes de distribution aléatoire dans Swift et
  ARKit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-30T16:12:18.000Z'
originalURL: https://freecodecamp.org/news/visualizing-random-distribution-algorithms-in-swift-and-arkit-4e05f502755b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DLjYdq6QI0HUu4SRVC90Mw.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: engineering
  slug: engineering
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Comment visualiser les algorithmes de distribution aléatoire dans Swift
  et ARKit
seo_desc: 'By Dan Wyszynski

  A tree in the forest

  I was recently working on a prototype where I needed to place a large amount of
  objects in 3D space. This was an AR project, and the thought was that these objects
  would be placed around you in a random fashion, ...'
---

Par Dan Wyszynski

### Un arbre dans la forêt

Je travaillais récemment sur un prototype où je devais placer un grand nombre d'objets dans un espace 3D. Il s'agissait d'un projet de réalité augmentée, et l'idée était que ces objets seraient placés autour de vous de manière aléatoire, se dispersant autour de vous alors qu'ils tombaient du ciel.

Cela soulève quelques problèmes. Tout d'abord, nous ne connaissons pas les environs actuels de l'utilisateur, nous devons donc limiter le rayon des objets lâchés à quelque chose que nous pouvons configurer en fonction de l'emplacement ou d'autres facteurs.

Ensuite, nous savons que les générateurs aléatoires intégrés ne sont pas très aléatoires à moins que des précautions spécifiques ne soient prises.

Enfin, la génération de points avec des générateurs aléatoires, aussi aléatoires soient-ils, entraîne des regroupements, où de nombreux points générés peuvent tomber dans des zones proches les unes des autres, vous laissant avec des endroits sans aucun point. Et personne ne veut de zones sans points : croyez-moi, je sais.

Il existe plusieurs façons d'accomplir une distribution aléatoire égale. Comme tout développeur qui se respecte, j'en ai trouvé quelques-unes qui ont des implémentations simples et qui fonctionnent bien pour notre objectif. Examinons chacune d'elles et implémentons-les en Swift en utilisant ARKit et SceneKit.

### Lancez les dés !

Avant de passer aux « bons » algorithmes, nous devrions voir ce que nous obtenons en utilisant simplement des nombres aléatoires pour placer nos points. En faisant cela, nous allons mettre notre application en place et l'utiliser pour tester les autres implémentations sous la même forme.

Créons notre application et mettons en place certaines des bases. Ouvrez Xcode et créez un nouveau projet en utilisant le modèle d'application de réalité augmentée. Construisez et exécutez l'application pour vous assurer que tout fonctionne et que vous voyez le vaisseau par défaut apparaître devant votre téléphone lorsque vous exécutez l'application.

Ensuite, nous allons configurer notre projet comme nous l'avons fait pour le [premier tutoriel](https://medium.com/s23nyc-tech/getting-started-with-arkit-and-scenekit-76814862cc75) de ma série ARKit. Suivez les étapes de ce tutoriel, avec la seule différence étant le nom du fichier de scène. Au lieu de le nommer **HoverScene**, nous le nommerons `**MainScene**` à la place. Ajoutez le délégué de rendu comme décrit dans le tutoriel, et suivez la section **Extra Credits** où le reconnaisseur de geste de tapotement est créé.

À ce stade, le projet est presque prêt, mais nous n'avons pas (ni besoin) de la méthode `addSphere` qui est référencée dans ce tutoriel. Au lieu de cela, nous allons commencer à créer nos générateurs d'algorithmes.

Créez un fichier appelé `**PointGenerator.swift**`. Ici, nous mettrons plusieurs itérations de nos algorithmes. Commençons par le générateur de points de nombres aléatoires. Nous allons créer un protocole auquel nos algorithmes adhéreront, ce qui facilitera le passage d'un algorithme à l'autre dans notre source plus tard.

Notre protocole est simple. Étant donné un nombre de points à générer et une largeur et une longueur pour limiter les points, renvoie un tableau de points :

Notre `RandomPointGenerator` adhérera à cette classe et produira notre premier ensemble de résultats :

Le code ici est simple. Nous itérons et créons des points qui se trouvent dans les limites de largeur et de longueur, en plaçant des points de chaque côté du point médian de ces limites. Nous ajoutons les points créés à un tableau, puis nous retournons simplement les points.

Créez une classe appelée `Visualizer` dérivée de `SCNNode`. Cette classe servira de conteneur qui contient les objets que nous placerons dans le monde pour visualiser l'ensemble de points. Pour le moment, nous allons créer de petites sphères à chaque point généré par nos algorithmes.

Voici à quoi devrait ressembler notre classe :

D'accord, maintenant nous sommes prêts à créer nos points. Retournez à notre classe `MainScene` et ajoutez une méthode appelée `createPointField`, qui prend une position `SCNVector3` :

Nous allons appeler cela depuis notre `ViewController` lorsque nous tapons sur l'écran. Allons dans notre méthode `didTapScreen` et faisons en sorte que la partie où nous avons précédemment créé une sphère (dans ce premier tutoriel) ressemble à ce qui suit :

Construisez et exécutez, et nous avons maintenant notre premier algorithme implémenté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q7WoWRzhOP9iSMBkKDVofA.jpeg)
_Placement aléatoire de points. Pas génial._

Remarquez comment les sphères sont regroupées à certains endroits. C'est exactement ce que nous voulons éviter.

Je ne vais pas entrer dans des descriptions détaillées de chaque algorithme, mais je vais fournir des liens vers les sites que j'ai trouvés informatifs et qui m'ont inspiré pour implémenter en Swift et AR.

#### Échantillonnage de Poisson et le meilleur candidat de Mitchell

Ce dont nous avons besoin comme alternative à la méthode du générateur de nombres aléatoires est un algorithme qui retourne un ensemble de points qui sont proches les uns des autres, mais pas plus proches qu'une distance minimale spécifiée. C'est là que l'**échantillonnage de disque de Poisson** entre en jeu. Il existe plusieurs façons d'implémenter l'algorithme de disque de Poisson. Celui que nous allons implémenter dans notre code s'appelle l'**algorithme du meilleur candidat de Mitchell**. Il est facile à implémenter et s'exécute rapidement.

L'idée derrière l'algorithme est de placer des points, et au fur et à mesure que vous les placez, vérifiez s'ils répondent à l'exigence d'être au moins à la distance minimale des points déjà placés. Pour ce faire, vous échantillonnez le point au fur et à mesure que vous le placez, en regardant la distance que les points à proximité ont. Si aucun point n'est dans la distance minimale requise, placez le nouveau point, sinon, essayez de trouver un autre emplacement. Vous pouvez en lire plus sur l'algorithme [ici](https://bost.ocks.org/mike/algorithms/).

Pour implémenter, nous allons créer une autre implémentation de notre protocole `**PointGenerator**` :

Retournons à notre classe `MainScene`, commentons les lignes du générateur aléatoire, et ajoutons ces nouvelles lignes :

Exécutez l'application à nouveau, et regardons nos résultats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7xvbJ3FRTKwiEPdCKmPhWQ.jpeg)
_Disque de Poisson utilisant la méthode du meilleur candidat de Mitchell_

Beaucoup mieux ! Il n'y a pas de grands regroupements ou de zones stériles. C'est maintenant quelque chose que nous pouvons utiliser pour placer des objets dans le monde. D'autres utilisations pour cet algorithme incluent des choses comme la génération dynamique de textures à l'exécution ou des générateurs de bruit.

Nous avons ce dont nous avons besoin avec cette implémentation, et nous allons l'utiliser plus tard. Mais que se passe-t-il si nous voulions avoir quelque chose d'un peu différent, où nous avons besoin d'une distribution uniforme dans une frontière circulaire ? C'est là que l'algorithme de la graine de tournesol entre en jeu.

### Extra Credit

#### Algorithme de la graine de tournesol

Tout au long de l'histoire, nous avons trouvé des motifs mathématiques dans la nature. L'une des caractéristiques intéressantes de nombreux motifs qui sont imités dans la nature est l'existence de la séquence de Fibonacci dans les plantes. Ces caractéristiques se manifestent par des motifs en spirale dans les feuilles, les graines et les arrangements de pétales. L'étude de ces motifs s'appelle la **Phyllotaxie**. L'algorithme suivant implémente le modèle mathématique de l'une de ces spirales. Vous pouvez trouver plus d'informations [ici](https://thatsmaths.com/2014/06/05/sunflowers-and-fibonacci-models-of-efficiency/) et [ici](https://www.popmath.org.uk/rpamaths/rpampages/sunflower.html).

Retournons à notre fichier `PointGenerator` et créons notre nouvelle implémentation :

Vous remarquerez ici que nous ignorons les paramètres **width** et **height** passés en entrée. Cela est dû au fait qu'au lieu de contraindre les points à une région, nous allons les distribuer uniformément en spirale jusqu'à ce que nous n'ayons plus de points.

Changer l'**alpha** dans le paramètre passé à la méthode `sunflower` contrôle la granularité des points au bord de la frontière. C'est-à-dire que nous pouvons rendre la frontière plus lisse ou plus rugueuse en contrôlant la distribution des points. Le code ci-dessus utilise un `alpha` de `2`, qui est élevé, et donne une frontière plus uniforme.

Allons dans notre `MainScene` à nouveau, et commentons l'algorithme précédent. Ajoutons un appel pour obtenir nos points générés par le motif `Sunflower` :

Exécutons notre application à nouveau et voyons ce que nous obtenons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jfw0td6NYTbk0m9m637FJQ.jpeg)
_Algorithme du Tournesol_

Comme vous pouvez le voir, nous avons un motif qui imite la façon dont les tournesols tiennent leurs graines. Il existe également une variation intéressante que nous pouvons appliquer à l'algorithme, comme détaillé dans l'un des commentaires de cette question Stack Overflow [question](https://stackoverflow.com/questions/28567166/uniformly-distribute-x-points-inside-a-circle).

En changeant le `theta` en un relèvement, le commentateur a transformé l'algorithme en une formation géodésique.

Changez la ligne `theta` dans notre code en ce qui suit :

Exécutons notre algorithme à nouveau et voyons à quoi il ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DLjYdq6QI0HUu4SRVC90Mw.jpeg)
_Algorithme du Tournesol avec motif en spirale_

Cool ! Maintenant nous avons le motif en spirales.

En parlant de spirales, vérifions un dernier algorithme.

### La spirale de Vogel

Ici, nous avons un autre algorithme étroitement lié qui utilise également une séquence de Fibonacci et l'[Angle d'or](https://en.wikipedia.org/wiki/Golden_angle). Vous pouvez en lire plus sur la spirale de Vogel [ici](https://www.codeproject.com/Articles/1221341/The-Vogel-Spiral-Phenomenon) et [ici](http://www.dcs.gla.ac.uk/~jhw/spirals/).

Implémentons-le, puis nous le modifierons pour voir comment il influence les résultats.

Dans notre classe `PointGenerator`, ajoutons notre implémentation de cet algorithme.

Cet algorithme, comme l'algorithme de la graine de tournesol, ignore également les paramètres **width** et **height**.

Remplaçons l'algorithme précédent par nos nouveaux appels.

Faisons un essai et voyons ce que nous obtenons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E8jaDtxL84_HPeJVAmXu3w.jpeg)
_Spirale de Vogel_

Bien ! Maintenant, essayons différentes variations de cet algorithme. En changeant la formule, nous pouvons obtenir différentes formations en spirale. Changez la déclaration `it` en la ligne suivante :

Exécutez cela et voyez ce que nous obtenons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QAo1ria723ab_6VSTUTgVg.jpeg)
_Spirale de Vogel, ressemblant au Tournesol_

Cette spirale ressemble maintenant à une version inversée de notre spirale de Tournesol avec le `theta` mis à jour. Intéressant !

Essayons avec la formule suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uBr1Oa3mrnt3GmdxCiWg5g.jpeg)
_Spirales de Vogel_

Similaire au premier algorithme, mais les spirales sont séparées. Très cool !

Nous avons maintenant parcouru 4 algorithmes différents, y compris le placement strictement aléatoire de nombres aléatoires qui n'est pas très bon. Chacun de ces algorithmes a sa place dans notre boîte à outils, et ils peuvent être utilisés pour répondre à une variété de besoins.

### Extra Credit, Deuxième Partie

Ce ne serait pas un article de ma part si nous ne faisions pas quelque chose de cool avec ce que nous venons d'apprendre, n'est-ce pas ?

Téléchargez quelques modèles d'arbres depuis une boutique de modèles 3D comme Sketchfab ou Turbosquid. Convertissez-les au format Collada (DAE) si nécessaire et ajoutez-les à votre projet. Vous devrez peut-être les redimensionner pour qu'ils soient à la bonne échelle lorsque vous les placez dans votre scène, mais vous saurez quand vous les utiliserez. Assurez-vous d'utiliser un modèle à faible polycarte puisque nous parlons d'instancier des dizaines, voire des centaines d'instances d'objets.

Créons une classe `Tree` qui dérive de `**SceneObject**` (nous avons créé cette classe dans notre précédent tutoriel). Nous allons la faire charger un arbre aléatoire parmi ceux que nous avons ajoutés à notre application. Nous utilisons la fonction de commodité aléatoire que nous avons également ajoutée dans un précédent tutoriel.

Voici à quoi ressemble ma classe `Tree` :

Utilisons l'algorithme de Mitchell et réduisons le nombre de modèles (points) que nous voulons générer à 60. Selon le nombre de polygones dans vos modèles, cela pourrait être trop grand. J'ai commencé avec un ensemble différent de modèles et cela a pris un certain temps pour placer 20 modèles. Commencez bas et montez progressivement. Pour les modèles que j'ai utilisés, je pouvais aller plus haut, mais 60 était assez dense.

Dans notre code `Visualizer`, changeons notre création d'arbre pour animer un peu l'échelle.

Dans mon cas, avec les modèles que j'ai utilisés, j'ai dû les réduire un peu pour les amener à une taille raisonnable, d'où vient ce 0,45. J'ai également baissé la position un peu pour qu'ils reposent sur le plan du sol. Vous pouvez ajuster ces nombres à ce qui convient à votre situation.

Construisez et exécutez, et maintenant nous avons une petite forêt heureuse créée avec presque aucun effort.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3xGOTLUtmoisLbHm-CO2ag.gif)
_Notre petite forêt heureuse_

J'espère que vous avez apprécié cette petite expérience. N'hésitez pas à montrer votre travail dans la section des commentaires !

[Daniel Wyszynski](https://medium.com/@AbovegroundDan) est un développeur qui a travaillé sur plus de plateformes et de langages qu'il ne veut l'admettre. Il croit en la construction de produits qui créent des expériences utilisateur mémorables. Pour Dan, les utilisateurs passent en premier, les plateformes en second. Suivez Dan sur [Medium](https://medium.com/@AbovegroundDan) ou [Twitter](https://twitter.com/AbovegroundDan) pour en savoir plus sur lui. Consultez également le blog [s23NYC: Engineering](https://medium.com/s23nyc-tech), où beaucoup de contenu intéressant de l'équipe d'innovation numérique de Nike est publié.

_Note de l'auteur : Les opinions exprimées sont les miennes et ne représentent pas nécessairement celles de mon employeur._