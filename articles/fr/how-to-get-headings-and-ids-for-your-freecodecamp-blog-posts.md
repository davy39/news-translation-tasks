---
title: Comment obtenir les titres et les ID pour votre table des matières de blog
  freeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-07T21:31:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-headings-and-ids-for-your-freecodecamp-blog-posts
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/brett-jordan-M9NVqELEtHU-unsplash-1.jpg
tags:
- name: Blogging
  slug: blogging
- name: freeCodeCamp.org
  slug: freecodecamp
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
- name: writing tips
  slug: writing-tips
seo_title: Comment obtenir les titres et les ID pour votre table des matières de blog
  freeCodeCamp
seo_desc: 'By Scott Spence

  In this post we''re going to get all the headings from a freeCodeCamp blog post
  to make a Table of Contents (ToC) in Ghost CMS.

  I recently published quite a large post here on freeCodeCamp and needed to add a
  table of contents to the p...'
---

Par Scott Spence

Dans cet article, nous allons récupérer tous les titres d'un article de blog freeCodeCamp pour créer une table des matières (ToC) dans Ghost CMS.

J'ai récemment publié [un article assez long](https://www.freecodecamp.org/news/build-your-developer-portfolio-from-scratch-with-sveltekit-and-graphcms/) ici sur freeCodeCamp et j'ai dû ajouter une table des matières à l'article.

Il y a un très bon article de soutien écrit par Colby Fayock sur la façon de faire cela. Il détaille le processus très clairement.

Vous pouvez consulter la vidéo et le guide très complet à ce sujet pour tous les détails :

%[https://www.freecodecamp.org/news/how-to-add-a-table-of-contents-to-your-blog-post-or-article/]

L'article de Colby explique pourquoi vous voudriez une table des matières (ToC) et comment en créer une en utilisant l'éditeur Ghost (l'éditeur utilisé pour écrire cet article dans le CMS Ghost).

Le problème, c'est que j'avais 33 titres dans l'article pour lesquels je devais ajouter des liens. Et l'idée de faire défiler un document de 10 000 mots pour obtenir un titre puis de faire défiler jusqu'en haut pour l'ajouter à la table des matières m'a fait me demander s'il n'y avait pas une meilleure façon de faire !

### Table des matières :

* [JavaScript à la rescousse !](#heading-javascript-a-la-rescousse)
* [Obtenir les propriétés de l'élément](#heading-obtenir-les-proprietes-de-lelement)
* [Obtenir l'id de l'élément et `innerText`](#heading-obtenir-lid-de-lelement-et-innertext)
* [Filtrer sur le `localName`](#heading-filtrer-sur-le-localname)
* [Conclusion](#heading-conclusion)

## JavaScript à la rescousse !

Avec cette idée en tête, j'ai fait une recherche rapide et j'ai trouvé une [réponse Stack Overflow](https://stackoverflow.com/a/7115083/1138354) que je pouvais utiliser. Voici le snippet :

```js
var ids = document.querySelectorAll('[id]');

Array.prototype.forEach.call( ids, function( el, i ) {
  // "el" est votre élément
  console.log( el.id ); // log l'ID
});
```

Alors, passons maintenant au navigateur et essayons cela.

Je vais me rendre sur cet article publié dans le navigateur et ouvrir les outils de développement. (Dans Chrome et Edge, c'est F12 pour ouvrir les outils de développement.) Ensuite, je vais coller ce code d'exemple dans la console et appuyer sur entrée, voici le résultat :

![La fenêtre du navigateur avec les outils de développement ouverts et le snippet de code exécuté montrant tous les IDs des éléments sur la page](https://www.freecodecamp.org/news/content/images/2022/01/image-42.png)

## Obtenir les propriétés de l'élément

Pas mal, mais je veux aussi le titre du titre, donc une façon rapide de voir les propriétés des éléments est d'envelopper l'`el` dans des accolades :

```js
let ids = document.querySelectorAll('[id]');

Array.prototype.forEach.call(ids, (el) => {
  console.log({el});
});
```

Vous remarquerez que j'ai nettoyé un peu la fonction, en remplaçant la fonction en ligne par une fonction fléchée et en remplaçant `var` par `let` pour que la syntaxe soit plus moderne.

L'exécution de ce snippet dans le navigateur me donne maintenant l'objet pour chaque élément :

![La page du navigateur avec les outils de développement ouverts sur la console montrant les éléments individuels sous forme d'objets](https://www.freecodecamp.org/news/content/images/2022/01/image-43.png)

Je peux ensuite développer l'un des éléments pour obtenir toutes les propriétés qui s'y rapportent. À partir de là, je vais vouloir obtenir l'`id` (que je savais déjà être là) et aussi le `innerText` qui est le titre du titre :

![La page du navigateur avec les outils de développement ouverts sur la console avec l'un des objets éléments développé pour montrer toutes les propriétés](https://www.freecodecamp.org/news/content/images/2022/01/image-45.png)

## Obtenir l'`id` et le `innerText` de l'élément

Ajoutons l'élément `innerText` au snippet sur lequel nous travaillons et voyons à quoi cela ressemble maintenant. Voici le snippet :

```js
let ids = document.querySelectorAll('[id]');

Array.prototype.forEach.call(ids, (el) => {
  console.log(el.id);
  console.log(el.innerText);
});
```

Et voici le résultat que nous obtenons de cela :

![La page du navigateur avec les outils de développement ouverts sur la console montrant tout le innerText de chaque élément avec un id](https://www.freecodecamp.org/news/content/images/2022/01/image-46.png)

D'accord, c'est vraiment bruyant car cela montre le `innerText` de chaque élément dans le document avec beaucoup d'informations non pertinentes. Tout ce qui nous intéresse vraiment, c'est le titre du titre et son id.

## Filtrer sur le `localName`

Tous les titres que j'utilise dans l'article sont des titres `h2`, donc je veux un moyen de filtrer cela. Donc, à partir des propriétés `{el}`, je devrais prendre le `localName` qui désigne le type de l'élément `h2` dans le cas présent.

Alors, utilisons une fonction `if` pour voir si le `localName` inclut `h2` et si c'est le cas, enregistrons cela. J'utiliserai également un littéral de modèle pour ajouter l'id d'ancre `#` au début de l'id :

```js
let ids = document.querySelectorAll('[id]');

Array.prototype.forEach.call(ids, (el) => {
  if (el.localName.includes(`h2`)) {
    console.log(`#${el.id}`);
    console.log(el.innerText);
  }
});
```

Regardons le résultat maintenant :

![La page du navigateur avec les outils de développement ouverts sur la console avec la fonction if pour filtrer sur les éléments h2](https://www.freecodecamp.org/news/content/images/2022/01/image-47.png)

Beaucoup mieux !

Maintenant, je peux utiliser ce résultat pour commencer à créer ma ToC !

%[https://youtu.be/8UnglHuuVTA]

## Conclusion

Nous avons pris ce qui pourrait être un processus assez long et nous l'avons transformé en un snippet pratique que nous pouvons utiliser dans la console du navigateur chaque fois que nous devons créer une ToC pour nos articles de blog.

C'est tout, j'espère que vous l'avez trouvé utile ! 👍

Si vous aimez le contenu, vous pouvez consulter beaucoup plus de moi sur mon [blog](https://scottspence.com/) et vous pouvez me suivre sur [Twitter](https://twitter.com/spences10).