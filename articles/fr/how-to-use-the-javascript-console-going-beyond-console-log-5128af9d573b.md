---
title: 'Comment utiliser la console JavaScript : aller au-delà de console.log()'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T16:46:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-javascript-console-going-beyond-console-log-5128af9d573b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*98a_Z2uEDzLDmjPM4k37iQ.png
tags:
- name: debugging
  slug: debugging
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Comment utiliser la console JavaScript : aller au-delà de console.log()'
seo_desc: 'By Yash Agrawal

  One of the easiest ways to debug anything in JavaScript is by logging stuff using
  console.log. But there are a lot of other methods provided by the console that can
  help you debug better.

  Let’s get started.

  The very basic use case is ...'
---

Par Yash Agrawal

L'une des façons les plus simples de déboguer quoi que ce soit en JavaScript est d'utiliser `console.log` pour journaliser des informations. Mais il existe de nombreuses autres méthodes fournies par la console qui peuvent vous aider à mieux déboguer.

Commençons.

Le cas d'utilisation le plus basique consiste à journaliser une chaîne de caractères ou un ensemble d'objets JavaScript. Tout simplement,

```
console.log('Est-ce que cela fonctionne ?');
```

Maintenant, imaginez un scénario où vous avez un ensemble d'objets que vous devez journaliser dans la console.

```
const foo = { id: 1, verified: true, color: 'green' };const bar = { id: 2, verified: false, color: 'red' };
```

La manière la plus intuitive de journaliser cela est de simplement faire `console.log(variable)` l'un après l'autre. Le problème devient plus apparent lorsque nous voyons comment cela s'affiche sur la console.

![Image](https://cdn-media-1.freecodecamp.org/images/c220lbTo-NzOW5Q3jZr-sPJBZv5HeGad2Xx-)
_Aucun nom de variable visible_

Comme vous pouvez le voir, aucun nom de variable n'est visible. Cela devient extrêmement ennuyeux lorsque vous avez un ensemble de ces variables et que vous devez développer la petite flèche à gauche pour voir exactement quel est le nom de la variable. Entrez les noms de propriétés calculés. Cela nous permet de regrouper toutes les variables ensemble dans un seul `console.log({ foo, bar });` et le résultat est facilement visible. Cela réduit également le nombre de lignes `console.log` dans notre code.

#### console.table()

Nous pouvons aller plus loin en mettant tout cela ensemble dans un tableau pour le rendre plus lisible. Chaque fois que vous avez des objets avec des propriétés communes ou un tableau d'objets, utilisez `console.table()`. Ici, nous pouvons utiliser `console.table({ foo, bar})` et la console affiche :

![Image](https://cdn-media-1.freecodecamp.org/images/Wv3Q2yinN6TXt9ZHxRhcE8QSTlCVhyvMBizE)
_console.table en action_

#### console.group()

Cela peut être utilisé lorsque vous souhaitez regrouper ou imbriquer des détails pertinents ensemble pour pouvoir lire facilement les journaux.

Cela peut également être utilisé lorsque vous avez quelques instructions de journalisation dans une fonction et que vous souhaitez pouvoir voir clairement la portée correspondant à chaque instruction.

Par exemple, si vous journalisez les détails d'un utilisateur :

```
console.group('Détails de l\'utilisateur');console.log('nom : John Doe');console.log('métier : Développeur de logiciels');
```

```
// Groupe imbriquéconsole.group('Adresse');console.log('Rue : 123 Townsend Street');console.log('Ville : San Francisco');console.log('État : CA');console.groupEnd();
```

```
console.groupEnd();
```

![Image](https://cdn-media-1.freecodecamp.org/images/IRUQRsXWEuhhPwrr7H5IzT3nvvtmxY3axklR)
_Journaux groupés_

Vous pouvez également utiliser `console.groupCollapsed()` au lieu de `console.group()` si vous souhaitez que les groupes soient réduits par défaut. Vous devrez cliquer sur le bouton descriptif à gauche pour développer.

#### console.warn() & console.error()

Selon la situation, pour vous assurer que votre console est plus lisible, vous pouvez ajouter des journaux en utilisant `console.warn()` ou `console.error()`. Il y a aussi `console.info()` qui affiche une icône "i" dans certains navigateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/7mhbJuMysLPrDtYAXvN7HDdbDFNTe64ZlK3D)
_journaux d'avertissement et d'erreur_

Cela peut être poussé plus loin en ajoutant un style personnalisé. Vous pouvez utiliser une directive `%c` pour ajouter du style à toute instruction de journalisation. Cela peut être utilisé pour différencier les appels d'API, les événements utilisateur, etc. en gardant une convention. Voici un exemple :

```
console.log('%c Auth ',             'color: white; background-color: #2274A5',             'Page de connexion rendue');console.log('%c GraphQL ',             'color: white; background-color: #95B46A',             'Obtenir les détails de l\'utilisateur');console.log('%c Erreur ',             'color: white; background-color: #D33F49',             'Erreur lors de l\'obtention des détails de l\'utilisateur');
```

Vous pouvez également changer la `font-size`, `font-style` et d'autres choses CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/1O8gEl3YMYTaBA6JAfXI-ZQY0x9LVBasnzKF)
_Stylisation des instructions console.log_

#### console.trace()

`console.trace()` affiche une trace de pile dans la console et montre comment le code est arrivé à un certain point. Il existe certaines méthodes que vous ne souhaitez appeler qu'une seule fois, comme la suppression d'une base de données. `console.trace()` peut être utilisé pour s'assurer que le code se comporte comme nous le voulons.

#### console.time()

Une autre chose importante en matière de développement frontend est que le code doit être rapide. `console.time()` permet de chronométrer certaines opérations dans le code pour les tester.

```
let i = 0;
```

```
console.time("Boucle While");while (i < 1000000) {  i++;}console.timeEnd("Boucle While");
```

```
console.time("Boucle For");for (i = 0; i < 1000000; i++) {  // Boucle For}console.timeEnd("Boucle For");
```

![Image](https://cdn-media-1.freecodecamp.org/images/x1xRANcn-DekwoMEL6tYgWmdZcNp7JKMNxOp)
_Sortie de console.time() pour les boucles_

Espérons que cet article a fourni des informations sur diverses façons d'utiliser la console. Si vous avez des questions ou si vous souhaitez que je développe davantage, laissez-moi un message ci-dessous ou contactez-moi sur [twitter](http://twitter.com/yagrawl) ou par [email](mailto:yagrawl2@gmail.com).