---
title: Comment créer un Décorateur de type Python en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-28T22:49:11.000Z'
originalURL: https://freecodecamp.org/news/creating-a-python-like-decorator-in-javascript-dce3415115c8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nIO9zHIGk94uWLQ-XwRd9g.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment créer un Décorateur de type Python en JavaScript
seo_desc: 'By Sam Galizia

  In this article, I want to show you how I created a Python-like decorator function
  in JavaScript and, in the process, show at least one practical use case.

  At the end, I want to demonstrate how I used this to solve a more in-depth prob...'
---

Par Sam Galizia

Dans cet article, je veux vous montrer comment j'ai créé une fonction décorateur de type Python en JavaScript et, dans le processus, montrer au moins un cas d'utilisation pratique.

À la fin, je veux démontrer comment j'ai utilisé cela pour résoudre un problème plus approfondi et peut-être inspirer certains d'entre vous à faire de même !

#### Installation

Commençons par un petit rappel (ou leçon) sur les décorateurs en Python. En Python, il existe des fonctions appelées décorateurs qui suivent cette syntaxe, `@decorator`.

En code, elles seraient suivies d'une autre fonction comme ceci :

L'extrait de code ci-dessus utilise la version de sucre syntaxique de l'utilisation des décorateurs en Python. Pour mieux comprendre ce qui se passe ici, supprimons ce sucre syntaxique.

Dans ce deuxième extrait, nous examinons la définition du décorateur et comment nous décorons une fonction sans le sucre syntaxique.

L'un des points les plus importants à retenir est que le décorateur enveloppe simplement notre fonction originale à l'intérieur d'une fonction wrapper et l'appelle.

En utilisant cette technique d'enveloppement de notre fonction, nous sommes en mesure d'effectuer des tâches avant et après l'exécution de notre fonction. Examinons un cas d'utilisation qui éclairera davantage le fonctionnement de tout cela.

#### Création de notre décorateur

Nous allons créer un décorateur de timing qui nous indiquera combien de temps il faut à une fonction pour s'exécuter.

Dans le décorateur de timing, nous commençons par noter l'heure actuelle et la sauvegarder sous le nom start. Nous exécutons ensuite la fonction originale, et une fois celle-ci terminée, nous marquons l'heure actuelle comme end. Enfin, nous retournons la différence entre les heures de début et de fin, ce qui nous donne essentiellement le temps qu'il a fallu pour exécuter la fonction.

Ce cas d'utilisation simple n'est que la partie émergée de l'iceberg en ce qui concerne les décorateurs. Avant d'approfondir les cas d'utilisation, je veux montrer à quel point il est facile d'obtenir le même résultat en JavaScript.

Ce que vous voyez ci-dessus est le même décorateur de timing que nous avons créé en Python, mais écrit en JavaScript. Je veux souligner quelques-unes des petites différences de syntaxe qui sont différentes de la version Python.

Premièrement, à l'intérieur de notre fonction décorateur, nous utilisons des fonctions anonymes en JavaScript. L'utilisation de la fonction anonyme permet également de la retourner tout en la définissant.

Deuxièmement, nous avons également utilisé une fonction anonyme dans la syntaxe d'expression de fonction à la ligne 10. Nous passons une fonction anonyme comme argument à `timing` plutôt que d'utiliser une fonction nommée.

Ce sont des différences de syntaxe mineures dans le langage et, espérons-le, elles ne vous perturberont pas trop si vous n'êtes pas familier avec elles.

#### Approfondir

Maintenant que nous avons examiné un exemple simple, je veux approfondir un cas plus utile. Dans le processus, nous allons passer en revue le problème que j'ai rencontré lorsque j'ai décidé de poursuivre cette solution.

Il s'agit d'un problème en deux parties, alors examinons la première partie : les appels réseau échoués.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1PHgY3g8dvTa-UtKJ6LUlg.jpeg)
_Page d'erreur 500 Internal Server Error de GitHub_

Lorsque vous travaillez avec des API, vous vous retrouverez incontestablement à gérer des appels réseau qui échouent pour diverses raisons. Ne serait-il pas agréable de pouvoir faire en sorte que ces appels réseau se réessayent eux-mêmes ?

Eh bien, il se trouve que vous pouvez le faire ! Dans l'extrait suivant, nous allons créer un décorateur en JavaScript qui utilisera une bibliothèque npm appelée retry pour faire exactement cela.

*Sur une note secondaire, il est tout à fait possible d'écrire le code de réessai vous-même. J'ai choisi d'utiliser une bibliothèque pour simplifier un peu les choses, car ce n'est pas le sujet principal de cet article.

D'accord, c'était beaucoup à assimiler ! J'ai essayé de commenter des parties pour aider à expliquer ce qui se passe, mais décomposons cela étape par étape.

Tout d'abord, nous nécessitons la bibliothèque retry, que vous pouvez trouver [ici](https://www.npmjs.com/package/retry), et nous procédons à la création de notre fonction décorateur.

À l'intérieur de notre décorateur, la première chose que nous voulons faire est de créer une opération. Les opérations font partie de la bibliothèque retry et indiquent que nous avons quelque chose que nous voulons faire et qui peut nécessiter plus d'une tentative.

Dans la configuration de l'opération, vous pouvez voir que j'ai défini `{retries: 2}`. Les options peuvent être passées dans le constructeur d'opération sous forme d'objet contenant l'option de configuration que vous souhaitez modifier. La définition de `retries` est la manière dont vous pouvez spécifier le nombre maximum de tentatives.

La bibliothèque retry dispose de nombreuses configurations que vous pouvez utiliser pour personnaliser le fonctionnement de vos réessais, mais je ne veux pas m'égarer. Consultez la [bibliothèque npm](https://www.npmjs.com/package/retry) pour en savoir plus !

