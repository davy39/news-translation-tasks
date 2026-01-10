---
title: Les Callbacks JavaScript Expliqués avec les Minions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-11T14:59:39.000Z'
originalURL: https://freecodecamp.org/news/javascript-callbacks-explained-using-minions-da272f4d9bcd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BWBpJFpxubK7zjG_ucusFg.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les Callbacks JavaScript Expliqués avec les Minions
seo_desc: 'By Kevin Kononenko

  Callbacks. Asynchronous. Non-blocking.

  These JavaScript concepts are making you tear your hair out.

  I was there too at one point. I needed an analogy to make these abstract concepts
  become easy enough that I could teach them to som...'
---

Par Kevin Kononenko

Callbacks. Asynchrone. Non-bloquant.

Ces concepts JavaScript vous donnent mal à la tête.

J'ai été là aussi à un moment donné. J'avais besoin d'une analogie pour rendre ces concepts abstraits suffisamment faciles pour que je puisse les enseigner à quelqu'un d'autre (et prouver que je les comprenais vraiment moi-même).

Bien sûr, il y avait quelques bons tutoriels (comme [celui-ci](https://github.com/maxogden/art-of-node) et [celui-ci](http://javascriptissexy.com/understand-javascript-callback-functions-and-use-them/)). Mais chaque tutoriel commençait immédiatement avec des termes complexes.

J'avais besoin de quelque chose auquel je pouvais me connecter.

J'avais besoin des Minions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lYgVvfqI8_gVkIiwJAd31w.png)

Alors, je vais utiliser ces adorables minions pour expliquer les callbacks. Dans cette petite analogie, vous êtes leur maître. Vous pouvez ordonner à votre armée de minions de faire ce que vous voulez dans votre code. Mais :

1. Il n'y a qu'un seul maître.
2. Les minions doivent prendre des ordres de vous. Ils ne peuvent pas prendre leurs propres décisions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MGmQ9AlWiGcQ8mNs7dkBTw.jpeg)

> **_Minion._** _Nom. Quelqu'un qui n'est pas puissant ou important et qui obéit aux ordres d'un chef ou patron puissant._

#### Le Concept Principal

Chaque fois que vous voyez « function() » dans votre jQuery ou JavaScript **à l'intérieur d'une autre fonction ou méthode**, imaginez plutôt qu'il dit « minion() ». Vous ne pouvez pas réellement taper cela car le langage JavaScript ne reconnaît pas « minion() » (sauf si vous créez une fonction réelle appelée « minion »). Mais c'est maintenant ce que vous faites lorsque vous créez une fonction de callback - **donner des ordres aux minions**.

_Un exemple avec un minion prêt pour les ordres_

```
function myFunction(input, function(err, data){
```

```
});
```

Cela revient essentiellement à dire...

```
function myFunction(input, minion(err, data){
```

```
});
```

Un exemple avec juste une vieille fonction, pas de minion disponible :

```
function addOne(data){:
```

```
  return data++;
```

```
};
```

### Exemples jQuery

#### Super Basique

Alors, rappelez-vous, c'est un peu comme dire :

Que fait un callback ici ?

Vous, le maître/patron, devez surveiller les événements dans tout le fichier, et potentiellement dans plusieurs fichiers. Vous n'avez pas le temps pour un petit gestionnaire de clics jQuery ! Alors, vous le déléguez à un minion, comme montré dans l'exemple 2.

Maintenant, c'est une fonction simple, et vous pourriez probablement la faire vous-même, mais que se passerait-il si elle faisait 20 lignes de long ? Vous ne pouvez pas être distrait par une fonction de 20 lignes lorsque vous devez également prendre d'autres instructions de l'utilisateur !

Alors, vous dites à un minion de le faire à la ligne 1 après que l'utilisateur a cliqué sur '.myButton'. Cela vous libère pour donner d'autres ordres à plus de minions - beaucoup plus efficace que de le faire vous-même et de faire attendre d'autres fonctions importantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qetQ9kESbuqpF3Q31aFDng.jpeg)

#### Exemple d'Animation

Examinons une séquence d'affichage/masquage pour vraiment souligner l'importance de ces minions.

Dans cet exemple, si vous lisez le code dans l'ordre et que vous n'aviez pas de minions à vos côtés, la console enregistrerait « One », « Two », « Three ». MAIS, vous avez des minions, et la console enregistrera **en réalité** « One », « Three », « Two » dans ce cas. Voici pourquoi :

Ligne 1 : Vous avez ordonné à votre premier minion, et vous êtes passé à surveiller d'autres événements déclenchés par l'utilisateur.

Ligne 2 : Votre premier minion a lu l'instruction de la console, puis est passé à la ligne 3.

Ligne 3 : Le Minion 1 **a fait appel à un autre minion pour aider** : le Minion 2. Plus précisément, le Minion 2 doit rester là et attendre que la méthode show() soit terminée avant de continuer ses instructions. Vous avez maintenant deux minions qui travaillent pour vous, essayant simultanément de terminer leur travail dans la fonction aussi rapidement que possible !

Le Minion 1 saute maintenant jusqu'à la ligne 7, puisque le Minion 2 doit accomplir les lignes 4-5. Il lit l'instruction console.log, et a terminé - plus de callbacks, plus de travail à faire. Le Minion 2, quelques fractions de milliseconde derrière, lit console.log("Two") puis s'assure que la div enfant est affichée à la ligne 5. Maintenant, ce minion a également terminé.

Voici une leçon incroyablement importante : Vos fonctions de callback **définissent l'ordre dans lequel différentes actions se produisent**. Pensez à la puissance de cela : vous pouvez vous assurer qu'une action se produit après une autre, plutôt que d'être forcé de créer une longue chaîne consécutive de commandes. Cela permet beaucoup plus de flexibilité. Si vous ne pouviez pas forcer les minions à exécuter vos ordres, vous devriez tout faire vous-même.

La logique jQuery ci-dessus **ne fonctionne qu'avec les callbacks, en fait**. À la ligne 5, l'affichage de la div enfant **doit** se produire après l'affichage de la div parente. [Vous ne pouvez pas afficher une div enfant](http://stackoverflow.com/questions/5521387/show-child-div-within-hidden-parent-div) si la div parente est masquée. La seule façon de garantir que la div enfant sera affichée **après** la div parente est un callback.

Si il n'y avait pas de callbacks dans l'exemple ci-dessus, la ligne 5 pourrait provoquer une erreur car la méthode show() à la ligne 3 n'aurait pas encore été complétée. Le Minion 1, qui a commencé à la ligne 1, transmet la tâche de compléter les lignes 4-5 au Minion 2 afin que **le Minion 2 puisse attendre la fin de la méthode show() à la ligne 3** avant de commencer le travail sur les lignes 4-5. Cela garantit que le Minion 2 commencera et terminera la deuxième instruction show() après que la première instruction show() soit terminée. Le Minion 1 passe ensuite au reste de la fonction externe, sans avoir besoin d'attendre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cSSzRJb_1A4Sm8PMhU954g.jpeg)

