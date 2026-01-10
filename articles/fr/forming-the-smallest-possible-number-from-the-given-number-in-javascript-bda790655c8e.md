---
title: Comment former le plus petit nombre possible à partir d'un nombre donné en
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-29T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/forming-the-smallest-possible-number-from-the-given-number-in-javascript-bda790655c8e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XoEDgZmZ-IWBZivc4DJakg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: Comment former le plus petit nombre possible à partir d'un nombre donné
  en JavaScript
seo_desc: 'By Prashant Yadav

  In this tutorial, we will implement an algorithm to form the smallest possible number
  with ES6.


  Source: Pixabay

  Input: 55010 7652634

  Output: 10055 2345667

  Note: The transformed number should not start with 0 if it has at least one ...'
---

Par Prashant Yadav

Dans ce tutoriel, nous allons implémenter un algorithme pour former le plus petit nombre possible avec [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/).

![Image](https://cdn-media-1.freecodecamp.org/images/w8OnyWg2LPtjbRckRL41TKnrqr6ObvUOZbEW)
_Source : Pixabay_

```
Entrée : 55010 7652634
```

```
Sortie : 10055 2345667
```

**Note** : Le nombre transformé ne doit pas commencer par 0 s'il contient au moins un caractère non nul.

Nous allons utiliser deux approches différentes pour résoudre ce problème. Tout sera écrit en [ES6](https://learnersbucket.com/tutorials/es6/es6-intro).

* Dans la première approche, nous supposerons que le nombre fourni est au format chaîne et nous le résoudrons en utilisant le tri, ce qui prendra O(nlogn).
* Dans la deuxième approche, nous le résoudrons avec une valeur numérique en O(d) temps, où d est le nombre de chiffres.

### Utilisation du tri O(nlogn).

#### Implémentation

* Nous convertirons le nombre en tableau de caractères, puis nous trions ce tableau.
* Après le tri, nous vérifierons si le premier caractère du tableau est 0.
* S'il n'est pas 0, nous joindrons le tableau et le retournerons.
* S'il est 0, nous trouverons le premier nombre non nul et l'échangerons avec 0, puis le retournerons.

```
function smallestPossibleNumber(num){
```

```
//Créer un tableau de caractères et le trier par ordre croissantlet sorted = num.split('').sort();
```

```
//Vérifier si le premier caractère n'est pas 0, puis joindre et retourner it if(sorted[0] != '0'){    return sorted.join('');}
```

```
//trouver l'index du premier caractère non nul let index = 0; for(let i = 0; i < sorted.length; i++){  if(sorted[i] > "0"){    index = i;    break;  } }
```

```
//Échanger les index  let temp = sorted[0];  sorted[0] = sorted[index];  sorted[index] = temp;
```

```
//retourner la chaîne après avoir joint les caractères du tableau return sorted.join(''); }
```

Exécution du programme

```
Entrée :console.log(smallestPossibleNumber('55010'));console.log(smallestPossibleNumber('7652634'));console.log(smallestPossibleNumber('000001'));console.log(smallestPossibleNumber('000000'));
```

```
Sortie :100552345667100000000000
```

```
/*Comment cela fonctionne  let sorted = num.split('').sort();   = ['5','5','0','1','0'].sort() = ['0','0','1','5','5']  if(sorted[0] != '0'){   // '0' != '0' condition échoue     return sorted.join('');  }    //Trouver l'index du premier caractère non nul  let index = 0;  for(let i = 0; i < sorted.length; i++){     if(sorted[i] > '0'){  // '1' > '0'       index = i;      // index = 2;       break;          // break;     }  }    //échanger l'index  var temp = sorted[0];        sorted[0] = sorted[index];  sorted[index] = temp;    //retourner la chaîne  return sorted.join('');*/
```

#### Comment cela fonctionne

Nous avons d'abord créé le tableau de caractères comme `['5', '5', '0', '1', 0]` . Ensuite, nous l'avons trié pour obtenir `['0', '0', '1', '5', '5']` . Après cela, nous avons trouvé le premier élément non nul et l'avons échangé avec le premier élément nul comme `['1', '0', '0', '5', '5']` . Maintenant, nous avons notre plus petit nombre prêt, il nous suffit de les concaténer ensemble et de le retourner.

En savoir plus sur [split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split), [sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort), [join()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join).

Complexité temporelle : O(nlogn).  
Complexité spatiale : O(n).

#### Explication de la complexité temporelle et spatiale

Nous créons un tableau de caractères qui prendra O(n) temps. Ensuite, le tri du tableau prendra O(nlogn).

Après cela, nous trouvons l'index du plus petit nombre non nul qui peut prendre O(n) dans le pire des cas et la jointure du tableau pour créer la chaîne prendra O(n). Comme toutes ces opérations s'exécutent les unes après les autres. Donc la complexité temporelle est O(n + nlogn + n + n) = O(nlogn).

Nous créons un tableau de caractères à partir de la chaîne, donc la complexité spatiale est O(n).

### Utilisation de la valeur numérique O(logn).

Il y a un inconvénient dans cette approche : si le nombre ne contient que des zéros, il retournera un seul zéro.

#### Implémentation

* Nous allons créer un tableau de nombres de 0 à 9.
* Ensuite, nous allons suivre les chiffres présents dans le nombre en augmentant leur compte dans le tableau.
* Après cela, nous allons trouver le plus petit chiffre non nul et diminuer son compte de 1.
* À la fin, nous allons recréer le nombre en les arrangeant par ordre croissant et retourner le résultat.
* Cette solution est basée sur le tri par comptage.

```
function smallestPossibleNumber(num) {    // initialiser la fréquence de chaque chiffre à zéro   let freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];          // compter la fréquence de chaque chiffre dans le nombre   while (num > 0){      let d = parseInt(num % 10); // extraire le dernier chiffre     freq[d]++; // incrémenter le compte     num = parseInt(num / 10); //supprimer le dernier chiffre   }
```

```
// Définir le chiffre le plus à gauche au minimum sauf 0   let result = 0;    for (let i = 1 ; i <= 9 ; i++) {       if (freq[i] != 0) {          result = i;          freq[i]--;          break;      }    }           // arranger tous les chiffres restants   // par ordre croissant   for (let i = 0 ; i <= 9 ; i++) {      while (freq[i]-- != 0){          result = result * 10 + i;       }   }        return result; }
```

Exécution du programme

```
Entrée :console.log(smallestPossibleNumber('55010'));console.log(smallestPossibleNumber('7652634'));console.log(smallestPossibleNumber('000001'));console.log(smallestPossibleNumber('000000'));
```

```
Sortie :10055234566710
```

```
/* Comment cela fonctionne   // initialiser la fréquence de chaque chiffre à zéro   let freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];      // compter la fréquence de chaque chiffre dans le nombre   while (num > 0){      let d = parseInt(num % 10); // extraire le dernier chiffre     freq[d]++; // incrémenter le compte             num = parseInt(num / 10); //supprimer le dernier chiffre   }    //Après l'incrémentation du compte   //freq = [2, 1, 0, 0, 0, 2, 0, 0, 0, 0]      // Définir le chiffre le plus à gauche au minimum sauf 0   let result = 0;    for (let i = 1 ; i <= 9 ; i++) {       if (freq[i] != 0) {          result = i;          freq[i]--;          break;      }    }    // result = 1     // arranger tous les chiffres restants   // par ordre croissant   for (let i = 0 ; i <= 9 ; i++) {      while (freq[i]-- != 0){          result = result * 10 + i;       }   }
```

```
   //10   //100   //1005   //10055   //10055      return result*/
```

Complexité temporelle : O(nlogn).  
Complexité spatiale : O(1).

#### Explication de la complexité temporelle et spatiale

Nous supprimons chaque chiffre du nombre et incrémentons son compte respectif dans un tableau, ce qui prendra O(logn). Ensuite, nous trouvons le plus petit nombre non nul dans le tableau en O(10).

Après cela, nous réarrangeons les chiffres pour créer le plus petit nombre en O(10 * logn). La complexité temporelle est O(logn + 10 + 10logn) = O(logn) ou O(d), où d est le nombre de chiffres.

Nous utilisons un espace constant (un tableau de 10 nombres), donc la complexité spatiale est O(1).

Si vous avez aimé cet article, donnez-lui quelques ? et partagez-le ! Si vous avez des questions à ce sujet, n'hésitez pas à me les poser.

_Pour plus de contenu comme celui-ci et des solutions algorithmiques en Javascript, suivez-moi sur_ [**Twitter**](https://twitter.com/LearnersBucket)_._ J'écris sur [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), React, Nodejs, [Structures de données](https://learnersbucket.com/tutorials/topics/data-structures/), et [Algorithmes](https://learnersbucket.com/examples/topics/algorithms/) sur [_learnersbucket.com_](https://learnersbucket.com/)_.