---
title: Symbole de coche – HTML pour Unicode de coche
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-12T19:17:04.000Z'
originalURL: https://freecodecamp.org/news/checkmark-symbol-html-for-checkmark-unicode
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/checkmark.png
tags:
- name: HTML
  slug: html
- name: unicode
  slug: unicode
seo_title: Symbole de coche – HTML pour Unicode de coche
seo_desc: "If you take a look at your keyboard, you'll see that there’s no key for\
  \ typing a checkmark. \nYou could decide to copy the checkmark symbol from the internet\
  \ and paste it directly into your HTML code, but an easier way to do it is to use\
  \ the appropria..."
---

Si vous regardez votre clavier, vous verrez qu'il n'y a pas de touche pour taper une coche. 

Vous pourriez décider de copier le symbole de coche depuis Internet et de le coller directement dans votre code HTML, mais une méthode plus simple consiste à utiliser le caractère Unicode approprié ou l'entité de caractère HTML.

Si vous vous demandez ce que sont Unicode et les entités de caractères HTML, ce sont tous deux des morceaux de texte qui représentent différents emojis, symboles et caractères.

Dans vos projets web, vous pourriez vouloir afficher une coche pour indiquer un consentement ou un accord. Donc, dans cet article, je vais vous montrer comment utiliser le caractère Unicode et l'entité de caractère HTML appropriés pour intégrer des coches dans vos projets web. Je vais également vous montrer 4 autres variations du symbole de coche.

## Les caractères Unicode et HTML pour les coches
Le caractère Unicode pour afficher une coche est `U+2713`. Si vous décidez d'utiliser cet Unicode pour afficher une coche en HTML et que vous le tapez comme tel, ce que vous tapez est affiché comme ceci :

```html
 <h1>Languages of the web</h1>
 <h3>U+2713 HTML</h3>
 <h3>U+2713 CSS</h3>
 <h3>U+2713 JavaScript</h3>
 <h3>U+2713 PHP</h3>
```

**Alors, comment utiliser l'Unicode U+2713 pour afficher le symbole de coche ?**

Supprimez le `U+` et remplacez-le par un esperluette (`&`), un signe dièse (#) et `x`. Ensuite, tapez 2713, puis un point-virgule. Cela devient `&#x2713;`.

```html
 <h1>Languages of the web</h1>
 <h3>&#x2713; HTML</h3>
 <h3>&#x2713; CSS</h3>
 <h3>&#x2713; JavaScript</h3>
 <h3>&#x2713; PHP</h3>
```
![ss2-3](https://www.freecodecamp.org/news/content/images/2022/04/ss2-3.png)

Vous pouvez également utiliser l'entité de caractère HTML pour une coche afin d'afficher le symbole de coche. Il s'agit de `&#10003;` ou `&check;` :

```html
<h1>Languages of the web</h1>
<h3>&check; HTML</h3>
<h3>&#10003; CSS</h3>
<h3>&#10003; JavaScript</h3>
<h3>&check; PHP</h3>
```
![ss2-3](https://www.freecodecamp.org/news/content/images/2022/04/ss2-3.png)

## Autres variations du symbole de coche
Outre le traditionnel `U+2713`, `&#10003;` ou `&check;`, il existe d'autres variations telles que :

### `&#10004;` pour une coche plus épaisse
```html
<h1>Languages of the web</h1>
<h3>&#10004; HTML</h3>
<h3>&#10004; CSS</h3>
<h3>&#10004; JavaScript</h3>
<h3>&#10004; PHP</h3>
```
![ss3-2](https://www.freecodecamp.org/news/content/images/2022/04/ss3-2.png)

### U+2705 – `&#x2705;` pour une coche blanche épaisse
```html
<h1>Languages of the web</h1>
<h3>&#x2705; HTML</h3>
<h3>&#x2705; CSS</h3>
<h3>&#x2705; JavaScript</h3>
<h3>&#x2705; PHP</h3>
```
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/04/ss4-1.png)

### U+2611 – `&#x2611;` pour une coche de bulletin de vote
```html
<h1>Languages of the web</h1>
<h3>&#x2611; HTML</h3>
<h3>&#x2611; CSS</h3>
<h3>&#x2611; JavaScript</h3>
<h3>&#x2611; PHP</h3>
```
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/04/ss5-1.png)

### U+221A – `&#x221A;` pour une coche en forme de racine carrée
```html
<h1>Languages of the web</h1>
<h3>&#x221A; HTML</h3>
<h3>&#x221A; CSS</h3>
<h3>&#x221A; JavaScript</h3>
<h3>&#x221A; PHP</h3>
```
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/04/ss6-1.png)

## Conclusion
Cet article vous a montré la chaîne Unicode pour une coche, comment l'utiliser, ainsi que d'autres variations de celle-ci. 

Vous avez également appris l'entité de caractère HTML équivalente pour le symbole de coche, au cas où vous ne souhaiteriez pas l'afficher avec la chaîne Unicode.

Maintenant, allez insérer quelques coches dans votre code.