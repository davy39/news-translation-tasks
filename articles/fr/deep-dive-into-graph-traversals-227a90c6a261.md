---
title: Plongée approfondie dans les traversées de graphes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T22:08:58.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-graph-traversals-227a90c6a261
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Pebp8Cds-RLs417qaOS_8A.png
tags:
- name: algorithms
  slug: algorithms
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Plongée approfondie dans les traversées de graphes
seo_desc: 'By Sachin Malhotra

  There are over 2.07 billion monthly active Facebook Users worldwide as of Q3 2017.
  The most important aspect of the Facebook network is the social engagement between
  users. The more friends a user has, the more engaging the convers...'
---

Par Sachin Malhotra

Il y a plus de 2,07 milliards d'utilisateurs actifs mensuels sur Facebook dans le monde au troisième trimestre 2017. L'aspect le plus important du réseau Facebook est l'engagement social entre les utilisateurs. Plus un utilisateur a d'amis, plus les conversations deviennent engageantes via les commentaires sur les publications, les messages, etc. Si vous avez utilisé Facebook de manière assez régulière, vous devez connaître la fonctionnalité de recommandation d'amis.

Facebook recommande un ensemble de personnes que nous pouvons ajouter comme amis. La plupart du temps, ce sont des personnes dont nous n'avons jamais entendu parler auparavant. Pourtant, Facebook pense que nous devrions les ajouter. La question est : **comment Facebook parvient-il à établir un ensemble de recommandations pour une personne spécifique** ?

Une façon de faire cela est basée sur les amis communs. Par exemple :- Si un utilisateur A et C ne se connaissent pas, mais qu'ils ont un ami commun B, alors probablement A et C devraient aussi être amis. Et si A et C ont 2 amis communs et A et D ont 3 amis communs ? Comment l'ordre des suggestions sera-t-il ?

Dans ce cas, il semble assez évident de suggérer D plutôt que C à A parce qu'ils ont plus d'amis communs et sont plus susceptibles de se connecter.

Cependant, deux personnes peuvent ne pas toujours avoir d'amis communs, mais elles peuvent avoir des connexions communes de 2e ou 3e degré.

### Connexions de Nième Degré

* A et B sont amis. **(0 degré)**
* A et B sont des amis de **1er degré**, ce qui signifie qu'ils ont un ami commun.
* A et B sont des amis de **2e degré** s'ils ont un ami qui est un ami de 1er degré avec l'autre personne. Par exemple :- A — C — D — B, alors A et B sont des amis de 2e degré.
* De même, A et B sont des amis de **Nième degré** s'ils ont N connexions entre eux. Par exemple :- A — X1 — X2 — X3….. — XN — B.

En regardant cette approche pour la recommandation, nous devons être capables de trouver le degré d'amitié que deux utilisateurs donnés partagent sur Facebook.

### Entrée dans les Traversées de Graphes

Maintenant que nous savons comment les recommandations d'amis peuvent être faites, reformulons ce problème afin que nous puissions l'examiner d'un point de vue algorithmique.

Imaginons un graphe non orienté de tous les utilisateurs de Facebook, où les sommets **V** représentent les utilisateurs et les arêtes **E** représentent les amitiés. En d'autres termes : si les utilisateurs A et B sont amis sur Facebook, il y a une arête entre les sommets A et B. Le défi est de trouver le degré de connexion entre deux utilisateurs.

Plus formellement, nous devons voir la distance la plus courte entre deux nœuds dans un graphe non orienté et non pondéré.

![Image](https://cdn-media-1.freecodecamp.org/images/QilmOLSsdharIgiiepyEGax0G1QKOK6xF-Bc)

Considérons deux sommets dans ce graphe non orienté A et C. Il y a deux chemins différents pour atteindre C :

1. A → B → C et   
2. A → G → F → E → D → C

Clairement, nous voulons prendre le chemin le plus court lorsque nous essayons de voir le degré de connexion entre deux personnes sur le réseau social.

Jusqu'à présent, tout va bien.

Avant de continuer, regardons la complexité de ce problème. Comme indiqué précédemment, Facebook compte environ 2,07 milliards d'utilisateurs au troisième trimestre 2017. Cela signifie que notre graphe aura environ 2,07 milliards de nœuds et au moins (2,07 milliards — 1) arêtes (si chaque personne a au moins un ami).

C'est une échelle énorme pour résoudre ce problème. De plus, nous avons également vu qu'il peut y avoir plusieurs chemins pour atteindre un sommet de destination donné à partir d'un sommet source dans le graphe, et nous voulons le plus court pour résoudre notre problème.

Nous allons examiner deux algorithmes classiques de traversée de graphes pour résoudre notre problème :

1. Recherche en profondeur et   
2. Recherche en largeur.

### Recherche en Profondeur

Imaginez que vous êtes coincé dans un labyrinthe comme celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/ofXCEYDsZ5onF2rYKX4gsLuWej0dov1FkegH)

