---
title: Comment formater des dates en JavaScript avec une seule ligne de code
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2021-07-03T06:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-dates-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Formatting-Date-in-JavaScript-with-1-line-of-code.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment formater des dates en JavaScript avec une seule ligne de code
seo_desc: 'For a long time, I''ve used libraries like Date-fns whenever I need to
  format dates in JavaScript. But it gets really weird whenever I do this in small
  projects that require simple date formats which JavaScript offers by default.

  I discovered that mos...'
---

Pendant longtemps, j'ai utilisé des bibliothèques comme `Date-fns` chaque fois que j'avais besoin de formater des dates en JavaScript. Mais cela devient vraiment étrange chaque fois que je le fais dans de petits projets qui nécessitent des formats de date simples que JavaScript offre par défaut.

J'ai découvert que la plupart des développeurs font cela beaucoup. Et je pensais que c'était la meilleure façon jusqu'à ce que je réalise récemment que **nous n'avons pas toujours besoin d'utiliser des bibliothèques** pour formater des dates en JavaScript.

Au cas où vous seriez curieux d'essayer cela, voici le code :👋

```javascript
new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short", day:"numeric"}) 
// "Friday, Jul 2, 2021"
```

Après avoir essayé cela dans votre propre code et avoir vu que cela fonctionne, comprenons pourquoi cela fonctionne et apprenons quelques autres façons de formater des dates en JavaScript avec une seule ligne de code.

### Voici un Scrim interactif sur le formatage des dates en JavaScript avec une seule ligne de code

<iframe src="https://scrimba.com/scrim/co6234e429a20cd020aceb3cc?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

# Comment formater des dates en JS

Obtenir la date en JavaScript n'est généralement pas un problème, mais formater ces dates pour les adapter à votre projet peut être fastidieux pour les débutants. À cause de cela, la plupart des gens finissent par utiliser des bibliothèques.

La méthode la plus utilisée pour obtenir la date en JavaScript est l'objet `new Date()`.

Par défaut, lorsque vous exécutez `new Date()` dans votre terminal, il utilise le fuseau horaire de votre navigateur et affiche la date sous forme de chaîne de texte complète, comme **Fri Jul 02 2021 12:44:45 GMT+0100 (British Summer Time).**

Mais avoir quelque chose comme cela dans votre page web ou votre application n'est pas professionnel et n'est pas facile à lire. Cela vous oblige donc à chercher de meilleures façons de formater ces dates.

Examinons quelques méthodes qui opèrent sur un objet date.

# Méthodes de date en JavaScript

Il existe de nombreuses méthodes que vous pouvez appliquer à l'objet date. Vous pouvez utiliser ces méthodes pour obtenir des informations à partir d'un objet date. En voici quelques-unes :

* `getFullYear()` – obtient l'année sous forme de nombre à quatre chiffres (yyyy)

* `getMonth()` – obtient le mois sous forme de nombre (0-11)

* `getDate()` – obtient le jour sous forme de nombre (1-31)

* `getHours()` – obtient l'heure (0-23)

Et bien d'autres...

Malheureusement, la plupart de ces méthodes nécessitent encore beaucoup de code pour convertir les dates au format que nous souhaitons.

Par exemple, `new Date().getMonth()` donnera 6 qui représente **Juillet.** Pour utiliser Juillet dans mon projet, je devrais avoir un long code comme celui-ci qui peut vraiment être fastidieux :

```javascript
const currentMonth = new Date();
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
console.log(months[currentMonth.getMonth()]);
```

Examinons deux méthodes que vous pouvez utiliser pour formater vos dates de la meilleure façon afin de pouvoir les utiliser pour vos projets.

## La méthode toDateString() en JavaScript

La méthode JavaScript `toDateString()` retourne la partie date d'un objet date sous forme de chaîne en utilisant le format suivant :

1. Les trois premières lettres du nom du jour de la semaine

2. Les trois premières lettres du nom du mois

3. Le jour du mois à deux chiffres, complété par un zéro à gauche si nécessaire

