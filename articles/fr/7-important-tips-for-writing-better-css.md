---
title: 7 Conseils Importants pour Écrire un Meilleur CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-29T19:19:08.000Z'
originalURL: https://freecodecamp.org/news/7-important-tips-for-writing-better-css
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/resim-2.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: frontend
  slug: frontend
- name: Web Development
  slug: web-development
seo_title: 7 Conseils Importants pour Écrire un Meilleur CSS
seo_desc: 'By Cem Eygi

  One of the biggest issues in programming is dealing with maintenance. In a real-world
  scenario, we don''t always start developing projects from scratch. Mostly, we are
  assigned (or take) a project that has already been written maybe a coup...'
---

Par Cem Eygi

L'un des plus grands problèmes en programmation est la gestion de la maintenance. Dans un scénario réel, nous ne commençons pas toujours à développer des projets à partir de zéro. La plupart du temps, nous sommes assignés (ou prenons) un projet qui a déjà été écrit peut-être il y a quelques années ou même plus longtemps.

Pour travailler efficacement sur ce projet, nous devons d'abord comprendre le code source. C'est à ce moment-là que nous réalisons immédiatement l'importance du **code propre**. En tant que développeurs, nous devons essayer d'écrire notre code aussi proprement que possible.

Cela s'applique également au CSS. Il y a certains points auxquels nous devons prêter attention lors de l'écriture de CSS. Dans cet article, je souhaite partager avec vous certains des plus importants. Je crois que ces 7 conseils vous aideront à améliorer la qualité de votre code CSS.

Alors, commençons...

## 1. DRY

**DRY signifie "Don't Repeat Yourself" (Ne vous répétez pas)**. C'est un principe général de développement logiciel et peut être appliqué dans n'importe quel langage de programmation, ainsi qu'en CSS. Comme nous pouvons le comprendre de son nom, DRY vise à éviter ou réduire la répétition autant que possible.

Par exemple, nous pouvons créer 3 classes CSS pour 3 boutons comme ceci :

```css
.primary-button {
  background: blue;
  color: white;
  border-radius: 5px;
  padding: 10px 20px;
  text-align: center;
  font-size: 16px;
}

.form-button {
  background: green;
  color: white;
  border-radius: 5px;
  padding: 10px 20px;
  text-align: center;
  font-size: 16px;
}

.cancel-button {
  background: red;
  color: white;
  border-radius: 5px;
  padding: 10px 20px;
  text-align: center;
  font-size: 16px;
}
```

Ou nous pouvons utiliser le principe DRY en écrivant les règles communes **une fois** dans une classe supplémentaire et les règles différentes dans d'autres classes :

```css
.button {
  color: white;
  border-radius: 5px;
  padding: 10px 20px;
  text-align: center;
  font-size: 16px;
}

.primary-button {
  background: blue;
}

.form-button {
  background: green;
}

.cancel-button {
  background: red;
}
```

Comme nous pouvons le voir, l'application du principe DRY évite la répétition, diminue le nombre de lignes et améliore la lisibilité et même la performance.

## 2. Nommage

Le nommage des sélecteurs CSS est un autre point important pour écrire un meilleur CSS. Le nom d'un sélecteur doit être **auto-descriptif et lisible**...

```css
// MAUVAIS NOMMAGE

.p {
  // Règles
}

.myFirstForm {
  // Règles
}
```

Normalement, **<p>** est une balise HTML et signifie paragraphe. Ci-dessus, nous ne pouvons pas vraiment comprendre ce qu'est la **classe p**. De plus, vous devriez éviter les noms comme **myFirstForm**, et je ne conseille pas d'utiliser le **camel case**.

À la place, utilisez des noms déclaratifs (séparés par un tiret pour les noms multiples) :

```css
// BON NOMMAGE

.article-paragraph {
  // Règles
}

.contact-form {
  // Règles
}
```

Je pense que les noms ont plus de sens maintenant :)

Le nommage des choses en programmation n'est pas si facile, mais il existe diverses conventions de nommage que vous pouvez utiliser dans votre projet. **BEM (block element modifier)** en est une. J'ai déjà travaillé avec BEM et je peux le recommander.

## 3. Ne pas utiliser les styles en ligne

Il y a des arguments sur le web à ce sujet : certains vous disent de ne jamais utiliser les styles en ligne, tandis que d'autres soutiennent que cela peut être utile dans certains cas.

À mon avis, la meilleure pratique est de ne pas utiliser les styles en ligne. Je vais me concentrer ici sur les raisons pour lesquelles nous ne devrions pas le faire.

### Séparation des préoccupations

Selon le principe de séparation des préoccupations, le design (CSS), le contenu (HTML) et la logique (JavaScript) doivent être séparés pour des raisons comme une meilleure lisibilité et maintenance.

Inclure des règles CSS à l'intérieur des balises HTML brise cette règle :

```html
<div style="font-size: 16px; color: red;">Some Text</div>
```

> Nous devrions plutôt garder nos règles de style dans des fichiers CSS externes.

### Difficultés de recherche

Un autre problème avec l'utilisation des styles en ligne est que nous ne pouvons pas les rechercher. Donc, lorsque nous devons apporter une modification au style, nous cherchons normalement les sélecteurs CSS de l'élément HTML.

Par exemple, changeons la **taille de la police** du texte sur notre page web. Pour ce faire, nous trouvons d'abord cette partie spécifique sur le navigateur où le changement est nécessaire en regardant la structure HTML :

```html
<div class="text-bold">Some Text</div>
```

Ensuite, nous devons trouver le sélecteur, qui est la classe **text-bold** ici. Enfin, nous allons à cette classe et apportons les modifications :

