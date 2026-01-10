---
title: Aide-mémoire React – 9 cas courants de rendu HTML que vous devriez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-23T21:40:22.000Z'
originalURL: https://freecodecamp.org/news/react-cheatsheet-html-rendering
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/teaser.jpg
tags:
- name: cheatsheet
  slug: cheatsheet
- name: HTML
  slug: html
- name: React
  slug: react
seo_title: Aide-mémoire React – 9 cas courants de rendu HTML que vous devriez connaître
seo_desc: "By Ondrej Polesny\nWhenever I'm starting with a new framework or it's been\
  \ a while since I've used it, I always end up searching for the same simple things.\
  \ \nI'll Google how to render raw HTML, how to display a component based on a condition,\
  \ how to a..."
---

Par Ondrej Polesny

Chaque fois que je commence avec un nouveau Framework ou que cela fait un moment que je ne l'ai pas utilisé, je finis toujours par chercher les mêmes choses simples. 

Je vais chercher sur Google comment afficher du HTML brut, comment afficher un composant en fonction d'une condition, comment assigner une classe à un élément, et ainsi de suite.

C'est pourquoi j'ai créé cet aide-mémoire avec les neuf tâches les plus courantes que vous effectuerez régulièrement avec React [et JSX](https://reactjs.org/docs/introducing-jsx.html). 

Je les ai classés dans l'ordre où je les rencontre généralement lors de la construction d'une application. Dans les exemples ci-dessous, le premier extrait de code montrera la syntaxe, et le second montrera comment l'utiliser avec des données réelles.

## Comment afficher des données en HTML

Le cas d'utilisation le plus simple de tous – afficher la valeur d'une variable dans le balisage HTML. C'est généralement le premier test qui montre que l'application a traité les données et peut les afficher :

```js
{ variable }
```
```js
{ metadata.subtitle.value }
```

## Comment ajouter un attribut de classe standard

Alors que de nombreux Frameworks ne touchent pas au balisage HTML, React ne permet pas d'utiliser le mot réservé "class" pour le style. Nous devons utiliser `className` à la place, comme ceci :

```js
<... className="classname">
```
```js
<div className="sidebar__inner">
```

## Comment afficher des données dans les attributs HTML

Ce cas d'utilisation est lié à la création de liens. Mais dans de nombreux cas, vous devez également remplir des attributs comme title, data-{quelque-chose-dont-votre-application-a-besoin}, ou même de simples balises alt d'images :

```js
< ... name={variable}>
```
```js
<a href={`https://twitter.com/${author.twitter.value}`}>
```

## Comment afficher du HTML brut

Certains contenus sont structurés dans un autre système, par exemple, du texte enrichi composé dans un CMS headless. 

Dans ces cas, vous utilisez généralement un outil comme un SDK pour construire le HTML pour vous. Voici comment vous pouvez l'ajouter à votre balisage :

```js
< ... dangerouslySetInnerHTML={{__html: variable}}></...>
```
```js
<div dangerouslySetInnerHTML={{__html: article.teaser}}></div>
```

## Comment itérer sur des ensembles de données

Sur les pages d'index, les sitemaps, les pages de recherche, ou partout où vous avez besoin d'afficher des données d'une collection, React et JSX vous permettent de combiner la fonction (presque) toute-puissante `map` avec le balisage HTML :

```js
let components = collectionVariable.map((item) =>
  <Component data={item} key={item.uniqueKey} />);
...
<div>{components}</div>
```
```js
let articleComponents = articles.map((article) =>
  <Article data={article} key={article.id} ... />);
...
<div>{articleComponents}</div>
```

## Comment itérer sur des ensembles de données avec un index

C'est le même cas d'utilisation, mais il vous donne accès à un index de chaque élément itéré. Dans certains cas, l'index peut également être utilisé pour remplacer la clé unique :

```js
let components = collectionVariable.map((item, index) =>
  <Component data={item} index={index} key={uniqueKey} />);
...
<div>{components}</div>
```
```js
let articleComponents = articles.map((article) =>
  <Article data={article} index={index} key={article.id} ... />);
...
<div>{articleComponents}</div>
```

## Comment afficher un balisage conditionnel

C'est la condition _if_ typique en JSX. Elle est souvent utilisée pendant le chargement des données pour afficher des pré-chargeurs ou simplement pour décider quelle partie du balisage utiliser en fonction des données :

```js
{variable !== null && <... >}
```
```js
{data.length > 0 && <div> ... </div>}
```

## Comment afficher un balisage conditionnel incluant une branche else

La branche else est obtenue en inversant la condition :

```js
{variable !== null && <... >}
{variable == null && <... >}
```
```js
{data.length > 0 && <div> ... </div>}
{data.length == 0 && <div>Chargement...</div>}
```

## Comment transmettre des données aux composants enfants

Et enfin, quand vous commencez à utiliser des composants, voici comment vous fournissez des données aux enfants via les props :

```js
<component componentVariable={variable}>
```
```js
<links author={author}>
```

J'espère que cela vous évitera quelques recherches sur Google :-)

Si vous recherchez une version imprimable (PDF), elle est disponible sur mon [site personnel](https://ondrabus.com/react-vue-angular-cheatsheet) où vous trouverez également des aide-mémoires similaires pour Vue et Angular.