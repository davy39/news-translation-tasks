---
title: JavaScript String Contains – Comment utiliser JS .includes()
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-05T16:46:38.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-contains-how-to-use-js-includes
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/amie-bell-XGqS569rdgk-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript String Contains – Comment utiliser JS .includes()
seo_desc: "In JavaScript you can use the .includes() method to see if one string is\
  \ found in another. But how does it work exactly?\nIn this article, I will walk\
  \ you through a few code examples of the JavaScript string method called .includes().\
  \ \nBasic .includes..."
---

En JavaScript, vous pouvez utiliser la méthode `.includes()` pour vérifier si une chaîne est trouvée dans une autre. Mais comment cela fonctionne-t-il exactement ?

Dans cet article, je vais vous guider à travers quelques exemples de code de la méthode de chaîne JavaScript appelée `.includes()`.

## Syntaxe de base de `.includes()`

Voici la syntaxe de base pour la méthode `.includes()` :

```js
str.includes(search-string, optional-position)
```

Le paramètre `search-string` est la chaîne que vous recherchez dans `str`.

Le paramètre `position` est un nombre optionnel pour la position de départ de la recherche dans `str`. Si le paramètre de position est omis, la valeur par défaut est zéro.

Si `search-string` est trouvé, il retournera `true`. Si `search-string` n'est pas trouvé, il retournera `false`.

## Exemples de code pour la méthode includes

Dans ce premier exemple, nous avons la phrase "I love freeCodeCamp". Nous voulons voir si le mot "love" est inclus dans cette phrase.

Dans le code, `str` serait "I love freeCodeCamp" et `search-string` serait "love".

```js
"I love freeCodeCamp".includes("love")
```

Puisque le mot "love" est inclus dans `str`, le code retournera `true`.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-9.35.42-PM.png)

### La méthode `.includes()` est-elle sensible à la casse ?

Si nous modifions notre `str` en "I LOVE freeCodeCamp" et que `search-string` est toujours "love", alors la valeur de retour serait `false`.

```js
"I LOVE freeCodeCamp".includes('love')
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-9.40.56-PM.png)

Cela retourne `false` car la méthode `.includes()` est sensible à la casse. "LOVE" n'est pas la même chose que "love".

### Comment utiliser le paramètre de position optionnel

Nous allons modifier notre exemple pour utiliser le paramètre de position. Nous voulons maintenant vérifier si "love" est trouvé dans "I love freeCodeCamp" lorsque la recherche commence à la position 1.

Rappelez-vous que les chaînes utilisent un indexage basé sur zéro, ce qui signifie que la première lettre "I" est à l'index 0.

Notre code retournera `true` car lorsque nous commençons la recherche à la position 1, le mot "love" n'apparaît pas avant la position 2, donc il est complètement contenu dans la chaîne.

La position 1 jusqu'à la fin de la phrase inclut ces caractères et espaces.

```
" love freeCodeCamp"
```

Rappelez-vous que les espaces dans les chaînes obtiennent une valeur d'index.

Voici à quoi ressemblerait notre code en utilisant le paramètre de position.

```js
"I love freeCodeCamp".includes('love', 1)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-9.55.34-PM.png)

Si nous changeons la position pour qu'elle soit 3, alors le retour serait `false`.

```js
"I love freeCodecamp".includes('love', 3)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-04-at-10.06.30-PM.png)

Cela retourne `false` car la position 3 est la lettre "o".

La position 3 jusqu'à la fin de la phrase inclut ces caractères et espaces.

```
"ove freeCodeCamp"
```

Vous pouvez voir que le mot (entier) "love" n'est pas présent dans cette chaîne.

## Conclusion

En JavaScript, vous pouvez utiliser la méthode `.includes()` pour vérifier si une chaîne est trouvée dans une autre.

Voici la syntaxe de base pour la méthode `.includes()`.

```js
str.includes(search-string, optional-position)
```

Si `search-string` est trouvé, il retournera `true`. Si `search-string` n'est pas trouvé, il retournera `false`.

La méthode `.includes()` est sensible à la casse, ce qui signifie que si `search-string` ne correspond pas exactement à la casse dans `str`, elle retournera `false`.

Le paramètre `position` est un nombre optionnel pour la position de départ de la recherche dans `str`. Si le paramètre de position est omis, la valeur par défaut est zéro.

J'espère que vous avez apprécié cet article sur la méthode `.includes()` et bonne chance dans votre parcours JavaScript.