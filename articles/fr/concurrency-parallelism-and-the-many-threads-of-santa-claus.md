---
title: Concurence, parallélisme et les nombreux fils du Père Noël ?
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-12-24T01:18:11.000Z'
originalURL: https://freecodecamp.org/news/concurrency-parallelism-and-the-many-threads-of-santa-claus
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/cover-3.png
tags:
- name: Christmas
  slug: christmas
- name: Computer Science
  slug: computer-science
- name: concurrency
  slug: concurrency
- name: multithreading
  slug: multithreading
- name: parallelism
  slug: parallelism
- name: Threading
  slug: threading
seo_title: Concurence, parallélisme et les nombreux fils du Père Noël ?
seo_desc: 'Consider the following: Santa brings toys to all the good girls and boys.

  There are 7,713,468,100 people in the world in 2019, around 26.3% of which are under
  15 years old. This works out to 2,028,642,110 children (persons under 15 years of
  age) in t...'
---

Considérons ce qui suit : le Père Noël apporte des jouets à tous les bons garçons et filles.

En 2019, il y a [7,713,468,100 personnes](https://en.wikipedia.org/wiki/Demographics_of_the_world#Current_population_distribution) dans le monde, dont [environ 26,3 %](https://en.wikipedia.org/wiki/Demographics_of_the_world#Age_structure) ont moins de 15 ans. Cela représente 2,028,642,110 enfants (personnes de moins de 15 ans) dans le monde cette année.

Le Père Noël ne semble pas visiter les enfants de toutes les religions, alors nous généraliserons et n'inclurons que les chrétiens et les personnes non religieuses. Collectivement, cela représente [environ 44,72 %](https://en.wikipedia.org/wiki/List_of_religious_populations#Adherent_estimates_in_2019) de la population. Si nous supposons que tous les enfants suivent leurs parents, alors 907,208,751,6 enfants seraient éligibles pour le Père Noël.

Quel pourcentage de ces enfants sont sages ? Il est impossible de le savoir ; cependant, nous pouvons travailler sur quelques hypothèses. L'une d'elles est que le Père Noël fonctionne plus sur l'optimisme que sur l'économie et aurait probablement préparé la possibilité que chaque enfant soit un bon enfant une année donnée. Ainsi, il serait prêt à donner un jouet à chaque enfant. Supposons que ce fut une excellente année et que les 907,208,751,6 enfants reçoivent des jouets.

Cela fait beaucoup de cadeaux, et, comme nous le savons, ils sont tous fabriqués par les lutins du Père Noël dans son atelier du Pôle Nord de la Chine. Sachant qu'il y a 365 jours dans une année et que l'un d'eux est Noël, supposons que les lutins du Père Noël ont collectivement 364 jours pour créer et emballer 907,208,752 (arrondi) cadeaux. Cela représente 2,492,331,74 cadeaux par jour.

Presque deux millions et demi de cadeaux par jour, c'est une charge de travail lourde pour tout atelier. Examinons deux paradigmes que le Père Noël pourrait employer pour atteindre cet objectif : la concurrence et le parallélisme.

## Un processus séquentiel

Supposons que l'atelier du Père Noël soit dirigé par exactement un lutin très travailleur et très fatigué. La production d'un cadeau implique quatre étapes :

1. Découper le bois
2. Assemblage et collage
3. Peinture
4. Emballage cadeau

Avec un seul lutin, une seule étape pour un seul cadeau peut se produire à un moment donné. Si le lutin devait produire un cadeau à la fois du début à la fin, ce processus serait exécuté _séquentiellement_. Ce n'est pas la méthode la plus efficace pour produire deux millions et demi de cadeaux par jour ; par exemple, le lutin devrait attendre sans rien faire pendant que la colle du cadeau sèche avant de passer à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/sequence.png)

## Concurence

Pour être plus efficace, le lutin travaille sur tous les cadeaux _concurremment_.

Au lieu de terminer un cadeau à la fois, le lutin découpe d'abord tout le bois pour tous les jouets, un par un. Lorsque tout est découpé, le lutin assemble et colle les jouets ensemble, un après l'autre. Ce [traitement concurrent](https://en.wikipedia.org/wiki/Concurrent_computing) signifie que la colle du premier jouet a le temps de sécher (sans nécessiter plus d'attention de la part du lutin) pendant que les jouets restants sont collés ensemble. Il en va de même pour la peinture, un jouet à la fois, et enfin l'emballage.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/concurrency.png)

Puisqu'un lutin ne peut faire qu'une seule tâche à la fois, un seul lutin utilise la journée aussi efficacement que possible en produisant des cadeaux de manière concurrente.

## Parallélisme

Espérons que l'atelier du Père Noël compte plus d'un seul lutin. Avec plus de lutins, plus de jouets peuvent être construits simultanément au cours d'une journée. Ce travail simultané signifie que les cadeaux sont produits en _parallèle_. Le [traitement parallèle](https://en.wikipedia.org/wiki/Parallel_computing) effectué par plusieurs lutins signifie que plus de travail est accompli en même temps.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/parallel.png)

Les lutins travaillant en parallèle peuvent également employer la concurrence. Un lutin ne peut toujours s'attaquer qu'à une seule tâche à la fois, il est donc plus efficace d'avoir plusieurs lutins produisant des cadeaux de manière concurrente.

Bien sûr, si l'atelier du Père Noël compte, disons, deux millions et demi de lutins, chaque lutin n'aurait besoin de finir qu'un maximum d'un cadeau par jour. Dans ce cas, travailler de manière séquentielle ne nuit pas à l'efficacité de l'atelier. Il resterait encore 7,668,26 lutins pour aller chercher du café et du déjeuner.

## Le Père Noël et les threads

Après tout le travail acharné des lutins, c'est au Père Noël de livrer les cadeaux – tous les 907,208,752.

Le Père Noël n'a pas besoin de rendre visite à chaque enfant ; seulement à l'arbre de chaque foyer. Alors, combien d'arbres le Père Noël doit-il visiter ? Encore une fois avec une généralisation large, nous dirons que le nombre moyen d'enfants par foyer dans le monde est [2,45, basé sur les taux de fécondité prévus de l'année](https://en.wikipedia.org/wiki/Demographics_of_the_world#Total_fertility_rate). Cela fait 370,289,286,4 maisons à visiter. Arrondissons cela à 370,289,287.

Combien de temps le Père Noël a-t-il ? La légende dit une nuit, ce qui signifie une rotation terrestre, et donc 24 heures. [NORAD confirme](https://www.noradsanta.org/).

Cela signifie que le Père Noël doit visiter 370,289,287 foyers en 24 heures (86,400 secondes), à un rythme de 4,285,75 foyers par seconde, sans compter le temps qu'il faut pour mettre les cadeaux sous l'arbre et prendre un cookie.

Clairement, le Père Noël n'existe pas dans notre dimension. Cela est particulièrement probable étant donné que, malgré le fait qu'il soit potelé et rond, il passe par une cheminée (avec un feu allumé, tout en restant indemne) en portant un sac de jouets contenant des cadeaux pour tous les enfants du foyer. Nous n'avons même pas considéré le fait que son traîneau transporte suffisamment de jouets pour chaque garçon et fille croyants dans le monde, et qu'il vole.

Le Père Noël existe-t-il en dehors de nos règles de physique ? Comment une seule entité pourrait-elle gérer de voyager autour du monde, livrer des colis, en moins de 24 heures à un rythme de 4,285,75 foyers par seconde, et encore avoir le temps pour du lait et des cookies et embrasser maman ?

Une chose est certaine : le Père Noël utilise Internet. Aucune autre technologie n'a encore permis aux colis de voyager aussi loin et aussi rapidement. Même ainsi, tenter d'atteindre plus de quatre mille foyers par seconde n'est pas une mince affaire, même avec la meilleure connexion internet gigabit que le Pôle Nord a à offrir. Comment le Père Noël pourrait-il augmenter son efficacité ?

Il y a clairement une seule conclusion logique à ce mystère : le Père Noël est un processus multithread.

## Un seul thread

Travaillons de l'extérieur vers l'intérieur. Considérez un [thread](https://en.wikipedia.org/wiki/Thread_(computing)) comme une tâche particulière, ou la séquence la plus granulaire d'instructions que le Père Noël pourrait exécuter. Un thread pourrait exécuter la tâche, `mettre le cadeau sous l'arbre`. Un thread est un composant d'un processus, dans ce cas, le processus du Père Noël de livrer des cadeaux.

Si le Père Noël est [monothread](https://en.wikipedia.org/wiki/Thread_(computing)#Single_threading), il, en tant que processus, ne pourrait accomplir qu'une seule tâche à la fois. Puisqu'il est vieux et un peu oublieux, il a probablement un ensemble d'instructions pour livrer des cadeaux, ainsi qu'un calendrier à respecter. Ces deux choses guident le thread du Père Noël jusqu'à ce que son processus soit complet.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/single.png)

Le Père Noël monothread pourrait fonctionner comme suit :

1. Atterrir le traîneau chez Timmy
2. Prendre le cadeau de Timmy dans le traîneau
3. Entrer dans la maison par la cheminée
4. Localiser le sapin de Noël
5. Placer le cadeau de Timmy sous le sapin de Noël
6. Sortir de la maison par la cheminée
7. Décoller avec le traîneau

Rincer et répéter… encore 370,289,286 fois.

## Multithreading

Le Père Noël [multithread](https://en.wikipedia.org/wiki/Thread_(computing)#Multithreading), en revanche, est le [Doctor Manhattan](https://dc.fandom.com/wiki/Jonathan_Osterman_(Watchmen)) du Pôle Nord. Il n'y a toujours qu'un seul Père Noël dans le monde ; cependant, il a l'incroyable capacité de multiplier sa conscience et d'accomplir plusieurs ensembles d'instructions de tâches simultanément. Ces travailleurs de tâches supplémentaires, ou threads de travail, sont créés et contrôlés par le processus principal du Père Noël livrant des cadeaux.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/cover-2.png)

Chaque thread de travail agit indépendamment pour compléter ses instructions. Puisqu'ils appartiennent tous à la conscience du Père Noël, ils partagent la mémoire du Père Noël et savent tout ce que le Père Noël sait, y compris sur quelle planète ils courent et où obtenir les cadeaux.

Avec cette connaissance partagée, chaque thread est capable d'exécuter son ensemble d'instructions en parallèle avec les autres threads. Ce parallélisme multithread rend le Père Noël unique aussi efficace que possible.

Si une livraison moyenne de cadeaux prend une heure, le Père Noël n'a besoin de créer que 4,286 threads de travail. Avec chacun faisant un voyage de livraison par heure, le Père Noël aura terminé tous les 370,289,287 voyages d'ici la fin de la nuit.

Bien sûr, en théorie, le Père Noël pourrait même créer 370,289,287 threads de travail, chacun volant vers un foyer pour livrer des cadeaux à tous les enfants ! Cela rendrait le processus du Père Noël extrêmement efficace, et expliquerait également comment il parvient à consommer tous ces cookies trempés dans le lait sans être rassasié. 🎄🍪

## Un Noël multithread efficace et joyeux

Grâce à l'informatique moderne, nous comprenons enfin comment le Père Noël parvient à accomplir la tâche apparemment impossible de livrer des jouets aux bons garçons et filles du monde entier. De ma famille à la vôtre, je vous souhaite un merveilleux Noël. N'oubliez pas d'accrocher vos bas sur l'étagère du routeur.

Bien sûr, rien de tout cela n'explique comment les rennes parviennent à voler.