---
title: React Hooks pour débutants – Apprenez à utiliser le hook useState en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-30T19:40:11.000Z'
originalURL: https://freecodecamp.org/news/learn-react-usestate-hook-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/philipp-katzenberger-jVx8JaO2Ddc-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: React Hooks pour débutants – Apprenez à utiliser le hook useState en 10
  minutes
seo_desc: 'By Eduardo Vedes

  Hey everyone 🌈 I haven''t written about handling state in React for a long time.
  The last time was in this article, four years ago, and it seems like it helped a
  lot of you.

  I received tons of views and amazing feedback, so thanks a ...'
---

Par Eduardo Vedes

Salut à tous 🌈 Je n'ai pas écrit sur la gestion de l'état dans React depuis longtemps. La dernière fois, c'était [dans cet article](https://www.freecodecamp.org/news/get-pro-with-react-setstate-in-10-minutes-d38251d1c781/), il y a quatre ans, et il semble que cela ait aidé beaucoup d'entre vous.

J'ai reçu des tonnes de vues et des retours incroyables, alors merci beaucoup – vous êtes vraiment géniaux ! 🎸

Bon, beaucoup de temps a passé depuis. Les Hooks sont arrivés dans React depuis la version v16.8 (en 2019) et il y a beaucoup de choses à suivre lors de l'utilisation de l'état dans React.

Apprenez-vous à gérer l'état et souhaitez-vous devenir un pro avec le hook **useState** ?

Super, vous êtes au bon endroit ! Prenez un café (ou un thé), attachez vos ceintures, et c'est parti !

