---
title: Comment utiliser la théorie des graphes pour construire un monde plus durable
subtitle: ''
author: Daniel García Solla
co_authors: []
series: null
date: '2022-08-19T20:50:13.000Z'
originalURL: https://freecodecamp.org/news/the-value-of-graph-theory-within-sustainability
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/graph-theory-image.png
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: algorithms
  slug: algorithms
- name: graph theory
  slug: graph-theory
- name: Math
  slug: math
- name: sustainability
  slug: sustainability
seo_title: Comment utiliser la théorie des graphes pour construire un monde plus durable
seo_desc: "Discrete mathematics is an area of math based on the study of formal structures\
  \ whose nature is fundamentally separate and distinct. \nThis means it focuses on\
  \ integers and natural sets of numbers, shapes, and other objects that you can count\
  \ finitely..."
---

Les mathématiques discrètes sont un domaine des mathématiques basé sur l'étude des structures formelles dont la nature est fondamentalement séparée et distincte. 

Cela signifie qu'elles se concentrent sur les entiers et les ensembles naturels de nombres, les formes et d'autres objets que vous pouvez compter de manière **finie** ou distinguer les uns des autres. Elles modélisent la réalité de manière spécifiquement adaptée à certaines applications du monde réel. 

De l'industrie et de la logistique à l'informatique et aux télécommunications, avoir une représentation quantifiée de tout ce qui nous entoure a conduit à des avancées magnifiques dans notre compréhension et notre contrôle du monde physique.

Il est important d'avoir au moins une idée approximative des principales distinctions entre discrétion et continuité pour aborder la **théorie des graphes**. Mais ces concepts ne sont pas très bien connus des personnes extérieures au monde des mathématiques.

Au début, les mathématiques continues sont celles principalement enseignées dans le système éducatif en raison de leur polyvalence, de leur utilité et de leur praticité dans la plupart des domaines. 

Elles sont basées sur l'analyse des nombres réels et des fonctions qui encapsulent les mappages entre ces quantités, ainsi que la notion de changement infinitésimal d'une variable. Cela aboutit à une série d'outils comme les limites ou les dérivées qui constituent le **calcul**.

D'autre part, le paradigme discret est plus simple et intuitif, à l'exception de quelques cas. Et sa finitude est donnée par l'élément primordial qui le constitue – les **ensembles**.

Parmi les domaines d'utilisation les plus notables figurent ceux dont les principaux composants impliquent des algorithmes et des structures de données. Bien que les cas d'utilisation des mathématiques ne soient pas ce que la plupart des gens pensent qu'ils sont. 

Dans le monde réel, nous ne rencontrons pas souvent de problèmes de la même manière que dans le système éducatif. En effet, les façons discrètes d'aborder les énigmes et de modéliser les données d'entrée dont nous avons besoin pour trouver une solution sont plus courantes que les façons continues, surtout en ce qui concerne les problèmes d'optimisation des systèmes.

Pour cette raison, nous devrions reconsidérer le rôle de cette façon de faire des mathématiques, car elle implique le développement de la **pensée critique** et de la **pensée computationnelle**. Cela est crucial pour l'ère actuelle dans laquelle nous sommes entourés de technologie. Cela implique également l'amélioration des compétences en résolution de problèmes, ce qui nous permet de faire face à tout nouveau défi. 

En faisant cela, nous pouvons voir à quel point il est pertinent d'appliquer une base mathématique solide aux menaces mondiales courantes qui augmentent quotidiennement, comme la désinformation, le manque de fluidité dans la manipulation de la technologie, l'instabilité géopolitique et même le changement climatique.

Nonobstant l'éloignement apparent entre ce dernier problème et la théorie des graphes elle-même, nous devrions réfléchir à la manière dont nous vivons et au système par lequel notre civilisation est maintenue telle que nous la connaissons.

## Objectifs de cet article

Cet article vise à expliquer la théorie des graphes, l'un des composants les plus significatifs de toutes les mathématiques discrètes, de manière intuitive, simple et visuelle. Je vais également essayer de guider son utilisation vers le développement de nouvelles techniques disruptives applicables dans des domaines tels que les **soins environnementaux**, nécessaires pour préserver et **régénérer** notre nature. 

Atteindre cet objectif efficacement ne suscitera pas seulement la curiosité ou inspirera les lecteurs qui pourraient avoir l'intention de continuer à apprendre, mais contribuera également à une prise de conscience accrue de la société sur les questions de durabilité. Cela augmentera la probabilité que, dans le futur, les problèmes que les scientifiques prédisent comme étant une menace pour notre existence et l'existence de la vie sur la planète soient maîtrisés, grâce aux connaissances scientifiques et spécifiquement à la contribution de la théorie des graphes.

