---
title: Comment fonctionne la concaténation de chaînes en JavaScript – l'opérateur
  "+" vs l'opérateur "+="
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-09-07T18:50:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-concatenation
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/pexels-francesco-ungaro-96081--1-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionne la concaténation de chaînes en JavaScript – l'opérateur
  "+" vs l'opérateur "+="
seo_desc: 'String concatenation is a common task that we do often. String concatenation
  is the operation of joining character strings end-to-end. For example, the concatenation
  of "snow" and "ball" is "snowball".

  In this article, I will be showing two methods b...'
---

La concaténation de chaînes est une tâche courante que nous effectuons souvent. La concaténation de chaînes est l'opération qui consiste à joindre des chaînes de caractères bout à bout. Par exemple, la concaténation de "snow" et "ball" donne "snowball".

Dans cet article, je vais vous montrer deux méthodes pour concaténer des chaînes en JavaScript. Je m'assurerai également de clarifier quand utiliser chaque méthode.

De plus, je vous fournirai un bon exercice de freeCodeCamp pour pratiquer ce concept. Si vous êtes intéressé par une explication vidéo étape par étape, alors vous êtes également au bon endroit !

J'ai récemment tweeté à ce sujet, et comme je l'avais promis, j'ai créé une vidéo et maintenant j'écris cet article pour vous. Consultez également le fil Twitter :

