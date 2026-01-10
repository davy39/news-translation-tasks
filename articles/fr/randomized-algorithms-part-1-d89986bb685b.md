---
title: 'Algorithmes randomisés : comment résoudre le problème de résolution de contention'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-07T21:26:34.000Z'
originalURL: https://freecodecamp.org/news/randomized-algorithms-part-1-d89986bb685b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*bhRlXxOE7_xOUQsS
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Algorithmes randomisés : comment résoudre le problème de résolution de
  contention'
seo_desc: 'By Chad Malla

  Randomized algorithms are very important in the field of theoretical computing science
  as well as real-world applications. For a lot of problems, to get a deterministic
  answer, a function that always returns the same answer given the sa...'
---

Par Chad Malla

Les algorithmes randomisés sont très importants dans le domaine de l'informatique théorique ainsi que dans les applications réelles. Pour de nombreux problèmes, obtenir une réponse déterministe, c'est-à-dire une fonction qui retourne toujours la même réponse pour une même entrée, est coûteux en calcul et ne peut pas être résolu en temps polynomial.

Lorsque nous introduisons une certaine randomisation avec l'entrée, nous **nous attendons** à avoir une complexité temporelle plus efficace. Ou nous **nous attendons** à avoir un ratio de la solution optimale avec une bonne borne supérieure sur le nombre d'itérations qu'il faudra pour obtenir cette solution.

Ces algorithmes sont souvent triviaux à concevoir. Mais il est beaucoup plus complexe d'analyser et de prouver le temps d'exécution/l'exactitude. Il est à noter qu'il y a une différence entre l'analyse probabiliste et l'analyse des algorithmes randomisés. Dans l'analyse probabiliste, nous donnons à l'algorithme une entrée supposée provenir d'une distribution de probabilité. Alors que dans l'algorithme randomisé, nous ajoutons un ou plusieurs nombres aléatoires à l'entrée. Les images suivantes devraient montrer la distinction. Les images proviennent des diapositives de cours de [Stanford](http://theory.stanford.edu/people/pragh/amstalk.pdf).