Cependant, étant donné son large champ d'application, il sera impossible d'expliquer entièrement la théorie des graphes dans cet article. Je vais donc me concentrer sur l'aspect visuel de toute explication plutôt que sur l'aspect formel, puisque vous pouvez facilement consulter cela dans n'importe quel manuel. Cela fournira également un point de vue différent de certaines définitions. 

De plus, il est essentiel que nous traitons l'idée d'un graphe de la manière la plus complète possible. Nous nous concentrerons sur son histoire, sa représentation et ses propriétés les plus descriptives plutôt que sur des concepts avancés comme les cycles singuliers. Cela vous aidera à saisir le noyau de la théorie des graphes et vous préparera à apprendre ces concepts avancés plus facilement.

### Voici ce que nous allons couvrir :

1. [Éléments de base de la théorie des graphes](#heading-elements-de-base-de-la-theorie-des-graphes)
2. [Histoire de la théorie des graphes](#heading-histoire-de-la-theorie-des-graphes)
3. [Définition d'un graphe](#heading-definition-dun-graphe)
4. [Représentations des graphes](#heading-representations-des-graphes)
5. [Propriétés des graphes](#heading-proprietes-des-graphes)
6. [Algorithmes et théorie des graphes](#heading-algorithmes-et-theorie-des-graphes)
7. [Pourquoi les graphes sont-ils importants pour atteindre la durabilité ?](#heading-pourquoi-les-graphes-sont-ils-importants-pour-atteindre-la-durabilite)
8. [Conclusion](#heading-conclusion)

## Éléments de base de la théorie des graphes

Que vous soyez nouveau dans la théorie des graphes ou que vous en sachiez déjà quelque chose, il est toujours utile de revoir les bases. 

Tout d'abord, introduisons l'idée d'un "graphe" avec une représentation habituelle que vous avez peut-être vue :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-90.png)
_Exemple d'un graphe arbitraire_

Ci-dessus, vous avez un graphe où nous pouvons voir, au niveau le plus fondamental, deux blocs de construction différents : les sommets (représentés par des cercles) et les arêtes (représentées par des lignes reliant les cercles). 

Vous pouvez créer une structure avec ces éléments qui peut encapsuler le fonctionnement de nombreux systèmes présents dans notre vie que nous ne réalisons même pas. 

Mais, le plus surprenant de tout est que la théorie des graphes dans son ensemble est dérivée d'un concept aussi simple que des **objets liés les uns aux autres**.

## Histoire de la théorie des graphes

Pour comprendre l'origine de cette idée, nous devons remonter au 18ème siècle, lorsque [**Leonhard Euler**](https://en.wikipedia.org/wiki/Leonhard_Euler) a résolu le célèbre problème des [**Sept ponts de Königsberg**](https://mathworld.wolfram.com/KoenigsbergBridgeProblem.html#:~:text=The%20K%C3%B6nigsberg%20bridge%20problem%20asks,that%20the%20trip%20ends%20in). 

À cette époque, la ville était traversée par la rivière Pregel, générant quatre morceaux de terre interconnectés avec sept ponts, comme on peut le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-91.png)
_Image extraite de [**ici**](https://en.wikipedia.org/wiki/File:Konigsberg_bridges.png" rel="noopener)_

La tâche consistait à trouver un chemin qui traverse tous les ponts sans passer par le même pont deux fois, en commençant et en terminant au même point. 

Au début, avec si peu de ponts, il peut être facile de trouver une solution par force brute en essayant des combinaisons de chemins. Mais, puisque nous ne savons pas si une solution réalisable existe, il est utile de formaliser les éléments du problème et de prouver correctement sa résolubilité avant de commencer tout processus. 

De plus, si le nombre de ponts augmente, il deviendra beaucoup plus complexe à résoudre, car les combinaisons augmentent remarquablement vite.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-92.png)
_Problème de Königsberg affiché sous forme de graphe_

Comme on peut le voir ci-dessus, Euler a représenté les zones terrestres avec des sommets de graphe (également appelés nœuds) et les ponts avec des arêtes, concluant qu'il était impossible d'avoir une telle traversée à travers le graphe. 

Brièvement, si nous regardons le nombre d'arêtes incidentes à chaque sommet, nous verrons que chaque valeur est impaire pour chaque nœud, ce qui signifie que le graphe ne possède pas de cycle eulérien. Cela signifie qu'il n'est pas un graphe eulérien, et nous ne pouvons pas prouver positivement le problème. 

Néanmoins, cette approche a représenté une percée dans la conception mathématique de diverses questions qui étaient encore non résolues. Les contributions d'Euler à l'élaboration de cette théorie, qui a été perfectionnée et élargie au fil des ans, ont fait de lui l'un des mathématiciens les plus influents de son époque.

## Définition d'un graphe

Maintenant que vous savez à quoi ressemble un graphe dessiné sur un diagramme, examinons la définition formelle officielle :

> Un graphe **G** est une paire d'ensembles **(V, E)** où **V** est un ensemble non nul contenant les sommets du graphe et **E** est un ensemble composé de paires d'éléments appartenant à **V.**

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-93.png)
_Définition formelle d'un graphe avec ses ensembles correspondants_

Ci-dessus, nous avons représenté les deux principaux composants d'un graphe dans deux ensembles correspondants, un pour les sommets **V** et un autre pour les arêtes **E**. Ainsi, notre graphe **G** est finalement une paire ordonnée de ces ensembles. Mais avant de continuer, nous devons examiner à l'intérieur de ces ensembles pour voir à quoi ils ressemblent et comprendre pourquoi.

D'une part, **V** est une collection d'éléments **v** dans laquelle chaque élément contient les données nécessaires pour définir un sommet. Abstraitement, ils sont appelés avec la lettre **v** et un indice numérique. 

Mais en pratique, ils peuvent être des objets complexes contenant des paramètres, des profils, etc. 

D'autre part, l'ensemble des arêtes **E** est un peu plus compliqué à définir puisqu'il doit déterminer les connexions entre les sommets. Dans ce cas, les éléments sont des paires non ordonnées de sommets de l'ensemble **V** de sorte que chaque paire est de la forme **{x, y}**.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-94.png)
_Représentations formelles et graphiques d'un graphe_

Pour vous familiariser avec ces structures ci-dessus, vous avez un graphe arbitraire, entièrement défini avec ses ensembles respectifs. Dans **V**, vous pouvez voir tous les sommets numérotés de 1 à 5 et placés dans le diagramme supérieur dans une distribution spécifique, mais vous pouvez les organiser selon vos besoins. 

Pendant ce temps, dans **E**, vous pouvez observer toutes les arêtes (lignes) établissant un lien d'interconnexion entre les sommets. 

La terminologie appropriée pour aborder ce lien est la suivante : par exemple, si nous avons l'arête {v1, v4}, nous l'appelons **incidente** à v1 et v4. De plus, ces sommets sont désignés comme étant **adjacents** puisque une arête les relie.

Comme vous pouvez le remarquer, il n'y a pas d'arête {v4, v1} dans **E**. Mais pour trouver une explication à ce phénomène, nous devons introduire la principale distinction qui génère deux classes de graphes. 

La première **(non orienté)**, à laquelle appartiennent les exemples ci-dessus, inclut tous les graphes dont les arêtes peuvent être parcourues dans les deux directions. Cela les rend des paires **non ordonnées** de sommets. 

D'autre part, nous pouvons avoir un graphe dans lequel toutes ses arêtes ne peuvent être parcourues que dans une seule direction, c'est-à-dire d'un sommet à un autre exclusivement. Ainsi, ses paires de sommets sur l'ensemble **E** doivent être **ordonnées**, ce qui signifie que aller de v1 à v4 n'est pas la même chose que d'aller de v4 à v1. Cette deuxième classe est connue sous le nom de **graphe orienté**.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-95.png)
_Exemple d'un graphe orienté._

Avant d'apprendre à représenter un graphe de manière computationnelle pour effectuer des opérations sur celui-ci, vous devez comprendre le concept de **degré** de sommet. 

Dans les graphes non orientés, le degré d'un sommet fait référence au nombre d'arêtes incidentes à celui-ci, en considérant que les arêtes auto-connectées (boucles) comptent pour 2 dans le score total. 

En revanche, dans les graphes orientés, nous avons des valeurs de **degré entrant** et de **degré sortant** pour chaque sommet, représentant le nombre d'arêtes entrantes et sortantes, respectivement.

## Représentations des graphes

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1_Dc_opxjAdBqAmnbX1VLd9g.png)
_Les 2 méthodes les plus populaires pour stocker un graphe de manière computationnelle_

Parfois, la solution la plus intuitive pour un problème n'est pas toujours la plus efficace en informatique. Dans ce contexte, cela génère différentes façons de représenter un graphe selon la nature d'un problème.

### Qu'est-ce qu'une matrice d'adjacence ?

Une matrice d'adjacence est l'une des méthodes les plus populaires pour stocker un graphe sur un ordinateur. Mais son principal inconvénient est la consommation de mémoire inutilisée. 

Pour les graphes **orientés** comme celui ci-dessus, il y a une matrice de taille **|V|x|V|** (où |V| est la cardinalité de l'ensemble des sommets, donc le nombre de sommets sur le graphe) où chaque élément peut être un 0 s'il n'y a pas de connexion entre les sommets ou un 1 si l'élément de la ligne relie celui de la colonne par une arête sortante. De plus, si le graphe est [**pondéré**](https://www.baeldung.com/cs/weighted-vs-unweighted-graphs), la valeur 1 est remplacée par le paramètre de **poids** associé à chaque arête lorsque cela est nécessaire.

Cependant, si le graphe est **non orienté**, les mêmes critères s'appliquent avec la différence que cette fois-ci, aucune distinction n'est faite entre les arêtes sortantes et entrantes. Il y aura donc une valeur 1 si une arête existe entre les éléments de la ligne et de la colonne.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-96.png)
_Définition des éléments de la matrice d'adjacence pour chaque type de graphe._

### Qu'est-ce qu'une matrice d'incidence ?

Similaire à la méthode précédente, il y a une matrice de taille **|V|x|E|** dans laquelle les mêmes règles sont remplies. La différence est que si une arête **e** est entrante vers un sommet **v**, l'élément correspondant sera un -1 au lieu de 0.

### Comment utiliser les listes d'adjacence

Lorsque l'on utilise des matrices, si le graphe a beaucoup de sommets mais peu d'arêtes **(un graphe clairsemé)**, la matrice contiendra un grand nombre de zéros. Cela gaspille beaucoup de mémoire et rend la représentation inefficace en termes d'espace.

Pour résoudre ce problème, les **listes d'adjacence** sont apparues comme une alternative remplaçant les matrices par une combinaison de différentes structures de données – des tableaux et des listes chaînées. 

Le noyau de cette méthode est un tableau contenant tous les nœuds du graphe. Chaque élément du tableau aura une liste chaînée contenant les sommets voisins de chaque nœud principal (sommets adjacents). Dans le cas des graphes orientés, seuls les éléments voisins connectés par une arête sortante du nœud principal seront à l'intérieur de la liste chaînée.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-97.png)
_Exemple d'un graphe représenté sous forme de liste d'adjacence_

Ainsi, si nous avons un graphe **dense** avec un grand nombre d'arêtes, nous devons le stocker sous forme de **matrice**. Cela a l'avantage d'une complexité temporelle O(1) lors de la vérification de la connexion des sommets et de la symétrie de la matrice le long de la diagonale principale dans les graphes non orientés. 

Mais, si notre graphe est **clairsemé**, la faible densité des arêtes fait qu'une **liste d'adjacence** est le meilleur choix pour le représenter de manière computationnelle.

## Propriétés des graphes

Comme tout autre objet mathématique, les graphes ont des propriétés spécifiques qui les rendent uniques et fonctionnels pour leurs objectifs. Certaines concernent leur composition, d'autres la topologie, et même l'accessibilité. 

Sans aucun doute, les propriétés les plus pertinentes concernent les traversées, car elles nous permettent de modéliser et d'optimiser des scénarios du monde réel.

### Qu'est-ce qu'une traversée de graphe ? 

Tout d'abord, nous avons besoin d'un nœud de départ v1 et d'un nœud d'arrivée v2 pour traverser un graphe. Ensuite, nous pouvons définir une **marche** de v1 à v2 comme une séquence alternée de sommets et d'arêtes. Là, nous pouvons parcourir ces éléments autant que nous en avons besoin, et il y a toujours une arête après un sommet (sauf le dernier). 

Dans le cas où v1 est égal à v2, la marche serait **fermée**.

Cependant, nous pouvons ajouter des restrictions de répétition. Donc, si nous voulons une marche dans laquelle aucune arête n'est répétée, elle est renommée **"trajet"**. Par conséquent, si le trajet est fermé, il serait désigné comme **"circuit"**. 

Il en va de même si nous restreignons la répétition des sommets – la marche est renommée **"chemin"**, et un chemin fermé est connu sous le nom de **"cycle"**.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-98.png)
_Exemples formels et graphiques des types de traversée de réseau._

![Image](https://cdn-images-1.medium.com/max/800/1*jqQrm3fY_X5CEhCkbloQmw.png)

Cette capacité de traversée s'accompagne d'une propriété intéressante valable pour tous les graphes existants orientés/non orientés. Elle est formalisée comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1_Dc_opxjAdBqAmnbX1VLd9g-1.png)
_Formalisation de la propriété de la somme des degrés._

Cela établit que la somme de tous les degrés des sommets est égale à deux fois la cardinalité de l'ensemble des arêtes dans un graphe non orienté. Si orienté, la somme se divise en deux termes, chacun se référant à chaque nœud dans les degrés entrant et sortant. 

Cela est assez simple à prouver, car chaque fois que vous ajoutez une arête à un graphe, vous avez besoin de deux sommets pour construire la paire d'éléments stockés sur **E.** Donc, si vous ajoutez une boucle (arête reliant un nœud à lui-même), vous avez quand même besoin de définir une paire d'éléments de **V**, indépendamment du fait qu'ils soient les mêmes. 

Cette caractéristique nous soutient lorsque nous résolvons des questions comme :

> Étant donné un graphe **6-régulier** (avec tous ses degrés de sommets définis à 6) _de_ **n** sommets, combien d'arêtes aura-t-il ?

Comme sa résolution est immédiate, approfondir la réflexion sur des questions similaires améliore votre compréhension de sa nature et de la raison pour laquelle c'est ainsi.

### Qu'est-ce que la connectivité ?

Maintenant, passons aux propriétés liées à la capacité de liaison du graphe. En commençant par un graphe non orienté, nous pouvons affirmer qu'un sommet **v** atteint **u** s'il existe un chemin de **v** à **u**. De plus, nous pouvons examiner le graphe dans son ensemble et le définir comme **connexe** si chaque paire de sommets qui s'y trouve est effectivement connectée.

Être connecté est souvent associé à l'unicité de ses composants. C'est-à-dire que si nous finissons avec un graphe **déconnecté**, son nombre de composants sera toujours supérieur à 1. 

Vous pouvez imaginer un composant comme une zone du graphe isolée et déconnectée du reste des sommets. Et cela, si nous considérons un graphe, sera connecté et n'aura qu'un seul composant connecté comme s'il s'agissait d'un graphe connecté.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-99.png)
_Exemple d'un graphe composé de 2 composants._

En revanche, lorsque nous traitons des graphes **orientés**, deux sommets **u** et **v** sont dits **fortement** connectés s'ils peuvent se rejoindre mutuellement et **faiblement** connectés s'ils sont connectés sur le graphe **sous-jacent** (toutes les arêtes remplacées par des arêtes non orientées).

Comme vous pouvez l'imaginer, ces propriétés génèrent de nombreuses possibilités et de nouvelles caractéristiques à considérer. 

Pour mentionner brièvement, nous pouvons tirer parti de la nature discrète des graphes pour supprimer des nœuds et des arêtes de ceux-ci. Par conséquent, des concepts tels que les points d'articulation ou les ponts émergent comme l'une des façons les plus simples d'étudier les points faibles d'un graphe.

Un **point d'articulation** est un sommet qui, si nous le supprimons du graphe ainsi que toutes ses arêtes incidentes, le graphe augmentera ses composants connectés. 

De même, un **pont** est simplement une arête répondant à la même condition précédente avec la différence qu'aucun sommet n'est supprimé du graphe.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-100.png)
_Exemple visuel d'un point d'articulation et d'un pont._

En extension de la section sur les propriétés, il est intéressant de mentionner certains outils et caractéristiques des graphes qui nous aideront à reconnaître la clé des algorithmes que nous verrons plus tard :

### Qu'est-ce que les sous-graphes ?

Leur nom est un indicateur approprié de ce que sont les sous-graphes, car il est assez illustratif. Un **sous-graphe** est une collection de sommets et d'arêtes que nous pouvons extraire d'un graphe arbitraire **G** pour former un autre graphe, généralement de taille réduite. 

Formellement, un graphe **H** est un sous-graphe de **G** s'il est formé par un sous-ensemble de sommets de **G** et de manière similaire un sous-ensemble d'arêtes de **G**, chaque arête étant une paire valide de nœuds.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-101.png)
_Exemple de validité d'un sous-graphe_

Le nombre de classifications et de recherches que nous pouvons effectuer sur les sous-graphes rend impossible de tout couvrir ici. Mais la base pour un apprentissage ultérieur que nous commencerons avec les idées suivantes sur sa morphologie, sa topologie et sa composition.

Un sous-graphe **H** couvre un graphe **G** si les deux ont les mêmes sommets stockés sur l'ensemble **V**. Dans cette situation, le sous-graphe **H** est connu sous le nom de [**sous-graphe couvrant**](https://youtu.be/Kh9LiX2farU).

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-102.png)
_Exemple d'un sous-graphe couvrant._

