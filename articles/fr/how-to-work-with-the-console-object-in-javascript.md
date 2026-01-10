---
title: Comment travailler avec l'objet Console en JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-07T21:29:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-the-console-object-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/computer-on-desk.jpg
tags:
- name: console
  slug: console
- name: JavaScript
  slug: javascript
seo_title: Comment travailler avec l'objet Console en JavaScript
seo_desc: 'When you run into errors inside your code, it''s important to know how
  to debug and find the source of the problem. The console object is a powerful tool
  that can help you with this.

  In this article, we will explore the console object and the variety ...'
---

Lorsque vous rencontrez des erreurs dans votre code, il est important de savoir comment le déboguer et trouver la source du problème. L'objet `console` est un outil puissant qui peut vous aider dans cette tâche.

Dans cet article, nous allons explorer l'objet `console` et les différentes méthodes qui vous aideront à déboguer votre code.

## Qu'est-ce que l'objet `console` ?

L'objet `console` est un objet global qui fournit un accès à la console de débogage du navigateur. Cet objet dispose de diverses méthodes qui peuvent être utilisées pour journaliser des messages, des erreurs, des avertissements et d'autres informations dans la console.

Dans cet article, nous examinerons les méthodes les plus couramment utilisées telles que `console.log`, `console.warn` et `console.error`.

## Comment accéder à la console dans votre navigateur

Pour accéder à la console dans votre navigateur, vous pouvez faire un clic droit sur la page et sélectionner `Inspecter`. Cela ouvrira les outils de développement. Vous pouvez également utiliser le raccourci clavier `Ctrl + Maj + I` sous Windows ou `Cmd + Option + I` sur Mac.

![Onglet Console dans Google Chrome](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-06-at-7.50.03-PM.png)

## Comment utiliser la méthode `console.log()`

La méthode la plus couramment utilisée pour déboguer les applications est la méthode `console.log`. Cette méthode est utilisée pour journaliser des messages et des variables dans la console.

```javascript
console.log("Bonjour, le monde !");
```

Lorsque vous exécutez ce code dans votre navigateur, vous verrez le message "Bonjour, le monde !" journalisé dans la console.

![Instruction de console affichant Bonjour, le monde](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-06-at-7.51.44-PM.png)

Cette méthode est également utile pour journaliser la valeur des variables dans la console et trouver des bugs dans votre code.

Supposons que nous voulions créer un générateur de Mad Libs. Il s'agit d'un jeu populaire où vous remplissez les blancs d'une histoire avec des mots aléatoires.

Voici le code que nous avons créé jusqu'à présent :

```js
function madLibsGenerator(verb, adjective, noun) {
  return `We shall ${verb} the${adjective}${noun}.`;
}

console.log(madLibsGenerator("dance", "big", "dog"));
```

Nous voulons voir ce que fait notre fonction, donc nous avons un `console.log(madLibsGenerator("dance", "big", "dog"));`. Mais lorsque nous vérifions la console, nous remarquons des problèmes d'espacement avec la phrase imprimée.

![Instruction d'impression pour le générateur Mad Libs](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-06-at-8.05.45-PM.png)

Maintenant que nous savons où se trouve le problème, nous pouvons corriger ces problèmes d'espacement dans la fonction ici :

```js
function madLibsGenerator(verb, adjective, noun) {
  return `We shall ${verb} the ${adjective} ${noun}.`;
}

console.log(madLibsGenerator("dance", "big", "dog"));
```

Maintenant, la console devrait imprimer le résultat correct.

![Résultat correct de Mad Libs](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-06-at-8.07.44-PM.png)

## Qu'est-ce que la méthode `console.warn()` ?

La méthode `console.warn` est utilisée pour journaliser des messages d'avertissement dans la console. Cette méthode est utile pour journaliser des messages qui ne sont pas des erreurs, mais qui sont nevertheless importants pour le développeur.

Par exemple, si vous construisez une application qui utilise une méthode obsolète, vous pouvez utiliser la méthode `console.warn` pour journaliser un message d'avertissement dans la console.

```javascript
console.warn(
  "Cette méthode est obsolète et sera supprimée dans la prochaine version"
);
```

Lorsque vous exécutez ce code dans votre navigateur, vous verrez le message d'avertissement `"Cette méthode est obsolète et sera supprimée dans la prochaine version"` journalisé dans la console.

![Exemple de méthode console.warn](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-06-at-8.08.44-PM.png)

## Qu'est-ce que la méthode `console.error()` ?

La méthode `console.error` est utilisée pour journaliser des messages d'erreur dans la console. Cette méthode est utile pour journaliser des messages indiquant qu'une erreur s'est produite dans votre application.

Supposons que vous avez une application qui essaie de récupérer des données à partir d'une API, mais que l'API est hors ligne. Vous pouvez utiliser la méthode `console.error` pour journaliser un message d'erreur dans la console.

Voici un exemple de la façon d'utiliser la méthode `console.error` pour journaliser un message d'erreur dans la console :

```javascript
fetch("https://api.example.com/data")
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((error) =>
    console.error("Il y a eu une erreur lors de la récupération des données", error)
  );
```

S'il y a une erreur lors de la récupération des données à partir de l'API, vous verrez le message d'erreur `"Il y a eu une erreur lors de la récupération des données"` journalisé dans la console.

![Exemple de message d'erreur échoué](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-06-at-8.09.28-PM.png)

## Conclusion

Il existe de nombreuses autres méthodes que vous pouvez utiliser avec l'objet `console` pour vous aider à déboguer votre code. Dans cet article, nous n'avons fait qu'effleurer la surface.

Pour en savoir plus sur l'objet `console` et les différentes méthodes que vous pouvez utiliser, consultez la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/API/Console).

Je vous encourage à explorer l'objet `console` et les différentes méthodes qu'il offre. C'est un outil puissant qui vous aidera à déboguer votre code et à trouver la source de tout problème que vous pourriez rencontrer.