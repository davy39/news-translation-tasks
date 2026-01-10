---
title: Un guide pratique pour écrire du JavaScript plus fonctionnel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T17:22:03.000Z'
originalURL: https://freecodecamp.org/news/a-practical-guide-to-writing-more-functional-javascript-db49409f71
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c_rulVp2cySUU7cqzguMyw.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un guide pratique pour écrire du JavaScript plus fonctionnel
seo_desc: 'By Nadeesha Cabral

  Functional programming is great. With the introduction of React, more and more JavaScript
  front-end code is being written with FP principles in mind. But how do we start
  using the FP mindset in everyday code we write? I’ll attempt ...'
---

Par Nadeesha Cabral

La programmation fonctionnelle est formidable. Avec l'introduction de React, de plus en plus de code front-end JavaScript est écrit en gardant à l'esprit les principes de la FP. Mais comment commencer à utiliser l'état d'esprit FP dans le code que nous écrivons au quotidien ? Je vais essayer d'utiliser un bloc de code quotidien et de le refactoriser étape par étape.

**Notre problème :** Un utilisateur qui arrive sur notre page `/login` aura optionnellement un paramètre de requête `redirect_to`. Comme `/login?redirect_to=%2Fmy-page`. Notez que `%2Fmy-page` est en réalité `/my-page` lorsqu'il est encodé comme partie de l'URL. Nous devons extraire cette chaîne de requête et la stocker dans le stockage local, afin qu'une fois la connexion effectuée, l'utilisateur puisse être redirigé vers `my-page`.

### Étape #0 : L'approche impérative

Si nous devions exprimer la solution sous la forme la plus simple d'une liste de commandes, comment l'écriions-nous ? Nous devrons

1. Analyser la chaîne de requête.
2. Obtenir la valeur `redirect_to`.
3. Décoder cette valeur.
4. Stocker la valeur décodée dans localStorage.

Et nous devons également placer des blocs try catch autour des fonctions "non sécurisées". Avec tout cela, notre bloc de code ressemblera à :

### Étape #1 : Écrire chaque étape comme une fonction

Pour un moment, oublions les blocs try catch et essayons d'exprimer tout cela comme une fonction ici.

Lorsque nous commençons à exprimer tous nos "résultats" comme des résultats de fonctions, nous voyons ce que nous pouvons refactoriser hors du corps de notre fonction principale. Lorsque cela se produit, notre fonction devient beaucoup plus facile à comprendre et beaucoup plus facile à tester.

Auparavant, nous aurions testé la fonction principale dans son ensemble. Mais maintenant, nous avons 4 fonctions plus petites, et certaines d'entre elles ne font que proxy d'autres fonctions, donc l'empreinte qui doit être testée est beaucoup plus petite.

Identifions ces fonctions de proxy et supprimons le proxy, afin d'avoir un peu moins de code.

### Étape #2 : Une tentative de composition de fonctions

D'accord. Maintenant, il semble que la fonction `persistRedirectToParams` soit une "composition" de 4 autres fonctions. Voyons si nous pouvons écrire cette fonction comme une composition, éliminant ainsi les résultats intermédiaires que nous stockons sous forme de `const`.

C'est bien. Mais je compatis pour la personne qui lit cet appel de fonction imbriqué. S'il y avait un moyen de démêler ce gâchis, ce serait génial.

### Étape #3 : Une composition plus lisible

Si vous avez fait du redux ou du recompose, vous avez probablement rencontré `compose`. Compose est une fonction utilitaire qui accepte plusieurs fonctions et retourne une fonction qui appelle les fonctions sous-jacentes une par une. Il existe d'autres [sources excellentes](https://medium.com/front-end-weekly/pipe-and-compose-in-javascript-5b04004ac937) pour apprendre la composition, donc je ne vais pas entrer dans les détails ici.

Avec compose, notre code ressemblera à :

Une chose avec compose est qu'il réduit les fonctions de droite à gauche. Donc, la première fonction qui est invoquée dans la chaîne `compose` est la dernière fonction.

Ce n'est pas un problème si vous êtes mathématicien et que vous êtes familier avec le concept, donc vous lisez naturellement cela de droite à gauche. Mais pour le reste d'entre nous, familiers avec le code impératif, nous aimerions lire cela de gauche à droite.

### Étape #4 : Piping et aplatissement

Heureusement, il y a `pipe`. `pipe` fait la même chose que `compose`, mais dans l'ordre inverse. Donc, la première fonction de la chaîne est la première fonction à traiter le résultat.

De plus, il semble que notre fonction `persistRedirectToParams` soit devenue un wrapper pour une autre fonction que nous appelons `op`. En d'autres termes, tout ce qu'elle fait est d'exécuter `op`. Nous pouvons nous débarrasser du wrapper et "aplatir" notre fonction.

Presque là. Rappelez-vous, que nous avons commodément laissé notre bloc `try-catch` derrière nous pour arriver à l'état actuel ? Eh bien, nous devons trouver un moyen de le réintroduire. `qs.parse` est non sécurisé ainsi que `storeRedirectToQuery`. Une option est de les rendre des fonctions wrapper et de les mettre dans des blocs `try-catch`. L'autre, manière fonctionnelle est d'exprimer `try-catch` comme une fonction.

### Étape #5 : Gestion des exceptions comme une fonction

Il existe quelques utilitaires qui font cela, mais essayons d'écrire quelque chose nous-mêmes.

Notre fonction ici attend un objet `opts` qui contiendra les fonctions `tryer` et `catcher`. Elle retournera une fonction qui, lorsqu'elle est invoquée avec des arguments, appelle le `tryer` avec lesdits arguments et, en cas d'échec, appelle le `catcher`. Maintenant, lorsque nous avons des opérations non sécurisées, nous pouvons les mettre dans la section `tryer` et, si elles échouent, les sauver et donner un résultat sûr depuis la section `catcher` (et même logger l'erreur).

### Étape #6 : Mettre tout ensemble

Donc, avec cela en tête, notre code final ressemble à :

C'est plus ou moins ce que nous voulons. Mais pour nous assurer que la lisibilité et la testabilité de notre code s'améliorent, nous pouvons factoriser les fonctions "sûres" également.

Maintenant, ce que nous avons, c'est une implémentation d'une fonction beaucoup plus grande, composée de 4 fonctions individuelles qui sont hautement cohésives, faiblement couplées, peuvent être testées indépendamment, peuvent être réutilisées indépendamment, tiennent compte des scénarios d'exception et sont hautement déclaratives. (Et à mon avis, elles sont un peu plus agréables à lire.)

Il y a un peu de sucre syntaxique FP qui rend cela encore plus agréable, mais ce sera pour une autre fois.