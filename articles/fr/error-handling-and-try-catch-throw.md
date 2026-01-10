---
title: 'JavaScript Try Catch : Gestion des exceptions expliquée'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T17:19:00.000Z'
originalURL: https://freecodecamp.org/news/error-handling-and-try-catch-throw
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d85740569d1a4ca3834.jpg
tags:
- name: Exception Handling
  slug: exception-handling
- name: JavaScript
  slug: javascript
seo_title: 'JavaScript Try Catch : Gestion des exceptions expliquée'
seo_desc: "The try...catch..finally statement specifies a block of code to try along\
  \ with a response should an error occur. The try statement contains one or more\
  \ try blocks, and ends with at least one catch and/or a finally clause.\ntry...catch:\n\
  try {\n   throw ..."
---

L'instruction `try...catch..finally` spécifie un bloc de code à essayer ainsi qu'une réponse en cas d'erreur. L'instruction `try` contient un ou plusieurs blocs `try`, et se termine par au moins une clause `catch` et/ou une clause `finally`.

### `try...catch` :

```javascript
try {
   throw new Error('my error');
} catch (err) {
  console.error(err.message);
}

// Sortie : my error
```

### `try...finally` :

```javascript
try {
   throw new Error('my error');
} finally {
  console.error('finally');
}

// Sortie : finally
```

Lorsque vous n'utilisez pas d'instruction `catch`, l'erreur n'est pas "attrapée", même si le code dans le bloc `finally` est exécuté. Au lieu de cela, l'erreur sera transmise au bloc `try` supérieur (ou au bloc principal).

### `try...catch...finally` :

```javascript
try {
   throw new Error('my error');
} catch (err) {
  console.error(err.message);
} finally {
  console.error('finally');
}

// Sortie :
// my error
// finally
```

**Utilisation typique :**

```javascript
try {
   openFile(file);
   readFile(file)
} catch (err) {
  console.error(err.message);
} finally {
  closeFile(file);
}
```

### `try...catch` imbriqués :

Vous pouvez également :

* Imbriquer une instruction `try-catch` dans un bloc `try`.

Vous pouvez imbriquer une instruction `try...catch` dans un bloc `try`. Par exemple, pour transmettre une erreur vers le haut :

```javascript
try {
  try {
    throw new Error('my error');
  } catch (err) {
    console.error('inner', err.message);
    throw err;
  } finally {
    console.log('inner finally');
  }
} catch (err) {
  console.error('outer', err.message);
}

// Sortie : 
// inner my error 
// inner finally 
// outer my error
```