![Image](https://cdn-media-1.freecodecamp.org/images/uUWWu2MehlSIZFqxqjtQC631yqQmUNFbWfi1)
_[http://theory.stanford.edu/people/pragh/amstalk.pdf](http://theory.stanford.edu/people/pragh/amstalk.pdf" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/Oh3j6hVPvOmpGmniOUlzHA1JDj2faDVxMXip)
_[http://theory.stanford.edu/people/pragh/amstalk.pdf](http://theory.stanford.edu/people/pragh/amstalk.pdf" rel="noopener" target="_blank" title=")_

Dans cet article, je vais aborder le problème de résolution de contention issu de _Algorithm Design_ de **Kleinberg** et **Tardos.**

### Résolution de contention

Le problème est le suivant : il y a **_n_ processeurs** qui partagent une **base de données unique _D_** et le temps est divisé en **_k_ intervalles discrets.** La **base de données sert** au plus **1 processeur à la fois.**

**Objectif :** Répartir les tours parmi les _n_ processeurs de manière **équitable.**

![Image](https://cdn-media-1.freecodecamp.org/images/mtXbehd0eHLRStPLp52iefvh0JCQvWBAQoB4)
_[http://www.cs.princeton.edu/courses/archive/spr05/cos423/lectures/13randomized.pdf](http://www.cs.princeton.edu/courses/archive/spr05/cos423/lectures/13randomized.pdf" rel="noopener" target="_blank" title=")_

Gardez à l'esprit qu'il n'y a aucune communication entre les processeurs pour planifier l'accès à la base de données. Si chaque processeur essaie en permanence d'accéder à _D_ en même temps, la base de données sera verrouillée, servant 0 processeur. Pas idéal. En randomisant la séquence des tentatives d'accès des processeurs, nous pouvons "lisser" la contention, évitant ainsi les verrouillages.

### Événements

Nous devons spécifier certains événements et les probabilités qui leur sont associées.

Pensez à ce qui se passe ici : un processeur _i_ essaie d'accéder à _D_ à l'instant _t_. Considérons cela comme notre premier événement.

> _E1 =_ A[i, t] : **P[i] (processus i) tente d'accéder à _D_ au tour _t_**

Cet événement a un complément : le processus ne tente pas d'accéder au tour t.

> E1^ = A[i, t]^ : **P[i] ne tente pas d'accéder à _D_ au tour _t_**

Soit A[i, t] avec une probabilité _p_ de se produire et, puisque toutes les probabilités individuelles dans un espace d'échantillonnage S = {E1, E1^} s'additionnent à 1, nous avons une probabilité de A[i,t]^ égale à _1-p_.

> Pr[A[i,t]] = p | Pr[A[i,t]^] = 1-p

Après avoir tenté d'accéder à la base de données, l'une des deux choses suivantes se produit pour le processus P[i] : il réussit ou il échoue.

> E2 = S[i,t] : **P[i] réussit à accéder à _D_ au tour _t_**

> E2^ = S[i,t]^ : **P[i] ne réussit pas à accéder à _D_ au tour _t_**

La réussite ne se produit que lorsque P[i] tente d'accéder à _D_ et que tous les autres processus ne le font pas. Il s'agit d'une intersection d'événements E1 pour tous les processus.

> S[i,t] = A[i,t] ∩ (∩j≠i A[j,t]^)

La probabilité de S[i,t] est donc la probabilité de A[i,t] multipliée par le produit des événements complémentaires A[j,t]^.

> Pr[S[i,t]] = Pr[A[i,t]] * ∏j≠i Pr[A[j,t]^] = p(1-p)^(n-1)

Vous vous souvenez des dérivées ? Elles sont égales à 0 aux minima ou maxima. Soit f(p) = p(1-p)^(n-1), alors la dérivée de f(p) est

f'(p) = (1-p)^(n-1) - (n-1)*p*(1-p)^n-2

Les valeurs évidentes qui rendent cette équation égale à 0 sont 0 et 1. Lorsque p = 0, aucun des processus ne tente d'accéder à la base de données. Lorsque p = 1, tous les processus tentent d'accéder en même temps. Ces deux situations ne nous intéressent pas. La seule autre valeur est lorsque p = 1/n.

**Définissons p = 1/n** et nous obtenons

> Pr[S[i,t]] = 1/n(1-1/n)^(n-1)

En calcul, il y a deux faits que nous allons utiliser.

1. (1-1/n)^n converge de manière monotone de 1/4 à 1/e
2. (1-1/n)^n-1 converge de manière monotone de 1/2 à 1/e

Nous voyons donc qu'il existe une borne asymptotique que nous pouvons utiliser.

1/n(1-1/n)^(n-1) converge de manière monotone de (≤) 1/2 *1/n à (≥) 1/e*1/n

> 1/en ≤ Pr[S[i,t]] ≤ 1/2n

Cela est asymptotiquement égal à _O(1/n)_

Un autre événement, les échecs...

E3 = F[i,t] : désigne l'événement "d'échec" où P[i] ne réussit pas à accéder à _D_ dans aucun des tours de 1 à _t_

Cela équivaut à spécifier l'intersection des événements, S[i,r]^ (aucun succès) pour r = 1...t

Cela aide finalement la probabilité de F[i,t] à devenir une équation mathématique commutable, car la probabilité de l'intersection des événements est le produit des probabilités des événements individuels.

**Pr[F[i,t]] = Pr[∩r=1.to.t (S[i,r]^)] = ∏r=1.to.t(Pr[S[i,r]^]) =**

**(1-p(1-p)^(n-1))^t**

* Pr[S[i,t]] = p(1-p)^(n-1), S[i,t]^ = 1-Pr[S[i,t]]

Vous vous souvenez des propriétés de convergence du calcul que nous avons vues précédemment ? Nous les utilisons ici pour obtenir

Pr[F[i,t]] = (1-**p(1-p)^(n-1)**)^t = (1-**1/n(1-1/n)^(n-1))**^t ≤ (1-1/en)^t

* p = 1/n car chacun des _n_ processeurs a une probabilité égale de tenter d'accéder à la base de données à l'instant _t_

Examinons maintenant le paramètre _t._

Si nous définissons _t_ = ceiling(en) pour nous assurer qu'il s'agit d'un entier, nous obtenons

Pr[F[i,t]] ≤ (1-1/en)^ceiling(en) ≤ (1-1/en)^en ≤ 1/e

Cette borne nous indique que la probabilité qu'un processus i ne réussisse pas dans ses tentatives des tours 1 à ceiling(en) est majorée par 1/e, indépendamment de n.

Définissons t = ceiling(en)*(c*ln(n)) alors nous avons

> **Pr[F[i,t]] ≤ (1-1/en)^t ≤ ((1-1/en)^ceiling(en))^(c*ln(n)) ≤ (1/e)^c*ln(n) ≤ 1/n^c = n^-c**

Un dernier événement... notre objectif est que les processus réussissent autant de tours que possible. En d'autres termes, si, par exemple,

E4 = **F[t]** : désigne **l'événement où le protocole échoue après _t_ tours**, alors nous aimerions **minimiser _t_** ici pour maximiser le nombre de tours où il réussit.

F[t] se produit **si et seulement si** l'un des F[i,t] se produit ; il suffit qu'un processus échoue pour dire que le protocole a échoué. Il s'agit donc de l'union des événements F[i,t] pour les processus i = 1...n.

F[t] = ∪i=1.to.n(F[i,t])

#### **Borne de l'union**

Il est difficile de calculer exactement ce qui précède car les événements F[i,t] ne sont pas indépendants. La solution facile consiste à les borner comme s'ils étaient tous indépendants.

> Étant donné les événements E1, ... En, nous avons **Pr[∪i=1.to.n(Ei)] ≤ ∑i=1.to.n(Pr[Ei])**

Pr[F[t]] ≤ ∑i=1.to.n(Pr[F[i,t]])

Rappelons que lorsque t = ceiling(en)*c*ln(n), cela donne une borne supérieure sur Pr[F[i,t]] ≤ n^-c

Prenons c = 2 et nous avons Pr[F[t]] ≤ ∑i=1.to.n(n^(-2)) = n*n^(-2) = 1/n

Quelle est la probabilité que tous les processus réussissent à accéder à _D_ au moins une fois dans les _t_ = 2*ceiling(en)*ln(n) tours ?

Prenons le complément de F[t], F[t]^ et arrivons à une probabilité

1-1/n.

#### Conclusion

Cette analyse était assez longue, et la plupart des analyses pour les algorithmes randomisés le sont. Il s'agit essentiellement d'un compromis, car les algorithmes sont plus faciles à concevoir et à comprendre que les algorithmes déterministes complexes qui sont coûteux en calcul pour arriver à la solution correcte. Avec les algorithmes randomisés, nous sommes prêts à accepter une petite erreur avec le luxe de l'efficacité.

Merci d'avoir lu. Je suis nouveau dans le monde du blogging, donc tout retour serait apprécié.