---
title: Introduction aux cas de switch en JavaScript
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-06-13T12:23:08.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-javascript-switch-cases
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/0_f2yYmYJFuG3pH07G.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
seo_title: Introduction aux cas de switch en JavaScript
seo_desc: 'In this short article, I will introduce you to JavaScript switch cases
  and how to use them with practical examples.

  This article will explain better with more practical examples to help you understand
  switch cases in depth.

  Prerequisites.


  Basic Java...'
---

Dans cet article court, je vais vous présenter les cas de switch en JavaScript et comment les utiliser avec des exemples pratiques.

Cet article expliquera mieux avec plus d'exemples pratiques pour vous aider à comprendre les cas de switch en profondeur.

### Prérequis.

* Connaissances de base en JavaScript

* Éditeur de code

* Navigateur Web

* Votre cerveau :)

Une instruction `switch` peut essentiellement remplacer plusieurs vérifications `if` en JavaScript.

Elle offre une manière plus descriptive de comparer une valeur avec plusieurs variantes.

### **La syntaxe du Switch**

Le `switch` a un ou plusieurs blocs `case` et un cas par défaut optionnel.

```javascript
switch(x) {
  case 'value1':  // si (x === 'value1')
    //code ici
    [break]

  case 'value2':  // si (x === 'value2')
    //code ici
    [break]

  default:
    //code ici
    [break]
}
```

* La valeur de `x` est vérifiée pour une égalité stricte avec la valeur du premier `case` (c'est-à-dire `value1`) puis avec le second (`value2`) et ainsi de suite.

* Si l'égalité est trouvée, `switch` commence à exécuter le code à partir du `case` correspondant, jusqu'au `break` le plus proche (ou jusqu'à la fin du `switch`).

* Si aucun cas ne correspond, alors le code `default` est exécuté (s'il existe).

### **Quelques exemples réels**

* ***Simple Switch Play & Pause***

L'instruction `switch` peut être utilisée pour plusieurs branches basées sur un nombre ou une chaîne de caractères :

```javascript
switch (movie) {
  case 'play':
    playMovie();
    break;
  case 'pause':
    pauseMovie();
    break;
  default:
    doNothing();
}
```

Si vous n'ajoutez pas d'instruction `break`, l'exécution "passera" au niveau suivant. Il est essentiel de marquer délibérément le passage avec un commentaire si vous l'avez vraiment voulu pour aider au débogage :

```javascript
switch (movie) {
  case 'play': // passage intentionnel
  case 'pause':
    pauseMovie();
    break;
  default:
    doNothing();
}
```

La clause default est optionnelle. Vous pouvez avoir des expressions dans la partie switch et les cas si vous le souhaitez ; les comparaisons ont lieu entre les deux en utilisant l'opérateur `===` :

```javascript
switch (3 + 7) {
  case 5 + 5:
    correct();
    break;
  default:
    neverhappens();
}
```

* ***Simple Switch de Calcul Mathématique***

```javascript
let average = 2 + 6;

switch (average) {
  case 4:
    alert( 'Trop petit' );
    break;
  case 8:
    alert( 'Exactement !' );
    break;
  case 10:
    alert( 'Trop grand' );
    break;
  default:
    alert( "Valeurs incorrectes !" );
}
```

Ici, le `switch` commence à comparer `average` avec la première variante `case` qui est `4`. La correspondance échoue.

Ensuite `8`. C'est une correspondance, donc l'exécution commence à partir de `case 8` jusqu'au `break` le plus proche.

Si **il n'y a pas** de `**break**`, **l'exécution continue avec le prochain** `**case**` **sans aucune vérification.**

Voici un exemple sans `break` :

```javascript
let average = 2 + 6;

switch (average) {
  case 4:
    alert( 'Trop petit' );
  case 8:
    alert( 'Exactement !' );
  case 10:
    alert( 'Trop grand' );
  default:
    alert( "Valeurs incorrectes !" );
}
```

Dans l'exemple ci-dessus, nous verrons l'exécution séquentielle de trois `alert` :

```javascript
alert( 'Exactement !' );
alert( 'Trop grand' );
alert( "Valeurs incorrectes !" );
```

* ***Cas de switch de la méthode getDay()***

La méthode `getDay()` retourne le jour de la semaine sous forme de nombre entre 0 et 6.

> *Dimanche=0, Lundi=1, Mardi=2, Mercredi=3, Jeudi=4, Vendredi=5, Samedi=6*

Cet exemple utilise le numéro du jour de la semaine pour calculer le nom du jour de la semaine :

```javascript
switch (new Date().getDay()) {
  case 0:
    day = "Dimanche";
    break;
  case 1:
    day = "Lundi";
    break;
  case 2:
     day = "Mardi";
    break;
  case 3:
    day = "Mercredi";
    break;
  case 4:
    day = "Jeudi";
    break;
  case 5:
    day = "Vendredi";
    break;
  case 6:
    day = "Samedi";
}
```

Le résultat de day sera le jour de la semaine actuel au format jour.

PS : Cela changera selon le moment où vous lisez cet article.

J'ai écrit cet article le 13/06/2019, qui est un jeudi, donc le résultat serait :

```python
Jeudi
```

### Le mot-clé default

Le mot-clé **default** spécifie le code à exécuter s'il n'y a pas de correspondance de cas, un peu comme une instruction else :

```javascript
switch (new Date().getDay()) {
  case 6:
    text = "Aujourd'hui, c'est samedi";
    break; 
  case 0:
    text = "Aujourd'hui, c'est dimanche";
    break; 
  default: 
    text = "Ce n'est pas encore le week-end !";
}
```

Le résultat de text sera :

```python
Ce n'est pas encore le week-end !
```

Le cas **default** n'a pas besoin d'être le dernier cas dans un bloc switch :

```javascript
switch (new Date().getDay()) {
  default: 
    text = "Ce n'est pas encore le week-end !";
    break;
  case 6:
    text = "Aujourd'hui, c'est samedi";
    break; 
  case 0:
    text = "Aujourd'hui, c'est dimanche";
}
```

> ***Si default n'est pas le dernier cas dans le bloc switch, n'oubliez pas de terminer le cas default par un break.***

### **Conclusion**

Il existe de nombreux exemples pratiques de cas de switch, vous pouvez vous rendre sur [google.com](https://google.com/) et effectuer une recherche rapide pour plus d'exemples de cas de switch.

Si cet article vous a aidé, montrez-le en le partageant.

Merci d'avoir lu !