Vous devez sortir d'une manière ou d'une autre. Il peut y avoir plusieurs routes depuis votre position de départ jusqu'à la sortie. L'approche naturelle pour sortir du labyrinthe est d'essayer tous les chemins.

Supposons que vous avez deux choix à l'endroit où vous vous trouvez actuellement. Évidemment, vous ne savez pas lequel mène à la sortie du labyrinthe. Vous décidez donc de faire le premier choix et de continuer dans le labyrinthe.

Vous continuez à faire des mouvements et vous continuez à avancer jusqu'à ce que vous atteigniez une impasse. Maintenant, vous voudriez idéalement essayer un chemin différent, et donc vous **retournez en arrière** à un point de contrôle précédent où vous avez fait l'un des choix, puis vous essayez un nouveau chemin, c'est-à-dire un chemin différent cette fois.

Vous continuez à faire cela jusqu'à ce que vous trouviez la sortie.

Essayer récursivement un chemin spécifique et revenir en arrière sont les deux composantes formant l'**algorithme de recherche en profondeur** (DFS).

Si nous modélisons le problème du labyrinthe comme un graphe, les sommets représenteraient la position de l'individu dans le labyrinthe et les arêtes dirigées entre deux nœuds représenteraient un seul mouvement d'une position à une autre. En utilisant DFS, l'individu essayerait tous les chemins possibles jusqu'à ce que la sortie soit trouvée.

Voici un exemple de pseudo-code pour cela.

```
1  procédure DFS(G,v):2      étiqueter v comme découvert3      pour toutes les arêtes de v à w dans G.adjacentEdges(v) faire4          si le sommet w n'est pas étiqueté comme découvert alors5              appeler récursivement DFS(G,w)
```

Pour une plongée plus profonde dans cet algorithme, consultez :-

