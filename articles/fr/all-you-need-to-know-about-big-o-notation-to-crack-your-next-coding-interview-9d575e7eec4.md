---
title: Tout ce que vous devez savoir sur la "Notation Big O" pour réussir votre prochain
  entretien de codage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T21:31:53.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-about-big-o-notation-to-crack-your-next-coding-interview-9d575e7eec4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KfZYFUT2OKfjekJlCeYvuQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Tout ce que vous devez savoir sur la "Notation Big O" pour réussir votre
  prochain entretien de codage
seo_desc: 'By Paul Rail

  As part of my software development education, I needed to build up skills in various
  areas to become fully prepared for my first software position. And any software
  education program worth their salt will include a fair portion of the cu...'
---

Par Paul Rail

Dans le cadre de ma formation en développement logiciel, j'ai dû acquérir des compétences dans divers domaines pour me préparer pleinement à mon premier poste en développement logiciel. Et tout programme de formation en développement logiciel qui se respecte inclura une partie importante du cursus consacrée à la préparation de l'infâme entretien de codage.

À cette fin, au début de chaque journée, **je travaille à résoudre des algorithmes, car cela constitue une grande partie (et pour beaucoup _la partie la plus difficile_) de la plupart des entretiens de codage.**

Une chose que j'ai rencontrée en travaillant sur des algorithmes en informatique est quelque chose appelé la **"Notation Big O"**.

C'est un concept assez abstrait et très ésotérique que la grande majorité des gens n'entendront jamais, ou ne se soucieront jamais. MAIS il est connu pour être une **question courante lors des entretiens de codage**, et donc c'est l'une des choses sur lesquelles j'ai passé du temps à tout apprendre.

### Ce que vous devez savoir

#### Voici ce que j'ai assimilé pour me préparer

Pour planter le décor pour le "Big O", nous devons d'abord reconnaître que **le logiciel est, bien sûr, largement basé sur les données**. D'énormes montagnes de données. Et l'utilisation de ces données est l'objectif du codage. Pour qu'un programme utilise des données, il doit souvent commencer par trier ces données dans un ordre logique. Qu'il s'agisse de manière alphabétique, chronologique, par taille, par date, et ainsi de suite.

Le **tri** se produit CONSTAMMENT, et représente en fait **une énorme partie de toute l'activité informatique et internet**. J'ai entendu des programmeurs dire que "Quick Sort est ce qui fait tourner tout l'internet".

Que veulent-ils dire par là ? Eh bien, le tri des données est une sous-section entière dans l'étude de l'informatique, et il existe de nombreux algorithmes bien définis pour le tri. Il y a **Quick Sort, Bubble Sort, Selection Sort, Merge Sort, Heap Sort** et bien d'autres. Chacun avec des approches différentes pour obtenir les mêmes ou des résultats similaires.

![Image](https://cdn-media-1.freecodecamp.org/images/ujZsW7PRqACIoFutozADQQaeD1dg8KTNwQdl)
_Source : [https://yourbasic.org/algorithms](https://yourbasic.org/algorithms" rel="noopener" target="_blank" title=")_

#### Mais lequel est le meilleur s'ils (presque) retournent tous le même résultat ?

Le meilleur signifie généralement le plus rapide. C'est là que le "Big O" entre en jeu.

La notation Big O, parfois aussi appelée "analyse asymptotique", examine principalement **le nombre d'opérations qu'un algorithme de tri prend pour trier complètement une très grande collection de données**. C'est une mesure d'efficacité et c'est ainsi que vous pouvez comparer directement un algorithme à un autre.

Lors de la création d'une simple application avec seulement quelques morceaux de données à traiter, ce type d'analyse est inutile. Mais lorsque vous travaillez avec de très grandes quantités de données, comme un site de médias sociaux ou un grand site de commerce électronique avec de nombreux clients et produits, **de petites différences entre les algorithmes peuvent être significatives.**

#### La notation Big O classe l'efficacité d'un algorithme

Elle le fait en fonction de "**O**" et "**n**" (exemple : "_O(log n)_"), où

* **O** fait référence à l'ordre de la fonction, ou à son taux de croissance, et
* **n** est la longueur du tableau à trier.

Travaillons à travers un exemple. Si un algorithme a la formule du nombre d'opérations requises de :

**_f_(n) = 6n^4 - 2n^3 + 5**

Alors que "**n**" approche l'infini (pour des ensembles de données très grands), parmi les trois termes présents, **6n^4** est le seul qui compte. Donc les termes mineurs, **2n^3** et **5**, sont en fait simplement omis car ils sont insignifiants. Il en va de même pour le "**6**" dans **6n^4**, en fait.

**Par conséquent, cette fonction aurait un taux de croissance d'ordre, ou une notation "big O", de O(n^4).**

En examinant de nombreux algorithmes de tri les plus couramment utilisés, la notation **O(n log n)** en général est la meilleure qui puisse être atteinte. Les algorithmes qui fonctionnent à cette notation incluent Quick Sort, Heap Sort et Merge Sort. **Quick Sort** est la norme et est utilisé comme défaut dans presque tous les langages de programmation.

![Image](https://cdn-media-1.freecodecamp.org/images/uKzmoTrYJbLljumcgitSieybiHBUBEasqyvd)
_Source : [http://bigocheatsheet.com/](http://bigocheatsheet.com/" rel="noopener" target="_blank" title=")_

Il est important de noter qu'**il n'existe pas un seul algorithme qui soit le plus rapide dans tous les cas**, car les données peuvent être entrées dans un programme dans tous les états possibles. Et les approches de chaque algorithme auront un meilleur et un pire scénario où ils performant au mieux ou au pire.

Bien que Quick Sort soit la norme, il est également en concurrence avec Merge Sort et Heap Sort, qui sont d'autres algorithmes de tri notés O(n log n). Il existe des scénarios où ceux-ci sont utilisés à la place.

Le concurrent le plus direct de Quick Sort est **Heap Sort**. Le temps d'exécution de Heap Sort est également O(n log n), mais le temps d'exécution moyen de Heap Sort est généralement considéré comme plus lent que celui de Quick Sort in-place.

Merge Sort est un **tri stable**, ce qui signifie qu'il préserve l'ordre d'entrée des éléments égaux dans la sortie, contrairement au Quick Sort in-place standard et au Heap Sort.

**Bubble / Insertion / Selection Sort fonctionnent à O(n²)**, ce qui, en termes de nombre d'opérations, **peut prendre significativement plus de temps** que ceux listés ci-dessus notés O(n log n) lorsqu'on traite de très grandes données. Mais il peut y avoir des scénarios où les autres sont plus rapides en fonction des données.

Il y a aussi des moments où quelque chose de très simple, comme Counting Sort, est idéal, car il est beaucoup plus rapide à écrire et beaucoup plus facile à visualiser et à comprendre.

Parfois, vous devez non seulement considérer les exigences de temps d'un algorithme, mais aussi les exigences d'espace de données (ou peut-être même plus). Certains algorithmes fonctionnent également avec une empreinte de stockage plus petite.

![Image](https://cdn-media-1.freecodecamp.org/images/2srsSpuZG0821IdAizBRdVVivfdyTCpMwNnT)
_Source : [http://bigocheatsheet.com/](http://bigocheatsheet.com/" rel="noopener" target="_blank" title=")_

### Pourquoi devez-vous savoir tout cela ?

Alors après tout cela, si vous utilisez toujours simplement l'algorithme de tri intégré d'un langage (qui est basé sur Quick Sort), alors pourquoi se soucier des algorithmes de tri et du "Big O" ? Pourquoi les entreprises vous poseraient-elles des questions à ce sujet lors d'un entretien ?

La réponse est que l'étude de la notation Big O vous permet de saisir le concept très important d'efficacité dans votre code. Ainsi, lorsque vous travaillez avec de grands ensembles de données, vous aurez une bonne idée de l'endroit où les principaux ralentissements sont susceptibles de causer des goulots d'étranglement, et où il faut porter plus d'attention pour obtenir les plus grandes améliorations. Cela s'appelle également l'analyse de sensibilité, et est une partie importante de la résolution de problèmes et de l'écriture de grands logiciels.

Donc, si vous essayez de vous préparer pour votre premier entretien, ou peut-être que vous avez eu des difficultés lors de votre dernier, augmenter vos connaissances sur des concepts comme la notation Big O et d'autres sujets en informatique vous aidera à prendre de l'avance. Vous serez mieux équipé pour démontrer votre potentiel et impressionner pour obtenir ce poste.