### Exemples en JavaScript Vanilla et Node.js

#### Utilisation de Paramètres et Callbacks

Très bien, un exemple un peu plus compliqué ! Les lignes 2 et 14 déclarent simplement des fonctions, alors sautons à la ligne 20 où l'action commence vraiment. J'ai appelé la fonction speakOrders avec deux paramètres. Le premier est un objet avec les instructions que je veux finalement que mon minion rapporte. Le second est un callback - une fonction nommée reportOrders dans ce cas.

Votre minion ne peut pas reportOrders jusqu'à ce que vous ayez parlé des ordres ! C'est ainsi que ces fonctions sont exécutées. À la ligne 20, j'ai appelé speakOrders avec des instructions. Je saute donc à la ligne 14 pour voir ce que la fonction speakOrders doit faire. Apparemment, elle transmet simplement ces instructions à la fonction de callback.

À la ligne 20, j'ai déclaré que la fonction de callback serait reportOrders, mais cela pourrait être n'importe quoi ! memorizeOrders, tellMySpouse, n'importe quelle autre fonction que vous nommez. Il est standard d'utiliser « callback » dans votre déclaration de fonction à la ligne 14 pour vous assurer que les autres personnes regardant votre code savent qu'un callback devra se produire. Cela pourrait être n'importe quel autre mot cependant ! Voici l'exemple reformulé, minion-ifié.

Il n'y a qu'un seul minion dans cet extrait entier - aux lignes 14-15, remplaçant « callback ».

**Ligne 20 :** J'appelle speakOrders. Je transmets les ordres - l'objet avec le nom et la spécialité. Le second paramètre pourrait être n'importe quoi - une chaîne, une fonction, ou autre chose.

**Lignes 14-15 :** Je définis que le second paramètre doit **être** une fonction de callback puisque à la ligne 15, le minion est suivi de (). Donc, chaque fois que nous appelons la fonction speakOrders, nous savons maintenant que le second paramètre sera une fonction. C'est reportOrders, dans ce cas.

**Ligne 15 :** Je sais de la ligne 20 que mon minion devra exécuter la fonction reportOrders. Il reçoit le paramètre orders, un objet. Il a besoin de ces instructions pour rapporter avec succès.

