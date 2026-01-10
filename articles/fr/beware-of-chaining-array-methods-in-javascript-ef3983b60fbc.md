---
title: Attention à l'enchaînement des méthodes de tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/beware-of-chaining-array-methods-in-javascript-ef3983b60fbc
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1s3_FsFSnJzT2Byq.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Attention à l'enchaînement des méthodes de tableau en JavaScript
seo_desc: 'By Balaganesh Damodaran

  JavaScript’s Array class exposes quite a few methods (filter, map, reduce), which
  iterate through an array and call an iterator function to perform actions on the
  array. Chaining these methods allows you to write clean, easy t...'
---

Par Balaganesh Damodaran

La classe Array de JavaScript expose plusieurs méthodes (filter, map, reduce), qui parcourent un tableau et appellent une fonction itérative pour effectuer des actions sur le tableau. L'enchaînement de ces méthodes permet d'écrire un code propre et facile à lire. Mais quel est le coût de cette commodité en termes de performance, et en vaut-il la peine ?

![Image](https://cdn-media-1.freecodecamp.org/images/4iKtwVSXgNmeSNOpUi2enoqqLfGHOsV8ezhB)

JavaScript est un langage "fonctionnel". Cela signifie que les fonctions sont des objets de première classe en JavaScript, et à ce titre, elles peuvent être passées en tant que paramètres à d'autres fonctions. Il existe plusieurs méthodes intégrées fournies par la bibliothèque standard JavaScript, qui utilisent ce fait pour nous permettre d'écrire un code propre, compréhensible et facile à lire.

#### Méthodes de tableau JavaScript intégrées, et enchaînement

Une classe intégrée qui utilise largement la nature fonctionnelle de JavaScript est la classe `Array`. Les `Array` en JavaScript exposent un certain nombre de méthodes d'instance, qui :

* acceptent une fonction comme argument,
* itèrent sur le tableau,
* et appellent la fonction, en passant l'élément du tableau comme paramètre à la fonction.

Les plus populaires de ces méthodes sont bien sûr `forEach`, `filter`, `map` et `reduce`. Comme certaines de ces méthodes retournent également l'instance `Array` comme valeur de retour de la méthode, elles sont souvent enchaînées comme ceci :

```
const tripExpenses = [{    amount: 12.07,    currency: 'USD',    paid: true}, {    amount: 1.12,    currency: 'USD',    paid: true}, {    amount: 112.00,    currency: 'INR',    paid: false}, {    amount: 54.17,    currency: 'USD',    paid: true}, {    amount: 16.50,    currency: 'USD',    paid: true}, {    amount: 189.50,    currency: 'INR',    paid: false}];
```

```
const totalPaidExpensesInINR = tripExpenses    .filter(expense => expense.paid)    .map(expense => {        if(expense.currency == 'USD')            return expense.amount * 70;        else            return expense.amount;    })    .reduce((amountA, amountB) => amountA + amountB);
```

Dans cet exemple, nous calculons le total des dépenses payées après les avoir converties de USD en INR. Pour ce faire, nous :

* `filter`ons `tripExpenses` pour extraire uniquement les dépenses payées,
* `map`pons le montant de la dépense de la devise spécifiée et le convertissons en INR, et
* `reduce`ons les montants en INR pour obtenir la somme.

Cela ressemble à un cas d'utilisation courant, très typique et valide pour l'enchaînement des méthodes de tableau, n'est-ce pas ? Beaucoup de développeurs qui ont été formés à écrire du JavaScript fonctionnel proposeraient quelque chose de similaire s'ils devaient résoudre ce problème.

#### Le problème avec l'enchaînement des méthodes de tableau

Actuellement, notre tableau `tripExpenses` ne contient que 6 éléments, donc cela est relativement rapide. Mais que se passe-t-il lorsque nous devons analyser les dépenses de voyage pour, par exemple, une entreprise entière d'employés pour toute l'année financière, et que notre tableau `tripExpenses` commence à contenir des centaines de milliers d'éléments ?

Grâce à JSPerf, nous pouvons visualiser ce coût assez facilement. Faisons donc un test de comparaison pour le même code avec `tripExpenses` contenant 10 éléments, 10 000 éléments et 100 000 éléments. Voici le résultat de la [comparaison JSPerf](https://jsperf.com/array-operations-builtin-vs-foreach/1) :

![Image](https://cdn-media-1.freecodecamp.org/images/oMRqEBBgNA9IHRWGLEzakbXFEMcL2Gfb2gyv)

Le graphique montre le nombre d'opérations par seconde, et plus c'est élevé, mieux c'est. Bien que je m'attendais à ce que le cas des 100 000 éléments soit lent, je ne m'attendais pas à ce que le cas des 10 000 éléments soit aussi lent. Comme ce n'est pas vraiment visible sur le graphique, regardons les chiffres :

* 10 Éléments — 6 142 739 ops par seconde
* 10 000 Éléments — 2 199 ops par seconde
* 100 000 Éléments — 223 ops par seconde

Ouch, c'est vraiment mauvais ! Et bien que le traitement d'un tableau de 100 000 éléments ne se produise peut-être pas souvent, 10 000 éléments est un cas d'utilisation très plausible que j'ai vu régulièrement dans plusieurs applications que j'ai développées (principalement côté serveur).

Cela nous montre que lorsque nous écrivons — même ce qui semble être un code assez simple — nous devons vraiment surveiller les problèmes de performance qui pourraient survenir à cause de la manière dont nous écrivons notre code.

Si, au lieu d'enchaîner les méthodes `filter`, `map` et `reduce` ensemble, nous réécrivons notre code de sorte que tout le travail soit fait en ligne, dans une seule boucle, nous pouvons obtenir des performances significativement meilleures.

```
let totalPaidExpensesInINR = 0;
```

```
for(let expense of tripExpenses){    if(expense.paid){        if(expense.currency == 'USD')            totalPaidExpensesInINR += (expense.amount * 70);        else            totalPaidExpensesInINR += expense.amount;    }}
```

Faisons une autre [comparaison JSPerf](https://jsperf.com/functional-vs-for-of-array-methods/1) pour voir comment cela se comporte par rapport à son homologue fonctionnel, dans un test de 10 000 éléments :

![Image](https://cdn-media-1.freecodecamp.org/images/qMXDUV7I2B1K8LguRGP6BwmcPSeG59PeuxaL)

Comme vous pouvez le voir, sur Chrome (et par extension Node.JS), l'exemple fonctionnel est 77 % plus lent que l'exemple for-of. Sur Firefox, les chiffres sont plus proches, mais l'exemple fonctionnel est toujours 16 % plus lent que l'exemple for-of.

#### Pourquoi un tel écart de performance ?

Alors, pourquoi l'exemple fonctionnel est-il si beaucoup plus lent que l'exemple for-of ? C'est une combinaison de facteurs, mais les principaux facteurs que, en tant que développeur, nous pouvons contrôler depuis le code utilisateur sont :

* Parcourir les mêmes éléments de tableau plusieurs fois.
* Le surcoût des appels de fonction pour chaque itération dans l'exemple fonctionnel.

Si vous regardez l'exemple for-of, vous verrez que nous ne parcourons le tableau `tripExpenses` qu'une seule fois. De plus, nous n'appelons aucune fonction depuis l'intérieur, mais effectuons nos calculs en ligne.

L'un des grands gains de performance des moteurs JavaScript modernes est l'inlining des appels de fonction. Cela signifie que le moteur compilera en réalité votre code dans une version où le compilateur remplace l'appel de fonction par la fonction elle-même (c'est-à-dire en ligne où vous appelez la fonction). Cela élimine le surcoût de l'appel de la fonction et offre d'énormes gains de performance.

Cependant, nous ne pouvons pas toujours dire avec certitude si un moteur JavaScript choisira d'inliner une fonction ou non, donc le faire nous-mêmes garantit que nous avons les meilleures performances possibles.

### Conclusion

Certains développeurs peuvent considérer l'exemple for-of comme moins lisible et plus difficile à comprendre que l'exemple fonctionnel. Pour cet exemple particulier, je dirais que les deux styles sont également lisibles. Cependant, dans le cas de l'exemple fonctionnel, la commodité de l'enchaînement des méthodes tend à cacher les multiples itérations et appels de fonction au développeur, rendant ainsi facile pour un développeur inexpérimenté d'écrire du code non performant.

Je ne dis pas que vous devriez toujours éviter la manière fonctionnelle — je suis sûr qu'il existe de nombreux cas valides pour utiliser la manière fonctionnelle et pour enchaîner les méthodes. Mais une règle générale à retenir en matière de performance et d'itération de tableaux en JavaScript est que si vous enchaînez des méthodes qui parcourent l'ensemble du tableau, vous devriez probablement vous arrêter et considérer l'impact sur les performances avant de continuer.

J'aimerais connaître votre opinion sur ce que j'ai écrit dans cet article. N'hésitez pas à laisser vos commentaires ci-dessous.

#### [6 février 2019] Quelques mises en garde et points à garder à l'esprit, comme le soulignent les commentateurs

Comme [le souligne](https://medium.com/@paul.beynon/thanks-for-taking-the-time-to-write-the-article-i-enjoyed-it-db916026647) [Paul B](https://www.freecodecamp.org/news/beware-of-chaining-array-methods-in-javascript-ef3983b60fbc/undefined), il y a un impact sur les performances lors de l'utilisation de `for...of` dans une forme transpilée dans les navigateurs, mais vous pouvez toujours utiliser une boucle for normale avec une variable itérative pour contourner cela. Cependant, comme le dit Paul, il y a plusieurs avantages à rester avec une fonction itérative. Allez lire [son commentaire](https://medium.com/@paul.beynon/thanks-for-taking-the-time-to-write-the-article-i-enjoyed-it-db916026647), il mérite d'être un article à part entière.

De plus, beaucoup de gens ont également dit que cela serait une optimisation prématurée ou une micro-optimisation, et je suis partiellement d'accord avec eux. Vous devriez en général toujours optimiser pour la lisibilité et la maintenabilité plutôt que pour la performance, jusqu'au point où la mauvaise performance commence réellement à vous impacter. Une fois que vous avez atteint ce point, vous pourriez vouloir reconsidérer vos itérateurs.

_Publié à l'origine sur [asleepysamurai.com](https://asleepysamurai.com/articles/beware-chaining-array-methods-javascript?ref=medium) le 8 janvier 2019._