Ensuite, nous configurons notre fonction anonyme qui enveloppera notre fonction originale. Vous avez peut-être été un peu confus lorsque vous avez regardé la ligne 9, `const args = arguments;`. Je sais que j'étais confus par cela lorsque je l'ai vu pour la première fois, alors laissez-moi expliquer.

En gros, puisque nous appelons `wrapped` plus loin dans la fonction dans une portée inférieure, nous devons récupérer les arguments maintenant afin de pouvoir y accéder plus tard. Le mot-clé `arguments` récupère les arguments de la portée de la fonction actuelle sous forme de tableau. Nous stockons les `arguments` actuels dans `args`, ce qui nous permet de les utiliser plus tard.

La partie suivante est celle où les choses commencent à devenir un peu confuses. J'utilise une bibliothèque de réseau qui retourne des promesses, et à cause de cela, nous devons intercepter la promesse à l'intérieur du décorateur. L'intercepter nous permet de vérifier si elle a réussi ou échoué et ensuite de faire quelque chose à ce sujet.

Ci-dessous se trouve simplement la partie interne de notre fonction d'enveloppement du décorateur.

Afin d'intercepter la réponse de l'appel réseau, nous enveloppons notre opération (qui contient notre fonction que nous voulons réessayer) à l'intérieur d'une autre promesse. Pour ceux d'entre vous qui ont déjà utilisé des promesses, je sais que cela peut sembler étrange, mais c'est nécessaire pour s'assurer que nous gérons le résultat de cet appel ici. Cela sera encore plus évident lorsque je montrerai mon exemple final, alors restez à l'écoute !

En continuant, maintenant que nous avons enveloppé notre fonction originale et la réessai de l'opération à l'intérieur de la promesse, nous pouvons réellement appeler `wrapped`. Lorsque nous l'appelons, nous devons nous assurer d'utiliser `apply(context, args...)` afin que nos paramètres originaux passés puissent être utilisés.

Une fois que nous obtenons une réponse de notre appel réseau, nous gérons les cas de succès et d'erreur. Le cas de succès est assez ennuyeux ici : en gros, si nous obtenons une réponse réussie, nous résolvons la promesse externe avec le résultat.

Le cas d'erreur est beaucoup plus intéressant ! Si la requête échoue, nous voulons réessayer, n'est-ce pas ? Cet extrait, `if (operation.retry(err)) { return; }` est intéressant car c'est le cœur de la bibliothèque retry. Nous essayons essentiellement d'appeler à nouveau la fonction. En faisant cela, nous passons l'erreur actuelle dans la fonction retry.

L'opération a un tableau interne d'erreurs, et l'appel de retry avec une erreur pousse cette erreur dans le tableau puis appelle à nouveau l'opération. C'est pourquoi nous avons dû appeler notre fonction originale à l'intérieur de `operation.attempt()`.

J'étais un peu confus au début par l'instruction `return;` à l'intérieur des accolades. Ce que j'ai appris en jouant avec cela, cependant, c'est qu'après avoir appelé `retry()`, la fonction doit retourner afin que `operation` puisse être exécutée à nouveau. Sinon, sans le retour, elle restait bloquée dans l'exécution et échouait avec une promesse non résolue.

Le dernier élément intéressant dans le code ci-dessus est lorsque nous ne pouvons pas faire une autre tentative, c'est-à-dire que nous venons d'exécuter notre dernière tentative. Dans ce cas, l'instruction if va échouer lorsque vous essayez d'appeler `retry()`, et nous contournons ce bloc pour atteindre la section finale où nous `reject(err)`. Cela est très important, car si vous n'incluez pas cette gestion d'erreur finale, la promesse externe ne se résoudra jamais.

#### La dernière pièce du puzzle

Wow, c'était beaucoup à expliquer et je suis sûr que c'était beaucoup à assimiler. Je veux vous montrer un dernier extrait, directement de ma base de code, qui montre comment j'ai utilisé cette fonctionnalité pour gérer l'expiration des tokens lors des appels réseau.

Un petit historique : je travaille avec l'API Spotify, et leurs tokens d'authentification ne sont valables que pendant 60 minutes. En raison de la courte durée de vie, j'ai dû rafraîchir fréquemment pendant le développement. Réalisant que cela pourrait poser un réel problème pour les utilisateurs, j'ai repensé à la manière dont nous avions résolu ce problème lors d'un stage que j'ai fait.

Mes expériences précédentes dans une situation similaire (en Swift sur iOS) m'ont amené à écrire ce dernier morceau de code ici. Je l'ai testé et il fonctionne merveilleusement bien ! L'utilisateur ne saura probablement même pas que son token a expiré, ce qui est comme cela devrait être, puis-je ajouter.

Il y a beaucoup de chemins de code de branchement dans la fonction ci-dessus, et la majorité n'est pas nouvelle. J'ai fait de mon mieux pour expliquer toute la logique dans les commentaires. J'utilise ce code et l'ai testé de nombreuses fois et le token se rafraîchit et la réponse est retournée comme prévu !

Ci-dessous se trouve un court cas d'utilisation de la manière dont j'utilise cette fonction après l'avoir écrite.

J'ai vraiment apprécié la rédaction de cet article, et j'adorerais recevoir des commentaires de la part de quiconque se sent prêt à le faire. Le code ci-dessus peut probablement être encore optimisé d'une certaine manière, mais c'est ce que j'utilise actuellement et cela fonctionne :)

J'espère que cela a aidé au moins une personne à résoudre un problème similaire. Si c'est le cas, j'adorerais savoir comment vous avez utilisé cela !