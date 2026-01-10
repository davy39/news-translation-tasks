---
title: Comment utiliser la déstructuration en JavaScript pour écrire un code plus
  propre et plus puissant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T18:00:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-destructuring-in-javascript-to-write-cleaner-more-powerful-code-9d1b38794050
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xJuGwNdtkReGucN_
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser la déstructuration en JavaScript pour écrire un code plus
  propre et plus puissant
seo_desc: 'By Ashay Mandwarya ?️??


  Sometimes you have to destroy to build something new.

  -Mistborn: The Hero of Ages


  ES6 introduced us to one of the most awaited JavaScript features: destructuring.
  As a concept, Destructuring is not new or groundbreaking and ...'
---

Par Ashay Mandwarya 💡✨

> Parfois, il faut détruire pour construire quelque chose de nouveau.

> -Mistborn: Le Héros des Âges

ES6 nous a introduit à l'une des fonctionnalités JavaScript les plus attendues : la déstructuration. En tant que concept, la déstructuration n'est pas nouvelle ni révolutionnaire et certains langages avaient déjà la déstructuration (💡) bien avant. Mais c'était une fonctionnalité très attendue et demandée en JavaScript.

La déstructuration est le processus de décomposition d'une structure. Dans le contexte de la programmation, les structures sont les structures de données, et déstructurer ces structures de données signifie déballer les valeurs individuelles de la structure de données. En JavaScript, la déstructuration peut être appliquée à un Objet ou à un Tableau.

**La déstructuration fait, brise quoi que ce soit... à quoi cela nous sert-il ??**

Avant de répondre à cette question, donnons une définition formelle de la déstructuration. _MDN à la rescousse !_

> La syntaxe d'**affectation par déstructuration** est une expression JavaScript qui permet de déballer des valeurs à partir de tableaux, ou des propriétés à partir d'objets, dans des variables distinctes. -MDN

Regardons quelques exemples pour mieux comprendre les bases de la déstructuration.

#### Tableaux

Exemple 1 :