**Ligne 2 :** La variable orders de la ligne 15 est maintenant référencée comme minionOrders dans la fonction. La fonction reportOrder se termine, et le nom et la spécialité sont rapportés.

Les callbacks sont importants ici pour **tracer clairement un chemin** que l'objet doit suivre. Sans callbacks, ce serait un tas de code dans un ordre avec peu de flexibilité pour réutiliser les fonctions et changer l'ordre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2slDIzfK12CcxrIiMZEEpg.jpeg)

#### Node.js

Jetez un œil à l'exemple suivant qui utilise [Express](http://expressjs.com/) et le [module request](https://github.com/request/request). C'est le plus difficile jusqu'à présent !

Imaginons que l'utilisateur vient d'effectuer une requête GET le long de la route /storeData. Nous commençons donc à la ligne 9. Cet exemple inclut des cas d'utilisation de callbacks des 3 exemples précédents.

1. Il y a un callback dans une méthode à la ligne 9, similaire à l'exemple du gestionnaire de clics jQuery.
2. Il y a une exécution asynchrone à la ligne 14, centrée autour d'une fausse requête API, similaire à l'exemple d'animation jQuery.
3. Il y a un paramètre de callback déclaré à la ligne 13, similaire à l'exemple en JS vanilla.

Pour rendre cela aussi clair que possible, voici le code minion-ifié, avec des numéros de minion indiquant l'ordre dans lequel ils seront exécutés.

**Ligne 9 :** L'utilisateur accède à la route. Vous, le patron, ordonnez au Minion 1 de se mettre au travail sur vos ordres. Il saute à la ligne 10 et voit la fonction readResult. Vous pouvez maintenant attendre plus de signaux de l'utilisateur pendant que vos minions sont au travail.

**Ligne 14 :** Le Minion 1 voit l'appel de requête, l'exécute sur la fausse API, et ordonne au Minion 2 d'attendre le résultat. Le Minion 1 peut passer à d'autres travaux. Comme il n'y en a plus, le Minion 1 est relevé de ses fonctions.

**Ligne 14 :** Le Minion 2 se met en action lorsque l'appel de requête est terminé. Il transporte maintenant trois morceaux d'informations potentiellement importantes de la route - err, response et body.

**Lignes 15-16 :** La variable globale « results » est définie sur la valeur body. Cette variable globale peut maintenant être utilisée dans d'autres fonctions également. Le Minion 2 dit au Minion 3 qu'il est temps de se mettre au travail sur ses instructions. Le Minion 3 a initialement reçu des instructions de la **ligne 10**, et avait attendu de les compléter jusqu'à ce qu'il soit appelé. C'est maintenant le moment de compléter logRes() !

**Ligne 5 :** Et les instructions sont... un console.log. C'était décevant. En tout cas, le Minion 3 a terminé maintenant.

Alors, comment le Minion 3 a-t-il été appelé après le Minion 2 ?

Une sorte de Minion-ception ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*xW5AVfJ9zj8OqIzTzVO3hQ.jpeg)

Si vous revenez au code de l'exemple Node 1, vous verrez que la ligne 13 initialise un callback. Cela signifie que chaque fois que la fonction readResult() est appelée, il doit y avoir un paramètre de callback. Cela prépare le callback pour une utilisation ultérieure à la ligne 16. À la ligne 16, le callback a la capacité d'utiliser les produits de la requête API à la ligne 14 car **l'appel de requête a lui-même un callback** !

Imaginez si callback/minion3 était une ligne plus bas que la ligne 17, en dehors de la portée de l'appel de requête. Tout d'abord, cela en ferait le Minion 2, car il serait exécuté avant que l'appel de requête ne soit terminé. Et, les résultats de l'appel de requête ne seraient pas encore disponibles, ce qui rendrait cette fonction entière assez inutile. Le but est de faire l'appel de requête puis de transmettre les résultats.

Encore une fois, l'utilisation de 2 callbacks séparés dans la fonction readResult() garantit que le Minion 3 se met au travail après la fin de la requête. Les callbacks fournissent un niveau de contrôle afin que vous puissiez déterminer cet ordre personnalisé.

#### Conclusion

Vous êtes le maître des minions, avec des hordes de petits serviteurs prêts à faire vos moindres désirs. Si vous pouvez leur donner les bonnes instructions, ils peuvent rendre votre vie beaucoup plus facile. Ils font tout le travail difficile et vous permettent d'écouter les instructions de l'utilisateur.

Cela vous a-t-il aidé ? Faites-le moi savoir dans les commentaires.