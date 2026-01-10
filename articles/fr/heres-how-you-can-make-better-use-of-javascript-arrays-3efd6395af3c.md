---
title: Voici comment mieux utiliser les tableaux JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T15:35:51.000Z'
originalURL: https://freecodecamp.org/news/heres-how-you-can-make-better-use-of-javascript-arrays-3efd6395af3c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IZcJKz3761vChU1VFHfzkw.jpeg
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: tips
  slug: tips
seo_title: Voici comment mieux utiliser les tableaux JavaScript
seo_desc: 'By pacdiv

  Quick read, I promise. Over the last few months, I noticed that the exact same four
  mistakes kept coming back through the pull requests I checked. I’m also posting
  this article because I’ve made all these mistakes myself! Let’s browse them ...'
---

Par pacdiv

Lecture rapide, je promets. Au cours des derniers mois, j'ai remarqué que les mêmes quatre erreurs revenaient sans cesse dans les pull requests que j'ai vérifiées. Je publie également cet article parce que j'ai commis toutes ces erreurs moi-même ! Parcourons-les pour nous assurer d'utiliser correctement les méthodes de tableau !

### Remplacer Array.indexOf par Array.includes

« Si vous cherchez quelque chose dans votre tableau, utilisez Array.indexOf. » Je me souviens avoir lu une phrase comme celle-ci dans mon cours lorsque j'apprenais JavaScript. La phrase est tout à fait vraie, sans aucun doute !

Array.indexOf « retourne le premier index auquel un élément donné peut être trouvé », dit la documentation MDN. Donc, si nous utilisons l'index retourné plus tard dans notre code, et Array.indexOf est la solution.

Mais, que faire si nous devons seulement savoir si notre tableau contient une valeur ou non ? Cela semble être une question oui/non, une question booléenne, je dirais. Pour ce cas, je recommande d'utiliser Array.includes qui retourne un booléen.

### Utiliser Array.find au lieu de Array.filter

Array.filter est une méthode très utile. Elle crée un nouveau tableau à partir d'un autre avec tous les éléments passant l'argument de rappel. Comme indiqué par son nom, nous devons utiliser cette méthode pour filtrer et obtenir un tableau plus court.

Mais, si nous savons que notre fonction de rappel ne peut retourner qu'un seul élément, je ne la recommanderais pas — par exemple, lors de l'utilisation d'un argument de rappel filtrant par un ID unique. Dans ce cas, Array.filter retournerait un nouveau tableau contenant un seul élément. En cherchant un ID spécifique, notre intention peut être d'utiliser la seule valeur contenue dans le tableau, rendant ce tableau inutile.

Parlons de la performance. Pour retourner tous les éléments correspondant à la fonction de rappel, Array.filter doit parcourir tout le tableau. De plus, imaginons que nous avons des centaines d'éléments satisfaisant notre argument de rappel. Notre tableau filtré serait assez grand.

Pour éviter ces situations, je recommande Array.find. Il nécessite un argument de rappel comme Array.filter, et il retourne la valeur du premier élément satisfaisant ce rappel. De plus, Array.find s'arrête dès qu'un élément satisfait le rappel. Il n'est pas nécessaire de parcourir tout le tableau. De plus, en utilisant Array.find pour trouver un élément, nous donnons une idée plus claire de notre intention.

### Remplacer Array.find par Array.some

J'admets avoir fait cette erreur de nombreuses fois. Ensuite, un ami bienveillant m'a conseillé de vérifier la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Methods_2) pour une meilleure méthode. Voici le point : cela est très similaire à notre cas Array.indexOf/Array.includes ci-dessus.

Dans le cas précédent, nous avons vu que Array.find nécessite un rappel comme argument et retourne un élément. Array.find est-il la meilleure solution si nous devons savoir si notre tableau contient une valeur ou non ? Probablement pas, car il retourne une valeur, pas un booléen.

Pour ce cas, je recommande d'utiliser Array.some qui retourne le booléen nécessaire. De plus, sémantiquement, utiliser Array.some souligne le fait que nous n'avons pas besoin de l'élément trouvé.

### Utiliser Array.reduce au lieu d'enchaîner Array.filter et Array.map

Admettons-le, Array.reduce n'est pas simple à comprendre. C'est vrai ! Mais, si nous exécutons Array.filter, puis Array.map, on a l'impression qu'il nous manque quelque chose, n'est-ce pas ?

Je veux dire, nous parcourons le tableau deux fois ici. La première fois pour filtrer et créer un tableau plus court, la deuxième fois pour créer un nouveau tableau (encore !) contenant de nouvelles valeurs basées sur celles que nous avons obtenues de Array.filter. Pour obtenir notre nouveau tableau, nous avons utilisé deux méthodes de tableau. Chaque méthode a sa propre fonction de rappel et un tableau que nous ne pouvons pas utiliser plus tard — celui créé par Array.filter.

Pour éviter de faibles performances sur ce sujet, mon conseil est d'utiliser Array.reduce à la place. Même résultat, meilleur code ! Array.reduce nous permet de filtrer et d'ajouter les éléments satisfaisants dans un accumulateur. Par exemple, cet accumulateur peut être un nombre à incrémenter, un objet à remplir, une chaîne ou un tableau à concaténer.

Dans notre cas, puisque nous avons utilisé Array.map, je recommande d'utiliser Array.reduce avec un tableau à concaténer comme accumulateur. Dans l'exemple suivant, selon la valeur de _env_, nous l'ajouterons à notre accumulateur ou laisserons cet accumulateur tel quel.

#### C'est tout !

J'espère que cela aide. N'hésitez pas à laisser des commentaires si vous avez des réflexions sur cet article ou si vous avez d'autres cas d'utilisation à montrer. Et si vous l'avez trouvé utile, donnez-moi quelques applaudissements ? et partagez-le. Merci pour la lecture !

PS : Vous pouvez [me suivre sur Twitter ici](https://twitter.com/pacdiv_io).

_Note :_ Comme mentionné par [malgosiastp](https://www.freecodecamp.org/news/heres-how-you-can-make-better-use-of-javascript-arrays-3efd6395af3c/undefined) et [David Piepgrass](https://www.freecodecamp.org/news/heres-how-you-can-make-better-use-of-javascript-arrays-3efd6395af3c/undefined) dans les commentaires, veuillez vérifier la compatibilité avant d'utiliser Array.find et Array.includes, qui ne sont actuellement pas supportés par Internet Explorer.