---
title: Comment trier un tableau d'objets par nom de propriété en JavaScript
subtitle: ''
author: Kaushal Joshi
co_authors: []
series: null
date: '2024-01-29T14:45:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-array-of-objects-by-property-name-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/How-to-sort-an-array-of-objects-by-object-s-property-name-in-JavaScript.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment trier un tableau d'objets par nom de propriété en JavaScript
seo_desc: 'In this tutorial, you''ll learn about one of the most common operations
  you''ll perform while working with JavaScript: sorting an array of objects by property
  name.

  Basic Array Concepts

  Let''s review some basic JavaScript concepts before delving deeper ...'
---

Dans ce tutoriel, vous apprendrez l'une des opérations les plus courantes que vous effectuerez en travaillant avec JavaScript : le tri d'un tableau d'objets par nom de propriété.

## Concepts de base des tableaux

Révisons quelques concepts de base de JavaScript avant d'approfondir le sujet afin que vous ayez les informations de base nécessaires.

### Tableaux JavaScript et tableau d'objets

Les tableaux sont l'un des éléments fondamentaux de tout langage de programmation. Ils sont la structure de données la plus simple, mais ils sont si puissants qu'ils sont la structure de données sous-jacente de nombreuses applications que nous utilisons aujourd'hui.

```javascript
const arr = ["apple", "banana", "orange", "mango"]
```

L'utilisation la plus typique des tableaux est d'envoyer des données d'une machine à une autre. Par machine, j'entends un client, un serveur, un serveur de base de données, etc. Ces données sont souvent une collection de enregistrements similaires regroupés dans un tableau. Chaque enregistrement est représenté par un objet, qui est un élément de tableau.

Ces tableaux sont appelés tableaux d'objets. Voici un exemple de tableau d'objets en JavaScript :

```javascript
const response = [
    {
        id: 1,
        name: "John",
        age: 41
    },
    {
        id: 2,
        name: "Zack",
        age: 35
    },
    {
        id: 3, 
        name: "Peter",
        age: 47
    }
]
```

Comme vous pouvez le voir, il s'agit simplement d'un tableau. Et chaque élément du tableau est un objet. D'où le nom, **tableau d'objets**.

Vous pouvez manipuler un tableau d'objets comme n'importe quel autre tableau et utiliser les fonctions de tableau intégrées. Mais il existe certaines situations où l'utilisation de fonctions intégrées n'est pas réalisable, et vous devez apporter certaines modifications pour atteindre l'objectif.

### Clés dans les objets JavaScript

Les objets en JavaScript sont des collections de paires clé-valeur, chaque clé identifiant une valeur spécifique. Pensez aux clés comme aux étiquettes que vous attribuez pour récupérer des informations dans un dictionnaire. Par exemple :

```javascript
const person = {
    id: 1,
    name: "John",
    age: 41
};
```

Dans l'exemple ci-dessus, `id`, `name` et `age` sont des clés tandis que '1', 'John' et '25' sont leurs valeurs correspondantes. Lorsque nous parlons de trier un tableau d'objets en fonction d'une clé, nous faisons référence au tri des éléments du tableau en fonction des valeurs associées à une propriété spécifique au sein de chaque objet.

### Détermination du type de données d'une propriété

Avant de trier, il est crucial de comprendre le type de données de la propriété que vous souhaitez utiliser comme clé de tri. JavaScript a différentes règles de tri pour les valeurs numériques et les chaînes de caractères. Connaître le type de données nous aide à choisir la méthode de tri appropriée.

Si vous n'êtes pas sûr du type de données, vous pouvez soit vérifier le type de données avec l'opérateur `typeof`, soit convertir le type dans celui que vous souhaitez.

```xml
// Vérification si le type est celui attendu
if(typeof obj.name === "string") {
	// Faire quelque chose
}

// Conversion du type de la propriété
const string = String(obj.propertyName)
const number = Number(obj.propertyName)
```

## Comment trier un tableau d'objets avec une clé spécifique de l'objet

Nous devons connaître deux choses avant de trier un tableau :

1. **Type de données :** Comprendre le type de données de la valeur que nous voulons trier.
    
2. **Ordre de tri :** Déterminer si nous voulons trier dans l'ordre croissant ou décroissant.
    

Nous allons couvrir divers cas d'utilisation pour avoir une vue d'ensemble de ces concepts.

### Comment trier un tableau en fonction des valeurs numériques

Commençons par trier un tableau en fonction des valeurs numériques, spécifiquement la propriété age. Notre objectif est d'avoir les éléments du tableau (c'est-à-dire les objets) triés dans l'ordre croissant en fonction de la propriété `age`. La méthode intégrée `sort()` sera notre outil de choix :

```javascript
response.sort((a, b) => a.age - b.age)
```

