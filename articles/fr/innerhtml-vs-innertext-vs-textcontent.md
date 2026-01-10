---
title: innerHTML vs innerText vs textContent – Quelles sont les différences ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-12-11T21:57:38.000Z'
originalURL: https://freecodecamp.org/news/innerhtml-vs-innertext-vs-textcontent
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Benjamin-Semah
seo_title: innerHTML vs innerText vs textContent – Quelles sont les différences ?
---

DevAfterHours-1.png
tags:
- name: DOM
  slug: dom
- name: Développement Front-end
  slug: front-end-development
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Développement Web
  slug: web-development
seo_title: null
seo_desc: 'Par Benjamin Semah

En HTML, innerHTML, innerText et textContent sont des propriétés du DOM (Document Object Model). Elles permettent de lire et de mettre à jour le contenu des éléments HTML.

Mais elles ont des comportements différents en termes de contenu qu'elles incluent et de la manière dont elles gèrent le balisage HTML.

---

Par Benjamin Semah

En HTML, `innerHTML`, `innerText` et `textContent` sont des propriétés du DOM (Document Object Model). Elles permettent de lire et de mettre à jour le contenu des éléments HTML.

Mais elles ont des comportements différents en termes de contenu qu'elles incluent et de la manière dont elles gèrent le balisage HTML.

À la fin de cet article, vous connaîtrez les différences entre ces trois propriétés et quand utiliser chacune d'entre elles.

## Table des matières

