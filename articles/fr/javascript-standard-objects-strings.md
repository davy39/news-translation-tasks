---
title: 'Objets standard JavaScript : Chaînes de caractères'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-standard-objects-strings
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d18740569d1a4ca35df.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: 'Objets standard JavaScript : Chaînes de caractères'
seo_desc: 'Surely you''ve heard that, in JavaScript, everything is an object. Strings,
  numbers, functions, arrays, and, well, objects, are considered objects.

  In this tutorial we''ll take a deep dive into the String "global" or "standard built-in"
  object, along w...'
---

Sûrement vous avez entendu dire que, en JavaScript, tout est un objet. Les chaînes de caractères, les nombres, les fonctions, les tableaux, et, bien sûr, les objets, sont considérés comme des objets.

Dans ce tutoriel, nous allons plonger en profondeur dans l'objet **String** "global" ou "standard intégré", ainsi que les méthodes qui lui sont associées.

## String.prototype.toUpperCase()

La méthode JavaScript `String.toUpperCase()` retourne la même chaîne sur laquelle elle a été appelée, mais en caractères majuscules.

### Syntaxe

```text
str.toUpperCase()
```

### Exemples

```text
console.log("hello world".toUpperCase()); // "HELLO WORLD"
```

## String.prototype.fromCharCode()

La méthode `String.fromCharCode()` retourne une chaîne créée en utilisant la séquence spécifiée de valeurs Unicode.

### Syntaxe

```text
String.fromCharCode(num1, num2...)
```

### **Paramètres**

Une séquence de nombres qui représentent des valeurs Unicode.

### Exemples

```text
String.fromCharCode(65, 66, 67);  // "ABC"

var test = String.fromCharCode(112, 108, 97, 105, 110);
document.write(test);

// Sortie : plain
```