```css
.text-bold {
  font-size: 16px;    // changer la taille de la police à 14px
  font-weight: bold;
}
```

Mais si les règles sont écrites **en ligne** au lieu d'utiliser des classes :

```html
<div style="font-size: 16px; font-weight: bold">Some Text</div>
```

Même si nous trouvons la balise HTML, nous ne pouvons pas savoir s'il y a d'autres règles **font-size** à l'intérieur du HTML ou non. Puisqu'il n'y a pas de sélecteur utilisé, nous devons parcourir toutes les pages HTML une par une, essayer de trouver les autres règles **font-size** et les modifier également.

Ne serait-ce pas plus facile avec un sélecteur CSS ? Mais il y a quelque chose de pire...

### Problèmes de spécificité / écrasement

Les styles en ligne ont la spécificité la plus élevée parmi les sélecteurs CSS (lorsque nous ne comptons pas les **balises !important**).

En supposant que nous utilisons à la fois une classe et un style en ligne pour un élément :

```css
.text-bold {
  font-size: 16px;
  font-weight: bold;
}
```

```html
<div class="text-bold" style="font-size: 14px">Some Text</div>
```

Ici, la **taille de la police** du texte sera **14px**, car les styles en ligne ont une spécificité plus élevée que les classes CSS. Lorsque vous apportez une modification dans la classe :

```css
.text-bold {
  font-size: 20px;
  font-weight: bold;
}
```

La taille de la police sera toujours de 14px. Donc votre modification dans la classe CSS ne fonctionnera pas, ce qui vous amènera à dire :

> "Hey, pourquoi mon code CSS ne fonctionne-t-il pas ? Je déteste CSS !"

et vous amènera à utiliser une **balise !important** qui fait des miracles :

```css
.text-bold {
  font-size: 20px !important;
  font-weight: bold;
}
```

Ce qui est un grand non et nous amène au point suivant...

## 4. Évitez la balise !important

D'accord, donc votre CSS ne fonctionnait pas comme prévu, et vous l'avez fait fonctionner en appliquant la **balise important** :

```css
!important
```

Que se passe-t-il ensuite ? **La balise !important a la spécificité la plus élevée de tous les sélecteurs CSS.**

Vous dites essentiellement au navigateur d'appliquer cette règle spécifique avec la **balise !important** toujours et en toutes circonstances. Ce n'est pas bon car les règles CSS peuvent différer d'un sélecteur à l'autre, du sélecteur parent à l'enfant.

**Le seul moyen de remplacer une balise importante est d'utiliser une autre balise importante**. Et cela conduit à utiliser de plus en plus de balises importantes. Croyez-moi, dans un avenir proche, le code de votre projet sera rempli de **balises !important**, ce qui rend votre code CSS beaucoup plus difficile à maintenir. Alors essayez de ne pas l'utiliser.

## 5. Utilisez un préprocesseur

Travailler avec un préprocesseur CSS comme Sass ou LESS est très utile dans les grands projets. Un préprocesseur apporte des fonctionnalités supplémentaires à notre code CSS que nous ne pouvons normalement pas faire.

Par exemple, nous pouvons définir des variables, des fonctions et des mixins, nous pouvons importer et exporter nos fichiers CSS dans d'autres fichiers CSS et nous pouvons écrire du code CSS imbriqué :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/resim-1.png)
_Exemple de code Sass_

Un préprocesseur a sa propre syntaxe et est ensuite traduit en CSS standard (dans un fichier CSS séparé) car les navigateurs ne comprennent pas la syntaxe.

J'aime travailler avec Sass et l'ai utilisé dans divers projets. J'ai couvert certains des [avantages de l'utilisation d'un préprocesseur CSS ici](https://medium.com/swlh/advantages-of-using-a-preprocessor-sass-in-css-eb7310179944).

## 6. Utilisez des raccourcis

Certaines des propriétés CSS comme les espacements, les marges, les polices et les bordures peuvent être écrites de manière beaucoup plus simple avec des raccourcis. L'utilisation de raccourcis aide à réduire le nombre de lignes de règles.

Donc, sans raccourcis, une classe CSS ressemblerait à ceci :

```css
.article-container {
  padding-top: 10px;
  padding-bottom: 20px;
  padding-left: 15px;
  padding-right: 15px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 15px;
  margin-right: 15px;
  border-width: 1px;
  border-style: solid:
  border-color: black;
}
```

et avec des raccourcis, cela ressemble à ceci :

```css
.article-container {
  padding: 10px 15px 20px 15px;
  margin: 10px 15px;
  border: 1px solid black;
}
```

[Vous pouvez trouver ici](https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties) plus d'informations sur la façon d'utiliser les propriétés de raccourcis et pour quelles propriétés CSS elles peuvent être appliquées.

## 7. Ajoutez des commentaires lorsque nécessaire

Normalement, un code de qualité n'a pas besoin de commentaires car il devrait déjà être clair et auto-descriptif. Mais encore, dans certains cas, nous pouvons avoir besoin d'écrire des explications supplémentaires.

```css
// Vos commentaires
.example-class {
  // vos règles
}
```

Donc, lorsque vous sentez que certaines parties du code ne sont pas claires, n'hésitez pas à ajouter des commentaires (mais d'un autre côté, assurez-vous de ne pas en abuser :)).

En tant que développeur Frontend avec quelques années d'expérience, ce sont les conseils les plus importants que je puisse suggérer pour améliorer vos compétences en CSS. Si vous avez des questions, ou si vous pensez qu'il y a aussi d'autres conseils pour écrire un meilleur CSS, n'hésitez pas à commenter ci-dessous.

**Si vous voulez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)**!**

Merci d'avoir lu !