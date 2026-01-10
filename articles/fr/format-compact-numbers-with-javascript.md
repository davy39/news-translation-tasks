---
title: Comment formater des nombres compacts avec l'API d'internationalisation JavaScript
subtitle: ''
author: Gerard Hynes
co_authors: []
series: null
date: '2023-01-04T15:39:17.000Z'
originalURL: https://freecodecamp.org/news/format-compact-numbers-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Format-Compact-Numbers.png
tags:
- name: api
  slug: api
- name: internationalization
  slug: internationalization
- name: JavaScript
  slug: javascript
seo_title: Comment formater des nombres compacts avec l'API d'internationalisation
  JavaScript
seo_desc: 'Sometimes it can be difficult to fit large numbers into your site or app''s
  layout, especially if you have to display several of them together.

  As a result, a lot of modern sites and apps use the same format to display large
  numbers in a compact way. ...'
---

Parfois, il peut être difficile de faire tenir de grands nombres dans la mise en page de votre site ou application, surtout si vous devez en afficher plusieurs ensemble.

En conséquence, de nombreux sites et applications modernes utilisent le même format pour afficher les grands nombres de manière compacte. Par exemple, afficher 123 000 sous la forme 123K.

![Profil YouTube et Instagram de freeCodeCamp utilisant le format de nombre compact.](https://www.freecodecamp.org/news/content/images/2022/12/freecodecamp_socials.png align="left")

*Profil YouTube et Instagram de freeCodeCamp utilisant le format de nombre compact.*

Vous pouvez le faire en écrivant une fonction de format personnalisée, en utilisant une bibliothèque tierce, ou, mieux encore, en utilisant une API JavaScript intégrée.

Vous pouvez bien sûr écrire votre propre fonction de formatage (et il y en a plusieurs disponibles sur Stack Overflow) mais vous devrez finir par vérifier de nombreuses conditions.

À titre d'information, depuis ES2021, JavaScript prend en charge l'utilisation de traits de soulignement comme séparateurs numériques pour faciliter la lecture des grands nombres dans votre code.

```javascript
function formatCompactNumber(number) {
  if (number < 1000) {
    return number;
  } else if (number >= 1000 && number < 1_000_000) {
    return (number / 1000).toFixed(1) + "K";
  } else if (number >= 1_000_000 && number < 1_000_000_000) {
    return (number / 1_000_000).toFixed(1) + "M";
  } else if (number >= 1_000_000_000 && number < 1_000_000_000_000) {
    return (number / 1_000_000_000).toFixed(1) + "B";
  } else if (number >= 1_000_000_000_000 && number < 1_000_000_000_000_000) {
    return (number / 1_000_000_000_000).toFixed(1) + "T";
  }
}

formatCompactNumber(12_000);        // 12.0K
formatCompactNumber(2_000_000);     // 2.0M
formatCompactNumber(2_500_000);     // 2.5M
formatCompactNumber(6_000_000_000); // 6.0B
formatCompactNumber(6_900_000_000); // 6.9B
```

Cette implémentation laisse encore un `.0` après un millier, million, milliard ou billion pair. Vous pourriez corriger cela en utilisant la méthode `replace` et une expression régulière.

```js
function formatCompactNumber(number) {
  if (number < 1000) {
    return number;
  } else if (number >= 1000 && number < 1_000_000) {
    return (number / 1000).toFixed(1).replace(/\.0$/, "") + "K";
  } else if (number >= 1_000_000 && number < 1_000_000_000) {
    return (number / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  } else if (number >= 1_000_000_000 && number < 1_000_000_000_000) {
    return (number / 1_000_000_000).toFixed(1).replace(/\.0$/, "") + "B";
  } else if (number >= 1_000_000_000_000 && number < 1_000_000_000_000_000) {
    return (number / 1_000_000_000_000).toFixed(1).replace(/\.0$/, "") + "T";
  }
}
```

Mais que faire si vous devez gérer des nombres négatifs ? Vous pourriez ajouter une autre condition.

```js
function formatCompactNumber(number) {
  if (number < 0) {
    return "-" + formatCompactNumber(-1 * number);
  }
  if (number < 1000) {
    return number;
  } else if (number >= 1000 && number < 1_000_000) {
    return (number / 1000).toFixed(1).replace(/\.0$/, "") + "K";
  } else if (number >= 1_000_000 && number < 1_000_000_000) {
    return (number / 1_000_000).toFixed(1).replace(/\.0$/, "") + "M";
  } else if (number >= 1_000_000_000 && number < 1_000_000_000_000) {
    return (number / 1_000_000_000).toFixed(1).replace(/\.0$/, "") + "B";
  } else if (number >= 1_000_000_000_000 && number < 1_000_000_000_000_000) {
    return (number / 1_000_000_000_000).toFixed(1).replace(/\.0$/, "") + "T";
  }
}
```

Comme vous pouvez probablement le voir maintenant, cela ne fait qu'effleurer la surface des choses que vous devriez considérer lors de l'écriture de votre propre fonction pour afficher des nombres compacts.

Il existe une [poignée de packages npm](https://www.npmjs.com/search?q=compact%20number) pour formater les nombres de manière compacte. Par exemple, vous pourriez installer [`cldr-compact-number`](https://github.com/snewcomer/cldr-compact-number), mais cela ajouterait également 3 kilooctets (ou 1,2 kilooctets compressés) à votre bundle JavaScript, ajoutant légèrement à votre temps de chargement de page.

Heureusement, vous n'avez pas besoin d'utiliser des bibliothèques tierces pour formater des nombres compacts, car il existe une solution relativement simple qui est prise en charge nativement en JavaScript.

## Comment utiliser l'API d'internationalisation JavaScript

L'[API d'internationalisation JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) vous aide à prendre en charge différentes langues et conventions de formatage lors de l'utilisation de JavaScript. Cela peut être tout, de la mise en forme des dates et heures à la connaissance de l'ordre de *a* ou *ä* lors de la comparaison de chaînes.

L'API a une excellente compatibilité avec les navigateurs, avec [98 % de support mondial](https://caniuse.com/?search=Internationalization%20API). Elle fonctionne en utilisant l'objet `Intl` pour créer un espace de noms pour la comparaison de chaînes sensible à la langue, la mise en forme des nombres, et la mise en forme des dates et heures.

En plus de `Intl.DateTimeFormat` pour formater les dates et heures, et `Intl.Collator` pour effectuer des comparaisons de chaînes sensibles à la langue, il y a `Intl.NumberFormat`. Cela vous permet de formater les nombres de manière spécifique à une langue.

Pour commencer, créez un formateur en utilisant le constructeur `Intl.NumberFormat`. Optionnellement, vous pouvez lui passer une ou plusieurs locales et un objet `options`.

```js
new Intl.NumberFormat(locales, options);
```

Une locale est un paramètre qui définit la langue, la région ou d'autres préférences de localisation de l'utilisateur. Dans ce cas, il s'agit d'une [balise de langue IETF](https://en.wikipedia.org/wiki/IETF_language_tag), telle que "en-US" pour l'anglais américain, "zh-CH" pour le mandarin, ou "uk" pour l'ukrainien.

Dans le navigateur, vous pouvez accéder à la locale de l'utilisateur en utilisant `navigator.language`. Si vous ne fournissez pas de locale, l'API tentera d'utiliser la locale de l'utilisateur depuis son navigateur.

L'objet `options` peut contenir des valeurs pour contrôler des choses comme la manière de formater la monnaie, si utiliser `l` ou `litres`, ou si afficher `+` ou `-` pour les valeurs positives ou négatives.

Une fois que vous avez créé un formateur, vous pouvez appeler sa méthode `format` et lui passer le nombre que vous souhaitez formater. Il retournera le nombre formaté selon la configuration que vous avez fournie.

Par exemple, vous pourriez utiliser l'API d'internationalisation pour formater les valeurs financières selon différentes devises :

```js
const number = 12345678.99

const germanCurrencyFormatter = new Intl.NumberFormat("de-DE", { style: "currency", currency: "EUR" });

const chineseCurrencyFormatter = new Intl.NumberFormat("zh-CH", { style: "currency", currency: "CNY" });

germanCurrencyFormatter.format(number); // 12.345.678,99 €
chineseCurrencyFormatter.format(number); // ¥12,345,678.99
```

L'une des options disponibles est `notation`. Cela contrôle le formatage lors de l'affichage des nombres. Les valeurs possibles pour `notation` sont :

* `"standard"` – formatage de nombre simple selon les conventions de la locale (par défaut)

* `"scientific"` – retourne l'ordre de grandeur pour un nombre

* `"engineering"` – retourne l'exposant de dix lorsque le nombre est divisible par trois

* `"compact"` – retourne une chaîne représentant l'exposant, telle que K pour les milliers

Donc, par exemple, si vous formatez le nombre 123456789 avec la locale définie sur "en", vous obtiendrez :

* standard : 123,456,789

* scientific : 1.235E8

* engineering : 123.457E6

* compact : 123M

Si vous voulez qu'un formateur affiche les grands nombres de manière compacte, définissez la locale sur votre locale souhaitée et définissez `notation` sur `"compact"`.

```js
const formatter = Intl.NumberFormat("en", { notation: "compact" });
```

Cela peut être utilisé pour créer une fonction de formatage beaucoup plus courte :

```js
function formatCompactNumber(number) {
  const formatter = Intl.NumberFormat("en", { notation: "compact" });
  return formatter.format(number);
}

formatCompactNumber(-57);               // -57
formatCompactNumber(999);               // 999
formatCompactNumber(8_554);             // 8.5K
formatCompactNumber(150_000);           // 150K
formatCompactNumber(3_237_512);         // 3.2M
formatCompactNumber(9_782_716_897);     // 9.8B
formatCompactNumber(7_899_693_036_970); // 7.9T
```

Maintenant, votre site ou application peut afficher même les plus grands nombres de manière compacte, rendant votre mise en page un peu plus propre et ordonnée.

### Merci d'avoir lu !

J'espère que ce guide rapide vous aidera lorsque vous travaillerez avec de grands nombres en JavaScript et peut-être vous encouragera à explorer davantage l'API d'internationalisation.