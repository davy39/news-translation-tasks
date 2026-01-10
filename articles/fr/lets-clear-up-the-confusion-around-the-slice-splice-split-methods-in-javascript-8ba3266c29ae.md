---
title: Clarifions la confusion autour des méthodes slice(), splice() & split() en
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T17:57:55.000Z'
originalURL: https://freecodecamp.org/news/lets-clear-up-the-confusion-around-the-slice-splice-split-methods-in-javascript-8ba3266c29ae
coverImage: https://cdn-media-1.freecodecamp.org/images/0*QaNtLL7jbyw3062_
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Clarifions la confusion autour des méthodes slice(), splice() & split()
  en JavaScript
seo_desc: 'By Cem Eygi

  JavaScript built-in methods help us a lot while programming, once we understand
  them correctly. I would like to explain three of them in this article: the slice(),
  splice() and split() methods. Perhaps because their naming is so similar t...'
---

Par Cem Eygi

Les méthodes intégrées de JavaScript nous aident beaucoup lors de la programmation, une fois que nous les comprenons correctement. J'aimerais expliquer trois d'entre elles dans cet article : les méthodes **`slice()`**, **`splice()`** et **`split()`**. Peut-être parce que leur nom est si similaire, elles sont souvent confondues, même parmi les développeurs expérimentés.

**Je conseille aux étudiants et aux développeurs juniors de lire cet article attentivement car ces trois méthodes peuvent également être demandées lors des ENTRETIENS D'EMBAUCHE.**

Vous pouvez trouver un résumé de chaque méthode à la fin. Si vous préférez, vous pouvez également regarder la version vidéo ci-dessous :