Et c'est tout ! Les objets du tableau sont triés par la propriété `age`. Vous pouvez confirmer cela en enregistrant la sortie dans la console :

```javascript
[
  { id: 2, name: 'Zack', age: 35 },
  { id: 1, name: 'John', age: 41 },
  { id: 3, name: 'Peter', age: 47 }
]
```

Si vous voulez trier dans l'ordre décroissant, vous devez simplement changer la position des variables à l'intérieur de la fonction.

```javascript
response.sort((a, b) => b.age - a.age)
```

Ainsi, le tableau sera trié dans l'ordre décroissant de `age`.

```javascript
[
  { id: 3, name: 'Peter', age: 47 },
  { id: 1, name: 'John', age: 41 },
  { id: 2, name: 'Zack', age: 35 }
]
```

Trier les nombres dans un tableau est facile – essayons maintenant quelque chose un peu plus difficile : trier en fonction des valeurs de chaîne de caractères.

### Comment trier un tableau en fonction des valeurs de chaîne de caractères

J'ai eu beaucoup de mal dans mes premiers jours à effectuer cette opération. Finalement, j'ai trouvé la méthode la plus facile pour le faire. Similaire à l'exemple précédent, ici nous voulons trier les objets en fonction des valeurs de chaîne de caractères.

Nous allons utiliser une fonction de chaîne intégrée `localCompare()`. Elle est utilisée pour comparer des chaînes de caractères en fonction d'un ordre sensible à la langue. Écrivons la fonction `sort()` avec l'aide de cette fonction :

```javascript
response.sort((a, b) => a.name.localeCompare(b.name));
```

```javascript
[
  { id: 1, name: 'John', age: 41 },
  { id: 3, name: 'Peter', age: 47 },
  { id: 2, name: 'Zack', age: 35 }
]
```

Comme prévu, les éléments du tableau seront triés en fonction de la propriété `name` à l'intérieur de chaque élément objet.

Trier dans l'ordre décroissant est également un jeu d'enfant :

```javascript
response.sort((a, b) => b.name.localeCompare(a.name));
```

La sortie sera comme suit :

```javascript
[
  { id: 2, name: 'Zack', age: 35 },
  { id: 3, name: 'Peter', age: 47 },
  { id: 1, name: 'John', age: 41 }
]
```

## Cas particuliers à considérer

Lors du tri de tableaux d'objets, il est essentiel de traiter les cas particuliers potentiels.

### La clé doit être présente dans tous les objets

Assurez-vous que la clé utilisée pour le tri existe dans tous les objets. Même si un seul objet manque la clé, le tableau original est retourné inchangé. Voici comment vous pouvez gérer un tel cas :

```javascript
if (array.every(obj => 'age' in obj)) {
    array.sort((a, b) => a.age - b.age);
} else {
    console.error("Certains objets manquent de la clé 'age'. Le tri n'est pas réalisable.");
}
```

### Les valeurs null ou undefined ne doivent pas être présentes

La clé que vous souhaitez utiliser pour le tri ne doit pas être `null` ou `undefined`. Vous pouvez passer une chaîne vide au lieu de la clé si elle est une valeur fausse.

```javascript
array.sort((a, b) => (a.name || "").localeCompare(b.name || ""));
```

### Toutes les valeurs doivent être des chaînes pour les comparaisons de chaînes

Lors du tri d'objets en fonction d'une clé particulière, si la clé est supposée être une chaîne, assurez-vous que la clé a le type de données String dans tous les cas. Une solution pour éviter les bugs potentiels est de convertir la clé en chaîne dans la fonction `sort()`.

```javascript
array.sort((a, b) => String(a.name).localeCompare(String(b.name)));
```

### Sensibilité locale

Lors de la manipulation de propriétés de chaîne, tenez compte de la sensibilité à la langue et à la casse. Fournissez des informations appropriées sur les locales et les options pour `localeCompare()`.

```javascript
array.sort((a, b) => a.title.localeCompare(b.title, 'en', { sensitivity: 'accent' }));
```

## Conclusion

Comprendre les opérations sur les tableaux augmentera l'efficacité de votre code et améliorera les performances de votre application. Dans cet article, vous avez appris comment trier des tableaux d'objets en fonction d'une clé à l'intérieur de l'objet.

J'espère que vous avez trouvé cet article utile. Si c'est le cas, n'oubliez pas de le partager avec vos amis afin que d'autres puissent en bénéficier. Si vous connaissez une meilleure méthode pour trier les tableaux, faites-le moi savoir ! J'adorerais apprendre.

Je suis le plus actif sur [Twitter (maintenant **X**)](https://twitter.com/clumsy_coder) si vous voulez dire bonjour !

### Lectures complémentaires

* [Fonction JavaScript sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
    
* [Objet Intl.Collator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Collator)
    
* [Fonction JavaScript localeCompare()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare)
    

Jusqu'à la prochaine fois, bon codage :)