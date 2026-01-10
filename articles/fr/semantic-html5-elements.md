---
title: Éléments sémantiques HTML5 expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-12T21:49:00.000Z'
originalURL: https://freecodecamp.org/news/semantic-html5-elements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ebe740569d1a4ca3ed0.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: Éléments sémantiques HTML5 expliqués
seo_desc: "Semantic HTML elements are those that clearly describe their meaning in\
  \ a human- and machine-readable way. \nElements such as <header>, <footer> and <article>\
  \ are all considered semantic because they accurately describe the purpose of the\
  \ element and ..."
---

Les éléments sémantiques HTML sont ceux qui décrivent clairement leur signification de manière lisible par les humains et les machines. 

Des éléments tels que `<header>`, `<footer>` et `<article>` sont tous considérés comme sémantiques car ils décrivent avec précision le but de l'élément et le type de contenu qu'ils contiennent.

### **Qu'est-ce que les éléments sémantiques ?**

HTML a été initialement créé comme un langage de balisage pour décrire des documents sur le premier internet. À mesure que l'internet grandissait et était adopté par plus de personnes, ses besoins changeaient. 

Là où l'internet était initialement destiné au partage de documents scientifiques, les gens voulaient maintenant partager d'autres choses également. Très rapidement, les gens ont commencé à vouloir rendre le web plus beau. 

Parce que le web n'a pas été initialement construit pour être conçu, les programmeurs utilisaient différentes astuces pour disposer les choses de différentes manières. Plutôt que d'utiliser `<table></table>` pour décrire des informations à l'aide d'un tableau, les programmeurs les utilisaient pour positionner d'autres éléments sur une page. 

À mesure que l'utilisation de mises en page conçues visuellement progressait, les programmeurs ont commencé à utiliser une balise "non sémantique" générique comme `<div>`. Ils donnaient souvent à ces éléments un attribut `class` ou `id` pour décrire leur but. Par exemple, au lieu de `<header>`, cela était souvent écrit comme `<div class="header">`. 

Comme HTML5 est encore relativement nouveau, cette utilisation d'éléments non sémantiques est encore très courante sur les sites web aujourd'hui.

### Liste des nouveaux éléments sémantiques

Les éléments sémantiques ajoutés dans HTML5 sont :

* `<article>`
* `<aside>`
* `<details>`
* `<figcaption>`
* `<figure>`
* `<footer>`
* `<header>`
* `<main>`
* `<mark>`
* `<nav>`
* `<section>`
* `<summary>`
* `<time>`

Des éléments tels que `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, et `<footer>` agissent plus ou moins comme des éléments `<div>`. Ils regroupent d'autres éléments ensemble en sections de page. Cependant, là où une balise `<div>` pourrait contenir n'importe quel type d'information, il est facile d'identifier quel type d'information irait dans une région sémantique `<header>`.

**Un exemple de mise en page d'éléments sémantiques par w3schools**

![Éléments sémantiques disposant une page par w3schools](https://www.w3schools.com/html/img_sem_elements.gif)

## Pourquoi utiliser des éléments sémantiques ?

Pour examiner les avantages des éléments sémantiques, voici deux morceaux de code HTML. Ce premier bloc de code utilise des éléments sémantiques :

```text
<header></header>
<section>
	<article>
		<figure>
			<img>
			<figcaption></figcaption>
		</figure>
	</article>
</section>
<footer></footer>
```

Tandis que ce second bloc de code utilise des éléments non sémantiques :

```text
<div id="header"></div>
<div class="section">
	<div class="article">
		<div class="figure">
			<img>
			<div class="figcaption"></div>
		</div>
	</div>
</div>
<div id="footer"></div>
```

Premièrement, c'est beaucoup **plus facile à lire**. C'est probablement la première chose que vous remarquerez en regardant le premier bloc de code utilisant des éléments sémantiques. C'est un petit exemple, mais en tant que programmeur, vous pouvez lire des centaines ou des milliers de lignes de code. Plus il est facile de lire et de comprendre ce code, plus cela facilite votre travail.

Il a une **meilleure accessibilité**. Vous n'êtes pas le seul à trouver les éléments sémantiques plus faciles à comprendre. Les moteurs de recherche et les technologies d'assistance (comme les lecteurs d'écran pour les utilisateurs ayant une déficience visuelle) sont également capables de mieux comprendre le contexte et le contenu de votre site web, ce qui signifie une meilleure expérience pour vos utilisateurs.

Dans l'ensemble, les éléments sémantiques conduisent également à un code plus **cohérent**. Lors de la création d'un en-tête utilisant des éléments non sémantiques, différents programmeurs pourraient écrire cela comme `<div class="header">`, `<div id="header">`, `<div class="head">`, ou simplement `<div>`. Il existe de nombreuses façons de créer un élément d'en-tête, et elles dépendent toutes de la préférence personnelle du programmeur. En créant un élément sémantique standard, cela facilite la tâche pour tout le monde.

Depuis octobre 2014, HTML4 a été mis à niveau vers HTML5, avec certains nouveaux éléments "sémantiques". À ce jour, certains d'entre nous peuvent encore être confus quant à la raison pour laquelle tant d'éléments différents qui ne semblent pas montrer de changements majeurs.

#### **`<section>` et `<article>`**

"Quelle est la différence ?", pourriez-vous demander. Ces deux éléments sont utilisés pour sectionner un contenu, et oui, ils peuvent définitivement être utilisés de manière interchangeable. C'est une question de situation. HTML4 n'offrait qu'un seul type d'élément conteneur, qui est `<div>`. Bien que cela soit encore utilisé dans HTML5, HTML5 nous a fourni `<section>` et `<article>` pour remplacer `<div>`.

Les éléments `<section>` et `<article>` sont conceptuellement similaires et interchangeables. Pour décider lequel de ceux-ci vous devez choisir, notez ce qui suit :

1. Un article est destiné à être distribuable ou réutilisable de manière indépendante.
2. Une section est un regroupement thématique de contenu.

```html
<section>
  <p>Top Stories</p>
  <section>
    <p>News</p>
    <article>Story 1</article>
    <article>Story 2</article>
    <article>Story 3</article>
  </section>
  <section>
    <p>Sport</p>
    <article>Story 1</article>
    <article>Story 2</article>
    <article>Story 3</article>
  </section>
