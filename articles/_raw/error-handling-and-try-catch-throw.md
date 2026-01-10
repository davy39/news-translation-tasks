---
title: 'JavaScript Try Catch: Exception Handling Explained'
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
seo_title: null
seo_desc: "The try...catch..finally statement specifies a block of code to try along\
  \ with a response should an error occur. The try statement contains one or more\
  \ try blocks, and ends with at least one catch and/or a finally clause.\ntry...catch:\n\
  try {\n   throw ..."
---

The `try...catch..finally` statement specifies a block of code to try along with a response should an error occur. The `try` statement contains one or more `try` blocks, and ends with at least one `catch` and/or a `finally` clause.

### `try...catch`:

```javascript
try {
   throw new Error('my error');
} catch (err) {
  console.error(err.message);
}

// Output: my error
```

### `try...finally`:

```javascript
try {
   throw new Error('my error');
} finally {
  console.error('finally');
}

// Output: finally
```

When you don't use a `catch` statement, the error is not "caught", even though the code in the `finally` block is executed. Instead, the error will continue to the upper `try` block (or main block).

### `try...catch...finally`:

```javascript
try {
   throw new Error('my error');
} catch (err) {
  console.error(err.message);
} finally {
  console.error('finally');
}

// Output:
// my error
// finally
```

**Typical usage:**

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

### Nested `try...catch`:

You can also:

* Nest a `try-catch` statement inside a `try` block.

You can nest a `try...catch` statement within a `try` block. For example, to throw an error upwards:

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

// Output: 
// inner my error 
// inner finally 
// outer my error
```