Au fait – si vous cherchez comment utiliser setState (dans les composants de classe), alors je vous recommande de consulter mon ancien article ["Comment devenir un pro avec React setState() en 10 minutes"](https://www.freecodecamp.org/news/get-pro-with-react-setstate-in-10-minutes-d38251d1c781/).

## Qu'est-ce qu'un Hook React ?

Un hook est une fonction spéciale qui vous permet de **"vous connecter à"** diverses fonctionnalités de React. Imaginez une fonction qui retourne un tableau avec deux valeurs :

* **La première valeur** : une variable avec l'état.
* **La deuxième valeur** : une variable avec un gestionnaire (une fonction pour changer l'état actuel).

C'est tout, facile comme bonjour. 🤗

Rappelez-vous qu'en JavaScript **"les valeurs sont des fonctions, et les fonctions sont des valeurs"**. J'ai appris cela en 2017 avec [**MPJ**](https://www.youtube.com/c/funfunfunction), l'un de mes développeurs et YouTubers préférés. Merci pour tout MPJ !

Au cas où cela vous aurait un peu confus, voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/01.png)
*les valeurs sont des fonctions, et les fonctions sont des valeurs*

Voyons ce qui se passe ici :

* Dans **a**, vous stockez un nombre. Je veux dire, vous attribuez la valeur **1** (qui est un nombre) à une variable appelée **a**.
* Dans **b**, vous stockez le résultat (valeur) de l'évaluation d'une expression.
* Dans **c**, vous stockez une fonction. Vous stockez une fonction non exécutée, qui est stockée comme une valeur, et prête à être exécutée à tout moment.
* Dans **d**, nous attribuons le résultat de l'évaluation de **c**.

Cela a du sens ? Avez-vous compris l'idée ? Oui, **les fonctions sont des valeurs, et les valeurs sont des fonctions** ! C'est tout ce que vous devez savoir pour l'instant.

**useState**, en particulier, vous permet d'ajouter un état React aux composants fonctionnels (composants déclarés comme une fonction, et non comme une classe).

En vérité, l'état est conservé à l'intérieur du hook, mais est accessible depuis le composant où vous "appelez" le hook.

## Les règles des Hooks React

En plus du fait que les Hooks sont des fonctions JavaScript, il y a quelques règles à suivre lors de leur utilisation :

### N'appeler les Hooks qu'au niveau supérieur

Ne pas appeler les hooks à l'intérieur de boucles, de conditions ou de fonctions imbriquées. Utilisez toujours les hooks au niveau supérieur de votre fonction React (composant), avant tout retour anticipé.

La raison derrière cela est que les hooks doivent être appelés dans le même ordre chaque fois qu'un composant est rendu. C'est ce qui permet à React de préserver correctement l'état des hooks entre plusieurs appels de useState et useEffect.

#### N'appeler les Hooks que depuis les fonctions React

Cela signifie que vous pouvez appeler les hooks depuis des fonctions React (composants) ou depuis des hooks personnalisés, mais pas depuis des fonctions JavaScript régulières.

Il existe ce plugin utile [ici](https://www.npmjs.com/package/eslint-plugin-react-hooks) qui fait respecter les règles des hooks. C'est un plugin très utile, alors assurez-vous de l'essayer.

## L'anatomie du hook useState

Pour utiliser le hook useState, vous devez savoir quelques choses.

💡 Vous pouvez consulter la figure ci-dessous pour mieux comprendre ce que je vais expliquer ici.

1. Vous devez l'importer depuis la bibliothèque React.
2. Vous devez l'invoquer à l'intérieur d'un composant React

```javascript
const [state, setState] = useState(initialValue)
```

Je ne suis pas sûr que vous compreniez la destructuration, alors pour ceux qui ne l'ont pas saisie du premier coup :

Je pourrais faire quelque chose comme ceci :

```javascript
const array = useState(initialValue)
```

Et ensuite, je pourrais utiliser l'état, à l'intérieur de la position 0, comme array[0], et le gestionnaire pour setState, à l'intérieur de la position 1, comme array[1].

Il se trouve que c'est beaucoup plus déclaratif de destructurer le tableau, car nous connaissons ses valeurs de première et deuxième position, et nous savons qu'elles correspondent à la valeur de l'état et à un gestionnaire pour la changer.

```javascript
const [first, second] = useState(initialValue)
```

Oui, nous pourrions faire cela. Mais nous pouvons appeler n'importe quoi à first et second. La seule règle est que ces variables correspondent aux première et deuxième positions du tableau retourné par la fonction **useState** (hook).

```javascript
const [state, setState] = useState(initialValue)
const [counter, setCounter] = useState(initialCount)
const [something, setSomething] = useState(initialSomething)
```

Si vous n'êtes pas familier avec la syntaxe de l'affectation par destructuration, n'hésitez pas à faire une pause dans la lecture et à jeter un coup d'œil à [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) ou [lire ce tutoriel utile](https://www.freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects/).

Allez-y – Je vais attendre ! (*Edo sirote un peu de* ☕)

3. Vous pouvez ensuite librement rendre l'état, ou appeler setState pour mettre à jour votre valeur d'état.

Et voici l'exemple le plus simple et entièrement fonctionnel que vous pouvez avoir :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/carbon.png)
*L'anatomie du hook useState*

## Quand utiliser le hook useState

Pour comprendre quand utiliser ce hook, nous devons commencer par apprendre quand nous avons besoin d'un état.

À première vue, nous pensons que lorsque nous avons besoin d'une variable qui change au fil du temps, nous devons la conserver dans l'état. Mais ce n'est pas vrai, la plupart du temps. Je veux dire, si votre variable peut être dérivée d'autres données, alors vous n'avez pas besoin d'état.

### Exemple d'état 1 :

Une couleur de thème, qui peut être claire ou foncée, selon l'heure, peut être dérivée des données du système.

Nous pouvons simplement obtenir l'heure (date) à partir de la fonction Date de JS. Donc nous n'avons pas besoin d'état ici, n'est-ce pas ? C'est une constante que vous pouvez déclarer avec une expression ou une fonction qui doit être évaluée.

### Exemple d'état 2 :

Un basculement de modal (pour afficher/masquer une modal).

Le basculement de modal peut être vrai ou faux, et il est déclenché lorsque l'utilisateur clique sur un bouton. Donc, dans ce cas, nous avons vraiment besoin d'état, car nous ne pouvons pas dériver ce type d'information – il ne dépend que de "quand et si" l'utilisateur déclenche l'événement ou non.

Soyez conscient de cette différence – entre ce qui peut être dérivé et ce qui dépend de l'utilisateur.

Vous voudrez utiliser le hook **useState** lorsque vous devez stocker une entrée d'un utilisateur.

💡 En règle générale, vous ne devriez utiliser l'état que pour conserver ce type d'information – qui nécessite que l'utilisateur saisisse des données ou déclenche des événements.

Un autre exemple très utilisé est les données de **formulaire**. Presque toutes les applications ou sites web doivent collecter des informations auprès de l'utilisateur. Et pour cela, il est assez courant (ou obligatoire) d'avoir un formulaire.

Les données de formulaire doivent être stockées dans l'état, au moins jusqu'à ce qu'elles soient persistées dans une base de données. Mais elles peuvent également être récupérées depuis une base de données et rendues modifiables à nouveau.

Cool, continuons.

## Comment utiliser plusieurs variables d'état dans React

Donc, si nous devons gérer plusieurs états, la meilleure approche recommandée est de les gérer séparément, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/carbon--1-.png)
*Compteur de chiens et chats (Gestion de plusieurs variables d'état)*

Il n'y a rien de mal à faire cela, malgré le fait que cela semble être primitif. C'est une bonne approche linéaire car nous continuons à travailler avec des primitives JavaScript (dans ce cas, des nombres).

Vous pouvez également mélanger l'état dans un objet :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/carbon--2-.png)

Ce cas devient un peu plus complexe. Nous avons initialisé un objet, au lieu d'une valeur primitive. Lorsque nous appelons setPets, nous devons être conscients que nous devons étendre l'objet pets existant, puis ajouter le changement, sinon nous le perdrons.

Avec l'ancienne API setState, cela n'était pas obligatoire – elle comprendrait que vous vouliez mettre à jour une clé de l'objet d'état. Mais de nos jours, ce n'est plus le cas, et j'aime cela. Maintenant, c'est plus déclaratif et plus un concept fondamental en JavaScript.

Si par hasard vous n'êtes pas familier avec la syntaxe de l'opérateur de propagation, n'hésitez pas à la consulter [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) ou [lire ce tutoriel utile](https://www.freecodecamp.org/news/javascript-object-destructuring-spread-operator-rest-parameter/).

## Asynchronicité de l'état

Attention, changer/muter l'état est une opération asynchrone.

Voyons une preuve :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/carbon--3-.png)
*L'état est asynchrone (il est groupé et mis à jour avec un délai)*

Donc, j'ai un peu mis à jour notre exemple initial de chiens. Cette fois, j'ai créé une fonction **handleDogsCount** pour vous la montrer.

À l'intérieur de handleDogsCount, j'appelle **setDogs** avec la nouvelle valeur.

Que se passe-t-il si j'ai besoin d'utiliser la valeur de l'état immédiatement pour une autre opération ?

Exact, l'état n'a pas encore été mis à jour. La meilleure façon d'aborder une opération immédiate est d'utiliser la valeur passée à la fonction handleDogsCount, et – en oubliant la valeur de l'état des chiens pour l'instant – en sachant à l'avance (c'est délicat, mais c'est ce que c'est) que la valeur n'a pas été mise à jour à temps.

## Comment muter l'état de manière fonctionnelle

D'accord, maintenant nous savons que l'état ne change pas immédiatement. Et il y a une autre question liée à cela. Que se passerait-il si vous pouviez cliquer sur le bouton Plus 1 million de fois par seconde ?

Possiblement, à la fin des 1 million de clics, le compteur serait de 999 998 (ou moins), et non de 1 000 000 comme prévu.

Pour éviter que cela ne se produise, nous pouvons définir l'état de manière fonctionnelle. Nous récupérerions la valeur de l'état précédent, afin que React puisse correctement regrouper toutes les requêtes et mettre à jour l'état de manière linéaire. De cette façon, nous ne perdrions pas d'informations en cours de route.

Pour cela, vous pourriez simplement faire ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/carbon--4-.png)
*Mutation de l'état de manière fonctionnelle*

D'accord, cool. Maintenant, nous sommes sûrs que React ne manquera rien en traitant nos 1 million de requêtes pour muter l'état.

Au lieu de récupérer la variable dogs pour ajouter ou soustraire un, nous nous appuyons sur le previousState qui est exposé à l'intérieur du gestionnaire setState de useState (dans ce cas, la fonction setDogs).

Attention, les objets et les tableaux sont comparés par référence, donc l'état complexe doit être correctement géré dans les tableaux de dépendances d'autres hooks, tels que **useEffect**. Nous en parlerons plus tard, dans un autre article !

Si vous êtes nouveau en JavaScript, laissez-moi vous donner un spoiler sur ce dont je parle :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/carbon--5-.png)
*Comparaison par référence*