Étant donné un graphe **G**, si nous appliquons l'opération de suppression de sommet n fois avec n<|V|, le graphe résultant sera un [**graphe induit**](https://youtu.be/1HXbz09Bipw).

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-103.png)
_Étapes prises pour atteindre un graphe induit._

La topologie ne concerne pas seulement les sous-graphes. Elle est également principalement étudiée avec des graphes généraux. Ainsi, passer en revue certaines classifications et caractéristiques larges rendra la théorie des graphes plus gérable.

Un graphe est dit **complet** s'il est non orienté, n'a pas de boucles et que chaque paire de nœuds distincts est connectée par une seule arête. De plus, nous pouvons avoir un graphe **n-complet** **Kn** en fonction du nombre de sommets.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-104.png)
_Exemple des 5 premiers graphes complets._

Nous devons également parler du domaine de la coloration des graphes. Un graphe est **bipartite** lorsque ses nœuds peuvent être divisés en deux [**ensembles disjoints**](https://en.wikipedia.org/wiki/Disjoint_sets) dont l'union résulte dans l'ensemble initial complet de sommets, avec la condition que chaque arête a ses extrémités sur les deux ensembles simultanément. Cela permet la possibilité de colorer chaque ensemble de sommets avec une couleur différente. 

De plus, il peut être un graphe [**bipartite complet**](https://youtu.be/VvCytJvd4H0) si les deux ensembles sont densément connectés (chaque sommet d'un ensemble est connecté avec tous les sommets de l'autre collection).

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-105.png)
_Quelques exemples de graphes bipartites complets arbitraires._

Vous pourriez également avoir besoin de représenter un graphe dans un plan sans que aucune de ses arêtes ne **s'intersecte**. Ensuite, si possible, le graphe sera **planaire**. Pour mieux comprendre l'état de cette caractéristique, nous pouvons utiliser le [**théorème de Kuratowski**](https://en.wikipedia.org/wiki/Kuratowski%27s_theorem). Il implique des concepts avancés comme l'**isomorphisme** et l'**homomorphisme** concernant les graphes complets k5 et les graphes bipartites complets k3,3.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-106.png)
_Différence visuelle entre les graphes planaires et non planaires._

### Quels sont les cycles particuliers ?

Enfin, certaines caractéristiques des graphes méritent une attention particulière. Par exemple, lorsqu'il s'agit de trouver des cycles, il existe une relation profonde avec les degrés des sommets, la topologie intégrale des graphes et la traversabilité. 

Pour visualiser cette relation, nous retournerons au problème de **Königsberg**. Dans celui-ci, nous devons traverser toutes les arêtes du graphe sans en répéter aucune, en commençant et en finissant au même sommet.

Puisque les graphes étaient nouveaux à l'époque, Euler a développé une solution en définissant un type unique de cycle que l'on ne trouve que dans les graphes répondant à des conditions précises – comme le degré de tous leurs nœuds étant pair. 

Ces cycles ont été nommés **Eulériens** d'après leur créateur, et chaque graphe qui en possède un est également appelé un **graphe Eulérien**. 

Il existe également des **chemins Eulériens**. Ceux-ci suppriment la condition de devoir commencer et finir au même sommet et nécessitent que le graphe ait exactement deux nœuds de degré impair, qui seront les extrémités du chemin.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1_Bg0mEKTsoZXGZwcD-F3_HQ.gif)
_Visualisation d'un chemin eulérien._

De plus, si nous nous concentrons sur des problèmes contemporains comme le problème du voyageur de commerce ([**TSP**](https://en.wikipedia.org/wiki/Travelling_salesman_problem)), un problème **NP-difficile** principalement utilisé par les entreprises de livraison et de logistique. 

Dans ce cas, nous réaliserons la pertinence des **cycles hamiltoniens** et des chemins pour soutenir des solutions pratiques à des questions similaires. Similaire à l'eulérianité, un graphe est **Hamiltonien** s'il contient un cycle dans lequel chaque sommet est utilisé au lieu des arêtes.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1_Bg0mEKTsoZXGZwcD-F3_HQ-1.gif)
_Visualisation d'un cycle hamiltonien._

Ces dernières propriétés deviennent difficiles à gérer, étant donné la complexité des problèmes impliqués. Bien que, connaître la fondation critique soutenant tout ce qui les entoure nous permet de continuer à explorer avec une confiance raisonnable.

## Algorithmes et théorie des graphes

Une fois que vous avez une solide compréhension de la théorie des graphes, de ses éléments, de ses attributs et de ses outils, nous devons également passer en revue certains algorithmes de base comprenant les principes de presque tous les autres processus de graphes. Ensuite, nous pouvons passer à l'utilisation de la théorie des graphes dans les projets de préservation du climat.

### Algorithme de recherche en largeur

Ici, nous ne considérerons que 3 algorithmes, car il en existe de nombreux types et très spécialisés pour des tâches déterminées.

Pour commencer avec quelque chose de simple et d'intuitif, nous allons démêler la [**recherche en largeur**](https://youtu.be/oDqjPvD54Ss). C'est un algorithme de traversée de graphe utilisé pour parcourir un graphe dans un mouvement en largeur. 

En termes simples, il commence à un sommet arbitraire et visite itérativement ses sommets adjacents, répétant cette étape jusqu'à ce qu'il n'y ait plus de sommets non visités. 

Ce comportement sert de chercheur de chemin le plus court à travers tous les nœuds du graphe, bien que vous puissiez arrêter l'exécution lorsqu'un sommet particulier est visité.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1_Bg0mEKTsoZXGZwcD-F3_HQ-2.gif)
_Représentation de l'algorithme de recherche en largeur_

### Algorithme de recherche en profondeur

Le deuxième algorithme est une variante du précédent, connu sous le nom de [**recherche en profondeur**](https://youtu.be/7fujbpJ0LB4). Son objectif est similaire mais est également utile pour détecter les cycles, les composants connectés, le [**tri topologique**](https://youtu.be/eL-KzMXSXXI), ou vérifier les partitions bipartites des graphes. 

Mais la manière dont il fonctionne diffère sur certains aspects, comme la précédence de la **profondeur** sur la **largeur** – c'est-à-dire que tous les nœuds voisins ne sont pas visités à chaque étape. Au lieu de cela, l'un d'eux est choisi pour un **approfondissement** supplémentaire, et le processus est répété jusqu'à ce que le chemin atteigne une impasse et revienne récursivement au nœud de départ, visitant chaque sommet.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1_Bg0mEKTsoZXGZwcD-F3_HQ-3.gif)
_Représentation de l'algorithme de recherche en profondeur_

### Algorithme du plus court chemin de Dijkstra

Enfin, le dernier que nous allons traiter est l'**algorithme de Dijkstra**, le solveur de problème de **plus court chemin à source unique** le plus répandu jamais créé. 

Il est conçu pour fonctionner dans des graphes pondérés avec des poids non négatifs, et tente de trouver l'itinéraire le plus efficace entre 2 nœuds sélectionnés. 

Comparé aux algorithmes précédents, ce changement augmente le nombre d'étapes avant l'achèvement. Cependant, l'idée clé derrière lui est simple :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-108.png)
_Exemple de graphe utilisé pour expliquer l'algorithme de Dijkstra_

Comme vous pouvez le voir dans l'exemple ci-dessus, si nous voulons aller de v1 à v2, nous pouvons sélectionner l'arête entre eux et arriver à notre destination après avoir parcouru six unités de distance. 

D'autre part, si nous choisissons de passer par les chemins v3 ou v4, nous marcherions sept unités. Nous devons donc prendre une **décision** sur le fait de prendre ou non un chemin particulier.

Sur les grands graphes, l'algorithme calcule les plus courts chemins provisoires le long de chaque nœud individuel. Il met ensuite à jour ces valeurs et minimise la "distance" (donnée par les poids) par une traversée complète du graphe, comme vous pouvez le voir dans [**cette**](https://youtu.be/EFg3u_E6eHU) animation.

## Pourquoi les graphes sont-ils importants pour atteindre la durabilité ?

À ce stade, vous avez peut-être réalisé que la théorie des graphes est précieuse car elle peut encapsuler et modéliser de manière abstraite des problèmes de nature nuancée. Surtout ceux dont l'origine découle de la nécessité de la société de poursuivre un degré de mondialisation qui apporte un niveau de bien-être à la vie de tous.

Pourtant, beaucoup d'entre nous ignorent que le confort que nous apprécions actuellement, apporté par les avancées en communications, transports, nutrition et divertissement, nécessite la coordination de systèmes complexes pour être en place. 

Ainsi, la surpopulation expérimentée depuis le vingtième siècle fait que ces systèmes sont si massifs qu'ils entraînent un impact environnemental sévère basé sur les émissions de CO2 et le déversement systématique de déchets dans les environnements naturels.

### Les graphes peuvent aider au transport de marchandises

Dans ce contexte, tout ce qui implique le transport de marchandises et la logistique contribue de manière significative aux émissions de CO2 dans l'atmosphère. C'est là que l'utilisation des graphes présente un avantage clair pour l'environnement. Ils peuvent trouver des chemins optimaux entre les villes ou les lieux du monde, réduisant les émissions des véhicules engagés dans un tel transport. 

Par exemple, vous pouvez expérimenter avec Google Maps en traçant des itinéraires entre des lieux éloignés. Vous remarquerez qu'il peut automatiquement choisir un itinéraire approprié, minimisant ainsi le coût environnemental correspondant. 

Google Maps fonctionne sur la base d'algorithmes de **plus court chemin à source unique** comme Dijkstra ou des algorithmes avancés tels que **A-star**. A-star est une variante heuristique de Dijkstra. Ceux-ci sont utilisés en combinaison avec d'autres mécanismes de graphes de pointe utilisés pour ajouter certaines contraintes aux algorithmes. 

### Les graphes peuvent aider à la gestion des déchets

Les graphes ont également une place dans l'industrie mondiale en simulant ou en gérant directement des **réseaux**, des processus de fabrication et des plannings. Ils peuvent potentiellement réduire la quantité d'énergie et de ressources incorrectement gérées/gaspillées.

Il est également intéressant de mentionner les nombreuses possibilités que les graphes ont à offrir lorsque nous traitons le problème de l'accumulation excessive de déchets. 

De nos jours, il est largement admis que les plantes et les arbres sont les principaux contributeurs à l'oxygène dans notre atmosphère grâce à la photosynthèse. Mais nous devons tenir compte du fait qu'entre 50 % et 85 % de l'oxygène libéré dans l'atmosphère chaque année est produit **sous la mer**. 

Ironiquement, les données sur les déchets jetés dans l'océan augmentent constamment à mesure que la société de consommation avance dans le temps, causant un impact dramatique sur les véritables poumons de notre planète, ainsi que sur les espèces animales qu'elle abrite. 

Pour éviter d'avoir à décider où déverser nos déchets, nous pouvons utiliser la théorie des graphes pour générer des simulations de systèmes physiques moléculaires, de structures atomiques et de réactions chimiques afin de développer de nouveaux matériaux recyclables ou biodégradables. Ceux-ci réduiraient l'impact environnemental des produits que nous utilisons. 

De plus, ces simulations ont le potentiel d'être utiles en biologie, où le décryptage du fonctionnement ultime de l'**ADN** peut conduire à une meilleure qualité des aliments, ainsi qu'à des méthodes de production de masse plus efficaces.

### Les graphes peuvent aider à l'apprentissage automatique et à l'IA

Enfin, l'application la plus connue des graphes est dans le domaine de l'**apprentissage automatique**. 

Malgré toutes les autres utilisations significatives des graphes en informatique (comme les réseaux de communication, les systèmes distribués ou les structures de données), l'apprentissage automatique nous a montré avec son évolution exponentielle au cours de la dernière décennie qu'il s'agit d'une technologie très prometteuse pour lutter contre le changement climatique. 

En termes simples, l'**apprentissage automatique** est un sous-ensemble de l'**intelligence artificielle** qui se concentre sur la capacité des machines à apprendre et à détecter des motifs dans de grands ensembles de données. Parfois, cet apprentissage est inspiré de phénomènes naturels comme les synapses des neurones humains, résultant en de nouvelles techniques telles que les [**réseaux de neurones artificiels**](https://en.wikipedia.org/wiki/Artificial_neural_network). 

En ce qui concerne la protection de l'environnement, la capacité de ces techniques à analyser de grandes quantités de données permet de mieux mesurer notre effet sur la planète. 

En tant qu'exemple concret, [**Joinus4theplanet**](https://joinus4theplanet.org/) est une initiative axée sur l'exploitation des réseaux sociaux pour sensibiliser à la valeur de la durabilité. Elle a développé un système d'apprentissage automatique capable d'effectuer le tri des déchets avec l'aide de [**modèles convolutionnels**](https://youtu.be/YRhxdVk_sIs) conçus pour traiter des données multidimensionnelles afin de pallier les effets d'un recyclage incorrect.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-109.png)
_Exemple d'un réseau social représenté sous forme de graphe. Image de [**Wikipedia.**](https://en.wikipedia.org/wiki/File:SocialNetworkAnalysis.png" rel="noopener ugc nofollow)_

## Conclusion

Si nous voulons maintenir un progrès considérable au sein de nos civilisations et offrir un avenir prospère aux générations futures, nous devons considérer les graphes comme un outil essentiel lors de la révision du fonctionnement de nos systèmes technologiques et économiques.