* [Qu'est-ce que la propriété `innerHTML` ?](#heading-quest-ce-que-la-propriete-innerhtml)
* [Qu'est-ce que la propriété `innerText` ?](#heading-quest-ce-que-la-propriete-innertext)
* [Qu'est-ce que la propriété `textContent` ?](#heading-quest-ce-que-la-propriete-textcontent)
* [Comment lire le contenu avec `innerHTML`, `innerText` et `textContent`](#heading-comment-lire-le-contenu-avec-innerhtml-innertext-et-textcontent)
* [Comment mettre à jour le contenu avec `innerHTML`, `innerText` et `textContent`](#heading-comment-mettre-a-jour-le-contenu-avec-innerhtml-innertext-et-textcontent)
* [Problèmes de sécurité lors de l'utilisation de `innerHTML`](#heading-problemes-de-securite-lors-de-lutilisation-de-innerhtml)
* [Conclusion](#heading-conclusion)

Tout d'abord, je vais expliquer comment ces trois propriétés fonctionnent. Ensuite, vous verrez quelques exemples d'utilisation pour comprendre les différences dans leur comportement.

## Qu'est-ce que la propriété `innerHTML` ?

Lorsque vous utilisez la propriété `innerHTML`, elle lit à la fois le balisage HTML et le contenu textuel de l'élément. Cela signifie que lorsque vous l'utilisez pour définir le contenu des éléments, vous pouvez inclure des balises HTML, et le navigateur les rendra correctement.

Cependant, soyez prudent si vous insérez du contenu provenant de l'entrée utilisateur ou de toute source non fiable avec `innerHTML`. Les attaquants peuvent utiliser la balise HTML `<script>` pour insérer et exécuter du code malveillant dans votre application. Plus d'informations à ce sujet plus tard dans l'article.

## Qu'est-ce que la propriété `innerText` ?

Cette propriété se concentre sur le contenu textuel rendu. Lorsque vous utilisez `innerText` pour lire le contenu d'un élément, il retourne le texte tel qu'il apparaît à l'écran. Il ignore les balises HTML. Et il n'inclut pas non plus le texte qui est masqué avec des styles CSS.

Lorsque vous devez tenir compte des styles, vous devriez envisager d'utiliser `innerText`. La modification de `innerText` d'un élément signifie que le navigateur peut avoir besoin d'ajuster la mise en page pour accommoder les changements de taille de texte, ce qui peut avoir des implications sur les performances.

## Qu'est-ce que la propriété `textContent` ?

La propriété `textContent` ignore également toutes les balises HTML et retourne uniquement le texte. Alors que `innerText` lit le texte tel qu'il est rendu à l'écran, `textContent` lit le texte tel qu'il est dans le balisage. Il retourne également tout le texte, qu'il soit rendu à l'écran ou non.

De plus, `textContent` ne traite que le texte brut et ne tient pas compte des styles. Donc, dans les situations où la performance est une préoccupation et où vous n'avez pas besoin de tenir compte des styles, `textContent` pourrait être un choix plus efficace par rapport à `innerText`.

## Comment lire le contenu avec `innerHTML`, `innerText` et `textContent`

Maintenant, voyons quelques exemples pratiques pour mieux comprendre les trois propriétés.

Le code suivant est un simple balisage pour une barre de navigation avec quatre éléments. Le dernier élément avec le texte "Pricing" est masqué (display défini sur none). Lisons le contenu de l'élément `nav` en utilisant les trois propriétés pour voir la différence.

```html
<nav>
  <a>Accueil</a>
  <a>À propos</a>
  <a>Contact</a>
  <a style="display: none">Tarifs</a>
</nav>
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.37.48-AM.png)
_Un exemple simple de barre de navigation_

### Obtenir le contenu avec `innerHTML`

```javascript
// Lecture du contenu avec innerHTML
const navElement = document.querySelector('nav')
console.log(navElement.innerHTML)
```

![Exemple innerHTML qui inclut à la fois le balisage et le texte](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.32.01-AM.png)
_Exemple innerHTML qui inclut à la fois le balisage et le texte_

La propriété `innerHTML` retourne le contenu complet y compris toutes les balises HTML à l'intérieur des éléments `nav` et leur contenu textuel.

### Obtenir le contenu avec `innerText`

```javascript
// Lecture du contenu avec innerText
const navElement = document.querySelector('nav')
console.log(navElement.innerText)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.36.52-AM.png)
_Exemple innerText qui imprime le texte tel qu'il apparaît à l'écran_

La propriété `innerText` retourne le contenu tel qu'il est rendu à l'écran. Elle ignore toutes les balises HTML. Et elle ignore également l'élément masqué (avec display défini sur none).

### Obtenir le contenu avec `textContent`

```javascript
// Lecture du contenu avec textContent
const navElement = document.querySelector('nav')
console.log(navElement.textContent)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-07-at-11.47.30-AM.png)
_Exemple textContent qui imprime le texte tel qu'il est dans le balisage y compris le texte masqué_

La propriété `textContent` retourne le contenu tel qu'il est dans le balisage HTML. Comme `innerText`, elle ignore également les balises HTML. Mais elle ne tient pas compte des styles, donc elle retourne le texte "Tarifs" même s'il est masqué.

## Comment mettre à jour le contenu avec `innerHTML`, `innerText` et `textContent`

Vous pouvez également utiliser les trois propriétés pour mettre à jour le contenu des éléments DOM. Lors de la mise à jour du contenu, les propriétés se comportent de manière similaire à lorsque vous les utilisez pour lire ou obtenir du contenu.

Voyons quelques exemples pour mieux comprendre.

### Définir le contenu avec `innerHTML`

Le balisage ci-dessous inclut un élément d'en-tête et un élément `<ul>` vide. Vous pouvez utiliser la propriété `innerHTML` pour insérer du contenu dans le `<ul>`.

```html
<h2>Langages de programmation</h2>
<ul class="languages-list"></ul>
```

```javascript
const langListElement = document.querySelector('.languages-list')

// Définir ou mettre à jour le contenu avec innerHTML
langListElement.innerHTML = `
  <li>JavaScript</li>
  <li>Python</li>
  <li>PHP</li>
  <li>Ruby</li>
`
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-9.50.06-AM.png)
_Un exemple de définition de contenu avec la propriété innerHTML_

Le code JavaScript passe une chaîne de liste HTML comme valeur pour `innerHTML`. La propriété `innerHTML` reconnaît les balises HTML et formate le contenu en conséquence.

Contrairement à `innerHTML`, `innerText` et `textContent` ignoreront les balises HTML et rendront tout comme une chaîne.

### Définir le contenu avec `innerText`

En utilisant le même exemple, voyons comment la propriété `innerText` mettra à jour le contenu de la liste des langages de programmation.

```javascript
const langListElement = document.querySelector('.languages-list')

langListElement.innerText = `
  <li>JavaScript</li>
  <li>Python</li>
  <li>PHP</li>
  <li>Ruby</li>
`
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-11.12.15-AM.png)
_Un exemple de définition de contenu avec la propriété innerText_

Remarquez comment `innerText` ignore les balises HTML et les imprime à l'écran comme faisant partie du texte. Mais il reconnaît toujours la mise en forme comme les sauts de ligne et les espaces blancs.

### Définir le contenu avec `textContent`

Lors de la définition ou de la mise à jour du contenu, la propriété `textContent` ignorera le balisage HTML et ignorera également des choses comme les sauts de ligne et les espaces blancs.

```javascript
const langListElement = document.querySelector('.languages-list')

langListElement.textContent = `
  <li>JavaScript</li>
  <li>Python</li>
  <li>PHP</li>
  <li>Ruby</li>
`
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-11.22.45-AM-1.png)

Parce que `textContent` ignore la mise en forme comme les sauts de ligne et les espaces blancs, tout le texte est imprimé sur la même ligne. Lorsque vous voulez le texte brut et que vous ne vous souciez pas de la mise en forme du texte, `textContent` est un choix approprié.

## Problèmes de sécurité lors de l'utilisation de `innerHTML`

Parce que `innerHTML` traite et interprète les balises HTML, il est conseillé de l'utiliser uniquement lors de l'insertion de contenu provenant de sources fiables. Ou lorsque vous avez correctement assaini et validé le contenu fourni.

Le navigateur exécutera tout code JavaScript que vous mettez dans la balise de script HTML. Et cela peut ouvrir la porte à des attaques de type [Cross-Site Scripting (XSS)](https://www.freecodecamp.org/news/cross-site-scripting-what-is-xss/) où les attaquants peuvent injecter et exécuter des scripts malveillants dans le contexte de votre page web.

Voici un exemple :

```html
<div id="commentSection"></div>
```

Supposons que vous utilisez le `div` ci-dessus comme conteneur pour les commentaires des utilisateurs dans votre application. Et que vous utilisez `innerHTML` pour ajouter de nouveaux commentaires sans aucune validation ou assainissement du commentaire.

Voici un exemple très basique de la manière dont un utilisateur peut injecter et exécuter un script malveillant :

```javascript
const commentSection = document.getElementById('commentSection')

let userComment = `<img src="malicious-script.jpg" onerror="alert('Script Malveillant Exécuté !')"> Voici mon commentaire !`;

commentSection.innerHTML = userComment;
```

![Image](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-2023-12-08-at-10.35.53-AM.png)
_Script malveillant exécuté via la balise <script> avec innerHTML_

L'utilisateur donne délibérément une valeur incorrecte pour l'attribut `src` de l'image. Cela déclenchera l'événement `onerror` qui exécute une alerte avec la chaîne "Script Malveillant Exécuté !".

Vous pouvez imaginer comment un attaquant peut tirer parti de cela pour injecter du code JavaScript nuisible, potentiellement voler des informations sensibles de l'utilisateur, manipuler le contenu de la page, ou effectuer d'autres actions malveillantes.

## Conclusion

Vous pouvez utiliser les trois propriétés `innerHTML`, `innerText` et `textContent` pour manipuler le contenu des éléments DOM. Mais elles se comportent différemment. Les comprendre vous aidera à décider quand il est approprié d'utiliser chacune d'entre elles.

La propriété `innerHTML` reconnaît les balises HTML et rend le contenu selon les balises. `innerText` et `textContent` ignorent les balises HTML et les traitent comme faisant partie du texte. Vous avez également appris dans cet article comment `innerHTML` peut entraîner des risques de sécurité et pourquoi vous devez en être conscient.

De plus, `innerText` lit le contenu tel qu'il apparaît à l'écran, ignore le contenu masqué et observe la mise en forme du texte. Mais `textContent` lit le contenu tel qu'il apparaît dans le balisage. Cela signifie qu'il lit également le contenu masqué. Mais il ignore également la mise en forme comme les espaces blancs et les sauts de ligne lorsque vous l'utilisez pour définir le contenu.

Merci d'avoir lu. Et bon codage. Pour des tutoriels plus approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).