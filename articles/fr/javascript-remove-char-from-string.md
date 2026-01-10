---
title: JS Supprimer un caractère d'une chaîne - Comment supprimer un caractère d'une
  chaîne en JavaScript
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-05-09T19:51:36.918Z'
originalURL: https://freecodecamp.org/news/javascript-remove-char-from-string
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/cckf4TsHAuw/upload/1d75957a397f479d41bc73b407025508.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: JS Supprimer un caractère d'une chaîne - Comment supprimer un caractère
  d'une chaîne en JavaScript
seo_desc: 'Manipulating strings is a fundamental skill in programming.

  A common task you might encounter when coding in JavaScript is trimming characters
  from a string. Trimming involves removing specific characters from the beginning
  and/or end of a string. Th...'
---

Manipuler des chaînes de caractères est une compétence fondamentale en programmation.

Une tâche courante que vous pourriez rencontrer lors de la programmation en JavaScript est la suppression de caractères d'une chaîne. La suppression implique de retirer des caractères spécifiques du début et/ou de la fin d'une chaîne. Ces caractères peuvent être des espaces, des tabulations, des sauts de ligne ou des virgules en fin de chaîne.

Vous pouvez également vouloir supprimer des caractères spécifiques que vous ne souhaitez pas dans votre programme et les remplacer par d'autres.

Dans cet article, vous apprendrez quelques méthodes que vous pouvez utiliser pour supprimer et retirer des caractères d'une chaîne en JavaScript.

## Comment supprimer les caractères d'espace blanc à l'aide de la méthode `trim()` en JavaScript

Vous pouvez supprimer les caractères d'espace blanc au début et à la fin d'une chaîne en utilisant la méthode intégrée `trim()`.

Voici la syntaxe générale de la méthode `trim()` :

```javascript
string.trim()
```

La méthode `trim()` est appelée directement sur la chaîne que vous souhaitez modifier. La méthode supprime tous les caractères d'espace blanc tels que les espaces, les tabulations ou les sauts de ligne, du début et de la fin de la chaîne.

Notez que la méthode `trim()` ne modifie pas la chaîne originale. Au lieu de cela, elle retourne une nouvelle chaîne modifiée, avec les caractères de début et de fin supprimés.

Prenons l'exemple suivant :

```javascript
let greeting = "    Hello World    ";

let trimmedGreeting = greeting.trim();

console.log(trimmedGreeting); // Sortie : "Hello World"
```

Dans l'exemple ci-dessus, j'ai déclaré une variable nommée `greeting` et j'ai assigné la valeur de chaîne `Hello World`. La chaîne a des espaces à la fois au début et à la fin.

Pour supprimer ces espaces de début et de fin, j'ai appelé la méthode `trim()` sur la variable `greeting` et j'ai stocké le résultat dans une nouvelle variable, `trimmedGreeting`.

Lorsque j'ai utilisé `console.log()` pour imprimer la nouvelle chaîne dans la console, les espaces de début et de fin avaient été supprimés.

La chaîne originale dans `greeting` contient toujours les espaces de début et de fin.

### Comment supprimer les caractères d'espace blanc au début à l'aide de la méthode `trimStart()` en JavaScript

Pour supprimer les caractères d'espace blanc uniquement au début d'une chaîne en JavaScript, vous pouvez utiliser la méthode `trimStart()`.

Prenons l'exemple suivant :

```javascript
let greeting = "    Hello World    ";

let trimmedGreeting = greeting.trimStart();

console.log(trimmedGreeting); // Sortie : "Hello World    "
```

Dans l'exemple ci-dessus, la variable `greeting` a une valeur de chaîne `Hello World`. La chaîne a des espaces au début et à la fin.

J'ai appelé la méthode `trimStart()` sur `greeting` et j'ai sauvegardé le résultat dans `trimmedGreeting`. Cette méthode supprime uniquement les espaces au début de la chaîne. Les espaces à la fin de la chaîne resteront.

### Comment supprimer les caractères d'espace blanc à la fin à l'aide de la méthode `trimEnd()` en JavaScript

Pour supprimer les caractères d'espace blanc uniquement à la fin d'une chaîne en JavaScript, vous pouvez utiliser la méthode `trimEnd()`.

Prenons l'exemple suivant :

```javascript
let greeting = "    Hello World    ";

let trimmedGreeting = greeting.trimEnd();

console.log(trimmedGreeting); // Sortie : "    Hello World"
```

