---
title: Immuabilité en JavaScript – Expliquée avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-12T23:21:23.000Z'
originalURL: https://freecodecamp.org/news/immutability-in-javascript-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/thumbnail.jpg
tags:
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
seo_title: Immuabilité en JavaScript – Expliquée avec des Exemples
seo_desc: 'By Deborah Kurata

  We often hear the terms: immutable and immutability. But what do they mean, and,
  as developers, why should we care?

  Immutable basically means something that cannot be changed. In programming, immutable
  is used to describe a value th...'
---

Par Deborah Kurata

Nous entendons souvent les termes : **immuable** et **immuabilité**. Mais que signifient-ils, et, en tant que développeurs, pourquoi devrions-nous nous en soucier ?

Immuable signifie essentiellement quelque chose qui ne peut pas être changé. En programmation, immuable est utilisé pour décrire une valeur qui ne peut pas être modifiée après avoir été définie.

Mais la plupart des programmes nécessitent de créer, mettre à jour et supprimer des données. Alors pourquoi voudrions-nous travailler avec des données qui ne peuvent pas être changées ?

Dans ce tutoriel, nous examinerons l'immuabilité des primitives, des tableaux et des objets avec des exemples en JavaScript. Et j'expliquerai pourquoi l'immuabilité est importante pour la programmation.

Vous pouvez également regarder la vidéo associée ici :

%[https://youtu.be/DBZESPS-5mQ]

Et voici un exemple JavaScript (que vous pouvez [également voir sur Stackblitz](https://stackblitz.com/edit/immutability-deborahk?file=index.js)) :

```js
// Import des feuilles de style
import './style.css';

// Écrivez du code JavaScript !
const appDiv = document.getElementById('app');
appDiv.innerHTML = `<h1>Ouvrez la console pour voir les résultats</h1>`;

class Person {
  //_name = "Nee";
  //_name = ["Nee", "Ra"];
  _name = { first: "Nee", middle: "L" };
  
  get name() {
    return this._name;
  }
  
  set name(value) {
    console.log('Dans le setter', value);
    this._name = value;
  }
}

let p = new Person();
//p.name = "Ra";                        // Le setter s'exécute
//p.name.push("Lee");                   // Le setter ne s'exécute pas
//p.name = [...p.name, "Lee"];          // Le setter s'exécute
//p.name.middle = "Lee";                // Le setter ne s'exécute pas
p.name = { ...p.name, middle: "Lee" };  // Le setter s'exécute

```

Commençons par les primitives.

## Primitives en JavaScript : Naturellement Immuables

En JavaScript, les primitives, comme les chaînes de caractères et les nombres, sont immuables par défaut. Cela signifie qu'une fois qu'une valeur primitive est créée, elle ne peut pas être changée. Attendez une minute, vous pourriez penser – je change les valeurs des variables primitives tout le temps !

Eh bien, il peut sembler que vous modifiez une valeur. Mais ce n'est pas réellement le cas. Voici un exemple.

```javascript
let greet = "Hello";
greet += ", World";  
console.log(greet);
```

La première ligne de ce code crée la chaîne `Hello` et l'assigne à la variable `greet`. La deuxième ligne ajoute `, World` à cette chaîne. Donc, il semble que nous changeons la chaîne `greet`. Mais JavaScript ne change pas la chaîne. Au contraire, il crée une nouvelle chaîne.

Regardons une illustration. Ici, nous avons une variable `greet` assignée à la chaîne `Hello`.

![Image](https://lh7-us.googleusercontent.com/9-7QkMgYxQdlMMreWAQywiB3yy4k7xi8WkfWNeP0dbDANyNCpUVulbPOsVD06EDGLuZKH4MK_8prwlIqqV0eRVI8BrH3VV8hE7nlxH2zsVg6Fw0HSqe_TN26vGgm_99pmlWKaqGqFU1xy6t0DjpRzMg)
_Figure 1. Le code crée la chaîne `Hello` et l'assigne à la variable `greet`._

Lorsque le code ajoute du texte, JavaScript crée une nouvelle chaîne. Il assigne ensuite la variable `greet` à cette nouvelle chaîne. La chaîne `Hello` d'origine n'est pas modifiée.

![Image](https://lh7-us.googleusercontent.com/T_KgVb_6Cy-rBP7bnxQUaosHDaFbvfh2MY8XNrEvsM0rJDgx7Qih1sH6OYL9qBLqlBIM3bNiKQ1jJKeM5UwQSurqkUr-MBztWjkFZbxtYgCL_V8PjfBhO4mYd_4lzym2xwtXjPpZ8p9cHzcCVGNuHXg)
_Figure 2. L'ajout de texte crée une nouvelle chaîne et l'assigne à la variable `greet`._

Ainsi, les chaînes de caractères et autres primitives sont immuables par défaut en JavaScript.

Et les tableaux ?

## Les Tableaux JavaScript sont Mutables

En JavaScript, les tableaux sont mutables par défaut. Cela signifie que le tableau peut être modifié après sa création. Nous pouvons le modifier "sur place", en ajoutant, supprimant ou changeant des éléments.

Regardons un exemple.

```javascript
let ages = [42, 22, 35];
ages.push(8);  
console.log(ages);
```

La première ligne de code définit un tableau et assigne une variable à ce tableau. Mais en JavaScript, la variable ne stocke pas le tableau. Elle stocke l'adresse mémoire où le tableau réside, comme illustré dans la Figure 3 ici :

![Image](https://lh7-us.googleusercontent.com/v7dmTur_H7PetKYQkvHGbjYPKWaZhkevFhgHO8gJxufnHN24p_h4gkAupNbqX9SqvLhjw8KFuuwSwWTMJocMX4t-D0r0vwRr6mvf-2G--SwSSuBi1mfqC31kUFzudwCB1qUJnqGPM7YDsWozqg0ZfDg)
_Figure 3. Une variable ne stocke pas un tableau – elle stocke l'adresse mémoire du tableau._

Dans la deuxième ligne de code de l'exemple précédent, nous utilisons la méthode `push` pour modifier le tableau d'origine. Dans ce cas, nous ajoutons 8 à la fin du tableau. Cela est montré dans la Figure 4 :

![Image](https://lh7-us.googleusercontent.com/TCWSxZMXMh5Oz06HncXSt5OapytcOfTRKdwCAAM3mac6XFndE6p_VpMkjkQAvUqxlTdpLwQaRorROsXCIcif8KJPtQmGKY7rbSQVad_QXAJ04AIyfY3Gn28cAeO2wHPSNcv4MN0KueD1AjmhKgrzYoM)
_Figure 4. Un tableau JavaScript est modifié "sur place"._

Remarquez que l'adresse mémoire du tableau ne change pas, mais le tableau lui-même change. Ainsi, la valeur du tableau est mutable.

Cette mutabilité offre de la flexibilité. Mais la mutabilité peut entraîner des effets secondaires non intentionnels, surtout dans les applications plus grandes ou celles impliquant des opérations concurrentes.

Et la mutabilité pose des problèmes. Supposons que vous avez du code dans un setter qui doit s'exécuter lorsque le tableau est modifié. Ou que vous travaillez avec un framework, comme Angular, qui fournit une détection de changements. Ou que vous utilisez une bibliothèque d'état, comme Redux, qui nécessite l'immuabilité.

Comme nous l'avons vu dans cet exemple, notre tableau est modifié... mais notre variable `ages` n'a pas réellement changé, puisque elle référence l'adresse mémoire. Ainsi, le setter ou la détection de changements ou la gestion d'état pourrait ne pas être conscient que le tableau a été modifié.

Pour éviter ces pièges de la mutabilité, nous, en tant que développeurs JavaScript, utilisons souvent des motifs ou des méthodes qui ne modifient pas le tableau d'origine mais retournent plutôt un nouveau tableau. Cela embrasse l'immuabilité.

## Comment Embrasser l'Immuabilité avec les Tableaux

Regardons un exemple alternatif :

```javascript
let ages = [42, 22, 35];
ages = [...ages, 8];  
console.log(ages);
```

Dans ce code, nous commençons avec le même tableau. Mais lorsque nous ajoutons un élément, nous utilisons l'opérateur de décomposition JavaScript. L'opérateur de décomposition fait une copie du tableau existant à une nouvelle adresse en "décomposant" le tableau existant.

Nous ajoutons ensuite le nouvel élément à cette copie. Nous réassignons également la variable `ages` à l'adresse du nouveau tableau (Figure 5).

![Image](https://lh7-us.googleusercontent.com/3zRss4le02LtJWuvVAodTOv6lGDWGBkoZ6LvluPSojWfkEDWU3n6R-PAktzUMd92Ua9sNzc-kuFis6u2xOFsUkKCjxR8SdPY4-4x43hP8Wp13CbA5XHE-aXBtq2VjMPGdMXtE_XaZbDTuiWzRHGGYaQ)
_Figure 5. En utilisant l'opérateur de décomposition, nous créons un nouveau tableau à une nouvelle adresse et l'assignons à la variable `ages`._

Remarquez que le tableau d'origine n'est pas modifié. En utilisant l'opérateur de décomposition, nous atteignons l'immuabilité.

En plus de l'opérateur de décomposition, de nombreuses méthodes de tableau créent également un nouveau tableau et traitent donc un tableau comme immuable. D'autres méthodes de tableau modifient le tableau sur place et sont donc mutables. Voici quelques exemples.

* `Map` crée un nouveau tableau à partir du tableau existant, en mappant chaque élément à l'aide d'une fonction que nous fournissons. Il laisse le tableau d'origine inchangé. Il supporte donc l'immuabilité.

```javascript
ages.map(x => x + 1);
```

* `Push` modifie le tableau d'origine sur place, mutant le tableau.

```javascript
ages.push(8);
```

* `Filter` crée un nouveau tableau avec les éléments correspondant aux critères définis. Il laisse le tableau d'origine inchangé.

```javascript
ages.filter(x => x > 21);
```

* `Sort` trie les éléments du tableau sur place, mutant ainsi le tableau.

```javascript
ages.sort();
```

* `Slice` crée un nouveau tableau à partir d'une portion d'un tableau existant. Ici, nous copions les éléments du tableau d'origine en commençant à l'index 1 jusqu'à l'index 3 dans un nouveau tableau.

```javascript
ages.slice(1, 3);
```

* `Splice` change le contenu d'un tableau sur place, en ajoutant, supprimant ou remplaçant des éléments existants. Dans cet exemple, le code commence à remplacer les éléments à l'index 2, ne remplace qu'un seul élément, et remplace l'élément par "18".

```javascript
ages.splice(2, 1, 18);
```

Ainsi, même si par défaut les tableaux sont mutables, nous pouvons utiliser des techniques d'immuabilité pour mieux gérer nos tableaux.

Et les objets ?

## La Nature Mutable des Objets JavaScript

Les objets en JavaScript sont également mutables par défaut. Nous pouvons ajouter ou supprimer des propriétés et changer les valeurs des propriétés "sur place" après qu'un objet a été créé.

```javascript
let p = {name:"Nee", age: 30};
p.age = 31;
console.log(p);
```

La première ligne de cet exemple de code déclare un objet personne avec des propriétés de nom et d'âge. Lorsqu'une variable est assignée à cet objet, la variable ne stocke pas l'objet, mais plutôt une adresse mémoire où l'objet réside.

![Image](https://lh7-us.googleusercontent.com/-z8t2kPHCLlKG5y2D8p37azjtcc-a-Na_JarvtrXgTHbcsCjpZd3pYPxSdA5NAtTfNNllVXevr71jfV6X9UymACPkr-WyeQAwi-Auc32G4q9H8WEOlm-S4c_CbEzV5FhLIjq8btJAsUr35m5wclTmtI)
_Figure 6. Une variable ne stocke pas un objet. Elle stocke plutôt l'adresse mémoire de l'objet._

La deuxième ligne de code de l'exemple précédent modifie la valeur d'une propriété d'objet, changeant l'âge. Cette modification altère directement l'objet personne d'origine.

![Image](https://lh7-us.googleusercontent.com/1OBvr491s67DqK4M3poTs31M5yjB2tQK9vo9QiWpLSSB-iSkC1qNKoypVC-Zhiitn56jMgfP_khoSNneCoPNJa9tp71Z3OSvgCl-jO15yaqGejOSa0WhL6VoapluQxjnxZ8SVluWcoe203m9t2nSdmU)
_Figure 7. Un objet JavaScript est modifié "sur place"._

Remarquez que l'adresse mémoire de l'objet ne change pas, mais l'objet lui-même change. Cela est similaire à la mutabilité des tableaux, et cela a du sens car les tableaux en JavaScript sont essentiellement des objets.

La mutabilité offre de la flexibilité mais peut entraîner des bugs complexes si elle n'est pas gérée avec soin.

Et comme avec un tableau, la mutabilité pose des problèmes. Supposons que vous avez du code dans un setter qui doit s'exécuter lorsque l'objet change. Ou que vous travaillez avec un framework, comme Angular, qui fournit une détection de changements. Ou que vous utilisez une bibliothèque d'état, comme Redux, qui nécessite l'immuabilité.

Dans cet exemple, notre objet a changé mais notre variable `p` n'a pas réellement changé, puisque elle référence l'adresse mémoire. Ainsi, le setter ou la détection de changements ou la gestion d'état peut ne pas voir que l'objet a été modifié.

Il est souvent préférable de gérer les objets de manière immuable. JavaScript fournit des fonctionnalités pour aider avec les objets immuables.

## Immuabilité avec les Objets

Voici un exemple alternatif :

```javascript
let p = {name:"Nee", age: 30};
p = {...p, age: 31};
console.log(p);
```

Nous commençons avec le même objet. Mais au lieu de changer directement la valeur d'une propriété d'objet, nous utilisons à nouveau l'opérateur de décomposition. L'opérateur de décomposition fait une copie de l'objet en le décomposant dans un nouvel objet à une nouvelle adresse. Nous mettons à jour la propriété dans ce nouvel objet. Nous réassignons ensuite la variable `p` à l'adresse du nouvel objet.

![Image](https://lh7-us.googleusercontent.com/_q_uW95z9GHcZi2SgUUpI1ht1P7dWqY4xF0z8P8cphnmMb_EkUwogdYQaGf1ZaqfKLxKtbWtzUDRZMtVcv8CiK3Zog5c1Wv6187x5gCeaTi8g_27x2HBRXucBbRHI9huMzh08VbE3CpM30mSlrLUiQc)
_Figure 8. En utilisant l'opérateur de décomposition, nous créons un nouvel objet à une nouvelle adresse et l'assignons à la variable `p`._

Remarquez que l'objet d'origine n'est pas modifié. En utilisant l'opérateur de décomposition, nous atteignons l'immuabilité.

Nous avons donc vu comment les primitives sont immuables par défaut. Et que les tableaux et les objets sont mutables, mais nous pouvons travailler avec eux de manière immuable.

Bien ! Mais pourquoi nous en soucions-nous ?

## Pourquoi l'Immuabilité est-elle Importante ?

Il y a plusieurs raisons pour lesquelles l'immuabilité est importante dans notre codage quotidien.

* Une fois qu'une valeur immuable est définie, elle n'est pas changée. Plutôt, une nouvelle valeur est créée. Cela rend la valeur prévisible et cohérente dans tout le code. Ainsi, cela aide à gérer l'état dans toute l'application. De plus, l'immuabilité est un principe clé dans les frameworks de gestion d'état, comme Redux.
* Le code devient plus simple et moins sujet aux erreurs lorsque les structures de données ne changent pas de manière inattendue. Cela simplifie également le débogage et la maintenance.
* Embrasser l'immuabilité est en ligne avec les principes de la programmation fonctionnelle, conduisant à moins d'effets secondaires et à un code plus prévisible.

## **Conclusion**

L'immuabilité est un concept fondamental en programmation. Une valeur immuable est une valeur qui ne peut pas être changée après avoir été créée.

Ce concept est important pour la programmation fonctionnelle et la gestion d'état. C'est un concept précieux, surtout lorsqu'on traite de la concurrence et de grandes bases de code complexes.

Pour voir ces concepts avec des animations, regardez la vidéo ici :

%[https://youtu.be/DBZESPS-5mQ]

Ou essayez mon lien stackblitz : [https://stackblitz.com/edit/immutability-deborahk](https://stackblitz.com/edit/immutability-deborahk). N'oubliez pas de forker mon projet pour essayer vos propres modifications.

Bien que les objets et tableaux JavaScript soient mutables par défaut, adopter une approche immuable pour les gérer peut conduire à un code plus propre, plus fiable et plus facile à maintenir.