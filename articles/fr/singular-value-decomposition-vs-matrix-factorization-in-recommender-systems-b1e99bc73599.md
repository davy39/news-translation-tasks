---
title: Décomposition en valeurs singulières vs. Factorisation de matrices dans les
  systèmes de recommandation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-26T21:57:01.000Z'
originalURL: https://freecodecamp.org/news/singular-value-decomposition-vs-matrix-factorization-in-recommender-systems-b1e99bc73599
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CMxI-q0DAMtcF-VGs10G0Q.jpeg
tags:
- name: Matrix Factorization
  slug: matrix-factorization
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: recommender-systems
  slug: recommender-systems
- name: 'tech '
  slug: tech
seo_title: Décomposition en valeurs singulières vs. Factorisation de matrices dans
  les systèmes de recommandation
seo_desc: 'By K. Delphino

  Recently, after watching the Recommender Systems class of Prof. Andrew Ng’s Machine
  Learning course, I found myself very discomforted not understanding how Matrix Factorization
  works.

  I know sometimes the math in Machine Learning is ve...'
---

Par K. Delphino

Récemment, après avoir regardé le cours sur les systèmes de recommandation du Prof. Andrew Ng dans son [cours de Machine Learning](https://www.coursera.org/learn/machine-learning), je me suis senti très mal à l'aise de ne pas comprendre comment fonctionne la factorisation de matrices.

Je sais que parfois les mathématiques en Machine Learning sont très obscures. Il est préférable de les considérer comme une boîte noire, mais ce modèle était très "magique" selon mes standards.

Dans de telles situations, j'essaie généralement de chercher sur Google des références supplémentaires pour mieux comprendre le concept. Cette fois, je me suis encore plus confondu. Alors que le Prof. Ng appelait l'algorithme (Low Factor) Matrix Factorization, j'ai trouvé une nomenclature différente sur Internet : Singular Value Decomposition.

Ce qui m'a le plus confondu, c'est que la Décomposition en valeurs singulières était très différente de ce que le Prof. Ng avait enseigné. Les gens continuaient de suggérer qu'ils étaient tous les deux la même chose.

Dans ce texte, je vais résumer mes découvertes et essayer de clarifier certaines des confusions que ces termes peuvent causer.

### Systèmes de recommandation

Les systèmes de recommandation (RS) sont simplement des moyens automatisés de recommander quelque chose à quelqu'un. Ces systèmes sont largement utilisés par les entreprises de commerce électronique, les services de streaming et les sites d'actualités. Ils aident à réduire la friction des utilisateurs lorsqu'ils essaient de trouver quelque chose qu'ils aiment.

Les RS ne sont définitivement pas une nouveauté : ils existent depuis au moins [1990](https://pdfs.semanticscholar.org/d663/d25cbc8212adf560b2b1f19a8800bd610ec2.pdf). En fait, une partie de l'engouement récent pour le Machine Learning peut être attribuée à l'intérêt pour les RS. En 2006, Netflix a fait un splash lorsqu'ils ont sponsorisé un concours pour trouver le meilleur RS pour leurs films. Comme nous le verrons bientôt, cet événement est lié au désordre de nomenclature qui a suivi.

### La représentation matricielle

Il existe de nombreuses façons de penser à recommander un film à quelqu'un. Une stratégie qui s'est avérée très efficace consiste à traiter les notes de films comme une matrice Utilisateurs x Films comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gKdORo4UrfI1hTyK_Ple9Q.png align="left")

*Créé avec* [*https://sheetsu.com/*](https://sheetsu.com/)

Dans cette matrice, les points d'interrogation représentent les films qu'un utilisateur n'a pas notés. La stratégie consiste alors à prédire ces notes d'une manière ou d'une autre et à recommander aux utilisateurs les films qu'ils aimeront probablement.

### Factorisation de matrices

Une réalisation très intelligente faite par les participants au concours de Netflix (notamment [Simon Funk](https://sifter.org/simon/journal/20061211.html)) était que les notes des utilisateurs n'étaient pas simplement des devinettes aléatoires. Les évaluateurs suivent probablement une logique où ils pondèrent les choses qu'ils aiment dans un film (une actrice spécifique ou un genre) par rapport aux choses qu'ils n'aiment pas (longue durée ou mauvaises blagues) et donnent ensuite une note.

Ce processus peut être représenté par une formule linéaire de la forme suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qEOpviYMyBHFXxVGMVPh_Q.png align="left")

où *xₘ* est un vecteur colonne avec les valeurs des caractéristiques du film *m* et *θᵤ* est un autre vecteur colonne avec les poids que l'utilisateur *u* donne à chaque caractéristique. Chaque utilisateur a un ensemble différent de poids et chaque film a un ensemble différent de valeurs pour ses caractéristiques.

Il s'avère que si nous fixons arbitrairement le nombre de caractéristiques et ignorons les notes manquantes, nous pouvons trouver un ensemble de poids et de valeurs de caractéristiques qui créent une nouvelle matrice avec des valeurs proches de la matrice de notation originale. Cela peut être fait avec une descente de gradient, très similaire à celle utilisée dans la régression linéaire. Au lieu de cela, nous optimisons maintenant deux ensembles de paramètres (poids et caractéristiques) en même temps.

En utilisant le tableau que j'ai donné comme exemple ci-dessus, le résultat du problème d'optimisation générerait la nouvelle matrice suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HRQtOWAk57l5defVkDgX5Q.png align="left")

Remarquez que la matrice résultante ne peut pas être une copie exacte de l'originale dans la plupart des ensembles de données réels, car dans la vie réelle, les gens ne font pas de multiplications et de sommations pour noter un film. Dans la plupart des cas, la note est simplement une impression instinctive qui peut également être affectée par toutes sortes de facteurs externes. Néanmoins, notre espoir est que la formule linéaire soit un bon moyen d'exprimer la logique principale qui guide les notes des utilisateurs.

D'accord, maintenant nous avons une matrice approximative. Mais comment cela nous aide-t-il à prédire les notes manquantes ? Rappelez-vous que pour construire la nouvelle matrice, nous avons créé une formule pour remplir toutes les valeurs, y compris celles qui sont manquantes dans la matrice originale. Donc, si nous voulons prédire la note manquante d'un utilisateur pour un film, nous prenons simplement toutes les valeurs des caractéristiques de ce film, nous les multiplions par tous les poids de cet utilisateur et nous additionnons le tout. Donc, dans mon exemple, si je veux prédire la note de l'utilisateur 2 pour le film 1, je peux faire le calcul suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*e-3sZLqlse0MXpfJleV-rA.png align="left")

Pour clarifier les choses, nous pouvons dissocier les *θ* et les *x* et les mettre dans leurs propres matrices (disons *P* et *Q*). Cela est effectivement une factorisation de matrice, d'où le nom utilisé par le Prof. Ng.

Cette factorisation de matrice est essentiellement ce que Funk a fait. Il a obtenu la troisième place dans le concours de Netflix, attirant beaucoup d'attention (ce qui est un cas intéressant où une troisième place est plus célèbre que les gagnants). Son approche a été répliquée et affinée depuis et est encore utilisée dans de nombreuses applications.

### Décomposition en valeurs singulières

Entrez la Décomposition en valeurs singulières (SVD). La SVD est une méthode sophistiquée pour factoriser une matrice en trois autres matrices (*A = UΣVᵀ*). La manière dont la SVD est effectuée garantit que ces trois matrices possèdent certaines propriétés mathématiques intéressantes.

Il existe de nombreuses [applications pour la SVD](https://en.wikipedia.org/wiki/Singular_value_decomposition#Applications_of_the_SVD). L'une d'entre elles est l'Analyse en Composantes Principales (PCA), qui consiste simplement à réduire un ensemble de données de dimension *n* à une dimension *k* (*k < n*).

Je ne vous donnerai pas plus de détails sur les SVD car [je ne les connais pas](https://towardsdatascience.com/svd-8c2f72e264f) moi-même. Le point est que **ce n'est pas la même chose** que ce que nous avons fait avec la factorisation de matrices. La plus grande preuve est que la SVD crée trois matrices alors que la factorisation de matrices de Funk n'en crée que deux.

Alors pourquoi la SVD apparaît-elle chaque fois que je cherche des systèmes de recommandation ? J'ai dû creuser un peu, mais j'ai finalement trouvé quelques pépites cachées. Selon [Luis Argerich](https://www.quora.com/What-is-the-difference-between-SVD-and-matrix-factorization-in-context-of-recommendation-engine/answer/Luis-Argerich) :

> Les algorithmes de factorisation de matrices utilisés pour les systèmes de recommandation tentent de trouver deux matrices : P, Q telles que P*Q correspond aux valeurs CONNUES de la matrice d'utilité. 
> 
> Ce principe est apparu dans le célèbre article SVD++ "Factorization meets the neighborhood" qui, malheureusement, a utilisé le nom "SVD++" pour un algorithme qui n'a **absolument aucun rapport avec la SVD**.

Pour l'enregistrement, je pense que Funk, et non les auteurs de SVD++, a d'abord proposé la factorisation de matrices mentionnée pour les systèmes de recommandation. En fait, SVD++, comme son nom l'indique, est une extension du travail de Funk.

[Xavier Amatriain](https://www.quora.com/Whats-the-difference-between-SVD-and-SVD++/answer/Xavier-Amatriain) nous donne une vue d'ensemble plus large :

> Commençons par souligner que la méthode généralement appelée "SVD" utilisée dans le contexte des recommandations **n'est pas, à proprement parler, la Décomposition en valeurs singulières mathématique** d'une matrice, mais plutôt une manière approximative de calculer l'approximation de faible rang de la matrice en minimisant la perte d'erreur quadratique. Une manière plus précise, bien que plus générique, d'appeler cela serait la factorisation de matrices. La version initiale de cette approche dans le contexte du Netflix Prize a été présentée par Simon Funk dans son célèbre article de blog Try This at Home. Il est important de noter que l'approche "vraie SVD" avait effectivement été appliquée à la même tâche des années auparavant, avec moins de succès pratique.

Wikipedia contient également des informations similaires dans son article sur la [factorisation de matrices (systèmes de recommandation)](https://en.wikipedia.org/wiki/Matrix_factorization_%28recommender_systems%29) :

> L'algorithme original proposé par Simon Funk dans son article de blog factorise la matrice de notation utilisateur-article en tant que produit de deux matrices de dimension inférieure, la première ayant une ligne pour chaque utilisateur, tandis que la seconde a une colonne pour chaque article. La ligne ou la colonne associée à un utilisateur ou à un article spécifique est appelée facteurs latents. Notez que, malgré son nom, **dans FunkSVD, aucune décomposition en valeurs singulières n'est appliquée.**

Pour résumer :

1. La SVD est une technique mathématique quelque peu complexe qui factorise les matrices en trois nouvelles matrices et a de nombreuses applications, y compris la PCA et les RS.

2. Simon Funk a appliqué une stratégie très intelligente lors du concours Netflix de 2006, factorisant une matrice en deux autres et utilisant la descente de gradient pour trouver des valeurs optimales des caractéristiques et des poids. **Ce n'est pas de la SVD**, mais il a utilisé ce terme pour décrire sa technique.

3. Le terme plus approprié pour ce que Funk a fait est la factorisation de matrices.

4. En raison des bons résultats et de la renommée qui a suivi, les gens appellent encore cette technique SVD parce que, eh bien, c'est ainsi que l'auteur l'a nommée.

J'espère que cela aide à clarifier un peu les choses.