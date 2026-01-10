---
title: Modèle RegEx d'URL – Comment écrire une expression régulière pour une URL
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-15T12:22:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-regular-expression-for-a-url
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/urlRegEx.png
tags:
- name: Regex
  slug: regex
seo_title: Modèle RegEx d'URL – Comment écrire une expression régulière pour une URL
seo_desc: 'Regular expressions provide a powerful and flexible way to define patterns
  and match specific strings, be it usernames, passwords, phone numbers, or even URLs.

  In this article, I''ll show you the fundamentals of crafting a regular expression
  for URLs....'
---

Les expressions régulières offrent un moyen puissant et flexible de définir des motifs et de faire correspondre des chaînes spécifiques, qu'il s'agisse de noms d'utilisateur, de mots de passe, de numéros de téléphone ou même d'URL.

Dans cet article, je vais vous montrer les bases de la création d'une expression régulière pour les URL. Que vous ayez besoin de valider les entrées utilisateur, d'extraire des composants des URL ou d'effectuer d'autres tâches liées aux URL, comprendre comment construire une regex pour les URL peut grandement améliorer la validation des URL dans vos applications.

Tout d'abord, laissez-moi vous montrer ce qu'est une URL.


## Ce que nous allons couvrir
- [Qu'est-ce qu'une URL ?](#heading-quest-ce-quune-url)
- [Comment écrire une expression régulière pour une URL](#heading-comment-ecrire-une-expression-reguliere-pour-une-url)
- [Tester la RegEx avec JavaScript](#heading-tester-la-regex-avec-javascript)
- [Conclusion](#heading-conclusion)


## Qu'est-ce qu'une URL ?
Une URL, abréviation de Uniform Resource Locator, est une chaîne qui identifie l'emplacement d'une ressource sur le web. Elle se compose généralement de divers composants, notamment :

- le protocole – par exemple, HTTP ou HTTPS
- le nom de domaine – par exemple, freecodecamp.org
- le sous-domaine – par exemple, Chinese.freecodecamp.org
- le numéro de port – 3000, 5000, 4000, et plus
- le chemin – par exemple, `freecodecamp.org/news`
- les paramètres de requête – par exemple, `https://example.com/search?q=apple&category=fruits`


## Comment écrire une expression régulière pour une URL
Une URL peut être une URL de base (sans sous-domaine, chemin ou paramètre de requête). Elle peut également contenir un sous-domaine, un chemin ou d'autres composants. En raison de cela, vous devez adapter votre expression régulière à la manière dont vous attendez l'URL.

Si les utilisateurs saisissent une URL de base, vous devez adapter votre regex pour cela, et si vous attendez une URL qui a un sous-domaine ou un chemin, vous devez adapter votre regex de cette manière. Si vous le souhaitez, vous pouvez également écrire une regex complexe qui peut accepter une URL sous n'importe quelle forme. Ce n'est pas impossible.

Voici un motif regex qui correspond à une URL de base de n'importe quelle extension de domaine :

```bash
(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?
```

Cela correspondrait à des domaines comme `https://www.freecodecamp.org`, `http://www.freecodecamp.org/`, `freeCodeCamp.org`, `google.co.uk`, `facebook.net`, `google.com.ng`, `google.com.in`, et de nombreuses autres URL de base.


Le motif ci-dessous correspond à n'importe quelle URL avec un chemin :
```bash
(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?\/[a-zA-Z0-9]{2,}
```

Cela inclut des URL comme `https://www.freecodecamp.org/news`,
`http://www.freecodecamp.org/ukrainian`, et d'autres

Si vous souhaitez faire correspondre une URL avec un sous-domaine, le motif ci-dessous peut le faire pour vous :
```js
(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?
```

Cela correspondrait à des sous-domaines comme `https://www.chinese.freecodecamp.org`,
`chinese.freecodecamp.org`, `https://chinese.freecodecamp.org`, et d'autres.

Si vous voulez une regex qui correspond à n'importe quelle URL qui est de base, a un sous-domaine ou un chemin, vous pouvez combiner tous les motifs que je vous ai montrés comme ceci :

```bash
(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})? 
```

Ce n'est pas la plus belle façon de faire les choses, mais cela fonctionne :
![ss1-5](https://www.freecodecamp.org/news/content/images/2023/05/ss1-5.png)

## Tester la RegEx avec JavaScript
En testant la regex en utilisant la méthode `test()` de JavaScript RegEx, j'ai obtenu `true` :

```js
const pattern =
  /(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?/g;

const urls = `https://www.freecodecamp.org
http://www.freecodecamp.org
google.co.uk
facebook.net
google.com.ng
google.com.in
freecodecamp.org
yoruba.freecodecamp.org
freecodecamp.org/yoruba

http://www.freecodecamp.org/news
freecodecamp.org/news

chinese.freecodecamp.org
https://chinese.freecodecamp.org`;

console.log(pattern.test(urls)); //true;
```

![ss2-2](https://www.freecodecamp.org/news/content/images/2023/05/ss2-2.png)


## Conclusion
Les motifs d'expressions régulières pour faire correspondre une URL dépendent de votre besoin spécifique – puisque les URL peuvent être sous diverses formes. Ainsi, lors de l'écriture des motifs pour l'URL, vous devez les écrire pour qu'ils conviennent à la manière dont vous attendez l'URL.

Écrire une regex qui correspond à tous les types d'URL fonctionne, mais ce n'est pas la meilleure façon de faire car elle est très difficile à lire et à déboguer.