Comme vous le voyez, **c** n'est pas strictement égal à **d**. Oui, allez-y et essayez ! Il se trouve que JavaScript compare les objets complexes (tout ce qui n'est pas [primitif](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)) par référence, et non par valeur.

Si je le transforme en chaîne, cela signifie que je compare des chaînes. Et parce qu'elles sont primitives, elles sont strictement égales (comparées par valeur).

## Comment initialiser l'état en tant que fonction

Si vous devez initialiser l'état avec un calcul coûteux, il est préférable de l'initialiser avec une fonction, et non une valeur.

```javascript
const [ dogs, setDogs] = useState(() => expensiveComputation())
```

Cela signifie que nous initialisons la variable de manière paresseuse. La valeur initiale sera attribuée uniquement lors du rendu initial (à nouveau, si c'est une fonction).

Lors des rendus ultérieurs (en raison d'un changement d'état dans le composant ou un composant parent), l'argument du hook useState sera ignoré et la valeur actuelle sera récupérée.

## Conclusion

Donc, il semble que nous soyons arrivés à la fin de ce voyage.

Vous avez appris ce qu'est un hook, les règles des hooks, comment useState fonctionne, son anatomie, et comment vous pouvez gérer plusieurs états.

Vous avez également appris quelques pièges (comme la gestion des objets d'état, ou que l'état est asynchrone), et quelques astuces pour améliorer les performances, comme l'initialisation de l'état en tant que fonction pour éviter d'évaluer constamment ce calcul.

J'espère que vous avez apprécié cet article sur le hook **useState**, ou simplement le "hook d'état".

## Dernier point mais non des moindres

Je suis [Edo](https://eduardovedes.com/). Je suis un défenseur de freeCodeCamp qui aime aider les gens à changer de carrière pour devenir ingénieur logiciel.

Si vous changez de carrière, ou pensez à faire un changement de carrière, cela pourrait vous inspirer de lire un peu de [mon histoire](https://www.freecodecamp.org/news/from-civil-engineer-to-web-developer-with-freecodecamp/), qui a été publiée ici sur la publication freeCodeCamp.

Vous pourriez également être intéressé par ["Comment devenir ingénieur logiciel junior en 6 mois"](https://www.freecodecamp.org/news/how-to-become-a-junior-software-engineer-in-6-months/).

Si vous avez aimé cet article, suivez-moi sur [Twitter](https://twitter.com/eduardovedes) et contactez-moi pour que nous puissions discuter !

Merci à tous 🌈, vous êtes géniaux !

Edo

### Pour en savoir plus sur les Hooks React...

1. [Documentation React](https://reactjs.org/docs/hooks-state.html)