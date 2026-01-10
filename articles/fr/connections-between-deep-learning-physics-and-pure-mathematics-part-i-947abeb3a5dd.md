---
title: Connexions entre les réseaux de neurones et les mathématiques pures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T08:23:21.000Z'
originalURL: https://freecodecamp.org/news/connections-between-deep-learning-physics-and-pure-mathematics-part-i-947abeb3a5dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GJj62r8BX02Sx0I26O3DUA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: 'Science '
  slug: science
- name: technology
  slug: technology
seo_title: Connexions entre les réseaux de neurones et les mathématiques pures
seo_desc: 'By Marco Tavora

  How an esoteric theorem gives important clues about the power of Artificial Neural
  Networks

  Nowadays, artificial intelligence is present in almost every part of our lives.
  Smartphones, social media feeds, recommendation engines, onlin...'
---

Par Marco Tavora

#### Comment un théorème ésotérique donne des indices importants sur la puissance des réseaux de neurones artificiels

De nos jours, l'intelligence artificielle est présente dans presque tous les aspects de notre vie. Les smartphones, les fils d'actualité des réseaux sociaux, les moteurs de recommandation, les réseaux publicitaires en ligne et les outils de navigation sont des exemples d'applications basées sur l'IA qui nous affectent au quotidien.

L'apprentissage profond a systématiquement amélioré l'état de l'art dans des domaines tels que la reconnaissance vocale, la conduite autonome, la traduction automatique et la reconnaissance visuelle d'objets. Cependant, les raisons pour lesquelles l'apprentissage profond fonctionne si spectaculairement bien ne sont pas encore pleinement comprises.

### Des indices des mathématiques

