---
title: Comment passer des fonctions de rappel à String.replace() en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-01T20:14:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-callback-functions-to-string-replace-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pawe--l-1121782.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment passer des fonctions de rappel à String.replace() en JavaScript
seo_desc: "By Dillion Megida\nDid you know that the string .replace() method accepts\
  \ a callback function? I just discovered it today and thought I'd share. \nWhat\
  \ do you need this function for? Why does it exist? I'll answer all these questions\
  \ as you go through ..."
---

Par Dillion Megida

Saviez-vous que la méthode `.replace()` accepte une fonction de rappel ? Je l'ai découvert aujourd'hui et j'ai pensé à le partager. 

Pourquoi avez-vous besoin de cette fonction ? Pourquoi existe-t-elle ? Je répondrai à toutes ces questions au fil de cet article.

## La méthode `replace()`

La méthode de chaîne `replace()` remplace des caractères de texte dans une chaîne. Elle prend deux arguments : la chaîne à remplacer et la valeur par laquelle elle doit être remplacée.

Avec cette méthode, vous pouvez remplacer des caractères de chaîne (comme "hello") ou [des caractères qui correspondent à un motif RegEx](https://www.freecodecamp.org/news/javascript-string-replace-example-with-regex/) (comme `/hi/`).

Voici la syntaxe de cette méthode :

```js
String.replace(string/pattern, replacer)
```

Voici quelques exemples montrant comment utiliser cette méthode :

```js
const sentence = "Hi my name is Dillion"

const replaced1 = sentence.replace("Dillion", "JavaScript")
console.log(replaced1)
// "Hi my name is JavaScript"

const replaced2 = sentence.replace(/\s/g, "-")
console.log(replaced2)
// "Hi-my-name-is-Dillion"
```

Mais l'argument `replacer` peut également être une fonction.

## Pourquoi utiliser une fonction comme méthode de remplacement ?

La raison est que, parfois, vous voulez effectuer une action sur les caractères qui correspondent au motif spécifié.

Voici la syntaxe :

```js
String.replace(/pattern/, function(matched){
    // faire quelque chose avec matched et retourner
    // la valeur de remplacement
})
```

Si vous utilisez un motif de chaîne littérale comme "Dillion", vous n'avez pas besoin de la fonction de rappel car vous savez déjà que c'est seulement "Dillion" que vous recherchez dans la phrase.

Mais avec les motifs RegEx, cela peut correspondre à plusieurs éléments. Voici un exemple :

```js
const sentence = "I am a good guy and you too"
const replaced = sentence.replace(/g\S*/g, "😂")

console.log(replaced)
// I am a 😂 😂 and you too
```

Le motif regex correspond à tous les mots qui commencent par "g" et deux mots correspondent : "good" et "guy". Dans ce cas, si nous voulons faire quelque chose avec la valeur correspondante, nous aurions besoin du rappel.

Voici un autre exemple :

```js
const sentence = "I am a good guy and you too"
const replaced = sentence.replace(/g\S*/g, function(matched){
    console.log("matched", matched)
    return "😂"
})

console.log(replaced)
// matched good
// matched guy
// I am a 😂 😂 and you too
```

Quels sont les exemples de choses que nous pouvons faire avec les valeurs correspondantes ? Il y a tellement de scénarios, mais je vais utiliser le cas d'utilisation qui m'a conduit à découvrir cela.

## Comment trouver et remplacer des URL dans un texte avec RegEx

Sur des plateformes comme WhatsApp et Twitter, vous remarquerez que lorsque vous publiez un message avec un lien, le lien est coloré différemment du reste du texte et se comporte comme un lien. Ensuite, lorsqu'on clique dessus, il redirige l'utilisateur vers une page distincte.

Comment y parviennent-ils ? L'idée est de remplacer les liens dans le texte par un élément qui possède certains styles et qui fonctionne également comme un lien.

Voici comment j'ai fait cela avec JavaScript :

```js
const text = "My website is https://dillionmegida.com and I write on http://freecodecamp.org/"

const regex = /https?:\/\/\S*/gi

const modifiedText = text.replace(regex, (url) => {
    return `<a class="text--link" href="${url}">${url}</a>`
})

console.log(modifiedText)
// My website is <a class="text--link" href="https://dillionmegida.com">https://dillionmegida.com</a> and I write on <a class="text--link" href="http://freecodecamp.org/">http://freecodecamp.org/</a>
```

La regex correspond aux motifs avec "https://..." (avec le s optionnel). En utilisant le rappel, je peux obtenir l' `url` qui correspond à la regex et l'utiliser pour créer une chaîne de balise d'ancrage avec une classe "text--link".

Avec cette chaîne retournée, je peux l'injecter dans le DOM. Dans mon cas, j'utilisais React, j'ai donc utilisé [dangerouslySetInnerHTML](https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml) pour l'injecter dans un paragraphe. Je peux spécifier une couleur pour la classe "text--link" dans ma feuille de style.

## Conclusion

Nous apprenons de nouvelles choses chaque jour, et j'espère que vous avez appris quelque chose en JavaScript aujourd'hui — la fonction de rappel dans `String.replace()`.

De plus, dans cet article, j'ai montré un bon cas d'utilisation pour tirer parti de cette fonction.

N'hésitez pas à partager ceci si vous le trouvez utile.