---
title: Python Bytes to String – Comment convertir une chaîne en bytes et vice versa
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-04-16T20:07:39.959Z'
originalURL: https://freecodecamp.org/news/python-bytes-to-string-code-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/zGuBURGGmdY/upload/6d5b13a8926b01576cba45ee0d72bfc8.jpeg
tags:
- name: Python
  slug: python
seo_title: Python Bytes to String – Comment convertir une chaîne en bytes et vice
  versa
seo_desc: 'You can use bytes in Python to represent data in binary form. In this article,
  you''ll learn how to convert bytes to a string, and vice versa.

  Before we look at the conversions, let''s talk about how bytes work in Python. You
  can skip to the next secti...'
---

Vous pouvez utiliser les bytes en Python pour représenter des données sous forme binaire. Dans cet article, vous apprendrez à convertir des bytes en chaîne de caractères, et vice versa.

Avant d'examiner les conversions, parlons de la manière dont les bytes fonctionnent en Python. Vous pouvez passer à la section suivante si vous comprenez déjà cela, ou si vous êtes simplement intéressé par les conversions.

## Comment fonctionnent les Bytes en Python

Vous pouvez créer des littéraux de bytes en préfixant la notation `b`. Cela indique à l'interpréteur Python qu'un ensemble de caractères doit être traité comme des bytes. Voici un exemple :

```python
byte_data = b'Hello'
```

Dans le code ci-dessus, nous avons préfixé `b` juste avant la valeur de la chaîne : `b'Hello'`. Si vous imprimez les caractères de la chaîne, vous obtiendrez une valeur binaire pour chacun. C'est-à-dire :

```python
byte_data = b'Hello'
print(byte_data[0]) # 72
```

Ainsi, au lieu de "H", 72 a été retourné. Si vous continuez à imprimer la valeur de chaque index dans la séquence, vous devriez obtenir leurs valeurs binaires :

```python
byte_data = b'Hello'
print(byte_data[0]) # 72 => H
print(byte_data[1]) # 101 => e
print(byte_data[2]) # 108 => l
print(byte_data[3]) # 108 => l
print(byte_data[4]) # 111 => 0
```

Maintenant, parlons de la manière de convertir une chaîne en bytes, et comment convertir des bytes en chaîne.

# Comment convertir une chaîne en bytes en Python

Vous pouvez utiliser la méthode `encode()` pour convertir une chaîne en bytes en Python. La méthode encode simplement une chaîne en utilisant un encodage spécifique comme UTF-8, ASCII, etc.

Voici un exemple :

```python
string_data = "Hello"
print(string_data[0]) # H
```

Dans le code ci-dessus, nous avons créé une chaîne appelée `string_data` avec une valeur de "Hello". Nous avons également imprimé le premier caractère de la chaîne, qui est "H".

Maintenant, convertissons la chaîne en bytes en utilisant la méthode `encode()` :

```python
string_data = "Hello"
byte_data = string_data.encode('utf-8')
print(byte_data[0]) # 72
```

Nous avons converti la variable `string_data` en bytes en utilisant la méthode `encode()` qui a pris "utf-8" comme paramètre. Nous avons stocké cette conversion dans la variable `byte_data` : `byte_data = string_data.encode('utf-8')`.

Enfin, nous avons imprimé le premier caractère de la variable `byte_data` et obtenu une valeur binaire : `print(byte_data[0]) # 72`.

# Comment convertir des bytes en chaîne en Python

Vous pouvez utiliser la méthode `decode()` pour convertir des bytes en chaîne en Python. Cela fonctionne comme la méthode `encode()` : attachez la variable à convertir en utilisant la notation par points et spécifiez le type d'encodage comme paramètre de la méthode.

Voici un exemple :

```python
byte_data = b'Hello'
string_data = byte_data.decode('utf-8')
print(string_data[0]) # H
```

Dans le code ci-dessus, nous avons créé un objet bytes appelé `byte_data`.

En utilisant la méthode `decode()`, nous l'avons converti en chaîne et l'avons stocké dans une variable `string_data` : `string_data = byte_data.decode('utf-8')`.

Lorsque vous imprimez les caractères de la variable `string_data`, vous devriez obtenir des caractères de chaîne au lieu de valeurs binaires : `print(string_data[0]) # H`

# Conclusion

Dans cet article, vous avez appris à utiliser les bytes en Python. Vous avez également appris deux méthodes de conversion :

* Comment convertir une chaîne en bytes en utilisant la méthode `encode()`.

* Comment convertir des bytes en chaîne en utilisant la méthode `decode()`.

Bon codage !