[Paul Dirac](https://en.wikipedia.org/wiki/Paul_Dirac), l'un des pères de la mécanique quantique et probablement le plus grand physicien anglais depuis [Sir Isaac Newton](https://www.westminster-abbey.org/abbey-commemorations/commemorations/sir-isaac-newton/), a un jour remarqué que les progrès en physique utilisant la « [méthode de la raison mathématique](http://www.damtp.cam.ac.uk/events/strings02/dirac/speach.html) » permettraient

> « ...d'inférer des résultats sur des expériences qui n'ont pas été réalisées. Il n'y a aucune raison logique pour que la [] méthode doive être possible, mais on a constaté en pratique qu'elle fonctionne et rencontre un succès raisonnable. Cela doit être attribué à une qualité mathématique dans la Nature, une qualité que l'observateur occasionnel de la Nature ne soupçonnerait pas, mais qui joue néanmoins un rôle important dans le schéma de la Nature. »

> — Paul Dirac, 1939

![Image](https://cdn-media-1.freecodecamp.org/images/5ZKarm0xndzz384YDVedKxTTau618wLukOBK)
_Portrait de Paul Dirac au sommet de ses pouvoirs (Wikimedia Commons)._

Il existe de nombreux exemples dans l'histoire où des concepts mathématiques purement abstraits ont finalement conduit à des applications puissantes bien au-delà du contexte dans lequel ils ont été développés. Cet article traite de l'un de ces exemples.

Bien que je travaille avec le machine learning depuis quelques années, je suis de formation [physicien théoricien](https://scholar.google.com/citations?user=SaB1GO0AAAAJ&hl=en) et j'ai un faible pour les mathématiques pures. Ces derniers temps, je me suis particulièrement intéressé aux connexions entre l'apprentissage profond, les mathématiques pures et la physique.

Cet article fournit des exemples de techniques puissantes issues d'une branche des mathématiques appelée [analyse mathématique](https://en.wikipedia.org/wiki/Real_analysis). Mon objectif est d'utiliser des résultats mathématiques rigoureux pour essayer de « justifier », au moins à certains égards, pourquoi les méthodes d'apprentissage profond fonctionnent si bien de manière surprenante.

![Image](https://cdn-media-1.freecodecamp.org/images/Iwu2ZtCJlo0yRbVQjxfldXmO1tZx9O4P19BZ)
_Représentation abstraite d'un réseau de neurones ([source](https://www.shutterstock.com/g/ktsdesign" rel="noopener" target="_blank" title="))._

### Un beau théorème

Dans cette section, je vais soutenir que l'une des raisons pour lesquelles les réseaux de neurones artificiels sont si puissants est intimement liée à la forme mathématique de la sortie de ses neurones.

![Image](https://cdn-media-1.freecodecamp.org/images/yDxrc-KkYWRqxhJNWZF85398nV8fMrOCjjAc)
_Un manuscrit d'Albert Einstein ([source](http://www.alberteinstein.info/manuscripts.html" rel="noopener" target="_blank" title="))._

Je vais justifier cette affirmation audacieuse en utilisant un théorème célèbre initialement prouvé par deux mathématiciens russes à la fin des années 50, le soi-disant [théorème de représentation de Kolmogorov-Arnold](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold_representation_theorem).

![Image](https://cdn-media-1.freecodecamp.org/images/FZ9m54A8ujLhtGC5Q5Ek45M3j7sPYdzzKqXi)
_Les mathématiciens Andrei Kolmogorov (à gauche) et Vladimir Arnold (à droite)._

#### Le 13ème problème de Hilbert

En 1900, [David Hilbert](https://en.wikipedia.org/wiki/David_Hilbert), l'un des mathématiciens les plus influents du 20ème siècle, a présenté une célèbre [collection de problèmes](https://en.wikipedia.org/wiki/Hilbert%27s_problems) qui a effectivement fixé le cours de la recherche mathématique du 20ème siècle.

Le théorème de représentation de Kolmogorov-Arnold est lié à l'un des célèbres [problèmes de Hilbert](https://en.wikipedia.org/wiki/Hilbert%27s_problems), qui ont tous énormément influencé les mathématiques du 20ème siècle.

#### Se rapprocher de la connexion avec les réseaux de neurones

Une généralisation de l'un de ces problèmes, le [13ème](https://en.wikipedia.org/wiki/Hilbert%27s_thirteenth_problem) problème spécifiquement, considère la possibilité qu'une fonction de _n_ variables puisse être exprimée comme une combinaison de sommes et de compositions de seulement deux fonctions d'une seule variable qui sont désignées par Φ et _ψ_.

Plus concrètement :

![Image](https://cdn-media-1.freecodecamp.org/images/5ciEd-xaR7lp3US513Jo20KsVnwtor2qBeWU)
_Théorème de représentation de Kolmogorov-Arnold_

Ici, _η_ et les λ sont des nombres réels. Il convient de noter que ces deux fonctions univariées sont Φ et _ψ_ peuvent avoir une structure hautement compliquée (fractale).

Trois articles, par Kolmogorov (1957), Arnold (1958) et [Sprecher](http://www.ams.org/journals/tran/1965-115-00/S0002-9947-1965-0210852-X/S0002-9947-1965-0210852-X.pdf) (1965) ont fourni une preuve qu'une telle représentation doit exister. Ce résultat est plutôt inattendu puisque, selon lui, la complexité déconcertante des fonctions multivariées peut être « traduite » en opérations triviales de fonctions univariées, telles que des additions et des compositions de fonctions.

### Et maintenant ?

Si vous êtes arrivé jusqu'ici (et je serais ravi si vous l'avez fait), vous vous demandez probablement : comment un théorème ésotérique des années 50 et 60 pourrait-il être même lointainement lié à des algorithmes de pointe tels que les réseaux de neurones artificiels ?

### Un rappel rapide des activations des réseaux de neurones

Les expressions calculées à chaque nœud d'un réseau de neurones sont des compositions d'autres fonctions, dans ce cas, les fonctions dites d'activation. Le degré de complexité de ces compositions dépend de la profondeur de la couche cachée contenant le nœud. Par exemple, un nœud dans la deuxième couche cachée effectue le calcul suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/L8v4n0-Pw16u8yIcdkQXoTADtSM5zyWJJQfr)
_Calcul effectué par la k-ième unité cachée dans la deuxième couche cachée._

Où les _w_ sont les poids, et les _b_ sont les biais. La similitude avec la fonction multivariée _f_ montrée quelques paragraphes plus haut est évidente !

Écrivons rapidement une fonction en Python uniquement pour la propagation avant qui sort les calculs effectués par les neurones. Le code de la fonction ci-dessous comprend les étapes suivantes :

* **Première ligne** : la première fonction d'activation _ψ_ agit sur la première étape linéaire donnée par :

```
x0.dot(w1) + b1
```

où `x0` est le vecteur d'entrée.

* **Deuxième ligne** : la deuxième fonction d'activation agit sur la deuxième étape linéaire

```
y1.dot(w2) + b2
```

* **Troisième ligne** : une [fonction softmax](https://en.wikipedia.org/wiki/Softmax_function#Neural_networks) est utilisée dans la couche finale du réseau de neurones, agissant sur la troisième étape linéaire

```
y2.dot(w3) + b3
```

La fonction complète est :

```
def forward_propagation(w1, b1, w2, b2, w3, b3, x0):        y1 = phi(x0.dot(w1) + b1)    y2 = phi(y1.dot(w2) + b2)    y3 = softmax(y2.dot(w3) + b3)        return y1, y2, y3
```

Pour comparer cela avec notre expression ci-dessus, nous écrivons :

```
y2 = phi(phi(x0.dot(w1) + b1).dot(w2) + b2)
```

La correspondance peut être rendue plus claire :

![Image](https://cdn-media-1.freecodecamp.org/images/T77L1UoWBNfvewKPTmoAzGReC54fhnp0eKzV)

### Une connexion entre deux mondes

Nous concluons donc que le résultat prouvé par Kolmogorov, Arnold et Sprecher implique que les réseaux de neurones, dont la sortie n'est rien d'autre que la composition répétée de fonctions, sont des objets extrêmement puissants, qui peuvent représenter n'importe quelle fonction multivariée ou presque n'importe quel processus dans la nature. Cela explique en partie pourquoi les réseaux de neurones fonctionnent si bien dans tant de domaines. En d'autres termes, le pouvoir de généralisation des réseaux de neurones est, au moins en partie, une conséquence du théorème de représentation de Kolmogorov-Arnold.

Comme le souligne [Giuseppe Carleo](https://indico.math.cnrs.fr/event/2435/), le pouvoir de généralisation de la formation de fonctions de fonctions de fonctions _ad_ nauseam a, d'une certaine manière, été « découvert indépendamment aussi par la nature » puisque les réseaux de neurones, qui fonctionnent comme montré ci-dessus en faisant précisément cela, sont une manière simplifiée de décrire comment nos cerveaux fonctionnent.

Merci beaucoup d'avoir lu ! Les critiques constructives et les retours sont toujours les bienvenus !

Mon [Github](https://github.com/marcotav) et mon site web [www.marcotavora.me](https://marcotavora.me/) contiennent d'autres choses intéressantes sur la science des données et la physique.

Il y a beaucoup plus à venir, restez à l'écoute !