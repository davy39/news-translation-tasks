---
title: Qu'est-ce que la récursivité ? Une fonction récursive expliquée avec des exemples
  de code JavaScript
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-02-04T00:03:39.000Z'
originalURL: https://freecodecamp.org/news/what-is-recursion-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/recursion-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: Qu'est-ce que la récursivité ? Une fonction récursive expliquée avec des
  exemples de code JavaScript
seo_desc: "Recursion is a technique used to solve computer problems by creating a\
  \ function that calls itself until your program achieves the desired result. \n\
  This tutorial will help you to learn about recursion and how it compares to the\
  \ more common loop.\nWhat ..."
---

La récursivité est une technique utilisée pour résoudre des problèmes informatiques en créant une fonction qui s'appelle elle-même jusqu'à ce que votre programme atteigne le résultat souhaité. 

Ce tutoriel vous aidera à apprendre la récursivité et à comprendre comment elle se compare à la boucle plus courante.

## Qu'est-ce que la récursivité ?

Supposons que vous avez une fonction qui enregistre les nombres de 1 à 5. Voici comment l'écrire en utilisant la récursivité :

```js
function log(num){
    if(num > 5){
        return;
    }
    console.log(num);
    log(num + 1);
}

log(1);
```

Lorsque vous exécutez le code ci-dessus, la fonction `log` s'appellera simplement elle-même tant que la valeur de la variable `num` est inférieure à `5`. 

Une fonction récursive doit avoir au moins une condition où elle cessera de s'appeler elle-même, sinon la fonction s'appellera indéfiniment jusqu'à ce que JavaScript génère une erreur.

La condition qui empêche une fonction récursive de s'appeler elle-même est connue sous le nom de **cas de base**. Dans la fonction `log` ci-dessus, le cas de base est lorsque `num` est supérieur à `5`.

## Pourquoi ne pas simplement utiliser une boucle ?

Tous les problèmes que vous pouvez résoudre en utilisant une fonction récursive auront toujours une solution alternative avec une boucle. L'exemple ci-dessus peut être remplacé par le code suivant :

```js
for(let i = 1; i <= 5; i++){
    console.log(i);
}
```

Les langages de programmation modernes comme JavaScript ont déjà les instructions `for` et `while` comme alternatives aux fonctions récursives. Mais certains langages comme Clojure n'ont pas d'instructions de boucle, vous devez donc utiliser la récursivité pour exécuter plusieurs fois un morceau de code.

De plus, une boucle `for` nécessite que vous sachiez combien de fois vous allez répéter l'exécution du code. Mais une fonction récursive et une boucle `while` peuvent être utilisées pour exécuter un morceau de code sans savoir combien de fois vous devez le répéter. Vous devez simplement connaître la condition qui arrête l'exécution.

Par exemple, supposons que vous avez une tâche comme suit :

* Sélectionnez aléatoirement un nombre entre 1 et 10 jusqu'à obtenir le nombre 5. 
* Enregistrez combien de fois vous devez exécuter le code jusqu'à ce que la méthode aléatoire retourne 5.

Voici comment procéder avec une fonction récursive :

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        console.log(`The random result: ${result}`);
        console.log(`How many times random is executed: ${count}`);
        return;
    }
    result = Math.floor(Math.random() * (10 - 1 + 1) + 1);
    count++;
    randomUntilFive(result, count);
}

randomUntilFive();
```

Vous ne pouvez pas remplacer le code ci-dessus par une boucle `for`, mais vous pouvez le remplacer par une boucle `while` :

```js
let result = 0;
let count = 0;

while (result !== 5) {
  result = Math.floor(Math.random() * (10 - 1 + 1) + 1);
  count++;
}

