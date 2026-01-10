---
title: JavaScript toLowerCase() – Comment convertir une chaîne en minuscules et majuscules
  en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-16T15:07:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-tolowercase-how-to-convert-a-string-to-lowercase-and-uppercase-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript toLowerCase() – Comment convertir une chaîne en minuscules et
  majuscules en JS
seo_desc: "This article explains how to convert a string to lowercase and uppercase\
  \ characters. \nWe'll also go over how to make only the first letter in a word uppercase\
  \ and how to make the first letter of every word in a sentence uppercase.\nLet's\
  \ get started!\n..."
---

Cet article explique comment convertir une chaîne de caractères en minuscules et en majuscules.

Nous verrons également comment mettre uniquement la première lettre d'un mot en majuscule et comment mettre la première lettre de chaque mot d'une phrase en majuscule.

Commençons !

## Comment utiliser la méthode `toLowerCase()` en JavaScript

La méthode `toLowerCase` convertit une chaîne de caractères en lettres minuscules.

La syntaxe générale de la méthode est la suivante :

```javascript
String.toLowerCase()
```

La méthode `toLowerCase()` ne prend aucun paramètre.

Les chaînes de caractères en JavaScript sont **immuables**. La méthode `toLowerCase()` convertit la chaîne spécifiée en une nouvelle chaîne composée uniquement de lettres minuscules et retourne cette valeur.

Cela signifie que l'ancienne chaîne d'origine n'est pas modifiée ou affectée de quelque manière que ce soit.

```javascript
let myGreeting = 'Hey there!';

console.log(myGreeting.toLowerCase());

//output
//hey there!
```

La chaîne `myGreeting` contient une seule lettre majuscule qui est convertie en minuscule.

Les lettres déjà en minuscules ne sont pas affectées par la méthode `toLowerCase()`, seules les majuscules le sont. Ces lettres conservent leur forme originale.

La chaîne dans l'exemple ci-dessous est composée de lettres majuscules. Elles sont toutes converties en minuscules lorsque la méthode `toLowerCase()` est appliquée.

```javascript
const anotherGreeting = 'GOOD MORNING!!';

console.log(anotherGreeting.toLowerCase());
//output
//good morning!!
```


## Comment utiliser la méthode `toUpperCase()` en JavaScript

La méthode `toUpperCase()` est similaire à la méthode `toLowerCase()`, mais elle convertit la valeur de la chaîne en majuscules.

La syntaxe générale pour appeler la méthode est la suivante :

```javascript
String.toUpper()
```

Elle ne prend aucun paramètre.

Comme les chaînes de caractères en JavaScript sont immuables, la méthode `toLowerCase()` ne modifie pas la valeur de la chaîne spécifiée.

Elle retourne plutôt une nouvelle valeur. La chaîne spécifiée est convertie en une nouvelle chaîne dont le contenu est composé uniquement de lettres majuscules. Cela signifie qu'il y aura maintenant deux chaînes : l'originale et la nouvelle convertie en majuscules.


```javascript
console.log('I am shouting!'.toUpperCase());

//output
//I AM SHOUTING!
```

Les lettres majuscules déjà présentes dans la chaîne ne seront pas affectées et resteront inchangées lorsque la méthode `toLowerCase()` est appelée.

### Comment mettre en majuscule uniquement la première lettre d'une chaîne en JavaScript

Que faire si vous souhaitez mettre uniquement la première lettre d'une chaîne en majuscule ?

Voici un exemple simple qui montre une façon de procéder.

Supposons qu'il y ait une variable appelée `myGreeting` avec la valeur de chaîne `hello`, entièrement en lettres minuscules.

```javascript
let myGreeting = 'hello';
```

Vous localisez et extrayez d'abord la première lettre de cette chaîne en utilisant son index. Ensuite, vous appelez la méthode `toUpperCase()` sur cette lettre spécifique.

Rappel : l'indexation en JavaScript (et dans la plupart des langages de programmation) commence à `0`, donc la première lettre a un index de `0`.

Enregistrez cette opération dans une nouvelle variable appelée `capFirstLetter`.

```javascript
let capFirstLetter = myGreeting[0].toUpperCase();

console.log(capFirstLetter);
// retourne la lettre 'H' dans ce cas
```

Ensuite, vous souhaitez isoler et supprimer ce premier caractère et conserver le reste de la chaîne.

Une façon de faire cela est d'utiliser la méthode `slice()`. Cela crée une nouvelle chaîne à partir de l'index spécifié jusqu'à la fin du mot.

Vous souhaitez commencer à partir de la deuxième lettre jusqu'à la fin de la valeur.

Dans ce cas, l'argument que vous devez passer à `slice()` est un index de `1`, car c'est l'index de la deuxième lettre.

De cette façon, le premier caractère est entièrement exclu. Une nouvelle chaîne est retournée sans lui, mais contenant le reste des caractères, moins cette première lettre.

Ensuite, enregistrez cette opération dans une nouvelle variable.

```javascript
let restOfGreeting = myGreeting.slice(1);

console.log(restOfGreeting);
// retourne la chaîne 'ello'
```

En combinant les deux nouvelles variables avec la concaténation, vous obtenez une nouvelle chaîne avec uniquement la première lettre en majuscule.

```javascript
let newGreeting = capFirstLetter + restOfGreeting;

console.log(newGreeting);
//Hello
```

Une autre façon est de combiner les étapes ci-dessus et de les isoler dans une fonction.

La fonction est créée une seule fois. La fonction retourne ensuite une nouvelle chaîne avec la première lettre en majuscule.

La quantité de code que vous devez écrire est considérablement réduite, tout en pouvant passer n'importe quelle chaîne comme argument sans écrire de code répétitif.

```javascript
function capFirst(str) {
     return str[0].toUpperCase() + str.slice(1);
 }

console.log(capFirst('hello'));
//output 
//Hello
```

### Comment mettre en majuscule la première lettre de chaque mot en JavaScript

Mais comment mettre en majuscule la première lettre de chaque mot dans une phrase ?

La méthode montrée dans la section ci-dessus ne fonctionnera pas, car elle ne traite pas plusieurs mots, mais seulement un mot unique dans une phrase.

Supposons que vous ayez une phrase comme celle ci-dessous. Vous souhaitez mettre en majuscule chaque premier mot de la phrase.

```javascript
let learnCoding = 'learn to code for free with freeCodeCamp';
```

La première étape consiste à diviser la phrase en mots individuels et à travailler avec chacun d'eux séparément.

Pour cela, vous utilisez la méthode `split()` et passez un espace comme argument. Cela signifie qu'à chaque espace dans la phrase fournie, un élément est passé dans un nouveau tableau.

Elle divise la phrase en fonction des espaces vides.

Créez une nouvelle variable et stockez le nouveau tableau.

```javascript
let splitLearnCoding = learnCoding.split(" ");

console.log(splitLearnCoding); 
//['learn', 'to', 'code', 'for', 'free', 'with', 'freeCodeCamp']
```


Maintenant, à partir de cette phrase, il y a un nouveau tableau de mots qui vous permet de manipuler chaque mot individuellement, séparément.

Puisqu'il y a maintenant un nouveau tableau, vous pouvez utiliser la méthode `map()` pour itérer sur chaque élément individuel à l'intérieur.

Dans la méthode `map()`, vous utilisez la même procédure montrée dans la section ci-dessus pour prendre chaque mot individuellement, mettre la première lettre en majuscule et retourner le reste du mot.

```javascript
let capSplitLearnCoding = splitLearnCoding.map(word => {
    return word[0].toUpperCase() + word.slice(1);
})

console.log(capSplitLearnCoding);
//['Learn', 'To', 'Code', 'For', 'Free', 'With', 'FreeCodeCamp']
```

La première lettre de chaque mot est maintenant en majuscule.

Il ne reste plus qu'à combiner les mots du tableau en une seule phrase.

Pour cela, vous utilisez la méthode `join()` et passez un espace comme argument.

```javascript
let learnCodingNew = capSplitLearnCoding.join(" ");

console.log(learnCodingNew);
//Learn To Code For Free With FreeCodeCamp
```

Comme montré dans la section ci-dessus, vous pouvez également créer une fonction qui combine toutes ces étapes. Vous pourrez alors passer n'importe quelle chaîne comme argument et chaque premier mot sera en majuscule.

```javascript
function capFirstLetterInSentence(sentence) {
    let words = sentence.split(" ").map(word => {
        return word[0].toUpperCase() + word.slice(1);
    })
    return words.join(" ");
}

console.log(capFirstLetterInSentence("i am learning how to code"));
//I Am Learning How To Code
```


## Conclusion

Et voilà ! C'est ainsi que vous utilisez les méthodes `toLowerCase()` et `toUpperCase()` en JavaScript.

Vous avez appris comment mettre en majuscule la première lettre d'un mot et comment mettre en majuscule la première lettre de chaque mot dans une phrase.

Si vous souhaitez apprendre JavaScript et mieux comprendre le langage, freeCodeCamp propose une [certification gratuite en JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

Vous commencerez par les bases en tant que débutant absolu du langage, puis vous passerez à des sujets plus complexes tels que la programmation orientée objet, la programmation fonctionnelle, les structures de données, les algorithmes et des techniques de débogage utiles.

À la fin, vous construirez cinq projets pour mettre vos compétences en pratique.

Merci d'avoir lu, et bon apprentissage !