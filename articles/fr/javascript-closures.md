---
title: Pourquoi vous devriez connaître les fermetures JavaScript
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-06-09T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-closures
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Why-JS-Closures-Matter.png
tags:
- name: Closure with example
  slug: closure-with-example
- name: beginner
  slug: beginner
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
seo_title: Pourquoi vous devriez connaître les fermetures JavaScript
seo_desc: "Fully understanding closures may seem like a right of passage to becoming\
  \ a JavaScript developer. \nThere is a reason why it can be difficult to make sense\
  \ of closures—because they are often taught backwards. You may have been taught\
  \ what a closures i..."
---

Comprendre pleinement les fermetures peut sembler être un rite de passage pour devenir un développeur JavaScript. 

Il y a une raison pour laquelle il peut être difficile de comprendre les fermetures—parce qu'elles sont souvent enseignées _à l'envers_. On vous a peut-être appris ce qu'est une fermeture, mais vous ne comprenez peut-être pas comment elles sont utiles pour le développeur moyen ou dans votre propre code.

**Alors pourquoi les fermetures comptent-elles dans notre code JavaScript quotidien ?**

Au lieu de voir les fermetures comme un sujet à mémoriser pour un quelconque quiz surprise, voyons quelles séries d'étapes peuvent nous mener à voir une fermeture en premier lieu. Une fois que nous verrons ce qu'elles sont, nous découvrirons pourquoi les fermetures valent la peine d'être connues et utilisées dans votre code JavaScript.

## Voir une fermeture en action ✨

Supposons que nous créons une application clone du site de blogging Medium, et que nous voulons que chaque utilisateur puisse aimer différents posts.

Chaque fois qu'un utilisateur clique sur le bouton d'appréciation, sa valeur sera incrémentée de un à chaque fois.

Pensez à cela comme le bouton d'applaudissements de Medium :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/react-clap-demo.gif)

La fonction qui gérera l'augmentation du compteur de 1 à chaque fois s'appelle `handleLikePost` et nous suivons le nombre de likes avec une variable nommée `likeCount` :

```js
// portée globale
let likeCount = 0;

function handleLikePost() {
  // portée de la fonction
  likeCount = likeCount + 1;
}

handleLikePost();
console.log("nombre de likes :", likeCount); // nombre de likes : 1

```

Chaque fois qu'un utilisateur aime un post, nous appelons `handleLikePost` et il incrémente notre `likeCount` de 1.

Et cela fonctionne parce que nous savons que les fonctions peuvent accéder aux variables en dehors d'elles-mêmes.

En d'autres termes, **les fonctions peuvent accéder à n'importe quelle variable définie dans n'importe quelle portée parente**.

Il y a cependant un problème avec ce code. Puisque `likeCount` est dans la portée globale, et non dans une fonction, `likeCount` est une variable globale. Les variables globales peuvent être utilisées (et modifiées) par n'importe quel autre morceau de code ou fonction dans notre application.

Par exemple, que se passerait-il si, après notre fonction, nous définissions par erreur notre `likeCount` à 0 ?

```js
let likeCount = 0;

function handleLikePost() {
  likeCount = likeCount + 1;
}

handleLikePost();
likeCount = 0;
console.log("nombre de likes :", likeCount); // nombre de likes : 0

```

Naturellement, `likeCount` ne peut jamais être incrémenté à partir de 0.

Lorsque seule une fonction a besoin d'une donnée donnée, elle doit simplement exister localement, c'est-à-dire, dans cette fonction.

Maintenant, déplaçons `likeCount` dans notre fonction :

```jsx
function handleLikePost() {
  // likeCount déplacé de la portée globale à la portée de la fonction
  let likeCount = 0;
  likeCount = likeCount + 1;
}

```

Notez qu'il y a une manière plus courte d'écrire la ligne où nous incrémentons `likeCount`. Au lieu de dire que `likeCount` est égal à la valeur précédente de `likeCount` et d'ajouter un comme ceci, nous pouvons simplement utiliser l'opérateur += comme suit :

```jsx
function handleLikePost() {
  let likeCount = 0;
  likeCount += 1;
}

```

Et pour que cela fonctionne comme avant et obtenir la valeur du compteur de likes, nous devons également déplacer notre `console.log` dans la fonction.

```jsx
function handleLikePost() {
  let likeCount = 0;
  likeCount += 1;
  console.log("nombre de likes :", likeCount);
}

handleLikePost(); // nombre de likes : 1

```

Et cela fonctionne toujours correctement comme avant.

Donc maintenant, les utilisateurs devraient pouvoir aimer un post autant de fois qu'ils le souhaitent, alors appelons `handleLikePost` quelques fois de plus :

```jsx
handleLikePost(); // nombre de likes : 1
handleLikePost(); // nombre de likes : 1
handleLikePost(); // nombre de likes : 1

```

Cependant, lorsque nous exécutons ce code, il y a un problème.

Nous nous attendrions à voir le `likeCount` continuer à augmenter, mais nous voyons simplement 1 à chaque fois. Pourquoi cela ?

Prenez un moment, regardez notre code et essayez d'expliquer pourquoi notre `likeCount` n'est plus incrémenté.

Regardons notre fonction `handleLikePost` et comment elle fonctionne :

```js
function handleLikePost() {
  let likeCount = 0;
  likeCount += 1;
  console.log("nombre de likes :", likeCount);
}

```

Chaque fois que nous l'utilisons, nous recréons cette variable `likeCount`, à laquelle est donnée une valeur initiale de 0.

Pas étonnant que nous ne puissions pas suivre le compteur entre les appels de fonction ! Il continue à être défini à 0 à chaque fois, puis il est incrémenté de 1, après quoi la fonction a fini de s'exécuter.

Nous sommes donc coincés ici. Notre variable doit vivre à l'intérieur de la fonction `handleLikePost`, mais nous ne pouvons pas préserver le compteur.

Nous avons besoin de quelque chose qui nous permette de préserver ou de nous souvenir de la valeur `likeCount` entre les appels de fonction.

Et si nous essayions quelque chose qui peut sembler un peu étrange au premier abord—et si nous essayions de mettre une autre fonction dans notre fonction :

```js
function handleLikePost() {
  let likeCount = 0;
  likeCount += 1;
  function() {

  }
}

handleLikePost();

```

Ici, nous allons nommer cette fonction `addLike`. Pourquoi ? Parce qu'elle sera responsable de l'incrémentation de la variable `likeCount` maintenant.

Et notez que cette fonction interne n'a pas besoin d'avoir un nom. Elle peut être une fonction anonyme. Dans la plupart des cas, c'est le cas. Nous lui donnons simplement un nom pour pouvoir en parler plus facilement et expliquer ce qu'elle fait.

`addLike` sera maintenant responsable de l'augmentation de notre `likeCount`, donc nous déplacerons la ligne où nous incrémentons de 1 dans notre fonction interne.

```js
function handleLikePost() {
  let likeCount = 0;
  function addLike() {
    likeCount += 1;
  }
}

```

Et si nous appelions cette fonction `addLike` dans `handleLikePost` ?

Tout ce qui se passerait, c'est que `addLike` incrémenterait notre `likeCount`, mais la variable `likeCount` serait toujours détruite. Donc encore une fois, nous perdons notre valeur et le résultat est 0.

Mais au lieu d'appeler `addLike` dans sa fonction englobante, que se passerait-il si nous l'appelions à l'extérieur de la fonction ? Cela semble encore plus étrange. Et comment ferions-nous cela ?

Nous savons à ce stade que les fonctions retournent des valeurs. Par exemple, nous pourrions retourner notre valeur `likeCount` à la fin de `handleLikePost` pour la passer à d'autres parties de notre programme :

```js
function handleLikePost() {
  let likeCount = 0;
  function addLike() {
    likeCount += 1;
  }
  addLike();
  return likeCount;
}

```

Mais au lieu de faire cela, retournons `likeCount` dans `addLike` puis retournons la fonction `addLike` elle-même :

```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
  // addLike();
}

handleLikePost();

```

Cela peut sembler bizarre, mais c'est autorisé en JS. Nous pouvons utiliser des fonctions comme n'importe quelle autre valeur en JS. Cela signifie qu'une fonction peut être retournée par une autre fonction. En retournant la fonction interne, nous pouvons l'appeler depuis l'extérieur de sa fonction englobante.