[**Plongée approfondie dans un graphe : Traversée DFS**](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)  
[_Pour le meilleur ou pour le pire, il y a toujours plus d'une façon de faire quelque chose. Heureusement pour nous, dans le monde du logiciel et_medium.com](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13)

Complexité temporelle : O(V + E)

### Recherche en Largeur

Imaginez une maladie contagieuse se propageant progressivement dans une région. Chaque jour, les personnes atteintes de la maladie infectent de nouvelles personnes avec lesquelles elles entrent en contact physique. De cette manière, la maladie effectue une sorte de **recherche en largeur** (BFS) sur la population. La « file d'attente » est l'ensemble des personnes qui viennent d'être infectées. Le graphe est le réseau de contacts physiques de la région.

Imaginez que vous devez simuler la propagation de la maladie à travers ce réseau. Le nœud racine de la recherche est le patient zéro, le premier connu à souffrir de la maladie. Vous commencez avec lui seul atteint de la maladie, et personne d'autre.

Maintenant, vous itérez sur les personnes avec lesquelles il est en contact. Certaines attraperont la maladie. Maintenant, itérez sur toutes ces personnes. Donnez la maladie aux personnes avec lesquelles elles sont en contact, à moins qu'elles ne l'aient déjà eue. Continuez jusqu'à ce que vous ayez infecté tout le monde, ou que vous ayez infecté votre cible. Ensuite, vous avez terminé. C'est ainsi que fonctionne la recherche en largeur.

![Image](https://cdn-media-1.freecodecamp.org/images/h1o4ufzwbIWjUvVCMPRNbkRsBwnrt19OMz8R)

L'algorithme de recherche BFS explore les sommets couche par couche en commençant par le tout premier sommet et ne passant à la couche suivante que lorsque tous les sommets de la couche actuelle ont été traités.

Voici un exemple de pseudo-code pour BFS.

```
1   procédure BFS(G, v):2       q = File()3       q.enfiler(v)4       tant que q n'est pas vide:5            v = q.defiler()6            si v n'est pas visité:7               marquer v comme visité (// Traiter le nœud)8               pour toutes les arêtes de v à w dans G.adjacentEdges(v) faire9                    q.enfiler(w)
```

Pour une compréhension plus approfondie de BFS, consultez [cet article](https://medium.com/basecs/going-broad-in-a-graph-bfs-traversal-959bd1a09255).

Complexité temporelle : O(V + E)

### Plus Courts Chemins

Allons de l'avant et résolvons notre problème initial : trouver le plus court chemin entre deux sommets donnés dans un graphe non orienté.

En regardant les complexités temporelles des deux algorithmes, nous ne pouvons pas vraiment faire la différence entre les deux pour ce problème. Les deux algorithmes trouveront un chemin (ou plutôt le plus court chemin) vers notre destination à partir de la source donnée.

Regardons l'exemple suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/Ke3GbCDyCsDEJbc2Q9o9vFkKN0gk-Q-FNF-r)

**Supposons que nous voulons trouver le plus court chemin du nœud 8 à 10**. Regardons les nœuds que DFS et BFS explorent avant d'atteindre la destination.

#### DFS

* **Traiter** 8 → **Traiter** 3 → **Traiter** 1.
* Retour en arrière à 3.
* **Traiter** 6 → **Traiter** 4.
* Retour en arrière à 6.
* **Traiter** 7.
* Retour en arrière à 6 → Retour en arrière à 3 → Retour en arrière à 8.
* **Traiter 10**.

Un total de 7 nœuds sont traités ici avant d'atteindre la destination. Maintenant, regardons comment BFS fait les choses.

#### BFS

* **Traiter** 8 → Enfiler 3, 10
* **Traiter** 3 → Enfiler 1,6
* **Traiter** 10.

Wow, c'était rapide ! Seulement 3 nœuds ont dû être traités et nous étions à notre destination.

L'explication de cette accélération que nous pouvons voir dans BFS et non dans DFS est que DFS prend un chemin spécifique et va jusqu'au bout, c'est-à-dire jusqu'à ce qu'il atteigne une impasse, puis revient en arrière.

C'est le principal inconvénient de l'algorithme DFS. Il peut avoir à explorer des milliers de niveaux (dans un réseau énorme comme celui de Facebook, simplement parce qu'il a sélectionné un mauvais chemin à traiter dès le début) avant d'atteindre le chemin contenant notre destination. BFS ne rencontre pas ce problème et est donc beaucoup plus rapide pour notre problème.

De plus, même si DFS trouve la destination, nous ne pouvons pas être sûrs que le chemin pris par DFS est le plus court. Il peut y avoir d'autres chemins également.

Cela signifie que dans tous les cas, pour le problème des plus courts chemins, DFS devrait parcourir l'ensemble du graphe pour obtenir le plus court chemin.

Dans le cas de BFS, cependant, la première occurrence du nœud de destination garantit qu'il s'agit de celui à la distance la plus courte de la source.

### Conclusion

Jusqu'à présent, nous avons discuté du problème des recommandations d'amis par Facebook et nous l'avons réduit au problème de trouver le degré de connexions entre deux utilisateurs dans le graphe du réseau.

Ensuite, nous avons discuté de deux algorithmes intéressants de traversée de graphes qui sont très couramment utilisés. Enfin, nous avons examiné quel algorithme performe le mieux pour résoudre notre problème.

**La recherche en largeur est l'algorithme que vous voulez utiliser si vous devez trouver la distance la plus courte entre deux nœuds dans un graphe non orienté et non pondéré.**

Regardons [ce problème amusant](https://leetcode.com/problems/minimum-genetic-mutation/description/) pour dépeindre la différence entre les deux algorithmes.

En supposant que vous avez lu attentivement l'énoncé du problème, essayons de modéliser cela comme un problème de graphe en premier lieu.

Que toutes les chaînes possibles deviennent des nœuds dans le graphe et nous avons une arête entre deux sommets s'ils ont une seule mutation entre eux.

Facile, n'est-ce pas ?

_Nous avons une chaîne de départ (lire sommet source) par exemple :- « AACCGGTT » et nous devons atteindre la chaîne de destination (lire sommet de destination) « AACCGGTA » en un nombre minimum de mutations (lire nombre minimum d'étapes) de sorte que toutes les chaînes intermédiaires (nœuds) doivent appartenir à la banque de mots donnée._

Essayez de résoudre ce problème par vous-même avant de regarder la solution ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/LCRoBOR966pUcZirT-TPB6TgF6q-ZQHLBHXB)

Si vous essayez de le résoudre en utilisant DFS, vous trouverez sûrement une solution, mais il y a un cas de test (ou plusieurs) qui dépassera la limite de temps allouée sur la plateforme LeetCode. C'est à cause du problème décrit précédemment quant à la raison pour laquelle DFS prend si longtemps (traiter 7 nœuds par opposition à 3 dans BFS) pour atteindre le sommet de destination.

J'espère que vous avez compris l'idée principale derrière les deux principales traversées de graphes, et la différence entre elles lorsque l'application est les plus courts chemins dans un graphe non orienté et non pondéré.

Veuillez recommander (❤) cet article si vous pensez qu'il peut être utile pour quelqu'un !