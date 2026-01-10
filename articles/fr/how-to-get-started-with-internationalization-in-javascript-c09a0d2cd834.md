---
title: Comment commencer avec l'internationalisation en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T19:25:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-internationalization-in-javascript-c09a0d2cd834
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c0jA-Wr3SikV8sBhMGAihQ.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment commencer avec l'internationalisation en JavaScript
seo_desc: 'By Alex Permyakov

  By adapting our apps for different languages and countries, we provide a better
  user experience. It’s simpler for users to deal with known notations for dates,
  currencies, and numbers.

  Internationalization (i18n) involves adding sup...'
---

Par Alex Permyakov

En adaptant nos applications pour différentes langues et pays, nous offrons une meilleure expérience utilisateur. Il est plus simple pour les utilisateurs de traiter avec des notations connues pour les dates, les devises et les nombres.

**L'internationalisation (i18n)** consiste à ajouter le support de différentes langues et pays dans votre application. Le nombre 18 représente le nombre de lettres entre le premier 'i' et le dernier 'n'.

Des exemples d'internationalisation pourraient être le support Unicode, la personnalisation de l'interface utilisateur pour différents alphabets, ou le tri de tableaux de chaînes non anglaises.

JavaScript implémente la spécification [Internationalization API](https://www.ecma-international.org/ecma-402/1.0/) et définit l'objet intégré [Intl](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl).

Et ce qui le rend si utile, c'est qu'il a une grande compatibilité multi-navigateurs et un [support Node.js](https://nodejs.org/api/intl.html) :

![Image](https://cdn-media-1.freecodecamp.org/images/afErT9QuFCwZj5spfEzr3KwZNpNKKJGaog10)
_[https://caniuse.com/#search=intl](https://caniuse.com/#search=intl" rel="noopener" target="_blank" title=")_

### Commençons !

L'objet `**Intl**` fournit l'accès à plusieurs constructeurs, comme :

* **Intl.DateTimeFormat** — formatage de date et d'heure sensible à la langue.
* **Intl.NumberFormat** — formatage de nombre sensible à la langue.
* **Intl.PluralRules** — formatage sensible au pluriel et règles de pluriel de la langue.
* **Intl.Collator** — comparaison de chaînes sensible à la langue.

La création de l'un de ces objets suit un modèle simple :

```
const formatter = new Intl.ctor(locales, options);
```

Par exemple, la locale "**de-AT**" : la langue allemande telle qu'elle est utilisée en Autriche :

```
const dateFormatterAT = new Intl.DateTimeFormat("de-AT");
```

Ensuite, nous appelons la méthode **format()** avec un objet **Date** fourni :

```
const date = new Date("2018-11-25");
const format = dateFormatterAT.format(date); // "25.11.2018"
```

Il ne contient que des codes de langue et de pays. Bientôt, nous verrons des exemples plus complets. [Vous pouvez trouver plus d'exemples de locales ici.](http://www.lingoes.net/en/translator/langcode.htm)

Nous pouvons utiliser [navigator.language](https://developer.mozilla.org/en-US/docs/Web/API/NavigatorLanguage/language) — la langue préférée de l'utilisateur, que nous utilisons comme locale :

![Image](https://cdn-media-1.freecodecamp.org/images/Yble1iDed6eDpaXr1GbDJw17eQQdBEpJLGu1)

Ici, au lieu d'appeler directement une méthode **format**, nous pouvons l'assigner comme une fonction. C'est génial car une fois que nous avons créé une fonction de format spécialisée, nous pouvons l'utiliser plusieurs fois.

Juste quelques lignes de code et vous avez une date localisée !

Alors, ensuite, nous allons approfondir et en apprendre davantage sur les locales. Si vous n'êtes pas prêt pour cela et que vous voulez seulement voir des démonstrations sympas comme celle-ci dans l'image ci-dessous — allez à la section des exemples ci-dessous !

![Image](https://cdn-media-1.freecodecamp.org/images/kR8E22SSQXkyqqeWQfufLZmnFGpyNC-rvXhu)

#### Approfondissons

Bien, cela suffit pour avoir une idée de son fonctionnement, mais les cas d'utilisation réels pourraient être bien plus compliqués. Que faire si nous voulions :

* afficher notre date en utilisant le calendrier japonais ou persan
* utiliser des chiffres thaïlandais ou arabes-indiens pour les dates et les nombres
* utiliser le chinois simplifié
* Toute combinaison des éléments ci-dessus ?

### Qu'est-ce qu'une Locale ?

Afin de travailler avec cette API, nous devons en apprendre davantage sur les locales. Tout d'abord, donnons une définition.

Une locale est un identifiant qui fait référence à un ensemble de préférences utilisateur telles que :

* les dates et heures
* les nombres et devises
* les noms traduits pour les fuseaux horaires, les langues et les pays
* les unités de mesure
* l'ordre de tri (collation)

Une locale n'est pas sensible à la casse. Ce n'est qu'une **convention**.

La locale doit être une chaîne contenant une [balise de langue BCP 47](http://tools.ietf.org/html/rfc5646), et toutes les parties sont séparées par des tirets.

Examinons l'exemple suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/FjMty-N4Fy5h5mLMYhFSEEzXfBB-Zwybpxnw)

Encore une fois, seulement quatre lignes de code ? Examinons le diagramme ci-dessous et analysons chaque partie de notre locale :

![Image](https://cdn-media-1.freecodecamp.org/images/QRkUyedHKCodZOv823VPd-N27228EDkZZx1I)

Sur cette image, vous pouvez voir que seule la première partie — le code de langue — est requise. Il est peu probable que vous ayez besoin d'une locale comme celle-ci. Mais c'est un bon exemple pour examiner chaque partie possible d'une locale et avoir une idée de ce qu'est une locale.

Notre locale contient toutes les parties possibles :

* **zh** (code de langue) — langue chinoise
* **Hans** (code de script) — écrit en caractères simplifiés
* **CN** (code de pays) — tel qu'utilisé en Chine.
* **bauddha** (variante) — utilisant un dialecte hybride bouddhiste sanskrit
* **u-nu-hanidec** (extension) — utilisant des nombres décimaux Han

Ci-dessous, vous pouvez trouver plus d'exemples pour les scripts, les variantes et les extensions.

#### Codes de script

Ceux-ci sont utilisés avec les balises de langue pour indiquer dans quel script une langue est écrite. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/PNwPXNYYAhR5xM2y-OLIh2QwFuAtxXxvmK4R)

#### Codes de variante

Les variantes représentent un dialecte linguistique.

![Image](https://cdn-media-1.freecodecamp.org/images/q3dQcoCGdJnMB-5jl1VhPliCNA5m5Jadrtzt)

#### Extensions

Cela inclut différents calendriers et systèmes numériques.

Les **calendriers** ont le préfixe "u-ca-", valeurs possibles (non exhaustives) :

![Image](https://cdn-media-1.freecodecamp.org/images/OLI1LkLJbxN65CR2UOeT8BMSRc6bVVXpehvk)

Les **systèmes numériques** ont le préfixe "u-nu", valeurs possibles (non exhaustives) :

![Image](https://cdn-media-1.freecodecamp.org/images/o049A-CGR9Fp4IZyTn2wI3IMy4z3ftQdbaXn)

L'organisation Iana est responsable de la mise à jour de [cette liste](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

### Négociation de locale

La dernière chose que nous devons apprendre sur les locales est la façon dont elles sont résolues. Nous avons vu cet exemple auparavant :

```
const formatter = new Intl.ctor(locales, options);
```

L'argument `locales` spécifie une seule locale ou un tableau de locales. L'environnement (navigateur ou Node.js) le compare avec les locales qu'il a disponibles et choisit la meilleure.

Il existe deux algorithmes de correspondance :

* **lookup** — vérifie du plus spécifique au moins spécifique : si **zh-Hans-SG** n'est pas disponible, obtenir **zh-Hans**, si non — **zh**, sinon — une locale par défaut.
* **best fit** (par défaut) — algorithme amélioré. Si "es-GT" — l'espagnol pour le Guatemala est demandé, mais non trouvé, alors au lieu de fournir un repli comme "es", "es-MX" — l'espagnol au Mexique sera choisi.

Si nous fournissons un tableau de locales, alors la première correspondance gagne.

Assez de théorie — maintenant, il est temps de pratiquer !

### Exemples

Le code pour les exemples peut être trouvé sur [GitHub](https://gist.github.com/alexpermyakov/69706e1ec5bff64efc14c15bc9e0bbcb).

#### Formatage de date/heure

![Image](https://cdn-media-1.freecodecamp.org/images/lNsn0KyU79jQIZowSVdleRqsbSWZMCB5-R9U)

Les locales ne sont pas la seule chose qui est géniale avec l'[Intl API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl). Vous pouvez modifier le résultat de manière souhaitable en utilisant un argument `options`.

![Image](https://cdn-media-1.freecodecamp.org/images/-LzjP9pShGYgbi5cPuIogpGI2UCTGlbZAZzf)

C'est une mise à jour massive par rapport à l'objet **Date** !

Contrairement à moment.js, vous **ne pouvez pas échanger manuellement** n'importe quelle partie de la date comme l'année et le mois. Vous devez utiliser la locale appropriée à la place. Cela peut sembler une **limitation**, mais cela le rend plus familier pour nos utilisateurs.

#### Formatage de nombre

Sachant comment traiter les dates, vous savez comment traiter les nombres. La seule différence est la liste des options :

![Image](https://cdn-media-1.freecodecamp.org/images/y-b7iSrasEiJvD2WqqDq0KDAO61HZWkDNSxN)

#### Formatage de devise

Pour les devises, nous utilisons le constructeur `Intl.NumberFormat`, mais nous fournissons une liste différente d'options :

![Image](https://cdn-media-1.freecodecamp.org/images/RyBT6EzHcO-K4UOimN3UGIEMJaWGAzQSc6xD)

Notez que nous ne convertissons pas d'argent ici. Tout ce que nous faisons est de formater le nombre 172630 en utilisant les règles de devise **appropriées**. Vous pouvez trouver la liste des [codes de devise](https://www.currency-iso.org/dam/downloads/lists/list_one.xml) ici.

#### Formatage des règles de pluriel

Cela vous indique quelle forme s'applique en fonction d'un nombre donné pour une locale spécifique :

![Image](https://cdn-media-1.freecodecamp.org/images/QvzCr-RKIwnXXRLp9LbGEQM9yxoamK-tNrnc)

Cela peut être très pratique pour formater les nombres ordinaux :

![Image](https://cdn-media-1.freecodecamp.org/images/cjYfaoKpb7V97e5vJqDqKcdxJEO2kZoVLIdE)

#### Tri de chaînes

Trier des chaînes qui contiennent des lettres supplémentaires comme _ä_ en allemand ou en suédois n'est pas ce que vous voulez faire manuellement, simplement parce que l'ordre dépend de la langue. Heureusement pour nous, nous avons `Intl.Collator`. Et encore une fois, tout ce que nous avons à faire est de fournir une locale requise :

![Image](https://cdn-media-1.freecodecamp.org/images/1V0DR0viMQe--PzGNPAoIayzO1bkpWVgZzX1)

### Conclusion

L'internationalisation est un sujet passionnant et complexe. Mais si vous savez ce qu'est une locale et comment la construire, le reste est super facile à utiliser.

### C'est tout !

Si vous avez des questions ou des commentaires, faites-le moi savoir dans les commentaires ci-dessous ou contactez-moi sur [Twitter](https://twitter.com/AlexDevBB).

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissements ? ci-dessous plusieurs fois pour montrer votre soutien ! ⏏⏏ ??

Voici d'autres articles que j'ai écrits :

[**Comment simplifier votre base de code avec map(), reduce() et filter() en JavaScript**](https://medium.freecodecamp.org/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f)  
[_Lorsque vous lisez à propos de Array.reduce et à quel point c'est génial, le premier et parfois le seul exemple que vous trouvez est la somme de222medium.freecodecamp.org](https://medium.freecodecamp.org/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f)[**Configuration d'API REST Node.js prêtes pour la production utilisant TypeScript, PostgreSQL et Redis.**](https://medium.com/@alex.permyakov/production-ready-node-js-rest-apis-setup-using-typescript-postgresql-and-redis-a9525871407)  
[_Il y a un mois, on m'a donné la tâche de construire une simple API de recherche. Tout ce qu'elle devait faire était de récupérer des données depuis un tiers222medium.com](https://medium.com/@alex.permyakov/production-ready-node-js-rest-apis-setup-using-typescript-postgresql-and-redis-a9525871407)

Merci d'avoir lu ❤️