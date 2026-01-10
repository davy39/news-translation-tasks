---
title: Exemples de sous-chaînes JavaScript - Méthodes Slice, Substr et Substring en
  JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-22T20:38:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-substring-examples-slice-substr-and-substring-methods-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c0d740569d1a4ca2fa6.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Exemples de sous-chaînes JavaScript - Méthodes Slice, Substr et Substring
  en JS
seo_desc: 'By Cem Eygi

  In daily programming, we often need to work with strings. Fortunately, there are
  many built-in methods in JavaScript that help us while working with arrays, strings
  and other data types. We can use these methods for various operations lik...'
---

Par Cem Eygi

En programmation quotidienne, nous devons souvent travailler avec des chaînes de caractères. Heureusement, il existe de nombreuses méthodes intégrées en JavaScript qui nous aident à travailler avec des tableaux, des chaînes et d'autres types de données. Nous pouvons utiliser ces méthodes pour diverses opérations comme la recherche, le remplacement, la concaténation de chaînes, et ainsi de suite.

Obtenir une sous-chaîne à partir d'une chaîne est l'une des opérations les plus courantes en JavaScript. Dans cet article, vous allez apprendre comment obtenir une sous-chaîne en utilisant 3 méthodes intégrées différentes. Mais d'abord, laissez-moi expliquer brièvement ce qu'est une sous-chaîne.

### Qu'est-ce qu'une sous-chaîne ?

Une sous-chaîne est un sous-ensemble d'une autre chaîne :

```javascript
"I am learning JavaScript and it is cool!"  -->  Chaîne originale

"I am learning JavaScript"  -->  Sous-chaîne

"JavaScript is cool!"  -->  Une autre sous-chaîne
```

Comme dans l'exemple ci-dessus, dans certains cas, nous devons obtenir une ou plusieurs sous-chaînes à partir d'une phrase complète ou d'un paragraphe. Voyons maintenant comment faire cela en JavaScript de 3 manières différentes.

**Vous pouvez également regarder la version vidéo des exemples d'utilisation ici :**

%[https://youtu.be/8um4gEiv5mg]

## 1. La méthode substring()

Commençons par la méthode substring(). Cette méthode obtient essentiellement une partie de la chaîne originale et la retourne sous forme de nouvelle chaîne. La méthode substring attend deux paramètres :

```javascript
string.substring(startIndex, endIndex);
```

* **startIndex** : représente le point de départ de la sous-chaîne
* **endIndex** : représente le point de fin de la sous-chaîne (optionnel)

Voyons l'utilisation dans un exemple. Supposons que nous avons la chaîne d'exemple suivante :

```javascript
const myString = "I am learning JavaScript and it is cool!";
```

Maintenant, si nous définissons le startIndex à 0 et le endIndex à 10, nous obtiendrons les 10 premiers caractères de la chaîne originale :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-21-19.17.10.png)
_**L'index du premier caractère est toujours 0**_

Cependant, si nous définissons uniquement un index de départ et aucun index de fin pour cet exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-21-19.16.46.png)

Alors nous obtenons une sous-chaîne commençant par le 6ème caractère jusqu'à la fin de la chaîne originale.

**Quelques points supplémentaires :**

* Si startIndex = endIndex, la méthode substring retourne une chaîne vide
* Si startIndex et endIndex sont tous deux supérieurs à la longueur de la chaîne, elle retourne une chaîne vide
* Si startIndex > endIndex, alors la méthode substring échange les arguments et retourne une sous-chaîne, en supposant que endIndex > startIndex

## 2. La méthode slice()

La méthode slice() est similaire à la méthode substring() et elle retourne également une sous-chaîne de la chaîne originale. La méthode slice attend également les deux mêmes paramètres :

```javascript
string.slice(startIndex, endIndex);
```

* **startIndex** : représente le point de départ de la sous-chaîne
* **endIndex** : représente le point de fin de la sous-chaîne (optionnel)

#### **Les points communs des méthodes substring() et slice() :**

* Si nous ne définissons pas d'index de fin, alors nous obtenons une sous-chaîne commençant par le numéro d'index donné jusqu'à la fin de la chaîne originale :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-01.03.15.png)

* Si nous définissons à la fois le startIndex et le endIndex, alors nous obtiendrons les caractères entre les numéros d'index donnés de la chaîne originale :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-01.03.43.png)

* Si startIndex et endIndex sont supérieurs à la longueur de la chaîne, elle retourne une chaîne vide

#### **Différences de la méthode slice() :**

* Si startIndex > endIndex, la méthode slice() retourne une chaîne vide
* Si startIndex est un nombre négatif, alors le premier caractère commence à partir de la fin de la chaîne (inverse) :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-15.54.09.png)

> **Note :** Nous pouvons également utiliser la méthode slice() pour les tableaux JavaScript. Vous pouvez trouver [ici mon autre article](https://www.freecodecamp.org/news/lets-clear-up-the-confusion-around-the-slice-splice-split-methods-in-javascript-8ba3266c29ae/) sur la méthode slice pour voir l'utilisation pour les tableaux.

## 3. La méthode substr()

[Selon les documents Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr), la méthode substr() est considérée comme une fonction héritée et son utilisation doit être évitée. Mais je vais tout de même expliquer brièvement ce qu'elle fait car vous pourriez la voir dans des projets plus anciens.

La méthode substr() retourne également une sous-chaîne de la chaîne originale et attend deux paramètres comme suit :

```javascript
string.substring(startIndex, length);
```

* **startIndex** : représente le point de départ de la sous-chaîne
* **length** : nombre de caractères à inclure (optionnel)

Vous pouvez voir la différence ici : la méthode substr() attend le deuxième paramètre comme une longueur au lieu d'un endIndex :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-00.40.29-2.png)

Dans cet exemple, elle compte essentiellement 5 caractères en commençant par le startIndex donné et les retourne sous forme de sous-chaîne.

Cependant, si nous ne définissons pas le deuxième paramètre, elle retourne jusqu'à la fin de la chaîne originale (comme le font les deux méthodes précédentes) :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Ekran-Resmi-2020-03-22-00.40.23.png)

> **Note :** Les 3 méthodes retournent la sous-chaîne sous forme de nouvelle chaîne et elles ne modifient pas la chaîne originale.

## Conclusion

Voici donc les 3 méthodes différentes pour obtenir une sous-chaîne en JavaScript. Il existe de nombreuses autres méthodes intégrées en JS qui nous aident vraiment beaucoup lorsque nous traitons de diverses choses en programmation. Si vous trouvez cet article utile, veuillez le partager sur les réseaux sociaux.

**Si vous souhaitez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !