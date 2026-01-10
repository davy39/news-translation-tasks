---
title: Pourquoi l'algorithme HyperLogLog est mon nouveau préféré
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-05T12:31:00.000Z'
originalURL: https://freecodecamp.org/news/my-favorite-algorithm-and-data-structure-hyperloglog-6583a25c8a4f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ij4OThN8DISD0zwH-7UlWQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Pourquoi l'algorithme HyperLogLog est mon nouveau préféré
seo_desc: 'By Alex Nadalin

  Every now and then I bump into a concept that’s so simple and powerful that I’m
  wish I’d discovered such an incredible and beautiful idea.

  I discovered HyperLogLog (HLL) a couple of years ago, and fell in love with it right
  after read...'
---

Par Alex Nadalin

De temps en temps, je tombe sur un concept si simple et puissant que je regrette de ne pas avoir découvert une idée aussi incroyable et belle plus tôt.

J'ai découvert [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog) (HLL) il y a quelques années et j'en suis tombé amoureux après avoir lu comment [Redis a décidé d'ajouter une structure de données HLL](http://antirez.com/news/75).

L'idée derrière HLL est d'une simplicité déconcertante mais extrêmement puissante. C'est ce qui en fait un algorithme si répandu, utilisé par des géants de l'internet comme Google et Reddit.

#### Collecte de numéros de téléphone

Mon ami Tommy et moi avons prévu d'aller à une conférence. En nous rendant sur place, nous avons décidé de parier sur qui rencontrerait le plus de nouvelles personnes. Une fois arrivés, nous avons commencé à discuter avec les gens et à compter le nombre de personnes avec lesquelles nous avons parlé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oIVPnmV6cE4mAbaK.png)

À la fin de l'événement, Tommy vient me voir avec son chiffre — disons 17 — et je lui dis que j'ai parlé à 46 personnes.

Clairement, je suis le gagnant, mais Tommy est frustré car il pense que j'ai compté plusieurs fois les mêmes personnes. Il croit n'avoir vu que peut-être 15 à 20 personnes différentes avec lesquelles j'ai parlé.

Donc, le pari est annulé. Nous décidons que pour notre prochain événement, nous noterons les noms des personnes pour être sûrs de compter des personnes uniques, et non simplement le nombre total de conversations.

À la fin de la conférence suivante, nous nous retrouvons avec une très longue liste de noms et — devinez quoi ? Tommy a eu quelques rencontres de plus que moi ! Nous en rions, et en discutant de notre approche pour compter les uniques, Tommy a une grande idée :

« Alex, tu sais quoi ? Nous ne pouvons pas nous promener avec un stylo et du papier et noter une liste de noms, c'est vraiment peu pratique ! Aujourd'hui, j'ai parlé à 65 personnes différentes et compter leurs noms sur ce papier a été un vrai calvaire. J'ai perdu le compte 3 fois et j'ai dû recommencer depuis le début ! »

« Oui, je sais, mais avons-nous même une alternative ? »

« Et si, pour notre prochaine conférence, au lieu de demander des noms, nous demandions aux gens les 5 derniers chiffres de leur numéro de téléphone ? Au lieu de gagner en comptant leurs noms, le gagnant sera celui qui aura parlé à quelqu'un avec la plus longue séquence de zéros initiaux dans ces chiffres. »

« Attends Tommy, tu vas trop vite ! Ralentis une seconde et donne-moi un exemple… »

« Bien sûr, demande simplement à chaque personne ces 5 derniers chiffres, d'accord ? Supposons qu'ils répondent '54701'. Il n'y a pas de zéro initial, donc la plus longue séquence de zéros initiaux est 0. La personne suivante à qui tu parles dit '02561' — c'est un zéro initial ! Donc ta plus longue séquence est maintenant 1. »

« Tu commences à avoir du sens pour moi… »

« Oui, donc si nous parlons seulement à quelques personnes, il y a des chances que notre plus longue séquence de zéros soit 0. Mais si nous parlons à peut-être 10 personnes, nous avons plus de chances qu'elle soit 1. »

« Maintenant, imagine que tu me dises que ta plus longue séquence de zéros est 5 — tu dois avoir parlé à des milliers de personnes pour trouver quelqu'un avec 00000 dans son numéro de téléphone ! »

« Mec, tu es un putain de génie ! »

#### Et cela, mes amis, est fondamentalement comment HyperLogLog fonctionne.

Il nous permet d'estimer les éléments uniques dans un grand ensemble de données en enregistrant la plus longue séquence de zéros dans cet ensemble.

Cela finit par créer un avantage incroyable par rapport au suivi de chaque élément dans l'ensemble. C'est une manière incroyablement efficace de compter les valeurs uniques, avec une précision relativement élevée.

> « L'algorithme HyperLogLog peut estimer des cardinalités bien au-delà de 10⁹ avec une précision relative (erreur standard) de 2 % tout en n'utilisant que 1,5 ko de mémoire »

> **Fangjin Yang —** [Rapide, économique et 98 % correct : Estimation de la cardinalité pour les Big Data](http://druid.io/blog/2012/05/04/fast-cheap-and-98-right-cardinality-estimation-for-big-data.html)

Puisque je peux simplifier à l'excès, examinons quelques détails supplémentaires de HLL.

### Plus de détails sur HLL

HLL fait partie d'une famille d'algorithmes qui visent à résoudre le problème de [l'estimation de la cardinalité](https://en.wikipedia.org/wiki/Count-distinct_problem) — autrement connu sous le nom de « problème de comptage distinct ». Comment pouvons-nous compter efficacement le nombre d'objets uniques dans un ensemble de données ?

Cela est extrêmement utile pour de nombreuses applications web d'aujourd'hui. Par exemple, lorsque vous souhaitez compter le nombre de vues uniques qu'un article sur votre site a générées.

Lorsque HLL s'exécute, il prend vos données d'entrée et les hache, les transformant en une séquence de bits :

```
Adresse IP du spectateur : 54.134.45.789
```

```
Hachage HLL : 010010101010101010111010...
```

Maintenant, une partie importante de HLL est de s'assurer que votre fonction de hachage distribue les bits aussi uniformément que possible. Vous ne voulez pas utiliser une fonction faible telle que :

Un HLL utilisant cette fonction de hachage retournerait des résultats biaisés si, par exemple, la [distribution de vos visiteurs est liée à une région géographique spécifique](https://stackoverflow.com/a/277537/934439).

Le [document original](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf) donne quelques détails supplémentaires sur ce qu'une bonne fonction de hachage signifie pour HLL :

> « Tous les estimateurs de cardinalité efficaces connus reposent sur la randomisation, qui est assurée par l'utilisation de fonctions de hachage. »

> « Les éléments à compter appartenant à un certain domaine de données D, nous supposons donnée une fonction de hachage, h : D → {0, 1}∞ ; c'est-à-dire que nous assimilons les valeurs hachées à des chaînes binaires infinies de {0, 1}∞, ou de manière équivalente à des nombres réels de l'intervalle unitaire. »

> « […] »

> « Nous postulons que la fonction de hachage a été conçue de manière à ce que les valeurs hachées ressemblent étroitement à un modèle uniforme de randomisation, à savoir, les bits des valeurs hachées sont supposés être indépendants et avoir chacun une probabilité [0,5] de se produire. »

> **Philippe Flajolet —** [HyperLogLog : L'analyse d'un algorithme d'estimation de cardinalité quasi-optimal](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)

Maintenant, après avoir choisi une fonction de hachage appropriée, nous devons aborder un autre piège : la [variance](https://en.wikipedia.org/wiki/Variance).

Revenons à notre exemple, imaginez que la première personne à qui vous parlez à la conférence vous dit que son numéro se termine par `00004` — jackpot !

Vous avez peut-être gagné un pari contre Tommy, mais si vous utilisez cette méthode dans la vie réelle, il y a des chances que des données spécifiques dans votre ensemble influencent négativement l'estimation.

Ne craignez plus, car c'est un problème que HLL a été conçu pour résoudre.

Peu savent que [Philippe Flajolet](https://en.wikipedia.org/wiki/Philippe_Flajolet), l'un des cerveaux derrière HLL, a été impliqué dans des problèmes d'estimation de cardinalité depuis longtemps. Assez longtemps pour avoir inventé l'[algorithme Flajolet-Martin en 1984](https://en.wikipedia.org/wiki/Flajolet%E2%80%93Martin_algorithm#Improving_accuracy) et [(super-)LogLog en 2003](http://algo.inria.fr/flajolet/Publications/DuFl03-LNCS.pdf).

Ces algorithmes ont déjà abordé certains des problèmes liés aux valeurs hachées aberrantes, en divisant les mesures en compartiments et en moyennant (quelque peu) les valeurs entre les compartiments.

Si vous vous êtes perdu ici, laissez-moi revenir à notre exemple original.

Au lieu de simplement prendre les 5 derniers chiffres d'un numéro de téléphone, nous en prenons 6. Maintenant, nous stockons la plus longue séquence de zéros initiaux avec le premier chiffre (le « compartiment »).

Cela signifie que nos données ressembleront à ceci :

```
Entrée : 708942 --> dans le 7ème compartiment, la plus longue séquence de 0 est 1
518942 --> dans le 5ème compartiment, la plus longue séquence de 0 est 0
500973 --> dans le 5ème compartiment, la plus longue séquence de 0 est maintenant 2
900000 --> dans le 9ème compartiment, la plus longue séquence de 0 est 5
900672 --> dans le 9ème compartiment, la plus longue séquence de 0 reste 5
```

```
Compartiments :
0: 0
1: 0
2: 0
3: 0
4: 0
5: 2
6: 0
7: 1
8: 0
9: 5
```

```
Sortie :
moyenne(compartiments) = 0,8
```

Comme vous pouvez le voir, si nous n'utilisions pas de compartiments, nous utiliserions plutôt 5 comme la plus longue séquence de zéros. Cela aurait un impact négatif sur notre estimation.

Bien que j'aie simplifié les mathématiques derrière les compartiments (ce n'est pas juste une simple moyenne), vous pouvez totalement voir comment cette approche a du sens.

Il est intéressant de voir comment Flajolet aborde la variance dans ses travaux :

> « Bien que nous ayons déjà une estimation assez bonne, il est possible de faire beaucoup mieux. Durand et Flajolet font l'observation que les valeurs aberrantes font beaucoup pour diminuer la précision de l'estimation ; en éliminant les plus grandes valeurs avant de faire la moyenne, la précision peut être améliorée. »

> « Plus précisément, en éliminant les 30 % des compartiments avec les plus grandes valeurs, et en moyennant seulement 70 % des compartiments avec les plus petites valeurs, la précision peut être améliorée de 1,30/√(m) à seulement 1,05/√(m) ! Cela signifie que notre exemple précédent, avec 640 octets d'état et une erreur moyenne de 4 % a maintenant une erreur moyenne d'environ 3,2 %, sans augmentation supplémentaire de l'espace requis. »

> « Enfin, la contribution majeure de Flajolet et al. dans le document HyperLogLog est d'utiliser un type différent de moyenne, en prenant la moyenne harmonique au lieu de la moyenne géométrique que nous venons d'appliquer. En faisant cela, ils sont capables de réduire l'erreur à 1,04/√(m), encore une fois sans augmentation de l'état requis »

> **Nick Johnson** — [Amélioration de la précision : SuperLogLog et HyperLogLog](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation)

### HLL dans la nature

Alors, où pouvons-nous trouver l'application des HLL ? Deux excellents exemples à l'échelle du web sont :

* [BigQuery](https://cloud.google.com/blog/big-data/2017/07/counting-uniques-faster-in-bigquery-with-hyperloglog), pour compter efficacement les uniques dans une table (`APPROX_COUNT_DISTINCT()`)
* [Reddit](https://redditblog.com/2017/05/24/view-counting-at-reddit/), où il est utilisé pour calculer combien de vues uniques un post a générées

En particulier, voyez comment HLL impacte les requêtes sur BigQuery :

```
SELECT COUNT(DISTINCT actor.login) exact_cnt
FROM `githubarchive.year.2016`
6,610,026 (4.1s elapsed, 3.39 GB processed, 320,825,029 rows scanned)
```

```
SELECT APPROX_COUNT_DISTINCT(actor.login) approx_cnt
FROM `githubarchive.year.2016`
6,643,627 (2.6s elapsed, 3.39 GB processed, 320,825,029 rows scanned)
```

Le deuxième résultat est une approximation (avec un taux d'erreur d'environ 0,5 %), mais prend une fraction du temps.

En résumé : **HyperLogLog est incroyable !**

Maintenant que vous savez ce que c'est et quand l'utiliser, allez faire des choses incroyables avec !

### Lectures complémentaires

* [HyperLogLog sur Wikipedia](https://en.wikipedia.org/wiki/HyperLogLog)
* le [document original](http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)
* [HyperLogLog++, l'implémentation améliorée de HLL par Google](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40671.pdf)
* [Nouvelle structure de données Redis : le HyperLogLog](http://antirez.com/news/75)
* [Damn Cool Algorithms: Cardinality Estimation](http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation)
* [Types de données HLL dans Riak](https://github.com/basho/riak_kv/blob/develop/docs/hll/hll.pdf)
* [HyperLogLog et MinHash](http://tech.adroll.com/blog/data/2013/07/10/hll-minhash.html)

_Publié à l'origine sur [odino.org](http://odino.org/my-favorite-data-structure-hyperloglog/) (13 janvier 2018).