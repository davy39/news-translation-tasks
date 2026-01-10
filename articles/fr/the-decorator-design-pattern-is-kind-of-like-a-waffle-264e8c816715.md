---
title: Le patron de conception Décorateur est un peu comme une gaufre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-25T23:29:10.000Z'
originalURL: https://freecodecamp.org/news/the-decorator-design-pattern-is-kind-of-like-a-waffle-264e8c816715
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4FU5faISak9BmmtnI12bpQ.jpeg
tags:
- name: design patterns
  slug: design-patterns
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Le patron de conception Décorateur est un peu comme une gaufre
seo_desc: 'By Sihui Huang

  The decorator pattern is about adding extra features to an existing object.

  Does that sound like French?

  No worries.

  We will come back to this later.

  Let’s take a look at some waffles first!

  The genius part about waffles is that they s...'
---

Par Sihui Huang

Le patron décorateur consiste à ajouter des fonctionnalités supplémentaires à un objet existant.

Cela vous semble-t-il du chinois ?

Pas de souci.

Nous y reviendrons plus tard.

Regardons d'abord quelques gaufres !

Le génie des gaufres, c'est qu'elles commencent simples et basiques. Parce qu'elles sont simples, presque tout se marie bien avec elles.

Les garnitures courantes pour les gaufres sont les fraises, les myrtilles, les mûres, les bananes, les amandes et les sirops.

![Image](https://cdn-media-1.freecodecamp.org/images/1*czVXA_H5JrZH1rsHkZTZxg.jpeg)

Essayons de créer une collection de différents objets gaufres.

Il y aura GaufreFraise, GaufreMyrtille, GaufreMure, GaufreBanane, GaufreAmande et GaufreSirop.

Attendez, nous pouvons avoir des fraises et des myrtilles sur la même gaufre. Cela nous donne une GaufreFraiseMyrtille.

Nous pouvons aussi avoir des fraises et des mûres sur la même gaufre. Cela nous donne une GaufreFraiseMure.

Personne ne nous empêche de mettre trois garnitures sur la même gaufre. Cela nous donne une GaufreFraiseMyrtilleMure.

Pour simplifier les choses, considérons les fraises, les myrtilles et les mûres comme des garnitures potentielles. Il y a huit combinaisons différentes[1].

Cela signifie-t-il que nous devons créer huit objets différents pour notre collection de gaufres ?

Si nous ajoutons les bananes à notre liste de garnitures potentielles, il y a 16 combinaisons différentes[2].

Il est évident que l'ajout d'une seule garniture à notre liste de garnitures entraîne une explosion dans notre collection de gaufres.

**Il n'est pas faisable de créer une classe de gaufre différente pour chaque combinaison possible de garnitures.** Il doit y avoir une meilleure façon de faire cela.

Et si, lorsque nous voulons une GaufreFraise au lieu de créer une GaufreFraise, nous créons une Gaufre et ajoutons des fraises dessus ?

Et pour la GaufreFraiseMyrtille alors ? ???

???Nous **pouvons créer une Gaufre, ajouter des fraises dessus, et ajouter des myrtilles dessus !???**

### Création des classes de gaufres

Regardons la classe de gaufre simple :

Vous pouvez créer une gaufre, la servir et la manger comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*weV8NQ2k6szFGp3W7UdUcw.png)

Et voici la classe GaufreFraise :

**Remarquez que nous passons un objet gaufre à l'intérieur du constructeur GaufreFraise pour créer une GaufreFraise.**

La classe GaufreFraise a :

1. La gaufre passée en paramètre
2. Les fraises comme garniture
3. Une méthode `serve` qui appelle la méthode `serve` de la gaufre passée en paramètre. Puis imprime `garnie de fraises`
4. Une méthode `eat` qui appelle la méthode `eat` de la gaufre passée en paramètre et imprime ensuite `et puis mange quelques fraises`

Vous pouvez créer une gaufre aux fraises, la servir et la manger comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hT_swQasc2fUWEHllWt5qQ.png)

Voici les classes GaufreMyrtille et GaufreMure :

Et vous pouvez les utiliser comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*M_3M_f0UkDH4UKQy772tTw.png)

### Extraire la partie commune

En remarquant que les classes GaufreFraise, GaufreMyrtille et GaufreMure sont presque identiques sauf pour leur `garniture`, nous pouvons extraire les parties communes dans une classe parente.

Dans `DecorateurGaufre`, `garniture` n'est plus un attribut de l'objet. Au lieu de cela, c'est une méthode qui peut être redéfinie par une classe enfant.

Maintenant, nous pouvons réécrire `GaufreFraise`, `GaufreMyrtille` et `GaufreMure` pour qu'elles héritent de `DecorateurGaufre` afin de bénéficier de ces fonctionnalités communes :

Et elles devraient toujours fonctionner de la même manière qu'avant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*F7esdyzUOeEKlE8gqgEQpw.png)

Voici les classes que nous créons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kmCmAVV-67wkMqDhR09dvg.png)

### Création d'une gaufre MyrtilleFraise

Maintenant, nous avons `Gaufre`, `GaufreFraise`, `GaufreMyrtille` et `GaufreMure`.

Il est temps d'atteindre l'objectif que nous nous étions fixé initialement :

**créer une Gaufre, ajouter des fraises dessus, et ajouter des myrtilles dessus**.

Tout simplement comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QiuxdYN-dwhk0t1f47Hl_A.png)

Et nous pouvons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vegaZ1Te-NyaLWGzhWO_0A.png)

### Que se passe-t-il ?! ???

Regardons de plus près comment nous avons créé la `gaufre_myrtille_fraise` :

Tout d'abord, nous avons créé une `gaufre_simple` avec `Gaufre` : `gaufre_simple = Gaufre.new`

![Image](https://cdn-media-1.freecodecamp.org/images/1*jW3Ptmd4LenA8r0yhrsRvQ.png)

Ensuite, nous avons créé `gaufre_fraise` en passant la `gaufre_simple` dans le constructeur `GaufreFraise`. `gaufre_fraise = GaufreFraise.new(gaufre_simple)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*oTHZFfPxKqIt6_2fYg74Gg.png)

Il est important de noter que lorsque nous créons la `gaufre_fraise`, nous conservons la `gaufre_simple` passée en paramètre comme variable d'instance de `gaufre_fraise` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OZ4w51QqltH6RjyNtAesMg.png)

Comme nous pouvons le voir, `gaufre_fraise.gaufre` et `gaufre_simple` sont le même objet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*D1n_qoh30U6p3OMLoGDvKg.png)

À ce stade, lorsque nous appelons `gaufre_fraise.serve`, nous appelons d'abord `gaufre_simple.serve` puis nous imprimons `garnie de fraises`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IWrELsik2PMCZS31d5yyIg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nounSGokjqaJo3AJJEbD-g.png)

Pour `gaufre_fraise.eat`, nous appelons d'abord `gaufre_simple.eat` puis nous imprimons `et puis mange quelques fraises`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OyFpsHk0hp6m2m13NGxc1A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dj_EkO2PeewA0LWi2uqztA.png)

Nous créons `gaufre_myrtille_fraise` en passant la `gaufre_fraise` dans le constructeur `GaufreMyrtille`. `gaufre_myrtille_fraise = GaufreMyrtille.new(gaufre_fraise)`

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZWzIgZX5HyZ1HkedPRPvEw.png)

Lorsque nous créons la `gaufre_myrtille_fraise`, nous conservons la `gaufre_fraise` passée en paramètre comme variable d'instance de `gaufre_myrtille_fraise` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*r9CRF5itgt635btmNldXgw.png)

Lorsque nous appelons `gaufre_myrtille_fraise.serve`, nous appelons d'abord `gaufre_fraise.serve`, qui appelle `gaufre_simple.serve` puis imprime `garnie de fraises`. Ensuite, nous imprimons `garnie de myrtilles`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aEai4fnfaqbgbnwq6a4Y4A.png)

Lorsque nous appelons `gaufre_myrtille_fraise.eat`, nous appelons d'abord `gaufre_fraise.eat`, qui appelle `gaufre_simple.eat` puis imprime `et puis mange quelques fraises`. Ensuite, nous imprimons `et puis mange quelques myrtilles`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TSLbCErIsP56O_HaOaDusw.png)

### La clé de la magie :

`gaufre_fraise` est construite sur `gaufre_simple`. Et `gaufre_myrtille_fraise` est construite sur `gaufre_fraise`.

La clé pour pouvoir construire des gaufres les unes sur les autres est que **toutes les gaufres doivent obéir à la même interface**.

Toutes les gaufres ont une méthode `serve` et une méthode `eat`.

C'est pourquoi, dans les classes `GaufreFraise/GaufreMyrtille/GaufreMure`, nous sommes confiants que la `gaufre` passée en paramètre a une méthode `serve` et une méthode `eat`.

Et nous pouvons utiliser la méthode `serve` et la méthode `eat` de la gaufre passée en paramètre lors de la définition d'une nouvelle méthode `serve` et d'une nouvelle méthode `eat`.

Un DecorateurGaufre ne se soucie pas du type de gaufre. Cela peut être une gaufre_simple, une gaufre_fraise ou une gaufre_alien.

**Tout ce qui compte, c'est qu'un DecorateurGaufre prenne une gaufre et retourne une gaufre améliorée. La gaufre qu'il prend et la gaufre qu'il retourne obéissent à la même interface.**

**Puisque tous les décorateurs prenant et retournant des gaufres obéissent à la même interface, le résultat d'un décorateur peut être passé à un autre décorateur.**

Tout simplement comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cwj-Kt-pZ9EJYeuT3qs8MQ.png)

ou comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*MbOB6SYS8sZl0vhjKxYu4w.png)

Maintenant, avec `Gaufre`, `GaufreFraise`, `GaufreMyrtille` et `GaufreMure`, nous pouvons créer toutes les huit gaufres différentes.

Ajouter la banane à notre liste de garnitures est aussi simple que :

![Image](https://cdn-media-1.freecodecamp.org/images/1*MgXjPD6Y6lBS_gEAONX3-Q.png)

### Vous venez d'apprendre le patron Décorateur ! ???

En voici la définition :

> Le décorateur attache des responsabilités supplémentaires à un objet de manière dynamique.

### Points à retenir :

1. **Le patron décorateur consiste à ajouter facilement des fonctionnalités supplémentaires à un objet existant.**
2. **L'objet à décorer (celui qui est passé à tous les décorateurs) et les objets retournés par les décorateurs doivent obéir à la même interface.**

Merci d'avoir lu ! J'espère que vous avez apprécié l'article. ?

Je publie sur [sihui.io](http://www.sihui.io/) chaque semaine.

Abonnez-vous pour ne pas manquer le prochain article de la série.

La prochaine fois, nous regarderons...

![Image](https://cdn-media-1.freecodecamp.org/images/1*2oEt4tQRLIGwIFExDLUJNw.png)

[1] GaufreSimple, GaufreFraise, GaufreMyrtille, GaufreMure, GaufreFraiseMyrtille, GaufreFraiseMure, GaufreMyrtilleMure et GaufreFraiseMyrtilleMure.

[2] [C(4, 0) + C(4, 1) + C(4, 2) + C(4, 3) + C(4, 4) = 16](https://www.calculatorsoup.com/calculators/discretemathematics/combinations.php)