---
title: Qu'est-ce qu'une conditionnelle en JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-14T12:25:00.000Z'
originalURL: https://freecodecamp.org/news/what-in-the-world-is-a-javascript-conditional-for
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/scott-webb-GQD3Av_9A88-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Conditionals
  slug: conditionals
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce qu'une conditionnelle en JavaScript ?
seo_desc: 'By Syk Houdeib

  This article is a beginner''s introduction to JavaScript conditionals. It covers
  why we need them, and how they fit into the front-end context. And why you will
  end up using them regularly.

  Introduction

  I came into development from a no...'
---

Par Syk Houdeib

Cet article est une introduction aux conditionnelles en JavaScript pour les débutants. Il explique pourquoi nous en avons besoin et comment elles s'intègrent dans le contexte du développement front-end. Et pourquoi vous finirez par les utiliser régulièrement.

## Introduction

Je suis arrivé dans le développement par un parcours non traditionnel. Une chose était toujours particulièrement difficile – pouvoir aller au-delà de la syntaxe d'un nouveau concept et le placer dans un contexte qui avait du sens.

Les conditionnelles sont un peu plus intuitives que d'autres concepts, mais je veux vous montrer le tableau d'ensemble. Dans cet article, je vais expliquer pourquoi nous avons besoin des conditionnelles et comment nous pouvons les utiliser en tant que développeurs front-end.

À l'aide d'un exemple pratique adapté aux débutants, vous verrez comment vous pouvez utiliser les conditionnelles pour traiter les données de différentes manières et pourquoi elles sont un outil fondamental en développement. N'hésitez pas à suivre pendant que vous lisez cet article.

Le seul prérequis est une compréhension de base des tableaux et des boucles. J'ai couvert ces sujets dans deux articles précédents :

**Tableaux** : [https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/)

**Boucles** : [https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/)

### L'installation

Imaginons que nous travaillons sur une plateforme en ligne qui nous permet de faire nos courses depuis un site web. C'est une application concrète des choses dont nous voulons parler ici.

Jetez un coup d'œil à [Lola Market](https://lolamarket.com/tienda), où je travaille, pour un exemple de ce à quoi cela pourrait ressembler.

Dans l'exemple que nous avons mis en place dans les articles précédents, nous avons pris un ensemble de produits (champignons, steak, poisson, aubergines et lentilles) et nous les avons organisés à l'intérieur d'un tableau. Nous avons ensuite stocké ce tableau comme une variable et utilisé une boucle `forEach` pour itérer sur la liste.

Nous supposons que cette liste de produits est maintenant affichée sur notre site web. Notre tâche est d'ajouter un "(v)" à côté des articles végétariens sur cette liste. C'est exactement le genre de chose que nous faisons régulièrement en front-end.

## Conditionnelles

Les conditionnelles sont des éléments de construction essentiels de la programmation. Elles sont un moyen de faire quelque chose uniquement **si** certaines **conditions** sont remplies. La conditionnelle la plus simple et la plus courante en JavaScript est l'instruction `if`. Voici un exemple :



```js
if (product === 'steak') {
    // faire des choses
}
```

Commençons par traduire cela en français : "Si la variable appelée `product` est exactement la chaîne de caractères 'steak', alors exécutez le code à l'intérieur."

Voici une analyse plus détaillée :

* `if` : C'est la conditionnelle.
* `(product === 'steak')` : C'est notre condition. Il existe de nombreuses façons de construire des conditions. Nous n'avons pas besoin de nous en soucier pour l'instant. Pour l'instant, gardez à l'esprit que tout ce que nous mettons ici sera toujours évalué à `true` ou `false`.
* `// faire des choses` : L'instruction. C'est ici que le code que nous voulons exécuter va. Il sera exécuté **uniquement** si le résultat de l'évaluation de la condition est `true`. Sinon, il sera ignoré.

Ce morceau de code fonctionnera très bien tout seul, mais nous pouvons avoir un contrôle beaucoup plus détaillé en utilisant ses amis `else if` et `else`. `else if` ajoute une autre condition à vérifier et exécute un autre bloc de code séparé, tandis que `else` devient l'action par défaut à prendre si aucune des conditions n'est remplie.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-214.png)
_Photo par [Unsplash](https://unsplash.com/@jckbck?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Jakub Dziubak</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Adapté aux végétariens

Concentrons-nous à nouveau sur notre objectif initial, qui est d'ajouter un "(v)" à côté du nom des articles végétariens. C'est un exemple parfait de quand nous devons utiliser une conditionnelle. Nous voulons un code qui, **si** le `product` dans le tableau **est** végétarien, imprime son nom et ajoute le "(v)". Et s'il n'est pas végétarien, imprime uniquement le nom du `product`.

Tout d'abord, nous devons identifier les articles végétariens. Normalement, cette information sera incluse avec les données que nous avons demandées à notre base de données. Mais puisque nous utilisons un exemple simplifié, nous le ferons manuellement. Nous savons que le steak et le poisson ne sont pas végétariens.

Remarquez, la condition que je teste est si un produit **n'est pas** végétarien. Cela est seulement parce qu'il y a plus de produits végétariens sur cette liste et je veux que la condition soit simple et que la conditionnelle fasse le moins de travail possible. J'aurais tout aussi facilement pu tester pour les articles végétariens à la place.

Il existe souvent de nombreuses conditions qui peuvent être utilisées pour atteindre le même objectif. Écrire de bonnes conditions qui sont efficaces et lisibles est une compétence utile qui vient avec la pratique.

Alors écrivons la condition qui sépare les végétariens des non-végétariens.

```js
if (product === 'steak' || product === 'fish') {
    console.log(product)
} else {
    console.log(product + '(v)')
}
```

En suivant l'exemple de mes articles précédents (liés ci-dessus), nous voulons placer la conditionnelle à l'intérieur de la boucle. La boucle nous donne chaque produit dans la liste à traiter individuellement. Ce bloc conditionnel est le code que nous exécutons pour chaque produit dans notre tableau de produits maintenant.

Actualisez le navigateur pour commencer avec une console fraîche, puis entrez ce qui suit :

* La variable `product` stockant notre tableau de produits.
* La boucle `forEach` itérant sur le tableau.
* Et notre bloc conditionnel à l'intérieur.

![The dev tools console with our full code now using the conditional inside of the loop](https://www.freecodecamp.org/news/content/images/2019/09/conditional.PNG)
_Le bloc conditionnel s'exécutant à l'intérieur d'une boucle_

### Exécution

Si nous lisons le code conditionnel en **français simple**, il dit : "**Si** le `product` actuellement sélectionné **est** exactement 'steak' **ou** 'fish', alors enregistrez `product` dans la console. Sinon, dans tous les autres cas, enregistrez `product` dans la console mais ajoutez également une chaîne "(v)" à la fin."

Note rapide, l'opérateur `===` vérifie que les expressions de gauche et de droite sont **exactement** les mêmes. et l'opérateur `||` signifie **ou**. Nous avons deux conditions à vérifier ici (steak ou fish). Si **l'une ou l'autre** des deux conditions est vraie, elle exécutera le code à l'intérieur.

Appuyez sur Entrée pour exécuter le code et voir les résultats.

![The result of executing the code in the console. It prints the vegetarian items with a (v) at the end](https://www.freecodecamp.org/news/content/images/2019/09/conditional-result.PNG)
_Le résultat de la boucle avec les conditionnelles_

Et voilà. Chaque fois que la boucle s'exécute, elle vérifie l'élément actuellement sélectionné `product` et passe par les conditionnelles.

* Est-ce que `product` est exactement la chaîne 'steak' ?
* Non. Vérifiez la condition suivante.
* Est-ce que `product` est exactement la chaîne 'fish' ?
* Non. Cette condition n'est pas remplie, le code à l'intérieur ne sera pas exécuté. Allez au code par défaut spécifié dans le bloc `else`.
* Imprimez `product` et ajoutez `(v)` à la fin.
* Cette itération est terminée. Commencez l'itération suivante.

Si elle trouve 'steak' ou 'fish', elle exécutera le code à l'intérieur de cette condition en enregistrant le nom du `product` sans le "(v)". Ensuite, la boucle termine cette itération et commence la suivante, et ainsi de suite. Ce processus se répète pour chaque élément du tableau jusqu'à ce que tout soit terminé et que la boucle ait enregistré le message correct pour chacun.

## Conclusion

Pour résumer, une **instruction conditionnelle** définit certaines **conditions**. Lorsque ces conditions sont remplies (ce qui signifie que la condition est évaluée à `true`), le code spécifié à l'intérieur du bloc conditionnel **s'exécute**. Sinon, il est ignoré et non exécuté.

Dans notre exemple, nous avons uniquement enregistré des messages dans la console. Mais nous pouvons utiliser la même idée pour manipuler le DOM afin d'afficher et de modifier le contenu sur un site web.

Voici quelques éléments dont vous aurez besoin pour approfondir vos connaissances et comprendre ces concepts plus en profondeur :

* **Conditionnelles** : L'instruction `if` est l'une des conditionnelles les plus couramment utilisées. Mais vous devrez apprendre d'autres comme l'instruction `while`, l'instruction `switch`, ou l'opérateur **ternaire** très utile.
* **Conditions** : Comprenez comment créer des conditions et comment elles sont évaluées. Pour cela, vous devez vous familiariser avec les concepts de "**truthy**" et "**falsy**". C'est lorsque des valeurs qui ne sont pas explicitement `true` ou `false` sont évaluées comme telles. Par exemple, une chaîne comme `'mushrooms'` est considérée comme vraie alors qu'une chaîne vide `''` est toujours considérée comme fausse.
* **Opérateurs logiques et opérateurs de comparaison** : Nous les avons vus dans nos conditions. Opérateurs logiques comme "et" et "ou", écrits `&&` et `||`. Opérateurs de comparaison comme "égal" et "supérieur à", écrits `===` et `>`. Ce sont des concepts simples qui sont le pain et le beurre de l'écriture de code.

### Clôture

Merci d'avoir lu. J'espère que vous avez trouvé cela utile. Et si vous avez aimé, le partager serait grandement apprécié. Si vous avez des questions ou des commentaires, je suis sur [Twitter](https://twitter.com/Syknapse) [@Syknapse](https://twitter.com/Syknapse) et j'adorerais avoir de vos nouvelles.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-157.png)
_Photo par [Claudia](https://twitter.com/__Santaella)_

Je m'appelle Syk et je suis développeur front-end chez [Lola Market](https://twitter.com/Tech_LolaMarket) à Madrid. J'ai changé de carrière pour devenir développeur web depuis un domaine sans rapport, alors j'essaie de créer du contenu pour ceux qui sont sur un parcours similaire. Mes messages privés sont toujours ouverts pour les développeurs web en herbe ayant besoin de soutien. Vous pouvez également lire ma transformation dans [cet article](https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/).