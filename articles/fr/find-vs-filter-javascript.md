---
title: find() vs filter() en JavaScript – Les différences expliquées avec des exemples
date: '2022-10-14T22:22:22.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/find-vs-filter-javascript
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Logo.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_desc: "By Aman Kalra\nA common interview question that JavaScript developers often\
  \ get asked is to explain the difference between the find() and filter() methods.\
  \ \nIn this tutorial today, I'll walk you through what these methods are and when\
  \ you should use t..."
---


Par Aman Kalra

<!-- more -->

Une question d'entretien courante que l'on pose souvent aux développeurs JavaScript est d'expliquer la différence entre les méthodes `find()` et `filter()`.

Dans ce tutoriel, je vais vous expliquer ce que sont ces méthodes et quand vous devriez les utiliser.

## Qu'est-ce que la méthode `filter()` ?

Cette méthode renvoie tous les éléments du tableau qui satisfont à la condition spécifiée dans la fonction de rappel (callback).

Voyons avec un exemple comment elle fonctionne réellement :

```
const x = [1, 2, 3, 4, 5];

const y = x.filter(el => el*2 === 2);

console.log("y is: ", y); // y is: [1]
```

Si vous vérifiez la sortie de l'exemple ci-dessus, la **valeur de y est** **un tableau d'un seul élément** qui satisfait à la condition. C'est parce que la méthode `filter()` itère sur tous les éléments du tableau puis renvoie un tableau filtré contenant les éléments qui satisfont à la condition spécifiée.

## Qu'est-ce que la méthode `find()` ?

Cette méthode renvoie le premier élément du tableau qui satisfait à la condition spécifiée dans la fonction de rappel.

Voyons avec un exemple comment elle fonctionne réellement :

```
const x = [1, 2, 3, 4, 5];

const y = x.find(el => el*2 === 2);

console.log("y is: ", y); // y is: 1
```

Maintenant, si vous regardez la sortie de l'exemple ci-dessus, la **valeur de y est 1**. C'est parce que la méthode `find()` cherche le premier élément du tableau qui satisfait à la condition spécifiée.

Les principales différences entre les exemples ci-dessus sont :

1.  `filter()` renvoie un tableau contenant l'élément qui satisfait à la condition, mais `find()` renvoie l'élément lui-même qui satisfait à la condition.
2.  Dans `filter()`, l'intégralité du tableau est parcourue même si l'élément recherché est présent dès le début. En revanche, avec `find()`, dès que l'élément qui satisfait à la condition est trouvé, il est immédiatement renvoyé.

## Cas d'utilisation pour `find()` et `filter()`

Lorsque vous avez un cas d'utilisation où vous attendez le retour de plusieurs éléments et que vous souhaitez effectuer une opération sur tous ces éléments, vous pouvez utiliser la méthode **filter()**. Mais si vous n'attendez qu'un seul élément du tableau, vous pouvez utiliser **find()** et ainsi éviter des itérations inutiles.

Voyons des exemples pour ces deux cas d'utilisation :

### 1\. Exemple de cas d'utilisation de filter()

```
const x = [1, 2, 3, 4, 5];

const y = x.filter(el => el%2 === 0);

console.log("y is: ", y); // y is: [2, 4]
```

Dans l'exemple ci-dessus, `**filter()**` est plus logique car vous voulez itérer sur tous les éléments du tableau pour trouver les éléments qui sont divisibles par 2.

### 2\. Exemple de cas d'utilisation de find()

```
const emp = [
    {
        name: "Ram",
        empID: 101
    },
    {
        name: "Sham",
        empID: 102
    },
    {
        name: "Mohan",
        empID: 103
    }
];

const res = emp.find(el => el.empID === 102);

console.log("res is: ", res); // res is: {name: 'Sham', empID: 102}
```

Dans l'exemple ci-dessus, `**find()**` est plus logique car il n'y a qu'un seul employé qui possède `102` comme `empID`. Ainsi, `find()` permet d'éviter d'itérer sur le troisième objet du tableau.

### **Merci de m'avoir lu !**

Si vous avez trouvé cet article utile, n'hésitez pas à le partager avec vos amis et collègues.