</section>
```

#### **`<header>` et `<hgroup>`**

L'élément `<header>` se trouve généralement en haut d'un document, d'une section ou d'un article et contient généralement le titre principal et certains outils de navigation et de recherche.

```html
<header>
  <h1>Company A</h1>
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact us</a></li>
  </ul>
  <form target="/search">
    <input name="q" type="search" />
    <input type="submit" />
  </form>
</header>
```

L'élément `<hgroup>` doit être utilisé lorsque vous voulez un titre principal avec un ou plusieurs sous-titres.

```html
<hgroup>
  <h1>Heading 1</h1>
  <h2>Subheading 1</h2>
  <h2>Subheading 2</h2>
</hgroup>
```

RAPPELEZ-VOUS que l'élément `<header>` peut contenir n'importe quel contenu, mais que l'élément `<hgroup>` ne peut contenir que d'autres en-têtes, c'est-à-dire de `<h1>` à `<h6>` et y compris `<hgroup>`.

#### **`<aside>`**

L'élément `<aside>` est destiné au contenu qui ne fait pas partie du flux du texte dans lequel il apparaît, mais qui y est néanmoins lié d'une certaine manière. Considérez `<aside>` comme une barre latérale à votre contenu principal.

```html
<aside>
  <p>This is a sidebar, for example a terminology definition or a short background to a historical figure.</p>
</aside>
```

Avant HTML5, nos menus étaient créés avec des `<ul>` et des `<li>`. Maintenant, avec ceux-ci, nous pouvons séparer nos éléments de menu avec un `<nav>`, pour la navigation entre vos pages. Vous pouvez avoir n'importe quel nombre d'éléments `<nav>` sur une page, par exemple, il est courant d'avoir une navigation globale en haut (dans le `<header>`) et une navigation locale dans une barre latérale (dans un élément `<aside>`).

```html
<nav>
  <ul>
    <li><a href="/home">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/contact">Contact us</a></li>
  </ul>
</nav>
```

#### **`<footer>`**

S'il y a un `<header>`, il doit y avoir un `<footer>`. Un `<footer>` se trouve généralement en bas d'un document, d'une section ou d'un article. Tout comme le `<header>`, le contenu est généralement des métainformations, telles que les détails de l'auteur, les informations légales et/ou les liens vers des informations connexes. Il est également valide d'inclure des éléments `<section>` dans un pied de page.

```html
<footer>&copy;Company A</footer>
```

#### **`<small>`**

L'élément `<small>` apparaît souvent dans un élément `<footer>` ou `<aside>` qui contiendrait généralement des informations de copyright ou des mentions légales, et d'autres textes similaires. Cependant, cela n'est pas destiné à rendre le texte plus petit. Il décrit simplement son contenu, sans prescrire la présentation.

```html
<footer><small>&copy;Company A</small> Date</footer>
```

#### **`<time>`**

L'élément `<time>` permet de joindre une date ISO 8601 non ambiguë à une version lisible par l'homme de cette date.

```html
<time datetime="2017-10-31T11:21:00+02:00">Tuesday, 31 October 2017</time>
```

Pourquoi se soucier de `<time>` ? Alors que les humains peuvent lire l'heure qui peut être désambiguïser par le contexte de la manière normale, les ordinateurs peuvent lire la date ISO 8601 et voir la date, l'heure et le fuseau horaire.

#### **`<figure>` et `<figcaption>`**

`<figure>` est utilisé pour envelopper votre contenu d'image, et `<figcaption>` est utilisé pour légender votre image.

```html
<figure>
  <img src="https://en.wikipedia.org/wiki/File:Shadow_of_Mordor_cover_art.jpg" alt="Shadow of Mordor" />
  <figcaption>Cover art for Middle-earth: Shadow of Mordor</figcaption>
</figure>
```

### **En savoir plus sur les nouveaux éléments HTML5 :**

* [w3schools](https://www.w3schools.com/html/html5_semantic_elements.asp) fournit des descriptions simples et claires de nombreux nouveaux éléments et comment/où ils doivent être utilisés.
* [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) fournit également une excellente référence pour tous les éléments HTML et approfondit chacun d'eux.