4. L'année à quatre chiffres (au moins), complétée par des zéros à gauche si nécessaire

```javascript
new Date().toDateString();
//"Fri Jul 02 2021"
```

Un inconvénient majeur de cette méthode est notre incapacité à manipuler la sortie de la date comme nous le souhaitons.

Par exemple, elle ne nous donne pas la possibilité d'afficher les dates selon notre langue. Examinons une autre méthode qui, à mon avis, est encore l'une des meilleures.

## La méthode toLocaleDateString() en JavaScript

Cette méthode retourne l'objet date sous forme de chaîne en utilisant les conventions locales. Elle prend également des options en tant qu'arguments qui permettent à vous/vos applications de personnaliser le comportement de la fonction.

**Syntaxe :**

```javascript
toLocaleDateString()
toLocaleDateString(locales)
toLocaleDateString(locales, options)
```

Examinons quelques exemples et leurs sorties :

```javascript
const currentDate = new Date();

const options = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };

console.log(currentDate.toLocaleDateString('de-DE', options));
//Freitag, 2. Juli 2021

console.log(currentDate.toLocaleDateString('ar-EG', options))
// 27442c4539290c 62 4a48444a48 62606261

console.log(currentDate.toLocaleDateString('en-us', options));
//Friday, Jul 2, 2021
```

Vous pouvez également décider de ne pas utiliser de locales ou d'options :

```javascript
new Date().toLocaleDateString()
// "7/2/2021"
```

Et vous pouvez également décider d'utiliser uniquement les locales. Cela affichera les mêmes informations que précédemment en fonction du fuseau horaire de mon navigateur.

```javascript
new Date().toLocaleDateString('en-US')
"7/2/2021"
```

Vous pouvez également décider de modifier les options comme vous le souhaitez. Il existe 4 options de base qui sont :

* `weekday` – Cela affiche le jour de la semaine en fonction de la façon dont vous souhaitez qu'il apparaisse (court ou long).

* `year` – Cela affiche l'année sous forme de nombre

* `month` – Cela affiche le mois de l'année en fonction de la façon dont vous souhaitez qu'il apparaisse (court ou long).

* `day` – Enfin, cela affiche le jour sous forme de nombre

```javascript
new Date().toLocaleDateString('en-us', { weekday:"long", year:"numeric", month:"short"}) // "Jul 2021 Friday"

new Date().toLocaleDateString('en-us', { year:"numeric", month:"short"})
// "Jul 2021"
```

# Conclusion

L'objet date dispose d'environ sept méthodes de formatage. Chacune de ces méthodes vous donne une valeur spécifique :

1. `toString()` vous donne **Fri Jul 02 2021 14:03:54 GMT+0100 (British Summer Time)**

2. `toDateString()` vous donne **Fri Jul 02 2021**

3. `toLocaleString()` vous donne **7/2/2021, 2:05:07 PM**

4. `toLocaleDateString()` vous donne **7/2/2021**

5. `toGMTString()` vous donne **Fri, 02 Jul 2021 13:06:02 GMT**

6. `toUTCString()` vous donne **Fri, 02 Jul 2021 13:06:28 GMT**

7. `toISOString()` vous donne **2021-07-02T13:06:53.422Z**

Si vous cherchez des formats de date plus avancés, vous devrez alors créer un format personnalisé vous-même. Consultez les ressources ci-dessous pour vous aider à comprendre comment créer des formats de date personnalisés.

## Ressources utiles

* [Tout ce que vous devez savoir sur la date en JavaScript](https://css-tricks.com/everything-you-need-to-know-about-date-in-javascript/)

* [JavaScript - Comment formater la date en JavaScript](https://www.tabnine.com/academy/javascript/how-to-format-date/)

* [Comment formater une date en JavaScript](https://flaviocopes.com/how-to-format-date-javascript/)

* [Le guide définitif de la manipulation de DateTime](https://www.toptal.com/software/definitive-guide-to-datetime-manipulation)