![Image](https://cdn-media-1.freecodecamp.org/images/vctLJdok3mwgR0m8Fsg3rQnc1Zt-0IdW1BY6)

Lorsque j'ai vu ce simple morceau de code pour la première fois, j'étais perplexe. Je n'ai pas compris ce qui s'était passé. Si vous êtes comme je l'étais, laissez-moi essayer de vous expliquer.

À la ligne 1, nous définissons 2 variables `a` et `b`. À la ligne suivante, les deux variables sont à l'intérieur d'un tableau du côté gauche qui est égalé à un tableau réel du côté droit. Dans les lignes suivantes, nous imprimons les valeurs de `a` et `b` et nous obtenons 7 et 8 respectivement, qui étaient les éléments du tableau RHS. La magie qui se produit à la ligne 2 s'appelle la déstructuration.

Le LHS déstructure le RHS et les valeurs obtenues en déballant les éléments sont assignées aux variables dans l'ordre.

**Mais pourquoi le LHS est-il à l'intérieur d'un tableau ???**

L'affectation par déstructuration utilise une syntaxe similaire, sur le LHS par rapport au RHS pour définir quelles valeurs déballer à partir de la variable source.

Exemple 2 :

![Image](https://cdn-media-1.freecodecamp.org/images/XLVhZxEiMUW3ZcImmob74XfJ35XNICjLHOrK)

Ici, nous avons introduit une autre variable `leftout` dans le code maintenant. Nous avons 2 types d'utilisations différents de `leftout` dans le code.

* `[a,b,leftout]->` Cela assigne le troisième élément du tableau à `leftout` comme prévu.
* `[a,b,...leftout]->` Cela donne les deux premières valeurs à `a` et `b` respectivement et le reste du tableau est assigné à la variable `leftout`.

La solution réside dans l'opérateur `...`. Cet opérateur regroupe tous les arguments restants (**_rest_**) en un seul tableau. Dans le dernier point, les deux premiers éléments du tableau sont assignés à `a` et `b` respectivement, et le reste des arguments est regroupé en un tableau (restructuration peut-être ??) et assigné à la variable `leftout`. Nous pouvons vérifier cela en regardant la sortie.

#### Objets

Exemple 1 :

![Image](https://cdn-media-1.freecodecamp.org/images/0IP9fC5h8SaQgOfRupMy3VrAprZD8Y7Ruuis)

La déstructuration fonctionne de la même manière pour les objets et les tableaux. L'objet du LHS a des propriétés `a` et `b` qui sont assignées respectivement aux propriétés `a` et `b` de l'objet RHS. Nous obtenons 1 et 2 respectivement en les imprimant.

Une chose à remarquer (_si vous avez_) est qu'il y a un léger changement de syntaxe (_maintenant vous avez_).

![Image](https://cdn-media-1.freecodecamp.org/images/wysq-sQxfF1KgL4u4RzGzyLeJJh2Xm6ayZIi)

> _Dans la déstructuration d'objets, tout le LHS et le RHS sont enveloppés dans `()`_

![Image](https://cdn-media-1.freecodecamp.org/images/AEvjPd-JS4LSFQKNPgft2P1HoBu6CsnZ6EXD)

Nous pouvons voir l'erreur que nous obtenons lorsque nous ne l'enveloppons pas dans `()`. **Il dit qu'une déclaration de statement est attendue.**

Ce qui se passe réellement, c'est que le fait d'enfermer quelque chose dans des accolades `{}` confond JavaScript, qui le considère comme un bloc et non comme un objet. En raison de cela, il recherche une déclaration pour le bloc (_déclaration de fonction_), donc nous enfermons le code dans `()`. Cela en fait une expression plutôt qu'un bloc, et nous obtenons nos résultats.

Exemple 2 :

![Image](https://cdn-media-1.freecodecamp.org/images/3VZxBELTjXt0s9TT4XPe9QgKblm-U2wLmocM)

Encore une fois, l'opérateur `rest`. Fonctionne comme dans les tableaux, sauf que cette fois les valeurs restantes sont regroupées dans un objet car la structure à utiliser est définie par le LHS.

### À quoi sert la déstructuration ?

Comme vu dans les exemples ci-dessus, nous connaissons maintenant l'importance de la déstructuration. Il y a beaucoup d'utilisations et différents cas d'utilisation de la déstructuration pour les objets et les tableaux. Nous allons en essayer quelques-uns. (**P.S. —** _les exemples sont valables pour les objets et les tableaux sauf mention contraire._)

#### Affectation de variables

Nous avons déjà vu comment les variables sont affectées dans les exemples ci-dessus, alors regardons un autre exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/qucTgfx8ChDUFSt5e23j9ZC-H-ytxvsm9df1)

Dans cet exemple, un tableau déjà créé est directement affecté pour la déstructuration. Les valeurs sont affectées aux variables néanmoins.

Cela s'applique également aux objets.

#### Valeurs par défaut

Parfois, il peut arriver que nous définissions `n` variables pour obtenir des valeurs à partir de la déstructuration, mais le tableau/objet peut n'avoir que `n-x` éléments. Dans ce cas, `x` variables seront affectées à `undefined`.

![Image](https://cdn-media-1.freecodecamp.org/images/bKDR20pG1uWtpsmLS1HBudY4Gqa7aMhWqb97)

Nous pouvons voir que `b` est indéfini car le tableau n'a tout simplement pas assez d'éléments pour déstructurer et affecter chaque variable.

![Image](https://cdn-media-1.freecodecamp.org/images/cwlRrrmE9KClkUQTlv-QZy9yLLnnhUU1ok8K)

La solution à cela est de donner des valeurs par défaut aux variables, afin que si elles n'ont pas assez d'éléments, les variables prennent des valeurs par défaut plutôt que d'être indéfinies.

#### Échange

L'échange est le processus d'interversion de valeurs entre 2 variables ou plus. Une méthode standard pour effectuer un échange est soit d'utiliser une variable temporaire, soit d'utiliser XOR. En JavaScript, la même chose peut être faite en utilisant la déstructuration.

![Image](https://cdn-media-1.freecodecamp.org/images/tLDijuHCNuduNyMosckz9Duuw6-kx90Qg5wc)
_Utilisation d'une variable temporaire_

![Image](https://cdn-media-1.freecodecamp.org/images/ODUhWbdggQIzMq8eFQMwQaDrQU6JeUJetUs6)
_Utilisation de la déstructuration_

Échange en utilisant une variable temp. Le code est auto-explicatif.

En utilisant la déstructuration, nous échangeons simplement la position des éléments et voilà ! Échange fait.

#### Ignorer les valeurs

Nous pouvons capturer et utiliser uniquement les valeurs qui sont nécessaires et rejeter ou ignorer les valeurs inutiles.

![Image](https://cdn-media-1.freecodecamp.org/images/zIJpQ2bE1p6MFfkierxlodGv1zvAGjxSmFEa)

Ici, nous pouvons voir que nous avons ignoré la valeur du milieu en ne l'affectant à aucune variable, ce qui nous évite des tracas.

#### Affectation indirecte du retour d'une fonction

![Image](https://cdn-media-1.freecodecamp.org/images/vw5YPLogWb2GhazAyBcLhlqEmpVQq7pN8pL0)

Ici, nous pouvons voir que la fonction x retourne un tableau. À la ligne 4 où nous déstructurons, nous fournissons l'appel de fonction qui retourne le tableau et non le tableau directement. Cela rend le code propre et facile à lire et à comprendre.

#### Affectation à de nouvelles variables

Les propriétés peuvent être déballées à partir d'un objet et affectées à une variable avec un nom différent de la propriété de l'objet.<Applicable uniquement aux objets>

![Image](https://cdn-media-1.freecodecamp.org/images/mdhZkJwQQ8sUBjGxMGB0-q1mRY40hNHuRN90)

Nous pouvons voir que les valeurs des propriétés sont également des variables auxquelles des valeurs sont affectées via la déstructuration.

#### Déstructuration d'objets et de tableaux imbriqués

![Image](https://cdn-media-1.freecodecamp.org/images/EDN-Rs05z2noXItyxqtnPY9fIo9G3fYZ5p5J)

Comme nous pouvons le voir, les données sont un objet qui a une propriété appelée location qui contient à son tour un tableau dont les éléments sont des objets.

Avec la déstructuration, nous devons obtenir les valeurs de toutes les propriétés présentes à l'intérieur de l'objet à l'intérieur du tableau de location.

Nous avons donc créé un objet appelé obj qui contient la même structure que l'objet de données, et les valeurs que nous voulons déballer sont fournies en tant que variables (mylatitude, mylongitude, mycity). Celles-ci sont à leur tour égalées au tableau de données (même syntaxe que la déstructuration précédente). Lorsque les variables sont imprimées, nous obtenons les valeurs respectives.

#### Déstructuration avec la boucle for-of

![Image](https://cdn-media-1.freecodecamp.org/images/ZMbT6bd6j3NX79H9wD5MwfUR4dpfw-TcKZ5S)

Dans l'extrait de code ci-dessus, nous avons un tableau de personnes dont les propriétés contiennent à leur tour un objet (people > object >family). Maintenant, nous voulons déballer certaines des valeurs de l'objet en utilisant la boucle for..of.

Dans la boucle, nous avons affecté une variable objet, avec la même structure que dans le tableau de personnes, en ignorant les valeurs dont nous n'avons pas besoin. Nous avons affecté les variables n et m respectivement aux propriétés name et mother, car ce sont les valeurs que nous voulons déballer. À l'intérieur de la boucle, nous imprimons les variables et nous obtenons les valeurs nécessaires.

### Le grand tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1qA678ILbFdyrsQbPU23KMUDk6KCS5g30XFC)
_Photo par [Unsplash](https://unsplash.com/@jeremybishop?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title="">Jeremy Bishop</a> sur <a href="https://unsplash.com?utm_source=medium&utm_medium=referral" rel="noopener" target="_blank" title=")_

Vous devez utiliser la déstructuration dans votre code ou la pratiquer pour vraiment la maîtriser. Cela semble simple dans les exemples parce que les exemples sont juste là pour vous faire comprendre les bases. Avec des opérations complexes/multiples (reduce()!), la déstructuration peut rapidement devenir confuse, ce que nous ne voulons pas !

De plus, vous pourriez aussi penser que la déstructuration est juste une syntaxe sucrée pour effectuer un ensemble de tâches (comme nous pouvons donner aux variables la valeur de chaque élément d'un tableau en utilisant une boucle for). Dans une certaine mesure, nous pouvons dire que c'est du sucre, mais lorsque nous regardons l'image plus large, 'Le Grand Tableau', nous comprendrons pourquoi la déstructuration a plus de valeur que celle d'un simple minimiseur de code.

JavaScript a de nombreuses opérations pour extraire ainsi que pour construire des données, mais toutes travaillent sur un élément à la fois.

**Pour construire**

![Image](https://cdn-media-1.freecodecamp.org/images/QZXe1vAOI2Ej9qAbqIh6Wy-jGFquOKRXRQoP)

**Pour extraire** (toujours un à la fois)

![Image](https://cdn-media-1.freecodecamp.org/images/u4ESs-rTstc3LGGnOC-pZMNU0Coi1vq-wlxD)

Bien qu'il existe une syntaxe pour construire plusieurs propriétés à la fois, elle ne peut être utilisée qu'au moment de l'affectation — elle ne peut pas être utilisée pour modifier un objet existant.

![Image](https://cdn-media-1.freecodecamp.org/images/g07Cm8JHppxOkVc7xSyb08lJtJWIgGCjWc7L)

Avant l'introduction d'ES6, il n'y avait aucun mécanisme pour extraire toutes les données à la fois. C'est là que la déstructuration a vraiment brillé. Elle vous permet d'extraire plusieurs propriétés d'un objet. Nous avons vu cela dans les exemples ci-dessus.

#### Pièges

Il n'y en a qu'un auquel je peux penser et dont nous avons discuté :

* Une instruction ne doit pas commencer par une accolade `{`

### Conclusion

J'ai essayé de simplifier la déstructuration en démontrant autant de cas d'utilisation de la déstructuration que possible. J'espère que cela a rendu ce concept clair pour vous. Maintenant, vous pouvez utiliser la déstructuration pour écrire un code puissant et propre.

![Image](https://cdn-media-1.freecodecamp.org/images/sUivtdGf22RnNFYooZCq1j0mWzsiOTnKt0yk)
_Google_