Mais comment ferions-nous cela ? Prenez un moment pour réfléchir et voir si vous pouvez le comprendre...

Tout d'abord, pour mieux voir ce qui se passe, affichons `handleLikePost` lorsque nous l'appelons et voyons ce que nous obtenons :

```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
}

console.log(handleLikePost()); // ƒ addLike()

```

Sans surprise, nous obtenons la fonction `addLike` affichée. Pourquoi ? Parce que nous la retournons, après tout.

Pour l'appeler, ne pourrions-nous pas simplement la mettre dans une autre variable ? Comme nous venons de le dire, les fonctions peuvent être utilisées comme n'importe quelle autre valeur en JS. Si nous pouvons la retourner depuis une fonction, nous pouvons aussi la mettre dans une variable. Alors mettons-la dans une nouvelle variable appelée `like` :

```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
}

const like = handleLikePost();

```

Et enfin, appelons `like`. Nous le ferons quelques fois et afficherons chaque résultat :

```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
}

const like = handleLikePost();

console.log(like()); // 1
console.log(like()); // 2
console.log(like()); // 3

```

Notre `likeCount` est enfin préservé ! Chaque fois que nous appelons `like`, le `likeCount` est incrémenté à partir de sa valeur précédente.

Alors, que s'est-il passé ici ? Eh bien, nous avons découvert comment appeler la fonction `addLike` depuis l'extérieur de la portée dans laquelle elle a été déclarée. Nous l'avons fait en retournant la fonction interne depuis la fonction externe et en stockant une référence à celle-ci, nommée `like`, pour l'appeler.

## Comment fonctionne une fermeture, ligne par ligne 🔍

C'était notre implémentation, bien sûr, mais comment avons-nous préservé la valeur de `likeCount` entre les appels de fonction ?

```js
function handleLikePost() {
  let likeCount = 0;
  return function addLike() {
    likeCount += 1;
    return likeCount;
  };
}

const like = handleLikePost();

console.log(like()); // 1

```

1. La fonction externe `handleLikePost` est exécutée, créant une instance de la fonction interne `addLike` ; cette fonction _ferme_ sur la variable `likeCount`, qui est une portée au-dessus.
2. Nous avons appelé la fonction `addLike` depuis l'extérieur de la portée dans laquelle elle a été déclarée. Nous l'avons fait en retournant la fonction interne depuis la fonction externe et en stockant une référence à celle-ci, nommée `like`, pour l'appeler.
3. Lorsque la fonction `like` finit de s'exécuter, normalement nous nous attendrions à ce que toutes ses variables soient garbage collectées (supprimées de la mémoire, ce qui est un processus automatique que le compilateur JS fait). Nous nous attendrions à ce que chaque `likeCount` disparaisse lorsque la fonction est terminée, mais ce n'est pas le cas.

Quelle est cette raison ? _Fermeture_.

**Puisque les instances de la fonction interne sont toujours vivantes (assignées à `like`), la fermeture préserve toujours les variables `countLike`.**

Vous pourriez penser qu'avoir une fonction écrite dans une autre fonction serait comme une fonction écrite dans la portée globale. Mais ce n'est pas le cas.

_C'est pourquoi la fermeture rend les fonctions si puissantes_, car c'est une propriété spéciale qui n'est présente dans rien d'autre dans le langage.

## La durée de vie d'une variable

Pour mieux apprécier les fermetures, nous devons comprendre comment JavaScript traite les variables qui sont créées. Vous vous êtes peut-être demandé ce qui arrive aux variables lorsque vous fermez votre page ou allez à une autre page dans une application. Combien de temps les variables vivent-elles ?

Les variables globales vivent jusqu'à ce que le programme soit abandonné, par exemple lorsque vous fermez la fenêtre. Elles sont présentes pendant toute la durée de vie du programme.

Cependant, les variables locales ont une courte durée de vie. Elles sont créées lorsque la fonction est appelée, et supprimées lorsque la fonction est terminée.

Donc auparavant, où `likeCount` était simplement une variable locale, lorsque la fonction était exécutée. La variable likeCount était créée au début de la fonction et ensuite détruite une fois l'exécution terminée.