console.log(`The random result: ${result}`);
console.log(`How many times random is executed: ${count}`);
```

En dehors des questions d'entretien de codage où vous devez résoudre le problème en utilisant la récursivité, vous pouvez toujours trouver une solution alternative qui utilise soit l'instruction de boucle `for` ou `while`.

## Comment lire une fonction récursive

Une fonction récursive n'est pas intuitive ou facile à comprendre au premier abord. Les étapes suivantes vous aideront à lire et à comprendre une fonction récursive plus rapidement :

* Identifiez toujours **le cas de base** de la fonction avant toute autre chose.
* Passez des arguments à la fonction qui atteindront immédiatement le cas de base.
* Identifiez les arguments qui exécuteront au moins une fois l'appel de la fonction récursive.

Essayons ces étapes en utilisant l'exemple `randomUntilFive()` ci-dessus. Vous pouvez identifier le cas de base pour cette fonction à l'intérieur de l'instruction `if` ci-dessus :

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        // le cas de base est déclenché
    }
    // appel récursif de la fonction
}

randomUntilFive();
```

Cela signifie que vous pouvez atteindre le cas de base en passant le nombre `5` dans le paramètre `result` comme suit :

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        console.log(`The random result: ${result}`);
        console.log(`How many times random is executed: ${count}`);
        return;
    }
}

randomUntilFive(5);
```

Bien que le paramètre `count` ne devrait pas être zéro, passer le nombre `5` comme argument à l'appel de la fonction ci-dessus remplit les exigences de la deuxième étape.

Enfin, vous devez trouver un argument qui exécutera au moins une fois l'appel de la fonction récursive. Dans le cas ci-dessus, vous pouvez passer n'importe quel nombre autre que `5` ou rien du tout :

```js
function randomUntilFive(result = 0, count = 0){
    if(result === 5){
        console.log(`The random result: ${result}`);
        console.log(`How many times random is executed: ${count}`);
        return;
    }
    result = Math.floor(Math.random() * (10 - 1 + 1) + 1);
    count++;
    randomUntilFive(result, count);
}

randomUntilFive(4); 
// n'importe quel nombre autre que cinq 
// exécutera l'appel récursif
```

Et vous avez terminé. Maintenant, vous comprenez que la fonction `randomUntilFive()` s'appellera récursivement jusqu'à ce que la valeur de `result` soit égale à cinq. 

## Comment écrire une fonction récursive

Écrire une fonction récursive est presque la même chose que la lire :

* Créez une fonction régulière avec un cas de base qui peut être atteint avec ses paramètres
* Passez des arguments dans la fonction qui déclenchent immédiatement le cas de base
* Passez les arguments suivants qui déclenchent l'appel récursif une seule fois.

Supposons que vous écrivez une fonction pour calculer les [factorielles](https://en.wikipedia.org/wiki/Factorial). Voici la factorielle de cinq :

**5*4*3*2*1 = 120**

Tout d'abord, le cas de base pour cette fonction est un, alors créons une fonction `factorial` qui retourne un :

```js
function factorial(num){
    if(num === 1){
        return num;
    }
    
}

console.log(factorial(1));
```

Passons maintenant à la troisième étape. Nous devons obtenir un appel récursif dans la fonction et l'appeler au moins une fois. Puisque le calcul de la factorielle diminue le nombre de un à chaque multiplication, vous pouvez le simuler en passant `num-1` dans l'appel récursif :

```js
function factorial(num){
    if(num === 1){
        return num;
    }
    return num * factorial(num-1) 
}

console.log(factorial(2));
```

Et maintenant, vous avez terminé. Vous pouvez tester la fonction en passant cinq à l'appel :

```js
console.log(factorial(5));
```

## Conclusion

Vous venez d'apprendre ce qu'est une fonction récursive et comment elle se compare aux instructions de boucle `for` et `while` courantes. Une fonction récursive doit toujours avoir au moins un cas de base pour qu'elle cesse de s'appeler elle-même, sinon elle provoquera une erreur. 

Lorsque vous lisez une fonction récursive, vous devez simuler une situation où le cas de base est immédiatement exécuté sans exécuter l'appel récursif. 

Une fois que vous avez couvert le cas de base, revenez en arrière d'une étape et essayez d'exécuter l'appel récursif au moins une fois. De cette façon, votre cerveau parcourra le code récursif et comprendra intuitivement ce qu'il fait.

Il en va de même pour l'écriture d'une fonction récursive. Créez toujours le cas de base en premier, puis écrivez un argument qui exécute l'appel récursif au moins une fois. Le reste sera plus facile à partir de là.

## Merci d'avoir lu ce tutoriel

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !