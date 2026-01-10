---
title: Trouver les plus courts chemins en utilisant la recherche en largeur d'abord
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-12T22:44:38.000Z'
originalURL: https://freecodecamp.org/news/exploring-the-applications-and-limits-of-breadth-first-search-to-the-shortest-paths-in-a-weighted-1e7b28b3307
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Dn4pxbJWrya6g1h0NNhaHw.png
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Trouver les plus courts chemins en utilisant la recherche en largeur d'abord
seo_desc: 'By Sachin Malhotra

  Do you know the amount of global air traffic in 2017? Do you know what the rise
  has been for air traffic over the past several years ? Well, lets look at some statistics.


  _Source: [https://www.statista.com/statistics/564769/airlin...'
---

Par Sachin Malhotra

Connaissez-vous le volume du trafic aérien mondial en 2017 ? Connaissez-vous l'augmentation du trafic aérien au cours des dernières années ? Eh bien, regardons quelques statistiques.

![Image](https://cdn-media-1.freecodecamp.org/images/6eQAOZ4fqSw7oBxo8eAFormyD7h6woe8upoG)
_Source : [https://www.statista.com/statistics/564769/airline-industry-number-of-flights/](https://www.statista.com/statistics/564769/airline-industry-number-of-flights/" rel="noopener" target="_blank" title=")_

Selon l'[Organisation de l'aviation civile internationale](https://www.icao.int/Pages/default.aspx) (OACI), un record de 4,1 milliards de passagers ont été transportés par l'industrie aéronautique sur des services réguliers en 2017. Et le nombre de vols a atteint 37 millions à l'échelle mondiale en 2017.

Cela représente beaucoup de passagers et beaucoup de vols occupant l'espace aérien quotidiennement à travers le monde. Puisqu'il y a des centaines et des milliers de ces vols partout dans le monde, il est inévitable qu'il existe différentes routes avec plusieurs escales entre un lieu et un autre.

Chaque vol a une source et une destination qui lui sont propres, ainsi qu'un prix standard pour un siège en classe économique qui lui est associé. Laissons de côté les billets en classe affaires et les sièges avec plus d'espace pour les jambes, etc. !

Dans un tel scénario, il est trop confus de choisir quel vol serait le meilleur si nous voulons aller d'un endroit à un autre.

Voyons le nombre d'options de vol que [StudentUniverse](https://www.studentuniverse.com/?noMoreRedirect=true) (qui propose des réductions pour les étudiants ?) me propose de Los Angeles à New Delhi.

![Image](https://cdn-media-1.freecodecamp.org/images/X9oBIPVUCIw5YKvkkmc8TymNyLLWtZdKto31)
_Chaque vol a un hyperlien Détails, donc nous avons recherché cela et trouvé 119 vols au total._

119 vols au total sont proposés. Ensuite, une fenêtre contextuelle apparaît sur le site web indiquant qu'il existe d'autres sites web qui pourraient proposer des vols similaires à des tarifs encore plus bas. ?

Autant de sites web et de vols innombrables pour une seule source et une seule destination.

En tant que développeur, si je veux résoudre ce problème, je construirais un système pour répondre efficacement aux requêtes suivantes :

* Nombre total de destinations accessibles (avec un nombre maximum d'escales) depuis ma position actuelle, et également lister ces destinations. 
Il faut garder ses options ouvertes lorsqu'on veut voyager ?.
* Il est un fait connu (à mon avis ?) qu'une route avec plusieurs escales tend à être une alternative moins chère aux vols directs. 
Ainsi, étant donné une source et une destination, nous pouvons vouloir trouver des routes avec au moins 2 ou 3 escales.
* Plus important encore : Quelle est la route la moins chère d'une source donnée à une destination donnée ?
* Et… Nous en viendrons à cela à la fin ?.

Comme vous pouvez le deviner, il pourrait y avoir potentiellement des milliers de vols en résultat des deux premières requêtes. Mais nous pouvons certainement réduire cela en fournissant d'autres critères pour diminuer la taille du résultat. Pour les besoins de cet article, concentrons-nous sur ces requêtes originales elles-mêmes.

### Modélisation du réseau de vols sous forme de graphe

Il est assez clair d'après le titre de cet article que les graphes seraient impliqués quelque part, n'est-ce pas ?

Modéliser ce problème comme un problème de parcours de graphe le simplifie grandement et rend le problème beaucoup plus traitable. Ainsi, en premier lieu, définissons notre graphe.

Nous modélisons le trafic aérien comme une :

* forêt
* pondérée
* possiblement cyclique
* dirigée. **G (V, E)**

**Dirigée** car chaque vol aura une source et une destination désignées. Celles-ci ont beaucoup de sens.

**Cyclique** car il est très possible de suivre une série de vols commençant à un endroit donné et se terminant au même endroit.

**Pondérée** car chaque vol a un coût qui lui est associé, qui serait le billet de vol en classe économique pour cet article.

Et enfin, une **forêt** car nous pourrions avoir plusieurs composantes connectées. Il n'est pas nécessaire que toutes les villes du monde aient un réseau de vols entre elles. Ainsi, le graphe peut être déconnecté, et donc une forêt.

Les sommets, **V**, seraient les lieux à travers le monde où il y a des aéroports fonctionnels.

Les arêtes, **E**, seraient représentatives de tous les vols constituant le trafic aérien. Une arête de `u -->`; v signifie simplement que vous avez un vol dirigé de l'emplacement / no`d`e u `t`o v .

![Image](https://cdn-media-1.freecodecamp.org/images/fUMFpsXMA9AJOyZjsIVzphouaIrojTB3nPbq)
_Réseau de vols échantillon avec l'étiquetage des coûts pour différents vols._

Maintenant que nous avons une idée de la manière de modéliser le réseau de vols sous forme de graphe, passons à la résolution de la première requête courante qu'un utilisateur pourrait avoir.

### Nombre total de destinations accessibles

Qui n'aime pas voyager ?

En tant que personne qui aime explorer différents endroits, vous voudriez savoir quelles sont toutes les destinations accessibles depuis votre aéroport local. Encore une fois, il y aurait des critères supplémentaires ici pour réduire les résultats de cette requête. Mais pour garder les choses simples, nous allons simplement essayer de trouver tous les lieux accessibles depuis notre aéroport local.

Maintenant que nous avons un graphe bien défini, nous pouvons appliquer des algorithmes de parcours pour le traiter.

En partant d'un point donné, nous pouvons utiliser soit la [recherche en largeur d'abord](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur) (BFS) soit la [recherche en profondeur d'abord](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur) (DFS) pour explorer le graphe ou les lieux accessibles depuis le lieu de départ **dans un nombre maximum d'escales.** Puisque cet article est entièrement consacré à l'algorithme de recherche en largeur d'abord, voyons comment nous pouvons utiliser le célèbre BFS pour accomplir cette tâche.

Nous allons initialiser la file d'attente BFS avec le lieu donné comme point de départ. Nous effectuons ensuite le parcours en largeur d'abord, et continuons jusqu'à ce que la file soit vide ou jusqu'à ce que le nombre maximum d'escales soit épuisé.

**Note :** Si vous n'êtes pas familier avec la recherche en largeur d'abord ou la recherche en profondeur d'abord, je vous recommande de lire [cet article](https://medium.freecodecamp.org/deep-dive-into-graph-traversals-227a90c6a261) avant de continuer.

Regardons le code pour initialiser notre structure de données de graphe. Nous devons également voir comment l'algorithme BFS finira par nous donner toutes les destinations accessibles depuis une source donnée.

Maintenant que nous avons une bonne idée de la manière dont le graphe doit être initialisé, regardons le code pour l'algorithme BFS.

L'exécution de `bfs` sur la ville de Los Angeles nous donnerait les destinations suivantes qui sont accessibles :

```
{'Chicago', 'France', 'Irlande', 'Italie', 'Japon', 'New Delhi', 'Norvège'}
```

C'était simple, n'est-ce pas ?

Nous verrons comment nous pouvons limiter le BFS à un nombre maximum d'escales plus tard dans l'article.

Dans le cas où nous avons un réseau de vols énorme, ce que nous aurions dans un scénario de production, nous ne voudrions pas idéalement explorer toutes les destinations accessibles depuis un point de départ donné.

C'est un cas d'utilisation si le réseau de vols est très petit ou ne concerne que quelques régions aux États-Unis.

Mais, pour un grand réseau, un cas d'utilisation plus réaliste serait de trouver toutes les routes de vol avec plusieurs escales. Examinons ce problème plus en détail et voyons comment nous pouvons le résoudre.

### Routes avec plusieurs escales

Il est un fait bien connu que, plus souvent qu'autrement, pour une source et une destination données, un voyage avec plusieurs escales est moins cher qu'un vol direct sans escale.

La plupart du temps, nous préférons le vol direct pour éviter les escales. De plus, les vols avec plusieurs escales ont tendance à prendre beaucoup de temps — que nous n'avons pas.

Cependant, si vous n'avez pas de délais à respecter et que vous voulez économiser de l'argent (et que vous êtes à l'aise avec la route à plusieurs escales que beaucoup de compagnies aériennes suggèrent), alors vous pourriez vraiment bénéficier de quelque chose comme cela.

De plus, vous pourriez passer par certains des plus beaux endroits du monde avec certains des aéroports les plus avancés que vous pouvez apprécier. Donc, c'est assez motivant en soi.

En termes de modèle de graphe dont nous avons parlé, étant donné une source et une destination, nous devons trouver des routes avec 2 escales ou plus pour une source et une destination données.

En tant qu'utilisateur final, nous ne voudrions pas voir les vols dans cet ordre pour cette requête :

```
[A, C, D, B], 2 escales, $X[A, E, D, C, F, W, G, T, B], 8 escales, $M[A, R, E, G, B], 3 escales, $K[A, Z, X, C, V, B, N, S, D, F, G, H, B, 11 escales, $P
```

Je sais. Personne dans son bon sens ne voudrait une route de vol avec 11 escales. Mais le point que j'essaie de faire est qu'un utilisateur final voudrait de la symétrie. Cela signifie qu'il voudrait voir tous les vols avec 2 escales en premier, puis tous les vols avec 3 escales et ainsi de suite jusqu'à peut-être un maximum de, disons, 5 escales.

Mais, toutes les routes de vol avec le même nombre d'escales doivent être affichées ensemble. C'est une exigence que nous devons satisfaire.

Voyons comment nous pouvons résoudre cela. Donc, étant donné le graphe des réseaux de vols, une source `S` et une destination `D`, nous devons effectuer un parcours en ordre de niveau et rapporter les routes de vol de `S -->`; D avec au moins 2 et au plus 5 escales. Cela signifie que nous devons faire un parcours en ordre de niveau jusqu'à une profondeur de 7 à partir du nœud de départ S .

Jetez un coup d'œil au code pour résoudre ce problème :

Cela pourrait ne pas être la meilleure façon de résoudre ce problème à grande échelle — la plus grande contrainte de mémoire serait due aux nœuds actuellement présents dans la file d'attente.

Puisque chaque nœud ou lieu peut avoir des milliers de vols vers d'autres destinations dans le monde, la file d'attente pourrait être énorme si nous stockons des données de vol réelles comme cela. Cela est juste pour démontrer l'un des cas d'utilisation de l'algorithme de recherche en largeur d'abord.

Maintenant, concentrons-nous simplement sur le parcours et regardons la manière dont il est fait. L'algorithme de parcours est simple en soi. Cependant, toute la complexité spatiale du parcours en ordre de niveau provient des éléments dans la file d'attente et de la taille de chaque élément.

Il existe plusieurs façons d'implémenter l'algorithme. De plus, chacune d'entre elles varie en termes de mémoire maximale consommée à tout moment par les éléments dans la file d'attente.

Nous voulons voir la mémoire maximale consommée par la file d'attente à tout moment pendant le parcours en ordre de niveau. Avant cela, construisons un réseau de vols aléatoire avec des prix aléatoires.

Regardons maintenant l'implémentation du parcours en ordre de niveau.

Ce qui précède est l'implémentation la plus facile et la plus directe de l'algorithme de parcours en ordre de niveau.

Avec chaque nœud que nous ajoutons à la file d'attente, nous stockons également les informations de niveau et nous poussons un tuple de `(nœud, niveau)` dans la file d'attente. Ainsi, chaque fois que nous retirons un élément de la file d'attente, nous avons les informations de niveau attachées au nœud lui-même.

Les informations de niveau pour notre cas d'utilisation signifieraient le nombre d'escales depuis la source jusqu'à cet endroit dans la route de vol.

Il s'avère que nous pouvons faire mieux en ce qui concerne la consommation de mémoire du programme. Regardons une approche légèrement meilleure pour effectuer le parcours en ordre de niveau.

L'idée ici est que nous ne stockons aucune information supplémentaire avec les nœuds étant poussés dans la file d'attente. Nous utilisons un objet `None` pour marquer la fin d'un niveau donné. Nous ne connaissons pas la taille d'un niveau à l'avance sauf pour le premier niveau, qui a simplement notre nœud `source`.

Ainsi, nous commençons la file d'attente avec `[source, None]` et nous continuons à retirer des éléments. Chaque fois que nous rencontrons un élément `None`, nous savons qu'un niveau s'est terminé et qu'un nouveau a commencé. Nous poussons un autre `None` pour marquer la fin de ce nouveau niveau.

Considérons un graphe très simple ici, puis nous allons faire un essai à sec à travers le graphe.

![Image](https://cdn-media-1.freecodecamp.org/images/goYMjFvXtEMQAndVXKeUTy2gPOrYPARq1H3k)

```
**************************************************** LEVEL 0 beginslevel = 0, queue = [A, None]level = 0, pop, A, push, B, C, queue = [None, B, C]pop None ******************************************* LEVEL 1 beginspush Nonelevel = 1, queue = [B, C, None]level = 1, pop, B, push, C, D, F, queue = [C, None, C, D, F]level = 1, pop, C, push, D, D (lol!), queue = [None, C, D, F, D, D]pop None ******************************************* LEVEL 2 beginspush Nonelevel = 2, queue = [C, D, F, D, D, None] .... and so on
```

J'espère que cela résume bien l'algorithme. C'est certainement une astuce ingénieuse pour effectuer un parcours en ordre de niveau, garder une trace des niveaux et ne pas rencontrer trop de problèmes de mémoire. Cela réduit certainement l'empreinte mémoire du code.

Ne vous laissez pas berner en pensant que c'est une grande amélioration.

C'en est une, mais vous devriez vous poser deux questions :

1. Quelle est l'ampleur de cette amélioration ?
2. Peut-on faire mieux ?

Je vais répondre à ces deux questions maintenant, en commençant par la deuxième question. La réponse à celle-ci est Oui !

Nous pouvons faire mieux ici et nous passer complètement du besoin de `None` dans la file d'attente. La motivation pour cette approche vient de l'approche précédente elle-même.

Si vous regardez de près l'essai à sec ci-dessus, vous pouvez voir que chaque fois que nous retirons un `None`, un niveau est terminé et l'autre est prêt pour le traitement. L'important est qu'un niveau entier suivant existe dans la file d'attente au moment du retrait d'un `None`. Nous pouvons utiliser cette idée de prendre en compte la taille de la file d'attente dans la logique de parcours.

Voici le pseudo-code pour cet algorithme amélioré :

```
queue = Queue()queue.push(S)level = 0while queue is not empty {      size = queue.size()      // size represents the number of elements in the current level      for i in 1..size {          element = queue.pop()          // Process element here          // Perform a series of queue.push() operations here
```

```
      level += 1
```

Et voici le code pour la même chose.

Le pseudo-code est explicite. Nous nous passons essentiellement du besoin d'un élément `None` supplémentaire par niveau et utilisons plutôt la taille de la file d'attente pour changer de niveaux. Cela conduirait également à une amélioration par rapport à la dernière méthode, mais dans quelle mesure ?

Jetez un coup d'œil au Jupyter Notebook suivant pour voir la différence de mémoire entre les trois méthodes.

* Nous suivons la taille maximale de la file d'attente à tout moment en considérant la somme des tailles des éléments individuels de la file d'attente.
* Selon la documentation de Python, `sys.getsizeof` retourne la taille du pointeur ou de la référence de l'objet en octets. Ainsi, nous avons économisé presque 4,4 Ko d'espace `(20224 — 15800 octets)` en passant à la méthode `None` depuis la méthode de parcours en ordre de niveau originale. Ce ne sont que les économies de mémoire pour cet exemple aléatoire, et nous ne sommes allés que jusqu'au 5ème niveau dans le parcours.
* La méthode finale ne donne qu'une amélioration de 16 octets par rapport à la méthode `None`. Cela est dû au fait que nous nous sommes débarrassés de seulement 4 objets `None` qui étaient utilisés pour marquer les 4 niveaux (à part le premier) que nous avons traités. Chaque taille de pointeur (pointeur vers un objet) est de 4 octets en Python sur un système 32 bits.

Maintenant que nous avons toutes ces routes multi-chemins intéressantes de notre source à notre destination et des algorithmes de parcours en ordre de niveau très efficaces pour les résoudre, nous pouvons examiner un problème plus lucratif à résoudre en utilisant notre propre BFS.

Quelle est la route de vol la moins chère de ma source à une destination donnée ? C'est quelque chose qui intéresserait instantanément tout le monde. Je veux dire, qui ne veut pas économiser de l'argent ?

### Plus court chemin d'une source donnée à une destination

Il n'y a pas beaucoup de description à donner pour l'énoncé du problème. Nous devons simplement trouver le plus court chemin et rendre l'utilisateur final heureux.

Algorithmiquement, étant donné un graphe orienté pondéré, nous devons trouver le plus court chemin de la source à la destination. Le plus court ou le moins cher serait une seule et même chose du point de vue de l'algorithme.

Nous n'allons pas décrire une solution BFS possible à ce problème car une telle solution serait intractable. Regardons le graphe ci-dessous pour comprendre pourquoi c'est le cas.

![Image](https://cdn-media-1.freecodecamp.org/images/ISBXi5XsxIfQ5AhgHeKmsEwBw12x8GtAsZRM)

Nous disons que BFS est l'algorithme à utiliser si nous voulons trouver le **plus court chemin** dans un [graphe non orienté et non pondéré](https://medium.freecodecamp.org/deep-dive-into-graph-traversals-227a90c6a261)**_._** La revendication pour BFS est que la première fois qu'un nœud est découvert pendant le parcours, cette distance depuis la source nous donnerait le plus court chemin.

La même chose ne peut pas être dite pour un graphe pondéré. Considérons le graphe ci-dessus. Si, par exemple, nous devions trouver le plus court chemin du nœud `A` à `B` dans la version non orientée du graphe, alors le plus court chemin serait le lien direct entre A et B. Ainsi, le plus court chemin aurait une longueur de `1` et BFS le trouverait correctement pour nous.

Cependant, nous traitons ici avec un graphe pondéré. Ainsi, la première découverte d'un nœud pendant le parcours **ne garantit pas** le plus court chemin pour ce nœud. Par exemple, dans le diagramme ci-dessus, le nœud `B` serait découvert initialement parce qu'il est le voisin de `A` et le coût associé à ce chemin (une arête dans ce cas) serait de `25`. Mais ce n'est pas le plus court chemin. Le plus court chemin est `A --> M --> E` --> B o`f` longueur 10.

La recherche en largeur d'abord n'a aucun moyen de savoir si une découverte particulière d'un nœud nous donnerait le plus court chemin vers ce nœud. Et donc, la seule façon possible pour BFS (ou DFS) de trouver le plus court chemin dans un graphe pondéré est de rechercher tout le graphe et de continuer à enregistrer la distance minimale de la source au sommet de destination.

Cette solution n'est pas réalisable pour un réseau énorme comme notre réseau de vols qui aurait potentiellement des milliers de nœuds.

Nous n'entrerons pas dans les détails de la manière dont nous pouvons résoudre cela. Cela est hors de portée pour cet article.

Que diriez-vous si je vous disais que BFS est l'algorithme idéal pour trouver le plus court chemin dans un graphe pondéré **avec une légère contrainte** ?

### Plus courts chemins sous contrainte

Puisque le graphe que nous aurions pour le réseau de vols est énorme, nous savons qu'explorer complètement n'est pas vraiment une possibilité.

Considérons le problème des plus courts chemins du point de vue du client. Lorsque vous voulez réserver un vol, voici les options que vous considérez idéalement :

* Il ne devrait pas être un vol trop long.
* Il devrait être dans votre budget (Très Important).
* Il peut avoir plusieurs escales mais pas plus de `K` où `K` peut varier d'une personne à l'autre.
* Enfin, nous avons des préférences personnelles qui impliquent des choses comme l'accès au salon, la qualité de la nourriture, les lieux d'escale et l'espace moyen pour les jambes.

Le point important à considérer ici est le troisième ci-dessus : il peut avoir plusieurs escales, mais pas plus de `K` où `K` peut varier d'une personne à l'autre.

Un client veut la route de vol la moins chère, mais il ne veut pas non plus, disons, 20 escales entre sa source et sa destination. Un client pourrait être d'accord avec un maximum de 3 escales, ou dans des cas extrêmes peut-être même 4 — mais pas plus que cela.

Nous voudrions une application qui trouverait la route de vol la moins chère avec [au plus K escales](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/) pour une source et une destination données.

![Image](https://cdn-media-1.freecodecamp.org/images/A3qPvKhi2p6Rfed4e28pAsR5wFDaB31-ai5V)
_Source : Leetcode.com_

Cette question de LeetCode a été la principale motivation pour moi d'écrire cet article. Je recommande fortement de lire la question une fois et de ne pas se fier uniquement à l'instantané ci-dessus.

« Pourquoi BFS fonctionnerait-il ici ? » pourrait-on demander. « C'est aussi un graphe pondéré et la même raison de l'échec de BFS que nous avons discutée dans la section précédente devrait s'appliquer ici. » NON !

Le nombre de niveaux que la recherche atteindrait est limité par la valeur `K` dans la question ou dans la description fournie au début de la section. Ainsi, essentiellement, nous essaierions de trouver le plus court chemin, mais nous n'aurions pas à explorer tout le graphe en tant que tel. Nous irions simplement jusqu'au niveau `K`.

Dans un scénario de la vie réelle, la valeur de `K` serait inférieure à 5 pour tout voyageur sensé ?.

Regardons le pseudo-code pour l'algorithme :

```
def bfs(source, destination, K):      min_cost = dictionary representing min cost under K stops for each node reachable from source. 
```

```
      set min_cost of source to be 0
```

```
      Q = queue()      Q.push(source)      stops = 0      while Q is not empty {
```

```
           size = Q.size           for i in range 1..size {                 element = Q.pop() 
```

```
                 if element == destination then continue
```

```
                 for neighbor in adjacency list of element {                        if stops == K and neighbor != destination        then continue  
```

```
                        if min_cost of neighbor improves, update and add back to the queue.                }           }               stops ++       }
```

Ceci est à nouveau un parcours en ordre de niveau et l'approche utilisée ici est celle qui utilise la taille de la file d'attente à chaque niveau. Regardons une version commentée du code pour résoudre ce problème.

**Essentiellement, nous gardons une trace de la distance minimale de chaque nœud depuis la source donnée. La distance minimale pour la source serait de 0 et +inf pour tous les autres initialement.**

Chaque fois que nous rencontrons un nœud, nous vérifions si la longueur du chemin minimal actuel peut être améliorée ou non. Si elle peut être améliorée, cela signifie que nous avons trouvé un chemin alternatif de la source à ce sommet avec un coût moins cher — une route de vol moins chère jusqu'à ce sommet. Nous mettons à nouveau ce sommet en file d'attente afin que les lieux et les nœuds accessibles à partir de ce sommet soient mis à jour (peut-être ou peut-être pas) également.

La chose clé est celle-ci :

```
# Pas besoin de mettre à jour le coût minimal si nous avons déjà épuisé nos K escales. if stops == K and neighbor != dst:    continue
```

Ainsi, nous venons de retirer le nœud représenté par `element` dans le code et `neighbor` peut être soit une destination, soit un autre nœud aléatoire. Si nous avons déjà épuisé nos `K` escales avec `element` étant la `Kème` escale, alors nous ne devrions pas traiter et mettre à jour (éventuellement) la distance minimale pour `neighbor`. Cela violerait notre condition maximale de `K` escales dans ce cas.

Il s'avère que j'ai résolu ce problème à l'origine en utilisant la programmation dynamique et cela a pris environ 165 ms pour s'exécuter sur la plateforme LeetCode. J'ai exécuté en utilisant BFS et c'était extrêmement rapide avec seulement 45 ms pour s'exécuter. Assez de motivation pour écrire cet article pour vous, les gars.

J'espère que vous avez pu tirer quelque bénéfice de cet article sur la recherche en largeur d'abord et certaines de ses applications. L'accent principal était de montrer son application aux plus courts chemins dans un graphe pondéré sous certaines contraintes ?.