## Les fermetures ne sont pas des instantanés - elles gardent les variables locales vivantes

Il est parfois affirmé que les fermetures JavaScript sont similaires à des instantanés, une image de notre programme à un certain moment. C'est une idée fausse que nous pouvons dissiper en ajoutant une autre fonctionnalité à notre bouton de like.

Supposons que dans certaines occasions rares, nous voulons permettre aux utilisateurs de "double liker" un post et d'incrémenter le `likeCount` de 2 à la fois au lieu de 1.

Comment ajouterions-nous cette fonctionnalité ?

Une autre façon de passer des valeurs à une fonction est bien sûr par le biais d'arguments, qui fonctionnent comme des variables locales.

Passons un argument appelé step à la fonction, qui nous permettra de fournir une valeur dynamique et modifiable pour incrémenter notre compteur au lieu de la valeur codée en dur 1.

```js
function handleLikePost(step) {
  let likeCount = 0;
  return function addLike() {
    likeCount += step;
    // likeCount += 1;
    return likeCount;
  };
}

```

Ensuite, essayons de créer une fonction spéciale qui nous permettra de double liker nos posts, doubleLike. Nous passerons 2 comme valeur de `step` pour la créer, puis nous essaierons d'appeler nos deux fonctions, `like` et `doubleLike` :

```js
function handleLikePost(step) {
  let likeCount = 0;
  return function addLike() {
    likeCount += step;
    return likeCount;
  };
}

const like = handleLikePost(1);
const doubleLike = handleLikePost(2);

like(); // 1
like(); // 2

doubleLike(); // 2 (le compteur est toujours préservé !)
doubleLike(); // 4

```

Nous voyons que le `likeCount` est également préservé pour `doubleLike`.

Que se passe-t-il ici ?

Chaque instance de la fonction interne `addLike` ferme sur les variables `likeCount` et `step` de la portée de sa fonction externe `handleLikePost`. `step` reste le même au fil du temps, mais le compteur est mis à jour à chaque appel de cette fonction interne. Puisque la fermeture concerne les variables et pas seulement des instantanés des valeurs, ces mises à jour sont préservées entre les appels de fonction.

Alors, que nous montre ce code—le fait que nous pouvons passer des valeurs dynamiques pour changer le résultat de notre fonction ? Qu'elles sont toujours vivantes ! Les fermetures gardent les variables locales vivantes à partir de fonctions qui auraient dû les détruire il y a longtemps.

En d'autres termes, elles ne sont pas statiques et immuables, comme un instantané de la valeur des variables fermées à un moment donné—les fermetures préservent les variables et fournissent un lien actif vers elles. En conséquence, nous pouvons utiliser les fermetures pour observer ou faire des mises à jour de ces variables au fil du temps.

## Qu'est-ce qu'une fermeture, exactement ?

Maintenant que vous voyez comment une fermeture est utile, il y a deux critères pour qu'une chose soit une fermeture, tous deux que vous avez vus ici :

1. Les fermetures sont une propriété des fonctions JavaScript, et seulement des fonctions. Aucun autre type de données ne les possède.
2. Pour observer une fermeture, vous devez exécuter une fonction dans une portée différente de celle où cette fonction a été initialement définie.

## Pourquoi devriez-vous connaître les fermetures ?

Répondons à la question initiale que nous nous sommes posée. Sur la base de ce que nous avons vu, faites une pause et essayez de répondre à cette question. Pourquoi devrions-nous nous soucier des fermetures en tant que développeurs JS ?

Les fermetures comptent pour vous et votre code parce qu'elles vous permettent de "vous souvenir" des valeurs, ce qui est une fonctionnalité très puissante et unique dans le langage que seules les fonctions possèdent.

Nous l'avons vu ici même dans cet exemple. Après tout, à quoi sert une variable de compteur de likes qui ne se souvient pas des likes ? Vous rencontrerez souvent cela dans votre carrière JS. Vous devez conserver une valeur d'une manière ou d'une autre et probablement la garder séparée des autres valeurs. Que utilisez-vous ? Une fonction. Pourquoi ? Pour suivre les données au fil du temps avec une fermeture.

Et avec cela, vous êtes déjà un pas en avance sur les autres développeurs.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*