%[https://twitter.com/Fahim_FBA/status/1699144812602220569?s=20]

Assurez-vous de me suivre sur [Twitter/X](https://twitter.com/Fahim_FBA) pour obtenir les dernières mises à jour sur mes nouvelles vidéos ou articles.

## Présentation vidéo :

Voici le moment que vous attendiez peut-être : oui, c'est une vidéo, et je l'ai spécialement préparée pour vous.

%[https://youtu.be/9eZMdTvvbJk]

Faites-moi savoir si vous aimez la présentation vidéo dans la section des commentaires de la vidéo. Assurez-vous également de [vous abonner à ma chaîne YouTube](https://www.youtube.com/@FahimAmin?sub_confirmation=1).

## Travailler avec des chaînes

Avant de parler de la concaténation de chaînes, parlons de quelques bases.

Supposons que je veux imprimer mon nom complet, mais que je ne veux pas saisir mon nom complet en une seule fois. Voir l'exemple ci-dessous :

```javascript
myName = "Md. Fahim ";
myName2 = "Bin Amin";
console.log(myName); // Md. Fahim 
console.log(myName2); // Bin Amin
```

Mon nom complet est "Md. Fahim Bin Amin". Je l'ai divisé en deux parties ou vous pouvez dire en deux moitiés. Par conséquent, `myName` contient mon prénom, `"Md. Fahim "` avec un espace à la fin pour avoir un espace avant d'imprimer mon nom de famille. Mais vous pouvez également ajouter cet espace comme espace de début dans la deuxième chaîne.

`myName2` contient mon nom de famille, `"Bin Amin"`. Ensuite, j'ai imprimé les valeurs de deux variables. Par conséquent, j'ai obtenu deux lignes séparées contenant mon nom complet. Mais ce n'est pas beau d'imprimer le nom d'une personne sur deux lignes différentes, n'est-ce pas ?

Résolvons ce problème maintenant. Il existe de nombreuses façons de le faire, mais nous allons utiliser les méthodes de **concaténation de chaînes**. Nous allons apprendre deux approches différentes pour utiliser la concaténation de chaînes ainsi que l'utilisation appropriée pour chacune d'elles.

## Méthode de concaténation de chaînes 1 – Utilisation de l'opérateur `+`

Il s'agit de la méthode la plus simple : elle utilise l'opérateur `+`. Laissez-moi d'abord vous donner un exemple, et je vous promets que cela sera très clair pour vous une fois que nous l'aurons examiné.

Supposons que je crée une nouvelle variable nommée `fullName` pour stocker mon nom complet. Mais comme précédemment, au lieu d'utiliser mon nom complet dans les guillemets doubles, j'utiliserai des chaînes séparées.

```javascript
fullName = "Md. Fahim " + "Bin Amin";
console.log(fullName); // Md. Fahim Bin Amin
```

Ici, j'ai fourni deux chaînes séparées dans une seule variable de chaîne, mais j'ai utilisé l'opérateur plus ( `+` ) pour ajouter la deuxième chaîne à la fin de la première chaîne. Ici, `"Md. Fahim "` est la première chaîne, et `"Bin Amin"` est la deuxième chaîne.

Puisque je veux un espace entre les deux chaînes séparées, j'ai ajouté un espace de fin dans la première chaîne. Mais vous pouvez également ajouter un espace de début dans la deuxième chaîne au lieu d'ajouter un espace de fin dans la première chaîne, comme je l'ai mentionné ci-dessus.

Il est important de noter que l'ordre des chaînes compte toujours dans la concaténation de chaînes.

Par exemple, si je change l'ordre (je donne la deuxième chaîne avant la première chaîne) dans la variable `fullName`, alors toute la chaîne obtient également une orientation différente et je n'obtiens pas le résultat que je veux (il imprime mal mon nom !).

```javascript
fullName =  "Bin Amin" + "Md. Fahim ";
console.log(fullName); // Bin AminMd. Fahim 
```

Il considère toujours la chaîne qui apparaît en premier comme la première chaîne et ajoute la chaîne suivante à la fin de cette première chaîne. Cela continue ainsi à chaque fois – peu importe combien de chaînes individuelles vous voulez ajouter dans une seule variable de chaîne.

```javascript
fullName =  "Bin Amin " + "Md. Fahim" + " My name is";
console.log(fullName); // Bin Amin Md. Fahim My name is
```

Ah ! Cela a l'air affreux. Laissez-moi corriger l'orientation maintenant :

```javascript
fullName = "My name is " + "Md. Fahim " + "Bin Amin";
console.log(fullName); // My name is Md. Fahim Bin Amin
```

Maintenant, c'est mieux.

## Méthode de concaténation de chaînes 2 – Utilisation de l'opérateur `+=`

Cette méthode est très pratique. Lorsque vous l'utilisez, nous ajoutons des chaînes séparées dans des lignes séparées. Laissez-moi vous donner un exemple.

Je vais utiliser une variable nommée `fullName` comme précédemment, mais au lieu d'utiliser l'opérateur `+` pour concaténer des chaînes comme précédemment, je vais utiliser `+=` :

```javascript
fullName = "Md. Fahim ";
fullName += "Bin Amin";
console.log(fullName); // Md. Fahim Bin Amin
```

Dans la première ligne, j'ai stocké mon prénom dans la variable `fullName`. Dans la deuxième ligne, j'ai stocké mon nom de famille dans cette même variable mais en utilisant l'opérateur `+=` (qui est en fait la combinaison pour `fullName = fullName + "Bin Amin"`). Il ajoute la deuxième chaîne à la fin de la première chaîne comme précédemment.

Cela me permet d'imprimer mon nom complet sur une seule ligne.

`+=` est une combinaison, donc l'utilisation directe de la méthode générique fonctionne également de la même manière comme ci-dessous :

```javascript
fullName = "Md. Fahim ";
fullName = fullName + "Bin Amin";
console.log(fullName); // Md. Fahim Bin Amin
```

Mais vous pouvez supposer que l'utilisation de `+=` sera la méthode la plus facile et la plus compacte. Je vous recommande donc d'utiliser directement l'opérateur `+=`.

### Quelle est la différence ?

Je sais que vous pourriez être confus et penser que si ces méthodes donnent exactement le même résultat, pourquoi devriez-vous apprendre les deux ? Quels sont les cas d'utilisation spécifiques pour chacune ?

Ne vous inquiétez pas ! Je vais répondre à votre question tout de suite.

Suivez le code ci-dessous où j'utilise la 1ère méthode :

```javascript
fullParagraph = "This is the first line of the paragraph. " + "This is the second line of the paragraph. " + "This is the third line of the paragraph. ";
console.log(fullParagraph); // This is the first line of the paragraph. This is the second line of the paragraph. This is the third line of the paragraph.
```

Ici, j'ai pris une variable nommée `fullParagraph` et j'ai stocké trois chaînes/sentences individuelles. Le résultat est exact, mais vous voyez que, en fonction du nombre de nouvelles chaînes/sentences ajoutées, la ligne pour stocker les données dans cette variable spécifique devient plus longue.

Plus vous ajoutez de chaînes ou de phrases différentes pour la concaténation de chaînes en utilisant la première méthode, plus une seule instruction devient longue. Ainsi, il devient très ennuyeux et difficile à inspecter plus tard.

Voici la deuxième méthode pour vous sauver ! 😉

Suivez le code ci-dessous où j'utilise la 2ème méthode :

```javascript
fullParagraph = "This is the first line of the paragraph. ";
fullParagraph += "This is the second line of the paragraph. ";
fullParagraph += "This is the third line of the paragraph. ";
console.log(fullParagraph); // This is the first line of the paragraph. This is the second line of the paragraph. This is the third line of the paragraph.
```

Ici, j'ai pris une variable nommée `fullParagraph` et stocké des chaînes individuelles dans des lignes individuelles. Comme d'habitude, je peux facilement ajouter de nouvelles chaînes dans de nouvelles lignes en utilisant l'opérateur `+=`.

Puisque je prends une nouvelle ligne pour ajouter de nouvelles chaînes à chaque fois, cela ne crée aucun problème pour moi. De plus, chaque instruction individuelle est courte et il est très facile à lire ou à inspecter plus tard. Le code semble également très propre.

Gardez à l'esprit que l'ordre des chaînes compte bien sûr dans chaque méthode. Cela signifie qu'elles suivent toujours l'orientation de l'ordre des chaînes lors de l'ajout (concaténation de chaînes).

### Quand utiliser chaque méthode

Je suppose que vous connaissez déjà la réponse. Mais, pour l'intérêt de cet article, laissez-moi la clarifier à nouveau.

Si vous utilisez une concaténation de chaînes où les chaînes individuelles sont relativement plus petites ou vous savez qu'elles resteront petites en taille, alors vous pouvez directement opter pour la première méthode.

Mais si vous savez que vous devrez peut-être ajouter des chaînes plus longues plus tard, alors vous devriez utiliser la deuxième méthode.

C'est tout !

## Pratiquer la concaténation de chaînes

Vous pouvez pratiquer ce concept [en utilisant cet exercice de freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/concatenating-strings-with-the-plus-equals-operator).

## Conclusion

J'espère que vous avez apprécié cet article. Il faut beaucoup de temps et d'efforts pour écrire un article approfondi et créer des vidéos pour vous. Alors, faites-moi savoir si cela vous aide ou non.

Connectons-nous sur [LinkedIn](https://www.linkedin.com/in/fahimfba/). Veuillez vous assurer de m'endosser sur les compétences pertinentes. Obtenir des recommandations de votre part me rend toujours heureux ! 😊

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur :

🎁GitHub : [FahimFBA](https://github.com/FahimFBA)

🎁YouTube : [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

Si vous êtes intéressé, vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Santé ! 🍻