La chaîne stockée dans `greeting` a des espaces au début et à la fin.

J'ai appelé la méthode `trimEnd()` sur `greeting` et j'ai sauvegardé le résultat dans `trimmedGreeting`. Cette méthode supprime uniquement les espaces à la fin de la chaîne. Les espaces au début de la chaîne resteront.

## Comment supprimer un caractère à l'aide de la méthode `replace()` en JavaScript

Pour supprimer un caractère spécifique d'une chaîne en JavaScript, vous pouvez utiliser la méthode `replace()`.

Voici la syntaxe générale de la méthode `replace()` :

```javascript
string.replace(pattern, replacement);
```

Vous appelez la méthode `replace()` sur une chaîne que vous souhaitez modifier. La méthode accepte deux arguments : `pattern` et `replacement`.

L'argument `pattern` spécifie le motif que vous souhaitez trouver et remplacer dans la chaîne. Cela peut être un caractère spécifique, une sous-chaîne ou un motif d'expression régulière que vous souhaitez trouver et remplacer dans la chaîne.

L'argument `replacement` est le nouveau caractère ou la nouvelle chaîne que vous souhaitez utiliser pour remplacer `pattern`.

Notez que la méthode `replace()` ne modifie pas la chaîne originale.

Prenons un exemple :

```javascript
let sentence = "I love dogs";

let modifiedSentence  = sentence.replace("dogs", "cats");

console.log(modifiedSentence); // Sortie : "I love cats"
```

J'ai d'abord déclaré une variable nommée `sentence` et j'ai assigné la valeur de chaîne `I love dogs`.

Ensuite, j'ai appelé la méthode `replace()` sur `sentence`, car je souhaite supprimer la sous-chaîne `dogs` et la remplacer par `cats`. J'ai ensuite stocké le résultat dans la nouvelle variable `modifiedSentence`.

Enfin, j'ai enregistré la chaîne stockée dans la variable `modifiedSentence` dans la console. La chaîne `"I love cats"` est imprimée dans la console.

La méthode `replace()` a trouvé la sous-chaîne `dogs` et l'a remplacée par `cats`, sans changer autre chose.

## Comment supprimer plusieurs instances d'un caractère à l'aide de la méthode `replace()` en JavaScript

Dans la section précédente, vous avez vu un exemple de la façon d'utiliser la méthode `replace()` pour remplacer un mot par un autre.

Que se passe-t-il cependant lorsque vous avez plusieurs occurrences du mot que vous souhaitez remplacer ?

```javascript
let sentence = "I love dogs because dogs are cute";

let modifiedSentence  = sentence.replace("dogs", "cats");

console.log(modifiedSentence); // Sortie : "I love cats because dogs are cute"
```

Dans l'exemple ci-dessus, la variable `sentence` a deux occurrences du mot `dogs` que je souhaite remplacer par le mot `cats`. Cependant, la méthode `replace()` par défaut ne remplace que la première occurrence de `dogs`.

Supprimer plusieurs occurrences d'un mot en utilisant la méthode `replace()` est un peu différent. Vous y parvenez en utilisant une expression régulière.

Réécrivons le code en utilisant une expression régulière :

```javascript
let sentence = "I love dogs because dogs are cute";

let modifiedSentence  = sentence.replace(/dogs/g, "cats");

console.log(modifiedSentence); // Sortie : "I love cats because cats are cute"
```

Dans l'exemple ci-dessus, j'ai remplacé toutes les occurrences de la chaîne `dogs` par la chaîne `cats`.

Au lieu de passer une chaîne comme premier argument à `replace()`, j'ai passé l'expression régulière `/dogs/g`, qui utilise le drapeau `g`. Ce drapeau signifie `global`, et correspond à toutes les occurrences du mot `dogs`, et pas seulement à la première.

## Conclusion

Dans cet article, vous avez appris les bases de la suppression des espaces et du remplacement des caractères dans les chaînes en JavaScript.

Plus précisément, vous avez appris comment utiliser la méthode `trim()` pour supprimer les caractères d'espace blanc au début et à la fin, et vous avez découvert les méthodes `trimStart()` et `trimEnd()` pour supprimer uniquement les caractères d'espace blanc au début ou uniquement à la fin, respectivement.

Enfin, vous avez appris comment utiliser la méthode `replace()` pour supprimer des caractères spécifiques et les remplacer par d'autres.

Merci d'avoir lu, et bon codage !