%[https://youtu.be/alFcHCWwS0I]

Alors commençons...

### Tableaux JavaScript

Tout d'abord, vous devez comprendre comment fonctionnent les **tableaux JavaScript**. Comme dans d'autres langages de programmation, nous utilisons des tableaux pour stocker plusieurs données en JS. Mais la différence est que les **tableaux JS peuvent contenir différents types de données en même temps.**

Parfois, nous devons effectuer des opérations sur ces tableaux. Ensuite, nous utilisons certaines méthodes JS comme **slice() & splice()**. Vous pouvez voir ci-dessous comment déclarer un tableau en JavaScript :

`let arrayDefinition = [];   // Déclaration de tableau en JS`

Maintenant, déclarons un autre tableau avec différents types de données. Je l'utiliserai ci-dessous dans les exemples :

`let array = [1, 2, 3, "hello world", 4.12, true];`

Cette utilisation est **valide** en JavaScript. Un tableau avec différents types de données : chaîne de caractères, nombres et un booléen.

### Slice()

La méthode **slice()** **copie** une partie donnée d'un tableau et retourne cette partie copiée sous forme de nouveau tableau. **Elle ne modifie pas le tableau original.**

`array.slice(from, until);`

* **From :** Découpe le tableau à partir d'un index d'élément
* **Until :** Découpe le tableau jusqu'à un autre index d'élément

Par exemple, je veux découper les trois premiers éléments du tableau ci-dessus. Puisque le premier élément d'un tableau est toujours indexé à 0, je commence à découper **"from"** 0.

`array.slice(0, until);`

Voici la partie délicate. Lorsque je veux découper les trois premiers éléments, je dois donner le paramètre **until** comme 3. **La** méthode **slice()** n'inclut pas le dernier élément donné.

```
array[0] --> 1              // inclus
array[1] --> 2              // inclus
array[2] --> 3              // inclus
array[3] --> "hello world"  // non inclus
```

Cela peut créer une certaine confusion. C'est pourquoi j'appelle le deuxième paramètre **"until"**.

`let newArray = array.slice(0, 3);   // La valeur de retour est également un tableau`

Enfin, j'assigne le tableau découpé à la variable **newArray**. Maintenant, voyons le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UECVH_JWknae04kVqTr1gg.png)
_Découper le **tableau** et assigner les membres à **newArray**_

![Image](https://cdn-media-1.freecodecamp.org/images/1*YImz2x-CAY-8wqoyT8c6eA.png)
_La variable **newArray** est maintenant un tableau, et le tableau original reste le même_

> _Note importante : la méthode **Slice()** peut également être utilisée pour les **chaînes de caractères.**_

### Splice()

Le nom de cette fonction est très similaire à **slice()**. Cette similitude de nom confond souvent les développeurs. La méthode **splice()** **modifie** un tableau, en ajoutant ou en supprimant des éléments. Voyons comment ajouter et supprimer des éléments avec **splice()** :

#### Suppression d'éléments

Pour supprimer des éléments, nous devons donner le paramètre **index**, et le **nombre d'éléments** à supprimer :

`array.splice(index, number of elements);`

**Index** est le **point de départ** pour supprimer des éléments. Les éléments qui ont un numéro d'index **plus petit** que l'index donné ne seront pas supprimés :

`array.splice(2);  // Chaque élément à partir de l'index 2 sera supprimé`

Si nous ne définissons pas le deuxième paramètre, chaque élément à partir de l'index donné sera supprimé du tableau :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OGTbYRkU4C_5iMF5Sw9lBA.png)
_Seuls les index 0 et 1 sont encore là_

En tant que deuxième exemple, je donne le deuxième paramètre comme 1, donc les éléments à partir de l'index 2 seront supprimés un par un chaque fois que nous appelons la méthode **splice()** :

`array.splice(2, 1);`

![Image](https://cdn-media-1.freecodecamp.org/images/1*uCZHAfeq46dG182y6oHrpg.png)
_Tableau au début_

**Après le 1er appel :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*gMh3g8RLvpAjMGxgfanB8w.png)
_**3** est supprimé donc **"hello world"** a maintenant l'index 2_

**Après le 2ème appel :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*6YWBPU0UsPeoJTcwn8-gWg.png)
_Cette fois, **"hello world"** est supprimé en tant qu'**index : 2**_

Cela peut continuer jusqu'à ce qu'il n'y ait plus d'index 2.

#### Ajout d'éléments

Pour ajouter des éléments, nous devons les donner en tant que 3ème, 4ème, 5ème paramètre (selon le nombre à ajouter) à la méthode **splice()** :

array.splice(index, number of elements, element, element);

Par exemple, j'ajoute **a** et **b** au tout début du tableau et je ne supprime rien :

`array.splice(0, 0, 'a', 'b');`

![Image](https://cdn-media-1.freecodecamp.org/images/1*E7TMFWTYGJDkuhG3VrTCKw.png)
_**a** et **b** ajoutés au début du tableau, aucun élément supprimé_

### Split()

Les méthodes **Slice()** et **splice()** sont pour les tableaux. La méthode **split()** est utilisée pour les **chaînes de caractères**. Elle divise une chaîne de caractères en sous-chaînes et les retourne sous forme de tableau. Elle prend 2 paramètres, et les deux sont **optionnels.**

`string.split(separator, limit);`

* **Separator :** Définit comment diviser une chaîne de caractères... par une virgule, un caractère, etc.
* **Limit :** Limite le nombre de divisions avec un nombre donné

La méthode **split()** ne fonctionne pas directement pour les **tableaux**. Cependant, nous pouvons d'abord convertir les éléments de notre tableau en une chaîne de caractères, puis nous pouvons utiliser la méthode **split()**.

Voyons comment cela fonctionne.

Tout d'abord, nous convertissons notre tableau en une chaîne de caractères avec la méthode **toString()** :

`let myString = array.toString();`

![Image](https://cdn-media-1.freecodecamp.org/images/1*JW9u0vQSmZM6wQ540w3eTg.png)

Maintenant, divisons **myString** par des **virgules**, limitons-les à **trois** sous-chaînes, et retournons-les sous forme de tableau :

`let newArray = myString.split(",", 3);`

![Image](https://cdn-media-1.freecodecamp.org/images/1*v53Ct4WVDXNsCjzDAtpc_g.png)
_Seuls les trois premiers éléments sont retournés_

Comme nous pouvons le voir, **myString** est divisé par des virgules. Puisque nous limitons la division à 3, seuls les trois premiers éléments sont retournés.

> _**NOTE :**_ Si nous avons une utilisation comme ceci : `_array.split("");_` alors chaque caractère de la chaîne sera divisé en sous-chaînes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*s7RYTgCHVGzZKXDJZYyjaQ.png)
_Chaque caractère est divisé un par un_

### Résumé :

#### Slice()

* Copie des éléments d'un tableau
* Les retourne sous forme de nouveau tableau
* Ne modifie pas le tableau original
* Commence à découper à partir de... jusqu'à l'index donné : **array.slice(from, until)**
* Slice n'inclut pas le paramètre d'index "until"
* Peut être utilisé à la fois pour les tableaux et les chaînes de caractères

#### Splice()

* Utilisé pour ajouter/supprimer des éléments d'un tableau
* Retourne un tableau des éléments supprimés
* Modifie le tableau
* Pour ajouter des éléments : **array.splice(index, number of elements, element)**
* Pour supprimer des éléments : **array.splice(index, number of elements)**
* Ne peut être utilisé que pour les tableaux

#### Split()

* Divise une chaîne de caractères en sous-chaînes
* Les retourne dans un tableau
* Prend 2 paramètres, tous deux optionnels : **string.split(separator, limit)**
* Ne modifie pas la chaîne de caractères originale
* Ne peut être utilisé que pour les chaînes de caractères

Il existe de nombreuses autres méthodes intégrées pour les tableaux et les chaînes de caractères JavaScript, qui facilitent le travail avec la programmation JavaScript. Ensuite, vous pouvez consulter mon nouvel article sur les [Méthodes de sous-chaînes JavaScript](https://www.freecodecamp.org/news/javascript-substring-examples-slice-substr-and-substring-methods-in-js/).

**Si vous voulez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !